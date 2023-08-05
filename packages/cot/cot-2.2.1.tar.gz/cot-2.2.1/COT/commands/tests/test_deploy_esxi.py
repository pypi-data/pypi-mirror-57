#!/usr/bin/env python
#
# test_deploy_esxi.py - test cases for the COTDeployESXi class and helpers
#
# August 2015, Glenn F. Matthews
# Copyright (c) 2013-2017 the COT project developers.
# See the COPYRIGHT.txt file at the top-level directory of this distribution
# and at https://github.com/glennmatthews/cot/blob/master/COPYRIGHT.txt.
#
# This file is part of the Common OVF Tool (COT) project.
# It is subject to the license terms in the LICENSE.txt file found in the
# top-level directory of this distribution and at
# https://github.com/glennmatthews/cot/blob/master/LICENSE.txt. No part
# of COT, including this file, may be copied, modified, propagated, or
# distributed except according to the terms contained in the LICENSE.txt file.

"""Unit test cases for the COT.deploy.COTDeployESXi class and helpers."""

import errno
import getpass
import logging
import re
import socket
import ssl
from distutils.version import StrictVersion

import mock
import requests
from pyVmomi import vim

try:
    import unittest2 as unittest
except ImportError:
    import unittest

from COT.tests import COTTestCase
from COT.commands.tests.command_testcase import CommandTestCase
import COT.commands.deploy_esxi
from COT.commands.deploy_esxi import COTDeployESXi, SmarterConnection
from COT.data_validation import InvalidInputError

logger = logging.getLogger(__name__)

# pylint: disable=missing-param-doc,missing-type-doc


@mock.patch('COT.ui.UI.get_password', return_value='passwd')
@mock.patch('subprocess.check_call')
class TestCOTDeployESXi(CommandTestCase):
    """Test cases for COTDeployESXi class."""

    # Some WARNING logger messages we may expect at various points:
    SERIAL_PORT_NOT_FIXED = {
        'levelname': 'WARNING',
        'msg': 'serial port.*will not be created or configured',
    }
    VSPHERE_ENV_WARNING = {
        'levelname': 'WARNING',
        'msg': "deploying.*vSphere.*power-on.*environment properties.*ignored",
    }
    OVFTOOL_VER_TOO_LOW = {
        'levelname': 'WARNING',
        'msg': "ovftool version is too low.*environment properties.*ignored",
    }
    BAD_CERTIFICATE = {
        'levelname': 'WARNING',
        'msg': "certificate verify failed",
    }
    SESSION_FAILED = {
        'levelname': 'ERROR',
        'msg': "Session failed",
    }

    command_class = COTDeployESXi

    # pylint thinks self.command is a Command instead of a COTDeployESXi,
    # so tell it to be quiet about members specific to COTDeployESXi:
    # pylint: disable=no-member

    def setUp(self):
        """Test case setup function called automatically prior to each test."""
        super(TestCOTDeployESXi, self).setUp()
        self.command.package = self.input_ovf
        self.command.hypervisor = 'esxi'
        # Stub out all ovftool dependencies
        # pylint: disable=protected-access
        self._ovftool_path = self.command.ovftool._path
        self._ovftool_version = self.command.ovftool._version
        self.command.ovftool._path = "/fake/ovftool"
        self.command.ovftool._version = StrictVersion("4.0.0")

    def tearDown(self):
        """Test case cleanup function called automatically."""
        # Remove our stub
        # pylint: disable=protected-access
        self.command.ovftool._path = self._ovftool_path
        self.command.ovftool._version = self._ovftool_version
        super(TestCOTDeployESXi, self).tearDown()

    def test_not_ready_with_no_args(self, *_):
        """Verify ready_to_run() is False without all mandatory args."""
        ready, reason = self.command.ready_to_run()
        self.assertEqual(ready, False)
        self.assertTrue(re.search("LOCATOR.*mandatory", reason))
        self.assertRaises(InvalidInputError, self.command.run)

        self.command.locator = "localhost"
        self.command.package = None
        ready, reason = self.command.ready_to_run()
        self.assertEqual(ready, False)
        self.assertTrue(re.search("PACKAGE.*mandatory", reason))
        self.assertRaises(InvalidInputError, self.command.run)

    def test_invalid_args(self, *_):
        """Negative tests for various arguments."""
        with self.assertRaises(InvalidInputError):
            self.command.configuration = ""
        with self.assertRaises(InvalidInputError):
            self.command.configuration = "X"
        with self.assertRaises(InvalidInputError):
            self.command.power_on = "frobozz"

    def test_ovftool_args_basic(self, mock_check_call, *_):
        """Test that ovftool is called with the basic arguments."""
        self.command.locator = "localhost"
        self.command.run()
        mock_check_call.assert_called_once_with([
            'ovftool',
            '--deploymentOption=4CPU-4GB-3NIC',    # default configuration
            '--name=input',
            self.input_ovf,
            'vi://{user}:passwd@localhost'.format(user=getpass.getuser())
        ])
        self.assertLogged(**self.VSPHERE_ENV_WARNING)
        self.assertLogged(**self.SERIAL_PORT_NOT_FIXED)

    def test_ovftool_args_advanced(self, mock_check_call, *_):
        """Test that ovftool is called with more involved arguments."""
        self.command.locator = "localhost/host/foo"
        self.command.datastore = "datastore1"
        self.command.configuration = "2CPU-2GB-1NIC"
        self.command.vm_name = "myVM"
        self.command.power_on = True
        self.command.ovftool_args = "--overwrite --vService:'A B=C D'"
        self.command.username = "u"
        self.command.password = "p"
        self.command.network_map = ["VM Network=VM Network"]

        self.command.run()
        mock_check_call.assert_called_once_with([
            'ovftool',
            '--overwrite',
            '--vService:A B=C D',
            '--deploymentOption=2CPU-2GB-1NIC',
            '--net:VM Network=VM Network',
            '--name=myVM',
            '--powerOn',
            '--datastore=datastore1',
            self.input_ovf,
            'vi://u:p@localhost/host/foo',
        ])
        self.assertLogged(**self.SERIAL_PORT_NOT_FIXED)

    def test_ovftool_vsphere_env_fixup(self, mock_check_call, *_):
        """Test fixup of environment when deploying directly to vSphere."""
        # With 4.0.0 (our default) and no power_on, there's no fixup.
        # This is tested by test_ovftool_args_basic() above.

        # With 4.0.0 and power_on, we fixup when deploying to vSphere:
        self.command.locator = "vsphere"
        self.command.power_on = True
        self.command.run()
        mock_check_call.assert_called_once_with([
            'ovftool',
            '--X:injectOvfEnv',
            '--deploymentOption=4CPU-4GB-3NIC',     # default configuration
            '--name=input',
            '--powerOn',
            self.input_ovf,
            'vi://{user}:passwd@vsphere'.format(user=getpass.getuser()),
        ])
        self.assertLogged(**self.SERIAL_PORT_NOT_FIXED)
        # Make sure we DON'T see the ENV_WARNING message
        self.logging_handler.assertNoLogsOver(logging.INFO)

        # With 4.0.0, we don't (need to) fixup when deploying to vCenter.
        # This is tested by test_ovftool_args_advanced() above.

        # With <4.0.0, we don't (can't) fixup, regardless.
        # Discard cached information and update the info that will be returned
        # pylint: disable=protected-access
        mock_check_call.reset_mock()
        self.command.ovftool._version = StrictVersion("3.5.0")
        self.command.run()
        mock_check_call.assert_called_once_with([
            'ovftool',
            # Nope! #'--X:injectOvfEnv',
            '--deploymentOption=4CPU-4GB-3NIC',     # default configuration
            '--name=input',
            '--powerOn',
            self.input_ovf,
            'vi://{user}:passwd@vsphere'.format(user=getpass.getuser()),
        ])
        self.assertLogged(**self.OVFTOOL_VER_TOO_LOW)
        self.assertLogged(**self.SERIAL_PORT_NOT_FIXED)

    def test_serial_fixup_invalid_host(self, *_):
        """Failure in fixup_serial_ports() connecting to an invalid host."""
        self.command.locator = "localhost"
        self.command.serial_connection = ['tcp::2222', 'tcp::2223']
        # pyvmomi 6.0.0.2016 and earlier raises ConnectionError,
        # pyvmomi 6.0.0.2016.4 and later raises socket.error
        with self.assertRaises((requests.exceptions.ConnectionError,
                                socket.error)) as catcher:
            self.command.run()
        # In requests 2.7 and earlier, we get the errno,
        # while in requests 2.8+, it's munged into a string only
        if catcher.exception.errno is not None:
            self.assertEqual(catcher.exception.errno, errno.ECONNREFUSED)
        self.assertRegex(
            catcher.exception.strerror,
            "(Error connecting to localhost:443: )?.*Connection refused")
        self.assertLogged(**self.VSPHERE_ENV_WARNING)

    mock_si = mock.create_autospec(
        COT.commands.deploy_esxi.vim.ServiceInstance)
    mock_sic = mock.create_autospec(
        COT.commands.deploy_esxi.vim.ServiceInstanceContent)
    mock_si.RetrieveContent.return_value = mock_sic
    mock_sic.rootFolder = 'vim.Folder:group-d1'

    mock_v = mock.create_autospec(COT.commands.deploy_esxi.vim.ViewManager)
    mock_sic.viewManager = mock_v

    mock_cv = mock.create_autospec(
        COT.commands.deploy_esxi.vim.view.ContainerView)
    mock_v.CreateContainerView.return_value = mock_cv

    @mock.patch('pyVim.connect.__FindSupportedVersion', return_value=['vim25'])
    @mock.patch('pyVim.connect.__Login', return_value=(mock_si, None))
    def test_serial_fixup_stubbed(self, *_):
        """Test fixup_serial_ports by mocking pyVmomi library."""
        self.command.locator = "localhost"
        self.command.vm_name = "mockery"

        mock_vm0 = mock.create_autospec(
            COT.commands.deploy_esxi.vim.VirtualMachine)
        mock_vm0.name = "wrong_vm"
        mock_vm = mock.create_autospec(
            COT.commands.deploy_esxi.vim.VirtualMachine)
        mock_vm.name = self.command.vm_name
        self.mock_cv.view = [mock_vm0, mock_vm]

        self.command.serial_connection = ['tcp:localhost:2222',
                                          'tcp::2223,server',
                                          '/dev/ttyS0']
        self.command.run()
        self.assertLogged(**self.VSPHERE_ENV_WARNING)

        self.assertTrue(mock_vm.ReconfigVM_Task.called)
        # TODO: any other validation of args or kwargs?
        _args, kwargs = mock_vm.ReconfigVM_Task.call_args
        spec = kwargs['spec']
        self.assertEqual(3, len(spec.deviceChange))
        change1, change2, change3 = spec.deviceChange
        self.assertEqual('add', change1.operation)
        self.assertEqual('add', change2.operation)
        self.assertEqual('add', change3.operation)
        self.assertEqual('tcp://localhost:2222',
                         change1.device.backing.serviceURI)
        self.assertEqual('client', change1.device.backing.direction)
        self.assertEqual('tcp://:2223', change2.device.backing.serviceURI)
        self.assertEqual('server', change2.device.backing.direction)
        self.assertEqual('/dev/ttyS0', change3.device.backing.deviceName)

        self.command.serial_connection = [
            'file:/tmp/foo.txt,datastore=datastore1'
        ]
        self.assertRaises(NotImplementedError,
                          self.command.run)
        self.assertLogged(**self.VSPHERE_ENV_WARNING)
        self.assertLogged(**self.SERIAL_PORT_NOT_FIXED)
        self.assertLogged(**self.SESSION_FAILED)

    @mock.patch('pyVim.connect.__FindSupportedVersion', return_value=['vim25'])
    @mock.patch('pyVim.connect.__Login', return_value=(mock_si, None))
    @mock.patch('COT.ui.UI.confirm_or_die', return_value=True)
    def test_serial_fixup_stubbed_create(self, mock_cod, *_):
        """Test fixup_serial_ports creation of serial ports not in the OVF."""
        self.command.package = self.minimal_ovf
        self.command.locator = "localhost"
        self.command.vm_name = "mockery"

        mock_vm = mock.create_autospec(
            COT.commands.deploy_esxi.vim.VirtualMachine)
        mock_vm.name = self.command.vm_name
        self.mock_cv.view = [mock_vm]

        self.command.serial_connection = ['tcp:localhost:2222']
        self.command.run()

        self.assertTrue(mock_vm.ReconfigVM_Task.called)
        self.assertTrue(mock_cod.called)
        # TODO: any other validation of args or kwargs?
        _args, kwargs = mock_vm.ReconfigVM_Task.call_args
        spec = kwargs['spec']
        self.assertEqual(1, len(spec.deviceChange))
        change1 = spec.deviceChange[0]
        self.assertEqual('add', change1.operation)
        self.assertEqual('tcp://localhost:2222',
                         change1.device.backing.serviceURI)
        self.assertEqual('client', change1.device.backing.direction)

    @mock.patch('pyVim.connect.__FindSupportedVersion', return_value=['vim25'])
    @mock.patch('pyVim.connect.__Login', return_value=(mock_si, None))
    def test_serial_fixup_stubbed_vm_not_found(self, *_):
        """Test fixup_serial_ports error case where the VM isn't found."""
        self.command.locator = "localhost"
        self.command.vm_name = "mockery"

        mock_vm0 = mock.create_autospec(
            COT.commands.deploy_esxi.vim.VirtualMachine)
        mock_vm0.name = "wrong_vm"
        mock_vm1 = mock.create_autospec(
            COT.commands.deploy_esxi.vim.VirtualMachine)
        mock_vm1.name = "also_wrong"
        self.mock_cv.view = [mock_vm0, mock_vm1]

        self.command.serial_connection = ['tcp:localhost:2222',
                                          'tcp::2223,server',
                                          '/dev/ttyS0']
        self.assertRaises(LookupError, self.command.run)
        self.assertLogged(**self.VSPHERE_ENV_WARNING)
        self.assertLogged(**self.SESSION_FAILED)

    @mock.patch('COT.commands.deploy_esxi.SmartConnection.__enter__')
    @unittest.skipUnless(hasattr(ssl, '_create_unverified_context'),
                         "Only applicable to Python 2.7+ and 3.4+")
    def test_serial_fixup_ssl_failure(self, mock_parent, *_):
        """Test SSL failure in pyVmomi."""
        mock_parent.side_effect = vim.fault.HostConnectFault(
            msg="certificate verify failed")
        self.command.locator = "localhost"
        self.command.serial_connection = ['tcp://localhost:2222']
        # Try twice - first time with default behavior encounters certificate
        # failure, second time (with self-signed certificates accepted)
        # encounters the same error again and raises it
        self.assertRaises(vim.fault.HostConnectFault,
                          self.command.fixup_serial_ports)
        self.assertEqual(mock_parent.call_count, 2)
        self.assertLogged(**self.BAD_CERTIFICATE)

    @mock.patch('COT.commands.deploy_esxi.SmartConnection.__enter__')
    def test_serial_fixup_other_hostconnectfault(self, mock_parent, *_):
        """Test HostConnectFault other than SSL failure."""
        mock_parent.side_effect = vim.fault.HostConnectFault(
            msg="Malformed response while querying for local ticket: foo")
        self.command.locator = "localhost"
        self.command.serial_connection = ['tcp://localhost:2222']
        # Try once and fail immediately
        self.assertRaises(vim.fault.HostConnectFault,
                          self.command.fixup_serial_ports)
        self.assertEqual(mock_parent.call_count, 1)

    @mock.patch('COT.commands.deploy_esxi.SmartConnection.__enter__')
    def test_serial_fixup_connectionerror(self, mock_parent, *_):
        """Test generic ConnectionError handling."""
        mock_parent.side_effect = requests.exceptions.ConnectionError
        self.command.locator = "localhost"
        self.command.serial_connection = ['tcp://localhost:2222']
        with self.assertRaises(requests.exceptions.ConnectionError) as catcher:
            self.command.fixup_serial_ports()
        self.assertEqual(catcher.exception.errno, None)
        self.assertEqual(catcher.exception.strerror,
                         "Error connecting to localhost:443: None")


class TestSmarterConnection(COTTestCase):
    """Test cases for SmarterConnection class methods."""

    def test_unwrap_connection_error_27(self):
        """Unwrap an error like a ConnectionError raised by requests 2.7."""
        errnum, inner_message = SmarterConnection.unwrap_connection_error(
            IOError(
                Exception(
                    'Connection aborted.',
                    IOError(61, 'Connection refused')
                )
            )
        )
        self.assertEqual(errnum, 61)
        self.assertEqual(inner_message, "Connection refused")

    class MaxRetryError28(Exception):
        """Mock of requests 2.8 MaxRetryError exception class."""

        def __init__(self, pool, url, reason):
            """Create fake exception."""
            self.pool = pool
            self.url = url
            self.reason = reason
            self.message = ("Max retries exceeded with url: %s (Caused by %r)"
                            % (url, reason))
            super(self.__class__, self).__init__("%s: %s" %
                                                 (pool, self.message))

    class NewConnectionError28(Exception):
        """Mock of requests 2.8 NewConnectionError exception class."""

        def __init__(self, pool, message):
            """Create fake exception."""
            self.pool = pool
            self.message = message
            super(self.__class__, self).__init__("%s: %s" % (pool, message))

    def test_unwrap_connection_error_28(self):
        """Unwrap an error like a ConnectionError raised by requests 2.8."""
        errnum, inner_message = SmarterConnection.unwrap_connection_error(
            self.MaxRetryError28(
                pool="HTTPSConnectionPool(host='localhost', port=443)",
                url="//sdk/vimServiceVersions.xml",
                reason=self.NewConnectionError28(
                    pool="VerifiedHTTPSConnection",
                    message="Failed to establish a new connection: "
                    "[Errno 61] Connection refused")
            )
        )
        self.assertEqual(errnum, None)
        self.assertEqual(inner_message,
                         "Failed to establish a new connection: "
                         "[Errno 61] Connection refused")
