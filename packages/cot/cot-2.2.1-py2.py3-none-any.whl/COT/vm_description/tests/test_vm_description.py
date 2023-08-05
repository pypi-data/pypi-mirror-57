# vm_description.py - Unit test cases for generic VMDescription class
#
# January 2015, Glenn F. Matthews
# Copyright (c) 2015-2017 the COT project developers.
# See the COPYRIGHT.txt file at the top-level directory of this distribution
# and at https://github.com/glennmatthews/cot/blob/master/COPYRIGHT.txt.
#
# This file is part of the Common OVF Tool (COT) project.
# It is subject to the license terms in the LICENSE.txt file found in the
# top-level directory of this distribution and at
# https://github.com/glennmatthews/cot/blob/master/LICENSE.txt. No part
# of COT, including this file, may be copied, modified, propagated, or
# distributed except according to the terms contained in the LICENSE.txt file.

"""Unit test cases for the COT.vm_description.VMDescription class."""

import os.path
from pkg_resources import resource_filename
try:
    import unittest2 as unittest
except ImportError:
    import unittest

import mock

from COT.vm_description import VMDescription
from COT.data_validation import ValueUnsupportedError

# pylint: disable=missing-type-doc,missing-param-doc


class TestVMDescription(unittest.TestCase):
    """Test cases for abstract VMDescription class."""

    TEXT_FILE = resource_filename(__name__, 'sample_cfg.txt')

    @mock.patch("os.path.exists", return_value=True)
    @mock.patch("os.path.isdir", return_value=True)
    @mock.patch("tempfile.mkdtemp", return_value="/foo/bar")
    @mock.patch("shutil.rmtree")
    @mock.patch("COT.vm_description.VMDescription.write")
    def test_context_manager(self, write, rmtree, *_):
        """Verify context manager logic."""
        # Successful exit - write() is called and working_dir is cleaned up
        with VMDescription("foo.txt", None):
            pass
        write.assert_called_once()
        rmtree.assert_called_once_with("/foo/bar")

        write.reset_mock()
        rmtree.reset_mock()

        # Error exit - cleanup still happens but write() is not called
        with self.assertRaises(RuntimeError):
            with VMDescription("foo.txt", None):
                raise RuntimeError("Gotcha!")
        write.assert_not_called()
        rmtree.assert_called_once_with("/foo/bar")

    def test_generic_class_apis(self):
        """Verify class APIs with generic implementations."""
        self.assertRaises(ValueUnsupportedError,
                          VMDescription.detect_type_from_name,
                          self.TEXT_FILE)

    def test_abstract_io_apis(self):
        """Get NotImplementedError from abstract I/O APIs."""
        ins = VMDescription(self.TEXT_FILE, self.TEXT_FILE)

        self.assertRaises(NotImplementedError,
                          ins.write)

        self.assertRaises(NotImplementedError, ins.predicted_output_size)

        ins.destroy()
        self.assertFalse(os.path.exists(ins.working_dir))

    def test_abstract_info_apis(self):
        """Get NotImplementedError from abstract info APIs."""
        ins = VMDescription(self.TEXT_FILE, None)

        with self.assertRaises(NotImplementedError):
            assert ins.platform
        self.assertRaises(NotImplementedError,
                          ins.info_string)
        self.assertRaises(NotImplementedError,
                          ins.profile_info_string)

        ins.destroy()
        self.assertFalse(os.path.exists(ins.working_dir))

    def test_abstract_disk_file_apis(self):
        """Get NotImplementedError from abstract disk and file APIs."""
        ins = VMDescription(self.TEXT_FILE, None)

        self.assertRaises(NotImplementedError,
                          ins.search_from_filename, self.TEXT_FILE)
        self.assertRaises(NotImplementedError,
                          ins.search_from_file_id, None)
        self.assertRaises(NotImplementedError,
                          ins.search_from_controller, None, None)
        self.assertRaises(NotImplementedError,
                          ins.find_open_controller, None)
        self.assertRaises(NotImplementedError,
                          ins.get_id_from_file, None)
        self.assertRaises(NotImplementedError,
                          ins.get_path_from_file, None)
        self.assertRaises(NotImplementedError,
                          ins.get_file_ref_from_disk, None)
        self.assertRaises(NotImplementedError,
                          ins.get_id_from_disk, None)
        self.assertRaises(NotImplementedError,
                          ins.get_common_subtype, None)
        self.assertRaises(NotImplementedError,
                          ins.check_sanity_of_disk_device,
                          None, None, None, None)
        self.assertRaises(NotImplementedError,
                          ins.add_file, self.TEXT_FILE, None)
        self.assertRaises(NotImplementedError,
                          ins.remove_file, self.TEXT_FILE)
        self.assertRaises(NotImplementedError,
                          ins.remove_file, self.TEXT_FILE, None)
        self.assertRaises(NotImplementedError,
                          ins.remove_file, self.TEXT_FILE, None, None)
        self.assertRaises(NotImplementedError,
                          ins.add_disk, self.TEXT_FILE, None, None)
        self.assertRaises(NotImplementedError,
                          ins.add_controller_device, None, None, None)
        self.assertRaises(NotImplementedError,
                          ins.add_disk_device,
                          None, None, None, None, None, None, None)
        self.assertRaises(NotImplementedError,
                          ins.find_empty_drive, None)

        ins.destroy()
        self.assertFalse(os.path.exists(ins.working_dir))

    def test_abstract_hardware_apis(self):
        """Get NotImplementedError from abstract hardware APIs."""
        ins = VMDescription(self.TEXT_FILE, None)

        with self.assertRaises(NotImplementedError):
            ins.validate_hardware()
        with self.assertRaises(NotImplementedError):
            assert ins.config_profiles
        with self.assertRaises(NotImplementedError):
            assert ins.default_config_profile
        self.assertRaises(NotImplementedError,
                          ins.create_configuration_profile,
                          None, None, None)
        self.assertRaises(NotImplementedError,
                          ins.delete_configuration_profile, None)
        with self.assertRaises(NotImplementedError):
            assert ins.system_types
        with self.assertRaises(NotImplementedError):
            ins.system_types = ["hello", "world"]
        self.assertRaises(NotImplementedError,
                          ins.set_cpu_count, 0, None)
        self.assertRaises(NotImplementedError,
                          ins.set_memory, 0, None)
        self.assertRaises(NotImplementedError,
                          ins.set_nic_type, None, None)
        self.assertRaises(NotImplementedError,
                          ins.set_nic_types, None, None)
        self.assertRaises(NotImplementedError,
                          ins.get_nic_count, None)
        self.assertRaises(NotImplementedError,
                          ins.set_nic_count, 0, None)
        with self.assertRaises(NotImplementedError):
            assert ins.networks
        with self.assertRaises(NotImplementedError):
            assert ins.network_descriptions
        self.assertRaises(NotImplementedError,
                          ins.create_network, None, None)
        self.assertRaises(NotImplementedError,
                          ins.set_nic_networks, None, None)
        self.assertRaises(NotImplementedError,
                          ins.set_nic_mac_addresses, None, None)
        self.assertRaises(NotImplementedError,
                          ins.set_nic_names, None, None)
        self.assertRaises(NotImplementedError,
                          ins.get_serial_count, None)
        self.assertRaises(NotImplementedError,
                          ins.set_serial_count, 0, None)
        self.assertRaises(NotImplementedError,
                          ins.get_serial_connectivity, None)
        self.assertRaises(NotImplementedError,
                          ins.set_serial_connectivity, None, None)
        self.assertRaises(NotImplementedError,
                          ins.set_scsi_subtype, None, None)
        self.assertRaises(NotImplementedError,
                          ins.set_ide_subtype, None, None)
        self.assertRaises(NotImplementedError,
                          ins.find_device_location, None)

        ins.destroy()
        self.assertFalse(os.path.exists(ins.working_dir))

    def test_abstract_product_apis(self):
        """Get NotImplementedError from abstract product APIs."""
        ins = VMDescription(self.TEXT_FILE, None)

        with self.assertRaises(NotImplementedError):
            assert ins.version_short
        with self.assertRaises(NotImplementedError):
            ins.version_short = "hello"
        with self.assertRaises(NotImplementedError):
            assert ins.version_long
        with self.assertRaises(NotImplementedError):
            ins.version_long = "hello world!"

        ins.destroy()
        self.assertFalse(os.path.exists(ins.working_dir))

    def test_abstract_property_apis(self):
        """Get NotImplementedError from abstract property APIs."""
        ins = VMDescription(self.TEXT_FILE, None)

        with self.assertRaises(NotImplementedError):
            assert ins.environment_properties
        with self.assertRaises(NotImplementedError):
            assert ins.environment_transports
        with self.assertRaises(NotImplementedError):
            ins.environment_transports = ['iso']
        self.assertRaises(NotImplementedError,
                          ins.get_property_value, None)
        self.assertRaises(NotImplementedError,
                          ins.set_property_value, None, None)
        self.assertRaises(NotImplementedError,
                          ins.config_file_to_properties, self.TEXT_FILE)

        ins.destroy()
        self.assertFalse(os.path.exists(ins.working_dir))

    def test_generic_instance_apis(self):
        """Verify APIs with generic implementations."""
        ins = VMDescription(self.TEXT_FILE, None)
        self.assertEqual(ins.input_file, self.TEXT_FILE)
        self.assertEqual(ins.output_file, None)
        self.assertTrue(os.path.exists(ins.working_dir))

        ins.output_file = self.TEXT_FILE
        self.assertEqual(ins.output_file, self.TEXT_FILE)

        ins.product_class = 'generic'
        self.assertEqual(ins.product_class, 'generic')

        out = ins.convert_disk_if_needed(self.TEXT_FILE, None)
        self.assertEqual(out, self.TEXT_FILE)

        ins.destroy()
        self.assertFalse(os.path.exists(ins.working_dir))
