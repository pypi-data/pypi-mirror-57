#!/usr/bin/env python
#
# ui.py - abstract user interface API for COT
#
# December 2014, Glenn F. Matthews
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

"""Generic semi-abstract user interface superclass.

**Classes**

.. autosummary::
  :nosignatures:

  UI
"""

import logging
import sys

logger = logging.getLogger(__name__)


class UI(object):
    """Abstract user interface functionality.

    Can also be used in test code as a stub that autoconfirms everything.

    **Properties**

    .. autosummary::
      :nosignatures:

      terminal_width

    **API Methods**

    .. autosummary::
      :nosignatures:

      choose_from_list
      confirm
      confirm_or_die
      validate_value
      fill_examples
      fill_usage
      get_input
      get_password
    """

    def __init__(self, force=False):
        """Constructor.

        Args:
          force (bool): See :attr:`force`.
        """
        self.force = force
        """Whether to automatically select the default value in all cases.

        (As opposed to interactively prompting the user.)
        """

        self.default_confirm_response = True
        """Knob for API testing, sets the default response to confirm()."""

        self._terminal_width = 80
        from COT.helpers import Helper
        Helper.USER_INTERFACE = self

    @property
    def terminal_width(self):
        """Get the width of the terminal in columns."""
        return self._terminal_width

    def fill_usage(self,   # pylint: disable=no-self-use
                   subcommand, usage_list):
        """Pretty-print a list of usage strings.

        Args:
          subcommand (str): Subcommand name/keyword
          usage_list (list): List of usage strings for this subcommand.
        Returns:
          str: Concatenation of all usage strings, each appropriately wrapped
          to the :attr:`terminal_width` value.
        """
        return "\n".join(["{0} {1}".format(subcommand, usage)
                          for usage in usage_list])

    def fill_examples(self, example_list):
        """Pretty-print a set of usage examples.

        Args:
          example_list (list): List of (example, description) tuples.
        Raises:
          NotImplementedError: Must be implemented by a subclass.
        """
        raise NotImplementedError("No implementation for fill_examples()")

    def confirm(self, prompt):
        """Prompt user to confirm the requested operation.

        Auto-accepts if :attr:`force` is set to ``True``.

        .. warning::
          This stub implementation does not actually interact with the user,
          but instead returns :attr:`default_confirm_response`. Subclasses
          should override this method.

        Args:
          prompt (str): Message to prompt the user with
        Returns:
          bool: ``True`` (user confirms acceptance) or ``False``
          (user declines)
        """
        if self.force:
            logger.warning("Automatically agreeing to '%s'", prompt)
            return True
        return self.default_confirm_response

    def confirm_or_die(self, prompt):
        """If the user doesn't agree, abort the program.

        A simple wrapper for :meth:`confirm` that calls :func:`sys.exit` if
        :meth:`confirm` returns ``False``.

        Args:
          prompt (str): Message to prompt the user with
        Raises:
          SystemExit: if user declines
        """
        if not self.confirm(prompt):
            sys.exit("Aborting.")

    def validate_value(self, helper_function, *args):
        """Ask the user whether to ignore a ValueError.

        Args:
          helper_function (function): Validation function to call, which
            may raise a ValueError.
          *args: Arguments to pass to `helper_function`.
        Raises:
          ValueError: if `helper_function` raises a ValueError and the
            user declines to ignore it.
        """
        try:
            helper_function(*args)
        except ValueError as err:
            if not self.confirm("Warning:\n{0}\nContinue anyway?".format(err)):
                raise

    def choose_from_list(self, footer, option_list, default_value,
                         header="", info_list=None):
        """Prompt the user to choose from a list.

        Args:
          footer (str): Prompt string to display following the list
          option_list (list): List of strings to choose amongst
          default_value (str): Default value to select if user declines
          header (str): String to display prior to the list
          info_list (list): Verbose strings to display in place of
              :attr:`option_list`

        Returns:
          str: :attr:`default_value` or an item from :attr:`option_list`.
        """
        if not info_list:
            info_list = option_list
        prompt_list = [header] + ["""{0:2}) {1}""".format(i, inf.strip())
                                  for i, inf in enumerate(info_list, start=1)]
        prompt_list.append(footer)
        prompt = "\n".join(prompt_list)
        while True:
            result = self.get_input(prompt, default_value)

            # Exact match or user declined to choose
            if result == default_value or result in option_list:
                return result
            # Unique prefix match
            match = [opt for opt in option_list if opt.startswith(result)]
            if len(match) == 1:
                return match[0]
            # Did user enter a list index?
            try:
                index = int(result)
                return option_list[index-1]
            except (ValueError, IndexError):
                pass
            logger.error("Invalid input. Please try again.")

    def get_input(self, prompt, default_value):
        """Prompt the user to enter a string.

        Auto-inputs the :attr:`default_value` if :attr:`force` is set to
        ``True``.

        .. warning::
          This stub implementation does not actually interact with the user,
          but instead always returns :attr:`default_value`. Subclasses should
          override this method.

        Args:
          prompt (str): Message to prompt the user with
          default_value (str): Default value to input if the user simply
              hits Enter without entering a value, or if :attr:`force`.

        Returns:
          str: Input value
        """
        if self.force:
            logger.warning("Automatically entering %s in response to '%s'",
                           default_value, prompt)
            return default_value
        return default_value

    def get_password(self, username, host):
        """Get password string from the user.

        Args:
          username (str): Username the password is associated with
          host (str): Host the password is associated with
        Raises:
          NotImplementedError: Must be implemented by a subclass.
        """
        raise NotImplementedError("No implementation of get_password()")
