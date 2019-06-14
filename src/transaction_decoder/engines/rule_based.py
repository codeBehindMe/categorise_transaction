# rule_based.py

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

import pandas as pd
from src.utils.stateless import is_string_in_string
from src.transaction_decoder.constants import DEFAULT_TRANSACTION_CATEGORY

SEARCH_CONSTANTS = (("(\s|^)(rent)(\s|$)", "RENT")
                    , ("(\s|^)(bupa)(\s|$)", "HEALTH")
                    , ("(\s|^)(osteopathy)(\s|$)", "HEALTH"))


class RegexCategoriser:

    def __init__(self):
        pass

    @staticmethod
    def _decode_description(desc: str) -> str:
        """
        Decodes a single description. The decode process is a linear search
        over set of regex expressions. It returns the first match. If no match
        is found, returns teh default transaction category.
        Args:
            desc: Description to search in.

        Returns:

        """

        for t in SEARCH_CONSTANTS:
            if is_string_in_string(t[0], desc):
                return t[1]
        return DEFAULT_TRANSACTION_CATEGORY

    def decode_set(self, descriptions: pd.Series):
        """
        Generates categories based on the descriptions.
        Args:
            descriptions:

        Returns:

        """

        return descriptions.apply(self._decode_description)

