# volbf
# Copyright (C) 2007-2013 volbf Foundation
#
# This file is part of volbf.
#
# volbf is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
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

import volbf.obj as obj
import volbf.plugins.mac.common as common
import volbf.plugins.mac.list_zones as list_zones
import volbf.plugins.mac.pslist as pslist

class mac_dead_procs(pslist.mac_pslist):
    """ Prints terminated/de-allocated processes """

    def calculate(self):
        common.set_plugin_members(self)
    
        zones = list_zones.mac_list_zones(self._config).calculate()

        for zone in zones:
            name = str(zone.zone_name.dereference())
            if name == "proc":
                procs = zone.get_free_elements("proc")        
                for proc in procs:
                    yield proc

