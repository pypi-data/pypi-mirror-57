# volbf
# Copyright (C) 2007-2013 volbf Foundation
#
# This file is part of volbf.
#
# volbf is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License Version 2 as
# published by the Free Software Foundation.  You may not use, modify or
# distribute this program under any other version of the GNU General
# Public License.
#
# volbf is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with volbf.  If not, see <http://www.gnu.org/licenses/>.
#

"""
@author:       Andrew Case
@license:      GNU General Public License 2.0
@contact:      atcuno@gmail.com
@organization: 
"""

import struct
from operator import attrgetter
import volbf.obj as obj
import volbf.debug as debug
import volbf.addrspace as addrspace
import volbf.plugins.mac.common  as mac_common
import volbf.plugins.mac.pstasks as mac_tasks
from volbf.renderers import TreeGrid

class mac_bash_env(mac_tasks.mac_tasks):
    """Recover bash's environment variables"""

    def unified_output(self, data):
        debug.error("This plugin is deprecated. Please use mac_psenv.")

    def generator(self, data):
        debug.error("This plugin is deprecated. Please use mac_psenv.")

    def render_text(self, outfd, data):
        debug.error("This plugin is deprecated. Please use mac_psenv.")

