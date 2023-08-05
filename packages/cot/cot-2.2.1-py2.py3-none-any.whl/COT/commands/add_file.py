#!/usr/bin/env python
#
# add_file.py - Implements "cot add-file" command
#
# October 2013, Glenn F. Matthews
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

"""Module for adding files to VM definitions.

.. autosummary::
  COTAddFile
"""

import os.path
import logging

from COT.data_validation import check_for_conflict, InvalidInputError
from .command import command_classes, ReadWriteCommand

logger = logging.getLogger(__name__)


class COTAddFile(ReadWriteCommand):
    """Add a file (such as a README) to the package.

    Inherited attributes:
    :attr:`~Command.ui`,
    :attr:`~ReadWriteCommand.package`,
    :attr:`~ReadWriteCommand.output`

    Attributes:
    :attr:`file`,
    :attr:`file_id`
    """

    def __init__(self, ui):
        """Instantiate this command with the given UI.

        Args:
          ui (UI): User interface instance.
        """
        super(COTAddFile, self).__init__(ui)
        self._file = None
        self.file_id = None
        """File identifier string."""

    @property
    def file(self):
        """File to be added to the package.

        Raises:
          InvalidInputError: if the file does not exist.
        """
        return self._file

    @file.setter
    def file(self, value):
        if not os.path.exists(value):
            raise InvalidInputError("Specified file '{0}' does not exist!"
                                    .format(value))
        self._file = value

    def ready_to_run(self):
        """Check whether the module is ready to :meth:`run`.

        Returns:
          tuple: ``(True, ready_message)`` or ``(False, reason_why_not)``
        """
        if self.file is None:
            return False, "FILE is a mandatory argument!"
        return super(COTAddFile, self).ready_to_run()

    def run(self):
        """Do the actual work of this command.

        Raises:
          InvalidInputError: if :func:`ready_to_run` reports ``False``
        """
        super(COTAddFile, self).run()

        vm = self.vm

        filename = os.path.basename(self.file)
        (file_obj, _, _, _) = vm.search_from_filename(filename)
        if self.file_id is not None:
            (file_obj2, _, _, _) = vm.search_from_file_id(self.file_id)
            file_obj = check_for_conflict("File to overwrite",
                                          [file_obj, file_obj2])
        if self.file_id is None:
            if file_obj is not None:
                self.file_id = vm.get_id_from_file(file_obj)
            else:
                self.file_id = filename

        if file_obj is not None:
            self.ui.confirm_or_die("Replace existing file {0} with {1}?"
                                   .format(vm.get_path_from_file(file_obj),
                                           self.file))
            logger.notice("Overwriting existing File in OVF")

        vm.add_file(self.file, self.file_id, file_obj)

    def create_subparser(self):
        """Create 'add-file' CLI subparser."""
        parser = self.ui.add_subparser(
            'add-file',
            usage=self.ui.fill_usage("add-file", [
                "FILE PACKAGE [-o OUTPUT] [-f FILE_ID]",
            ]),
            help="Add a file to an OVF package",
            description="""
Add or replace a file in the given OVF. If the specified file
and/or file-id match existing package contents, will replace it
(prompting for confirmation if --force was not set); otherwise, will
create a new file entry.""")

        parser.add_argument('-o', '--output',
                            help="""Name/path of new VM package to create """
                            """instead of updating the existing package""")
        parser.add_argument('-f', '--file-id',
                            help="""File ID string within the package """
                            """(default: same as filename)""")
        parser.add_argument('FILE', help="""File to add to the package""")
        parser.add_argument('PACKAGE',
                            help="Package, OVF descriptor or OVA file to edit")
        parser.set_defaults(instance=self)


command_classes.append(COTAddFile)
