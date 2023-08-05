#!/usr/bin/env python
#
# deploy.py - Implements "cot deploy" command
#
# June 2014, Kevin A. Keim
# Copyright (c) 2014-2017, 2019 the COT project developers.
# See the COPYRIGHT.txt file at the top-level directory of this distribution
#
# This file is part of the Common OVF Tool (COT) project.
# It is subject to the license terms in the LICENSE.txt file found in the
# top-level directory of this distribution. No part of COT, including this
# file, may be copied, modified, propagated, or distributed except
# according to the terms contained in the LICENSE.txt file.

"""Module for deploying VM descriptions to a hypervisor to instantiate VMs.

**Classes**

.. autosummary::
  :nosignatures:

  COTDeploy
  SerialConnection
"""

import logging
import re

from COT.data_validation import InvalidInputError, ValueUnsupportedError

from .command import ReadCommand

logger = logging.getLogger(__name__)


class SerialConnection(object):
    """Generic class defining a serial port connection."""

    @classmethod
    def from_cli_string(cls, cli_string):
        """Parse a string 'kind:value[,opts]' to build a SerialConnection.

        Based on the QEMU CLI for serial ports.

        Args:
          cli_string (str): String of the form 'kind:value[,opts]'
        Returns:
          SerialConnection: Created instance or None.
        Raises:
          InvalidInputError: if ``cli_string`` cannot be parsed

        Examples:
          ::

            >>> str(SerialConnection.from_cli_string('/dev/ttyS0'))
            '<SerialConnection kind: device value: /dev/ttyS0 options: {}>'
            >>> str(SerialConnection.from_cli_string('tcp::22,server'))
            "<SerialConnection kind: tcp value: :22 options: {'server': True}>"
            >>> str(SerialConnection.from_cli_string('telnet://1.1.1.1:1111'))
            '<SerialConnection kind: telnet value: 1.1.1.1:1111 options: {}>'

        """
        if cli_string is None:
            return None
        cli_string = cli_string.strip()
        if not cli_string:
            return None
        match = re.match(r"^([a-z]*):?([^ \t,]+),?(.*)$", cli_string)
        if not match:
            raise InvalidInputError("Could not parse string '{0}'"
                                    .format(cli_string))
        options = match.group(3)
        entries = options.split(',')
        options = {}
        for entry in entries:
            if not entry:
                continue
            inner_match = re.match(r"([^=]+)=?(.*)", entry)
            if inner_match:
                key = inner_match.group(1)
                value = inner_match.group(2)
                if not value:
                    value = True
                options[key] = value

        return cls(match.group(1), match.group(2), options)

    @classmethod
    def validate_kind(cls, kind):
        """Validate the connection type string and munge it as needed.

        Args:
          kind (str): Connection type string, possibly in need of munging.
        Returns:
          str: A valid type string
        Raises:
          ValueUnsupportedError: if ``kind`` is not recognized as valid
        """
        kind = kind.lower()
        if kind == '':
            kind = 'device'
        valid_kinds = [
            'device',   # physical serial port like /dev/ttyS0
            'file',     # output to file, no input
            'pipe',     # named pipe
            'tcp',      # raw tcp socket
            'telnet',   # telnet socket
        ]
        if kind in valid_kinds:
            return kind
        else:
            raise ValueUnsupportedError('connection type', kind, valid_kinds)

    @classmethod
    def validate_value(cls, kind, value):
        """Check that the given value is valid for the given connection kind.

        Args:
          kind (str): Connection type, valid per :func:`validate_kind`.
          value (str): Connection value such as '/dev/ttyS0' or '1.1.1.1:80'
        Returns:
          str: Munged value string.
        Raises:
          InvalidInputError: if value string is not recognized as valid
          NotImplementedError: if ``kind`` is not valid
        """
        if kind == 'device' or kind == 'file' or kind == 'pipe':
            # TODO: Validate that device path exists on target?
            # TODO: Validate that datastore and file path exists on target?
            # TODO: Validate that pipe path exists on target?
            return value
        elif kind == 'tcp' or kind == 'telnet':
            # //<host>:<port>
            # //:<port>
            # <host>:<port>
            # :<port>
            match = re.match(r'/?/?(.*:\d+)', value)
            if match:
                return match.group(1)
            raise InvalidInputError("'{0}' is not a valid value for "
                                    "a {1} connection"
                                    .format(value, kind))
        else:
            raise NotImplementedError("No support yet for validating '{0}'"
                                      .format(kind))

    @classmethod
    def validate_options(cls, kind, value, options):
        """Check that the given set of options are valid for this connection.

        Args:
          kind (str): Validated 'kind' string.
          value (str): Validated 'value' string. Currently unused.
          options (dict): Input options dictionary.
        Returns:
          dict: Validated options
        Raises:
          InvalidInputError: if options are not valid.
        """
        # pylint: disable=unused-argument
        if kind == 'file':
            if 'datastore' not in options:
                raise InvalidInputError("For a serial connection to a file, "
                                        "the datastore= option is required")
        return options

    def __init__(self, kind, value, options):
        """Construct a SerialConnection object of the given kind and value.

        Args:
          kind (str): Connection type string, possibly in need of munging.
          value (str): Connection value such as '/dev/ttyS0' or '1.1.1.1:80'
          options (dict): Input options dictionary.
        """
        logger.debug("Creating SerialConnection: "
                     "kind: %s, value: %s, options: %s",
                     kind, value, options)
        self.kind = self.validate_kind(kind)
        """Connection type string"""
        self.value = self.validate_value(self.kind, value)
        """Connection value such as '/dev/ttyS0' or '1.1.1.1:80'"""
        self.options = self.validate_options(self.kind, self.value, options)
        """Dictionary of connection options."""

    def __str__(self):
        """Represent SerialConnection object as a string."""
        return ("<SerialConnection kind: {0} value: {1} options: {2}>"
                .format(self.kind, self.value, self.options))


class COTDeploy(ReadCommand):
    """Semi-abstract class for commands used to deploy a VM to a hypervisor.

    Provides some baseline parameters and input validation that are expected
    to be common across all concrete subclasses.

    Inherited attributes:
    :attr:`~COT.command.Command.ui`,
    :attr:`~COT.command.ReadCommand.package`,

    Attributes:
    :attr:`generic_parser`,
    :attr:`parser`,
    :attr:`subparsers`,
    :attr:`hypervisor`,
    :attr:`configuration`,
    :attr:`username`,
    :attr:`password`,
    :attr:`power_on`,
    :attr:`vm_name`,
    :attr:`network_map`
    """

    def __init__(self, ui):
        """Instantiate this command with the given UI.

        Args:
          ui (UI): User interface instance.
        """
        super(COTDeploy, self).__init__(ui)
        # User inputs
        self._hypervisor = None
        self._configuration = None
        self.username = None
        """Server login username."""
        self.password = None
        """Server login password."""
        self._power_on = False
        self.vm_name = None
        """Name of the created virtual machine"""
        self._network_map = None
        self._serial_connection = []
        # Internal attributes
        self.generic_parser = None
        """Generic parser object providing args that most subclasses will use.

        Subclasses can call
        ``self.subparsers.add_parser(parents=[self.generic_parser])``
        to automatically inherit this set of args
        """
        self.subparsers = None
        """Subparser grouping for hypervisor-specific sub-subparsers.

        Subclasses should generally have their :func:`create_subparser`
        implementations create their sub-subparsers with
        ``parent=``:attr:`subparsers`.
        """

    @property
    def hypervisor(self):
        """Hypervisor to deploy to.

        Raises:
          InvalidInputError: if not a recognized value.
        """
        return self._hypervisor

    @hypervisor.setter
    def hypervisor(self, value):
        if value != "esxi":
            raise InvalidInputError("'{0}' is not a supported hypervisor"
                                    .format(value))
        self._hypervisor = value

    @property
    def configuration(self):
        """VM configuration profile to use for deployment.

        Raises:
          InvalidInputError: if not a profile defined in the VM.
        """
        return self._configuration

    @configuration.setter
    def configuration(self, value):
        if self.vm is not None:
            profiles = self.vm.config_profiles
            if value is not None and value not in profiles:
                raise InvalidInputError(
                    "'Configuration '{0}' is not a recognized "
                    "profile for '{1}'.\nValid options are:\n{2}"
                    .format(value, self.package, "\n".join(profiles)))
        self._configuration = value

    @property
    def power_on(self):
        """Whether to automatically power on the VM after deployment."""
        return self._power_on

    @power_on.setter
    def power_on(self, value):
        if value is not True and value is not False:
            raise InvalidInputError("power_on accepts boolean values only")
        self._power_on = value

    @property
    def network_map(self):
        """Get/set mapping of network names to networks."""
        return self._network_map

    @network_map.setter
    def network_map(self, value):
        for key_value_pair in value:
            try:
                (key, val) = key_value_pair.split('=', 1)
                logger.debug("network_map: key %s value %s", key, val)
                if key == '' or val == '':
                    raise ValueError("message is irrelevant")
                # Don't store the split values for now, as ovftool actually
                # prefers exactly this 'key=value' format. Just validate.
                # TODO - check 'key' against the list of networks in the OVF?
            except ValueError:
                raise InvalidInputError("Invalid network map '{0}' - mapping "
                                        "must be in 'network=target' form."
                                        .format(key_value_pair))
        self._network_map = value

    @property
    def serial_connection(self):
        """Get/set mapping of serial ports to various connection types."""
        return self._serial_connection

    @serial_connection.setter
    def serial_connection(self, value):
        self._serial_connection = []
        for string in value:
            conn = SerialConnection.from_cli_string(string)
            if conn:
                self._serial_connection.append(conn)

    def ready_to_run(self):
        """Check whether the module is ready to :meth:`run`.

        Returns:
          tuple: ``(True, ready_message)`` or ``(False, reason_why_not)``
        """
        if self.hypervisor is None:
            return False, "HYPERVISOR is a mandatory argument"
        return super(COTDeploy, self).ready_to_run()

    def run(self):
        """Do the actual work of this command."""
        super(COTDeploy, self).run()

        # ensure configuration was specified
        # if not specified and force not specified prompt for selection
        profile_list = self.vm.config_profiles

        if profile_list and self.configuration is None:
            if len(profile_list) == 1:
                # No need to prompt the user
                self.configuration = profile_list[0]
                logger.debug("Auto-selected only profile '%s'",
                             self.configuration)
            else:
                header, profile_info_list = self.vm.profile_info_list(
                    self.ui.terminal_width - 1)
                # Correct for the indentation of the list:
                header = "\n".join(["  " + h for h in header.split("\n")])
                self.configuration = self.ui.choose_from_list(
                    header=header,
                    option_list=profile_list,
                    info_list=profile_info_list,
                    footer="Enter configuration name or number",
                    default_value=self.vm.default_config_profile)

        if not self.serial_connection:
            # Get default serial connection information from VM definition.
            self.serial_connection = self.vm.get_serial_connectivity(
                self.configuration)

        serial_count = self.vm.get_serial_count(
            [self.configuration])[self.configuration]
        if len(self.serial_connection) > serial_count:
            self.ui.confirm_or_die(
                "{0} configuration '{1}' defines only {2} serial ports, "
                "but you have given connection information for {3} ports."
                "\nContinue to create additional ports?"
                .format(self.package, self.configuration, serial_count,
                        len(self.serial_connection)))
        elif serial_count > len(self.serial_connection):
            logger.warning("No serial connectivity information is "
                           "available for %d serial port(s) - "
                           "they will not be created or configured.",
                           serial_count - len(self.serial_connection))

    def create_subparser(self):
        """Create 'deploy' CLI subparser if it doesn't already exist.

        .. note::
          Unlike most commands, this one has subparsers of its own -
          ``'cot deploy PACKAGE <hypervisor>'`` so subclasses of this module
          should call ``super().create_subparser()`` (to create the main
          'deploy' subparser if it doesn't already exist) then call
          ``self.ui.add_parser(..., parent=self.subparsers, ...)`` to add
          their own sub-subparser.
        """
        import argparse

        if self.ui.subparser_lookup.get('deploy', None) is None:
            # Create 'cot deploy' parser
            parser = self.ui.add_subparser(
                'deploy',
                usage=self.ui.fill_usage("deploy", [
                    "PACKAGE esxi ...",
                ]),
                help="Create a new VM on the target hypervisor from the "
                "given OVF or OVA",
                description="Deploy an OVF or OVA to create a virtual machine "
                "on a specified server.")

            parser.add_argument('PACKAGE', help="OVF descriptor or OVA file")

            self.subparsers = parser.add_subparsers(
                prog="cot deploy",
                dest='HYPERVISOR',
                metavar='<hypervisor>',
                title="hypervisors")

            parser.set_defaults(instance=self)
        else:
            # Unfortunately argparse doesn't readily expose the subparsers of
            # an existing parser. The below should be considered experimental!
            self.subparsers = next(
                # pylint: disable=protected-access
                action for
                action in self.ui.subparser_lookup['deploy']._actions if
                type(action).name == '_SubParsersAction')

        # Create a generic parser with arguments to be shared by all
        self.generic_parser = argparse.ArgumentParser(add_help=False)

        self.generic_parser.add_argument('-u', '--username',
                                         help="Server login username")

        self.generic_parser.add_argument('-p', '--password',
                                         help="Server login password")

        self.generic_parser.add_argument(
            '-c', '--configuration',
            help="Use the specified configuration profile defined in the OVF. "
            "If unspecified and the OVF has multiple profiles, the user will "
            "be prompted or the default configuration will be used.")

        self.generic_parser.add_argument(
            '-n', '--vm-name',
            help="Name to use for the VM (if applicable) and any files "
            "created. If unspecified, the name of the OVF will be used.")

        self.generic_parser.add_argument(
            '-P', '--power-on', action='store_true',
            help="Power on the created VM to begin booting immediately.")

        self.generic_parser.add_argument(
            '-N', '--network-map', action='append', nargs='+',
            metavar=('OVF_NET1=HOST_NET1', 'OVF_NET2=HOST_NET2'),
            help="Map networks named in the OVF to networks (bridges, "
            "vSwitches, etc.) in the hypervisor environment. This argument "
            "may be repeated as needed to specify multiple mappings.")

        self.generic_parser.add_argument(
            '-S', '--serial-connection', action='append', nargs='+',
            metavar=('K1:V1[,O1]', 'K2:V2[,O2]'),
            help="Set connectivity for a serial port defined in the OVF. "
            "This argument may be repeated to specify more port connections. "
            "Each entry should be structured as 'kind:value' or "
            "'kind:value,options'.")


if __name__ == "__main__":   # pragma: no cover
    import doctest
    doctest.testmod()
