# stateless.py

# Author : aarontillekeratne
# Date : 2019-05-10

# This file is part of categorise_transaction.

# categorise_transaction is free software:
# you can redistribute it and/or modify it under the terms of the GNU General
# Public License as published by the Free Software Foundation, either version 3
# of the License, or (at your option) any later version.

# categorise_transaction is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with Foobar.  If not, see <https://www.gnu.org/licenses/>.

"""
Stateless utils to be used throughout the application.
"""

import re


def _regex_search_bool(a: str, b: str, *args):
    """
    Internal regex matching helper.
    Args:
        a: Regex or string.
        b: Search string
        *args: args for regec.

    Returns:


    """

    if re.search(a, b, *args):
        return True
    return False


def is_string_in_string(a: str, b: str, case_insensitive=True):
    """
    Checks to see if a string is contained within another string.
    Args:
        a: Matching string or regex expression.
        b: String to look in.
        case_insensitive: Check for case insensitivity.

    Returns:
        bool: True of found, else false.

    """

    if case_insensitive:
        return _regex_search_bool(a, b, re.IGNORECASE)
    return _regex_search_bool(a, b)
