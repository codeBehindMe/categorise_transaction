# test_stateless.py

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
Tests for the stateless utilities
"""

import pytest
from src.utils.stateless import is_string_in_string


@pytest.fixture
def search_cases():
    d = {"search_string": "a"
        , "wrapper_string": "apple"
        , "search_regex": "(\s|^)(rent)(\s|$)"
        , "wrapper_regex": "payed for rent"}

    yield d


@pytest.mark.usefixtures
class TestIsStringInString:

    def test_captures_string_all_lowercase(self, search_cases: {str: str}):
        """
        Base case
        Args:
            search_cases: FIXME

        Returns:

        """

        assert is_string_in_string(search_cases["search_string"],
                                   search_cases["wrapper_string"])

    def test_captures_different_cases(self, search_cases: {str: str}):
        """
        Checks that case differences (bi-directionally) between search and
        wrapper strings do not matter on the default setting.
        Args:
            search_cases: FIXME

        Returns:

        """
        assert is_string_in_string(search_cases["search_string"].upper()
                                   , search_cases["wrapper_string"])
        assert is_string_in_string(search_cases["search_string"]
                                   , search_cases["wrapper_string"].upper())

    def test_custom_case_behaviour(self, search_cases: {str: str}):
        """
        Checks to see that you can get the string in string to fail by using
        the case sensitivity flag.
        Args:
            search_cases: FIXME

        Returns:

        """

        assert not is_string_in_string(search_cases["search_string"]
                                       , search_cases["wrapper_string"].upper()
                                       , False)

    def test_custom_pattern(self, search_cases: {str: str}):
        """
        Checks that providing custom regex also works with the function.
        Args:
            search_cases: FIXME

        Returns:

        """

        assert is_string_in_string(search_cases["search_regex"]
                                   , search_cases["wrapper_regex"])
