#!/usr/bin/env python
#
# edit_product.py - Implements "edit-product" sub-command
#
# August 2013, Glenn F. Matthews
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

"""Module for editing product information in a VM description.

**Classes**

.. autosummary::
  :nosignatures:

  COTEditProduct
"""

import logging

from .command import command_classes, ReadWriteCommand

logger = logging.getLogger(__name__)


class COTEditProduct(ReadWriteCommand):
    """Edit product, vendor, and version information strings.

    Inherited attributes:
    :attr:`~Command.ui`,
    :attr:`~ReadWriteCommand.package`,
    :attr:`~ReadWriteCommand.output`

    Attributes:
    :attr:`product_class`
    :attr:`product`
    :attr:`vendor`
    :attr:`version`,
    :attr:`full_version`
    :attr:`product_url`
    :attr:`vendor_url`
    :attr:`application_url`
    """

    def __init__(self, ui):
        """Instantiate this command with the given UI.

        Args:
          ui (UI): User interface instance.
        """
        super(COTEditProduct, self).__init__(ui)
        self.product_class = None
        """Product class identifier."""
        self.product = None
        """Product description string."""
        self.vendor = None
        """Vendor string."""
        self.version = None
        """Short version string."""
        self.full_version = None
        """Long version string."""
        self.product_url = None
        """Product URL string."""
        self.vendor_url = None
        """Vendor URL string."""
        self.application_url = None
        """Application URL string."""

    def ready_to_run(self):
        """Check whether the module is ready to :meth:`run`.

        Returns:
          tuple: ``(True, ready_message)`` or ``(False, reason_why_not)``
        """
        if not any([
                self.product_class,
                self.product,
                self.vendor,
                self.version,
                self.full_version,
                self.product_url,
                self.vendor_url,
                self.application_url,
        ]):
            return False, ("No work requested! Please specify at least "
                           "one product information string to update")
        return super(COTEditProduct, self).ready_to_run()

    def run(self):
        """Do the actual work of this command.

        Raises:
          InvalidInputError: if :func:`ready_to_run` reports ``False``
        """
        super(COTEditProduct, self).run()

        if self.product_class is not None:
            logger.verbose("Updating product class from '%s' to '%s'",
                           self.vm.product_class, self.product_class)
            self.vm.product_class = self.product_class

        if self.product is not None:
            logger.verbose("Updating product string from '{0}' to '{1}'"
                           .format(self.vm.product, self.product))
            self.vm.product = self.product

        if self.vendor is not None:
            logger.verbose("Updating vendor string from '{0}' to '{1}'"
                           .format(self.vm.vendor, self.vendor))
            self.vm.vendor = self.vendor

        if self.version is not None:
            logger.verbose("Updating short version string from '{0}' to '{1}'"
                           .format(self.vm.version_short, self.version))
            self.vm.version_short = self.version

        if self.full_version is not None:
            logger.verbose("Updating long version string from '{0}' to '{1}'"
                           .format(self.vm.version_long, self.full_version))
            self.vm.version_long = self.full_version

        if self.product_url is not None:
            logger.verbose("Updating product URL from '{0}' to '{1}'"
                           .format(self.vm.product_url, self.product_url))
            self.vm.product_url = self.product_url

        if self.vendor_url is not None:
            logger.verbose("Updating vendor URL from '{0}' to '{1}'"
                           .format(self.vm.vendor_url, self.vendor_url))
            self.vm.vendor_url = self.vendor_url

        if self.application_url is not None:
            logger.verbose("Updating app URL from '{0}' to '{1}'"
                           .format(self.vm.application_url,
                                   self.application_url))
            self.vm.application_url = self.application_url

    def create_subparser(self):
        """Create 'edit-product' CLI subparser."""
        parser = self.ui.add_subparser(
            'edit-product',
            aliases=['set-product', 'set-version'],
            help="""Edit product info in an OVF""",
            usage=self.ui.fill_usage("edit-product", [
                "PACKAGE [-o OUTPUT] [-c PRODUCT_CLASS] \
[-p PRODUCT] [-n VENDOR] [-v SHORT_VERSION] [-V FULL_VERSION] \
[-u PRODUCT_URL ] [-r VENDOR_URL] [-l APPLICATION_URL]",
            ]),
            description="""
Edit product information attributes of the given OVF or OVA""")

        parser.add_argument('-o', '--output',
                            help="Name/path of new OVF/OVA package to create "
                            "instead of updating the existing OVF")
        parser.add_argument('-c', '--product-class',
                            help='Product class, such as "com.cisco.csr1000v"')
        parser.add_argument('-p', '--product',
                            help='Product name string, such as "Cisco IOS-XE"')
        parser.add_argument(
            '-n', '--vendor',
            help='Vendor string, such as "Cisco Systems, Inc."')
        parser.add_argument('-v', '--version', metavar="SHORT_VERSION",
                            help='Software short version string, such as '
                            '"15.3(4)S" or "5.2.0.01I"')
        parser.add_argument('-V', '--full-version',
                            help='Software long version string, such as '
                            '"Cisco IOS-XE Software, Version 15.3(4)S"')
        parser.add_argument(
            '-u', '--product-url',
            help='Product URL, such as "http://www.cisco.com/go/iosxrv"')
        parser.add_argument('-r', '--vendor-url',
                            help='Vendor URL, such as "http://www.cisco.com"')
        parser.add_argument(
            '-l', '--application-url',
            help='Application URL, such as "https://router1:530/"')
        parser.add_argument('PACKAGE',
                            help="OVF descriptor or OVA file to edit")
        parser.set_defaults(instance=self)


command_classes.append(COTEditProduct)
