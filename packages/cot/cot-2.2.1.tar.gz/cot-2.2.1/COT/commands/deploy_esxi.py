#!/usr/bin/env python
#
# deploy_esxi.py - Implements "cot deploy ... esxi" command
#
# August 2015, Glenn F. Matthews
# Copyright (c) 2014-2017 the COT project developers.
# See the COPYRIGHT.txt file at the top-level directory of this distribution
#
# This file is part of the Common OVF Tool (COT) project.
# It is subject to the license terms in the LICENSE.txt file found in the
# top-level directory of this distribution. No part of COT, including this
# file, may be copied, modified, propagated, or distributed except
# according to the terms contained in the LICENSE.txt file.

"""Module for deploying VMs to ESXi, vCenter, and vSphere.

**Classes**

.. autosummary::
  :nosignatures:

  COTDeployESXi
  SmarterConnection
  PyVmomiVMReconfigSpec

"""

import getpass
import logging
import os.path
import re
import shlex
import ssl
from distutils.version import StrictVersion

import requests
from pyVmomi import vim
from pyVim.connect import SmartConnection

from COT.data_validation import ValueUnsupportedError
from COT.helpers import helpers
from .command import command_classes
from .deploy import COTDeploy

logger = logging.getLogger(__name__)


class SmarterConnection(SmartConnection):
    """A smarter version of pyVmomi's SmartConnection context manager."""

    def __init__(self, ui, host, user, pwd, port=443):
        """Create a connection to the given server.

        Args:
          ui (UI): User interface instance.

        For the other parameters, see :class:`pyVim.connect.SmartConnection`
        """
        self.ui = ui
        self.server = host
        self.username = user
        self.password = pwd
        self.port = port
        super(SmarterConnection, self).__init__(host=host, user=user,
                                                pwd=pwd, port=port)

    def __enter__(self):
        """Establish a connection and use it as the context manager object.

        Unlike SmartConnection, this lets the user override SSL certificate
        validation failures and connect anyway. It also produces slightly
        more meaningful error messages on failure.

        Raises:
          vim.fault.HostConnectFault: TODO
          requests.exceptions.ConnectionError: TODO
        Yields:
          pyVmomi.VmomiSupport.vim.ServiceInstance: Session service instance.
        """
        logger.verbose("Establishing connection to %s:%s...",
                       self.server, self.port)
        try:
            return super(SmarterConnection, self).__enter__()
        except vim.fault.HostConnectFault as exc:
            if not re.search("certificate verify failed", exc.msg):
                raise
            # Self-signed certificates are pretty common for ESXi servers
            logger.warning(exc.msg)
            self.ui.confirm_or_die("SSL certificate for {0} is self-signed or "
                                   "otherwise not recognized as valid. "
                                   "Accept certificate anyway?"
                                   .format(self.server))
            # pylint: disable=protected-access, no-member
            # ssl._create_unverified_context doesn't exist in Python 3.3.
            _create_unverified_context = ssl._create_unverified_context
            ssl._create_default_https_context = _create_unverified_context
            return super(SmarterConnection, self).__enter__()
        except requests.exceptions.ConnectionError as exc:
            # ConnectionError can wrap another internal error; let's unwrap it
            # so COT can log it more cleanly
            exc.errno, inner_message = self.unwrap_connection_error(exc)
            if exc.strerror is None:
                exc.strerror = ("Error connecting to {0}:{1}: {2}"
                                .format(self.server, self.port, inner_message))
            raise

    def __exit__(self,     # pylint: disable=arguments-differ
                 exc_type, exc_value, trace):
        """Disconnect from the server.

        For the parameters, see :mod:`contextlib`.
        """
        super(SmarterConnection, self).__exit__()
        if exc_type is not None:
            logger.error("Session failed - %s", exc_value)
        # TODO - re-enable SSL certificate validation?

    @staticmethod
    def unwrap_connection_error(outer_e):
        """Extract inner attributes from a ConnectionError.

        ConnectionError often wraps another exception with more context;
        this function dives inside the ConnectionError to find that context.

        Args:
          outer_e (ConnectionError): ConnectionError to unwrap
        Returns:
          tuple: extracted (errno, inner_message)
        """
        errno = None
        inner_message = None
        while errno is None and outer_e is not None:
            inner_e = None
            if hasattr(outer_e, 'reason'):
                inner_e = outer_e.reason  # pylint: disable=no-member
            else:
                for arg in outer_e.args:
                    if isinstance(arg, Exception):
                        inner_e = arg
                        break
            if inner_e is not None:
                if hasattr(inner_e, 'strerror'):
                    inner_message = inner_e.strerror
                elif hasattr(inner_e, 'message'):
                    inner_message = inner_e.message
                else:
                    inner_message = inner_e.args[0]
                logger.debug("\nInner exception: %s", inner_e)
                if hasattr(inner_e, 'errno') and inner_e.errno is not None:
                    errno = inner_e.errno
            outer_e = inner_e
        return errno, inner_message


class PyVmomiVMReconfigSpec(object):
    """Context manager for reconfiguring an ESXi VM using PyVmomi."""

    def __init__(self, service_instance, vm_name):
        """Use the given name to look up a VM using the given service_instance.

        Args:
          service_instance (pyVmomi.VmomiSupport.vim.ServiceInstance):
            Connection to ESXi.
          vm_name (str): Virtual machine name.
        """
        self.service_instance = service_instance
        self.vm = self.lookup_object(vim.VirtualMachine, vm_name)
        if not self.vm:
            raise LookupError("No VM '{0}' was found!".format(vm_name))
        self.spec = vim.vm.ConfigSpec()

    def __enter__(self):
        """Use a ConfigSpec as the context manager object.

        Yields:
            pyVmomi.VmomiSupport.vim.vm.ConfigSpec: config specification
        """
        return self.spec

    def __exit__(self, exc_type, exc_value, trace):
        """If the block exited cleanly, apply the ConfigSpec to the VM.

        For the parameters, see :mod:`contextlib`.
        """
        # Did we exit cleanly?
        if exc_type is None:
            logger.verbose("Reconfiguring VM...")
            self.vm.ReconfigVM_Task(spec=self.spec)

    def lookup_object(self, vimtype, name):
        """Look up an object by name.

        Args:
          vimtype (object): currently only ``vim.VirtualMachine``
          name (str): Name of the object to look up.
        Returns:
          object: Located object
        """
        content = self.service_instance.RetrieveContent()
        container = content.viewManager.CreateContainerView(
            content.rootFolder, [vimtype], True)
        for item in container.view:
            if item.name == name:
                return item
        return None


class COTDeployESXi(COTDeploy):
    """Sub-command for deploying VMs on ESXi and VMware vCenter/vSphere.

    Inherited attributes:
    :attr:`~COT.commands.Command.ui`,
    :attr:`~COT.commands.ReadCommand.package`,
    :attr:`~COT.deploy.COTDeploy.generic_parser`,
    :attr:`~COT.deploy.COTDeploy.parser`,
    :attr:`~COT.deploy.COTDeploy.subparsers`,
    :attr:`~COT.deploy.COTDeploy.hypervisor`,
    :attr:`~COT.deploy.COTDeploy.configuration`,
    :attr:`~COT.deploy.COTDeploy.username`,
    :attr:`~COT.deploy.COTDeploy.password`,
    :attr:`~COT.deploy.COTDeploy.power_on`,
    :attr:`~COT.deploy.COTDeploy.vm_name`,
    :attr:`~COT.deploy.COTDeploy.network_map`
    :attr:`~COT.deploy.COTDeploy.serial_connection`

    Attributes:
    :attr:`locator`,
    :attr:`datastore`,
    :attr:`ovftool_args`
    """

    def __init__(self, ui):
        """Instantiate this command with the given UI.

        Args:
          ui (UI): User interface instance.
        """
        super(COTDeployESXi, self).__init__(ui)
        self.datastore = None
        """ESXi datastore to deploy to."""
        self.host = None
        """vSphere host to deploy to - set implicitly by self.locator."""
        self.server = None
        """vCenter server or vSphere host - set implicitly by self.locator."""
        self._locator = None
        self._ovftool_args = []

        self.ovftool = helpers['ovftool']

    @property
    def ovftool_args(self):
        """List of CLI arguments to pass through to ``ovftool``."""
        return list(self._ovftool_args)

    @ovftool_args.setter
    def ovftool_args(self, value):
        # Use shlex to split ovftool_args but respect quoted whitespace
        self._ovftool_args = shlex.split(value)
        logger.debug("ovftool_args split to: %s", self._ovftool_args)

    @property
    def locator(self):
        """Target vSphere locator."""
        return self._locator

    @locator.setter
    def locator(self, value):
        self._locator = value
        self.server = value.split("/")[0]
        self.host = os.path.basename(value)
        logger.debug("locator %s --> server %s / host %s",
                     value, self.server, self.host)

    @COTDeploy.serial_connection.setter  # pylint: disable=no-member
    def serial_connection(self, value):
        """Override parent property setter to add ESXi validation.

        For the parameters, see :meth:`~COTDeploy.serial_connection`
        """
        if len(value) > 4:
            raise ValueUnsupportedError(
                'serial port connection list', value,
                'no more than 4 connections (ESXi limitation)')
        super(COTDeployESXi, self.__class__).serial_connection.fset(self,
                                                                    value)

    def ready_to_run(self):
        """Check whether the module is ready to :meth:`run`.

        Returns:
          tuple: ``(True, ready_message)`` or ``(False, reason_why_not)``
        """
        if self.locator is None:
            return False, "LOCATOR is a mandatory argument"
        return super(COTDeployESXi, self).ready_to_run()

    def fixup_ovftool_args(self, ovftool_args, target):
        """Make any needed modifications to the ovftool arguments.

        Args:
          ovftool_args (list): Any existing ovftool arguments to begin with.
          target (str): deployment target URI
        Returns:
          list: Updated ovftool arguments
        """
        # pass selected configuration profile to ovftool
        if self.configuration is not None:
            ovftool_args.append("--deploymentOption=" + self.configuration)

        # pass network settings on to ovftool
        if self.network_map is not None:
            for netmap in self.network_map:
                ovftool_args.append("--net:" + netmap)

        # check if user entered a name for the VM
        if self.vm_name is None:
            self.vm_name = os.path.splitext(os.path.basename(self.package))[0]
        # pass name to ovftool
        ovftool_args.append("--name=" + self.vm_name)

        # tell ovftool to power on the VM if requested
        # TODO: if serial port fixup is needed, do not power on VM until
        # after serial ports are added.
        if self.power_on:
            ovftool_args.append("--powerOn")

        # specify target datastore
        if self.datastore is not None:
            ovftool_args.append("--datastore=" + self.datastore)

        # add package and target to the list
        ovftool_args.append(self.package)
        ovftool_args.append(target)

        logger.debug("Final args to pass to OVFtool: %s", ovftool_args)
        return ovftool_args

    def run(self):
        """Do the actual work of this command - deploying to ESXi.

        Raises:
          InvalidInputError: if :func:`ready_to_run` reports ``False``
        """
        super(COTDeployESXi, self).run()

        # ensure user provided proper credentials
        if self.username is None:
            self.username = getpass.getuser()
        if self.password is None:
            self.password = self.ui.get_password(self.username, self.server)

        target = ("vi://" + self.username + ":" + self.password +
                  "@" + self.locator)

        ovftool_args = self.ovftool_args

        vm = self.vm

        # If locator is a vCenter locator "<vCenter>/datacenter/host/<host>"
        # then environment properties will always be used.
        # Otherwise we may need to help and/or warn the user:
        if vm.environment_properties and not re.search("/host/", self.locator):
            if self.ovftool.version < StrictVersion("4.0.0"):
                self.ui.confirm_or_die(
                    "When deploying an OVF directly to a vSphere target "
                    "using ovftool prior to version 4.0.0, any OVF "
                    "environment properties will not be made available "
                    "to the new guest.\n"
                    "If your guest needs environment properties, please "
                    "either specify a vCenter target locator (such as "
                    "'<vCenter>/<datacenter>/host/<host>') "
                    "or upgrade to ovftool 4.0.0 or later.\n"
                    "Continue deployment without OVF environment?")
                logger.warning("COT is deploying directly to vSphere and the"
                               " available ovftool version is too low to add"
                               " the 'injectOvfEnv' option."
                               " OVF environment properties will be ignored.")
            elif not self.power_on:
                self.ui.confirm_or_die(
                    "When deploying an OVF directly to a vSphere target, "
                    "OVF environment properties can only be made available to "
                    "the new guest if the guest is to be powered on "
                    "immediately.\n"
                    "If your guest needs environment properties, please "
                    "either specify the '--power-on'/'-P' option or provide "
                    "a vCenter target locator (such as "
                    "'<vCenter>/<datacenter>/host/<host>') "
                    "instead of a vSphere target.\n"
                    "Continue deployment without OVF environment?")
                logger.warning("COT is deploying directly to vSphere but "
                               "--power-on is not requested. OVF "
                               "environment properties will be ignored.")
            else:
                logger.verbose("Since ovftool version is sufficient and user "
                               "requested --power-on, adding ovftool args to "
                               "ensure passthru of OVF environment to guest.")
                ovftool_args.append("--X:injectOvfEnv")

        ovftool_args = self.fixup_ovftool_args(ovftool_args, target)

        logger.info("Deploying VM...")
        self.ovftool.call(ovftool_args, capture_output=False)

        # VMWare has confirmed that they have no plan to implement serial port
        # orchestration in ovftool, so we have to do it ourselves now that
        # the VM has been created.
        if len(self.serial_connection) > 0:
            self.fixup_serial_ports()

        # TODO: only now power on VM if power_on was requested

    def fixup_serial_ports(self):
        """Use PyVmomi to create and configure serial ports for the new VM.

        Raises:
          NotImplementedError: If any :class:`~COT.deploy.SerialConnection`
              in :attr:`serial_connection` has a
              :attr:`~COT.deploy.SerialConnection.kind` other than
              'tcp', 'telnet', or 'device'
        """
        logger.info("Fixing up serial ports on deployed VM...")
        with SmarterConnection(self.ui,
                               self.server,
                               self.username,
                               self.password) as service_instance:
            logger.verbose("Connection established")
            with PyVmomiVMReconfigSpec(service_instance, self.vm_name) as spec:
                logger.verbose("Spec created")
                spec.deviceChange = []
                for entry in self.serial_connection:
                    self._create_serial_port(entry, spec)

        logger.info("Done with serial port fixup")

    @staticmethod
    def _create_serial_port(conn, spec):
        """Use PyVmomi to create a serial connection on a VM.

        Args:
          conn (SerialConnection): Serial connection to create
          spec (PyVmomiVMReconfigSpec): PyVmomi VM spec object
        """
        logger.verbose(conn)
        serial_spec = vim.vm.device.VirtualDeviceSpec()
        serial_spec.operation = 'add'
        serial_port = vim.vm.device.VirtualSerialPort()
        serial_port.yieldOnPoll = True

        if conn.kind == 'device':
            backing = serial_port.DeviceBackingInfo()
            logger.info("Serial port will use host device %s", conn.value)
            backing.deviceName = conn.value
        elif conn.kind == 'telnet' or conn.kind == 'tcp':
            backing = serial_port.URIBackingInfo()
            backing.serviceURI = conn.kind + '://' + conn.value
            if 'server' in conn.options:
                logger.info("Serial port will be a %s server at %s",
                            conn.kind, conn.value)
                backing.direction = 'server'
            else:
                logger.info(
                    "Serial port will connect via %s to %s. Use ',server' "
                    "option if a server is desired instead of client.",
                    conn.kind, conn.value)
                backing.direction = 'client'
        else:
            # TODO - support other backing types
            raise NotImplementedError("no support yet for backing type '{0}'"
                                      .format(conn.kind))

        serial_port.backing = backing
        serial_spec.device = serial_port
        spec.deviceChange.append(serial_spec)

    def create_subparser(self):
        """Add subparser for the CLI of this command.

        This will create the shared :attr:`~COTDeploy.parser`, then
        create our own sub-subparser under :attr:`~COTDeploy.subparsers`.
        """
        super(COTDeployESXi, self).create_subparser()

        import argparse
        # Create 'cot deploy ... esxi' parser
        parser = self.ui.add_subparser(
            'esxi',
            aliases=['vcenter', 'vmware', 'vsphere'],
            parent=self.subparsers,
            lookup_prefix="deploy-",
            parents=[self.generic_parser],
            usage=self.ui.fill_usage("deploy PACKAGE esxi", [
                "LOCATOR [-u USERNAME] [-p PASSWORD] [-c CONFIGURATION] "
                "[-n VM_NAME] [-P] [-N OVF1=HOST1 [-N OVF2=HOST2 ...]] "
                "[-S KIND1:VAL1[,OPTS1] [-S KIND2:VAL2[,OPTS2] ...]] "
                "[-d DATASTORE] [-o=OVFTOOL_ARGS]",
            ]),
            formatter_class=argparse.RawDescriptionHelpFormatter,
            help="Deploy to ESXi, vSphere, or vCenter",
            description="Deploy OVF/OVA to ESXi/vCenter/vSphere hypervisor",
            epilog=self.ui.fill_examples([
                ("Deploy to vSphere/ESXi server 192.0.2.100 with credentials"
                 " admin/admin, creating a VM named 'test_vm' from foo.ova.",
                 'cot deploy foo.ova esxi 192.0.2.100 -u admin -p admin'
                 ' -n test_vm'),
                ("Deploy to vSphere/ESXi server 192.0.2.100, with username"
                 " admin (prompting the user to input a password at runtime),"
                 " creating a VM based on profile '1CPU-2.5GB' in foo.ova,"
                 " and creating the serial port as a telnet server listening"
                 " on port 10022 of the host",
                 'cot deploy foo.ova esxi 192.0.2.100 -u admin -c 1CPU-2.5GB'
                 ' -S telnet://:10022,server'),
                ("Deploy to vSphere server 192.0.2.1 which belongs to"
                 " datacenter 'mydc' on vCenter server 192.0.2.100, and map"
                 " the two NIC networks to vSwitches. Note that in this case"
                 " -u specifies the vCenter login username.",
                 'cot deploy foo.ova esxi "192.0.2.100/mydc/host/192.0.2.1"'
                 ' -u administrator -N "GigabitEthernet1=VM Network"'
                 ' -N "GigabitEthernet2=myvswitch"'),
                ("Deploy with passthrough arguments to ovftool.",
                 'cot deploy foo.ova esxi 192.0.2.100 -u admin -p password'
                 ' --ovftool-args="--overwrite --acceptAllEulas"')
            ]))

        # ovftool uses '-ds' as shorthand for '--datastore', so let's allow it.
        parser.add_argument("-d", "-ds", "--datastore",
                            help="ESXi datastore to use for the new VM")

        parser.add_argument(
            "-o", "--ovftool-args",
            help="Quoted string describing additional CLI parameters to pass"
                 """ through to "ovftool". Examples:"""
                 """ -o="--foo", --ovftool-args="--foo --bar" """)

        parser.add_argument("LOCATOR",
                            help="vSphere target locator. Examples: "
                            '"192.0.2.100" (deploy directly to ESXi server), '
                            '"192.0.2.101/mydatacenter/host/192.0.2.100" '
                            '(deploy via vCenter server)')

        parser.set_defaults(instance=self)


command_classes.append(COTDeployESXi)
