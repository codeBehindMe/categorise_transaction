# description_decoder.py

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
Contains the decoders for description.
"""

import pandas as pd
from src.transaction_decoder.engines.rule_based import RegexCategoriser


class DescriptionDecoder:

    def __init__(self):
        regex_cat = RegexCategoriser()

    def decode_descriptions(self, descriptions: pd.DataFrame, *args, **kwargs):
        """
        Decode the descriptions.
        :param descriptions: Pandas dataframe of descriptions to decode.
        :param args:
        :param kwargs:
        :return:
        """
        pass
