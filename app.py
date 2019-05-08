# app.py

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

import os
from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    target = os.environ.get('TARGET', 'World')

    return f'hello {target}'


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))
