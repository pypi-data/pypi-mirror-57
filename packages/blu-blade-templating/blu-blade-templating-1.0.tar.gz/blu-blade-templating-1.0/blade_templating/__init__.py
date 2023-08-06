# Copyright (C) 2019 Blu Wireless Ltd.
# All Rights Reserved.
#
# This file is part of BLADE.
#
# BLADE is free software: you can redistribute it and/or modify it under the
# terms of the GNU General Public License as published by the Free Software
# Foundation, either version 3 of the License, or (at your option) any later
# version.
#
# BLADE is distributed in the hope that it will be useful, but WITHOUT ANY
# WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR
# A PARTICULAR PURPOSE.  See the GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along with
# BLADE.  If not, see <https://www.gnu.org/licenses/>.
#

import sys
import os

if 'BLADE_CORE_DIR' in os.environ:
    sys.path.append(os.environ['BLADE_CORE_DIR'])

if 'DESIGN_FORMAT_DIR' in os.environ:
    sys.path.append(os.path.join(os.environ['DESIGN_FORMAT_DIR'], 'python'))

sys.path.append(os.path.abspath(os.path.dirname(__file__)))