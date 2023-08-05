#!/usr/bin/env python
#
# install_helpers.py - Implements "cot install-helpers" command
#
# February 2015, Glenn F. Matthews
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

"""Implements "install-helpers" command."""

from __future__ import print_function

import argparse
import filecmp
import logging
import os
import sys
import textwrap
from pkg_resources import resource_listdir, resource_filename

from COT.helpers import Helper, HelperError, HelperNotFoundError, helpers
from .command import command_classes, Command

logger = logging.getLogger(__name__)


def guess_manpath():
    """Guess the directory path where man pages should be installed."""
    # If COT is installed in /foo/bar/bin/cot, man pages go in /foo/bar/man
    bin_dir = os.path.dirname(os.path.abspath(sys.argv[0]))
    logger.debug("invoked from directory: %s", sys.argv[0])
    if os.path.basename(bin_dir) == 'bin':
        man_dir = os.path.join(os.path.dirname(bin_dir), "man")
        logger.verbose("Program install directory %s matches 'bin', "
                       "so assume relative man path %s", bin_dir, man_dir)
    else:
        man_dir = "/usr/local/man"
        logger.verbose("Program install directory {0} does not appear "
                       "to be 'bin', assuming system install path {0}"
                       .format(man_dir))
    return man_dir


def verify_manpages(man_dir):
    """Verify installation of COT's manual pages.

    Args:
      man_dir (str): Base directory where manpages should be found.
    Returns:
      tuple: (result, message)
    """
    for filename in resource_listdir("COT", "docs/man"):
        src_path = resource_filename("COT", os.path.join("docs/man", filename))
        # Which man section does this belong in?
        section = os.path.splitext(filename)[1][1:]
        dest = os.path.join(man_dir, "man{0}".format(section))
        if not os.path.exists(dest):
            return True, "DIRECTORY NOT FOUND: {0}".format(dest)

        dest_path = os.path.join(dest, filename)
        if os.path.exists(dest_path):
            if filecmp.cmp(src_path, dest_path):
                logger.verbose("File %s does not need to be updated",
                               dest_path)
                continue
            logger.verbose("File %s needs to be updated", dest_path)
            return True, "NEEDS UPDATE"
        return True, "NOT FOUND"

    return True, "already installed, no updates needed"


def _install_manpage(src_path, man_dir):
    """Install the given manual page for COT.

    Args:
      src_path (str): Path to manual page file.
      man_dir (str): Base directory where page should be installed.
    Returns:
      tuple: (page_previously_installed, page_updated)
    Raises:
      IOError: if installation fails under some circumstances
      OSError: if installation fails under other circumstances
    """
    # Which man section does this belong in?
    filename = os.path.basename(src_path)
    section = os.path.splitext(filename)[1][1:]
    dest = os.path.join(man_dir, "man{0}".format(section))
    Helper.mkdir(dest)

    previously_installed = False
    dest_path = os.path.join(dest, filename)
    if os.path.exists(dest_path):
        previously_installed = True
        if filecmp.cmp(src_path, dest_path):
            logger.verbose("File %s does not need to be updated", dest_path)
            return previously_installed, False

    Helper.copy_file(src_path, dest_path)
    return previously_installed, True


def install_manpages(man_dir):
    """Install COT's manual pages.

    Args:
      man_dir (str): Base directory where manpages should be installed.
    Returns:
      tuple: (result, message)
    """
    installed_any = False
    some_preinstalled = False
    # default success message, may be overridden below by more specific msg
    msg = "successfully installed to {0}".format(man_dir)

    try:
        for filename in resource_listdir("COT", "docs/man"):
            src_path = resource_filename("COT", os.path.join("docs/man",
                                                             filename))
            prev, new = _install_manpage(src_path, man_dir)
            some_preinstalled |= prev
            installed_any |= new
    except (IOError, OSError, HelperError) as exc:
        return False, "INSTALLATION FAILED: " + str(exc)

    if some_preinstalled:
        if installed_any:
            msg = "successfully updated in {0}".format(man_dir)
        else:
            msg = "already installed, no updates needed"

    return True, msg


class COTInstallHelpers(Command):
    """Install all helper tools that COT requires.

    Inherited attributes:
    :attr:`~Command.ui`,
    """

    def __init__(self, ui):
        """Instantiate this command with the given UI.

        Args:
          ui (UI): User interface instance.
        """
        super(COTInstallHelpers, self).__init__(ui)
        self.ignore_errors = False
        self.verify_only = False

    def install_helper(self, helper):
        """Install the given helper module.

        Args:
          helper (Helper): Helper module to install.

        Returns:
          tuple: (result, message)
        """
        if helper.installed:
            return (True,
                    "version {0}, present at {1}"
                    .format(helper.version, str(helper.path)))
        elif self.verify_only:
            return (True, "NOT FOUND")
        else:
            try:
                helper.install()
                return (True,
                        "successfully installed to {0}, version {1}"
                        .format(str(helper.path), helper.version))
            except (NotImplementedError,
                    HelperError,
                    HelperNotFoundError) as exc:
                return (False, "INSTALLATION FAILED: " + str(exc))

    def manpages_helper(self):
        """Verify or install COT's manual pages.

        Returns:
          tuple: (result, message)
        """
        try:
            resource_listdir("COT", "docs/man")
        except OSError as exc:
            return False, "UNABLE TO FIND PAGES: " + str(exc)

        man_dir = guess_manpath()

        if self.verify_only:
            return verify_manpages(man_dir)
        else:
            return install_manpages(man_dir)

    def run(self):
        """Verify all helper tools and install any that are missing."""
        result = True
        results = {}
        for name in ['fatdisk', 'ovftool', 'qemu-img', 'vmdktool']:
            helper = helpers[name]
            rc, results[helper.name] = self.install_helper(helper)
            if not rc:
                result = False

        # We only need one of these three tools so stop as soon as one succeeds
        for name in ['mkisofs', 'genisoimage', 'xorriso']:
            isorc, results[name] = self.install_helper(helpers[name])
            if isorc:
                break
        if not isorc:
            result = False

        rc, results["COT manpages"] = self.manpages_helper()
        if not rc:
            result = False

        print("Results:")
        print("-------------")
        wrapper = textwrap.TextWrapper(width=self.ui.terminal_width,
                                       initial_indent="",
                                       subsequent_indent=(" " * 14))
        for name in sorted(results):
            print(wrapper.fill("{0:13} {1}".format(name + ":", results[name])))
        print("")
        if not result and not self.ignore_errors:
            raise EnvironmentError(1, "Unable to install some helpers")

    def create_subparser(self):
        """Create 'install-helpers' CLI subparser."""
        parser = self.ui.add_subparser(
            'install-helpers',
            help=("Install/verify COT manual pages and any third-party helper "
                  "programs that COT may require"),
            usage=self.ui.fill_usage('install-helpers',
                                     ["--verify-only",
                                      "[--ignore-errors]"]),
            description="""
Install or verify the installation of COT manual pages and various required
third-party helper programs for COT.

* qemu-img (http://www.qemu.org/)
* mkisofs  (http://cdrecord.org/)
* ovftool  (https://www.vmware.com/support/developer/ovf/)
* fatdisk  (http://github.com/goblinhack/fatdisk)
* vmdktool (http://www.freshports.org/sysutils/vmdktool/)""",
            epilog=self.ui.fill_examples([
                ("Verify whether COT can find all expected helper programs",
                 """
> cot install-helpers --verify-only
Results:
-------------
COT manpages: present in /usr/share/man/man1/
fatdisk:      present at /opt/local/bin/fatdisk
mkisofs:      present at /opt/local/bin/mkisofs
ovftool:      present at /usr/local/bin/ovftool
qemu-img:     present at /opt/local/bin/qemu-img
vmdktool:     NOT FOUND""".strip()),
                ("Have COT attempt to install missing helpers for you. "
                 "Note that most helpers require administrator / ``sudo`` "
                 "privileges to install. If any installation fails, "
                 "COT will exit with an error, unless you pass "
                 "``--ignore-errors``.",
                 """
> cot install-helpers
(...)
Results:
-------------
COT manpages: successfully installed to /usr/share/man
fatdisk:      successfully installed to /usr/local/bin/fatdisk
mkisofs:      present at /usr/bin/mkisofs
ovftool:      INSTALLATION FAILED: No support for automated
              installation of ovftool, as VMware requires a site
              login to download it. See
              https://www.vmware.com/support/developer/ovf/
qemu-img:     present at /usr/bin/qemu-img
vmdktool:     successfully installed to /usr/local/bin/vmdktool

[Errno 1] Unable to install some helpers""".strip())]),
            formatter_class=argparse.RawDescriptionHelpFormatter)

        group = parser.add_mutually_exclusive_group()

        # TODO - nice to have!
        # parser.add_argument('--dry-run', action='store_true',
        #              help="Report the commands that would be run to install "
        #             "any helper programs, but do not actually run them.")

        group.add_argument('--verify-only', action='store_true',
                           help="Only verify helpers -- do not attempt to "
                           "install any missing helpers.")

        group.add_argument('-i', '--ignore-errors', action='store_true',
                           help="Do not fail even if helper installation "
                           "fails.")

        parser.set_defaults(instance=self)


command_classes.append(COTInstallHelpers)
