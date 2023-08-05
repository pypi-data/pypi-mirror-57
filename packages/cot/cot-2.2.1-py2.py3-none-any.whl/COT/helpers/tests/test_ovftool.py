#!/usr/bin/env python
#
# test_ovftool.py - Unit test cases for COT.helpers.ovftool submodule.
#
# March 2015, Glenn F. Matthews
# Copyright (c) 2014-2017 the COT project developers.
# See the COPYRIGHT.txt file at the top-level directory of this distribution
# and at https://github.com/glennmatthews/cot/blob/master/COPYRIGHT.txt.
#
# This file is part of the Common OVF Tool (COT) project.
# It is subject to the license terms in the LICENSE.txt file found in the
# top-level directory of this distribution and at
# https://github.com/glennmatthews/cot/blob/master/LICENSE.txt. No part
# of COT, including this file, may be copied, modified, propagated, or
# distributed except according to the terms contained in the LICENSE.txt file.

"""Unit test cases for the COT.helpers.ovftool submodule."""

import mock

from COT.helpers.tests.test_helper import HelperTestCase
from COT.helpers.ovftool import OVFTool

# pylint: disable=missing-type-doc,missing-param-doc,protected-access


class TestOVFTool(HelperTestCase):
    """Test cases for OVFTool helper class."""

    def setUp(self):
        """Test case setup function called automatically prior to each test."""
        self.helper = OVFTool()
        super(TestOVFTool, self).setUp()

    @mock.patch('COT.helpers.helper.check_output',
                return_value="Error: Unknown option: 'version'")
    @mock.patch('distutils.spawn.find_executable',
                return_value="/fake/ovftool")
    def test_invalid_version(self, *_):
        """Negative test for .version getter logic."""
        self.helper._installed = True
        with self.assertRaises(RuntimeError):
            assert self.helper.version

    @mock.patch('distutils.spawn.find_executable',
                return_value="/fake/ovftool")
    @mock.patch('COT.helpers.helper.check_output')
    @mock.patch('subprocess.check_call')
    def test_install_already_present(self, mock_check_call,
                                     mock_check_output, *_):
        """Do nothing when trying to re-install."""
        self.helper._installed = True
        self.helper.install()
        mock_check_call.assert_not_called()
        mock_check_output.assert_not_called()

    def test_install_helper_unsupported(self):
        """No support for automated installation of ovftool."""
        with mock.patch('COT.helpers.ovftool.OVFTool.path',
                        new_callable=mock.PropertyMock, return_value=None):
            with self.assertRaises(NotImplementedError):
                self.helper.install()
