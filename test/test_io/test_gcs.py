# test_gcs.py

# Author : aarontillekeratne
# Date : 2019-05-08

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

from src.io.gcs import GoogleCloudStorage


class TestGoogleCloudStorage:

    def test_list_buckets(self):
        """
        Tests to see if the list buckets works
        :return:
        """
        gcs = GoogleCloudStorage()

        gcs.get_buckets()
