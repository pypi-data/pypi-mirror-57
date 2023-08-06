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

import volbf.plugins.mac.pstasks as pstasks
from volbf.renderers import TreeGrid
from volbf.renderers.basic import Address

class mac_psaux(pstasks.mac_tasks):
    """ Prints processes with arguments in user land (**argv) """

    def unified_output(self, data):
        return TreeGrid([("Pid", int),
                        ("Name", str),
                        ("Bits", str),
                        ("Stack", Address),
                        ("Length", int),
                        ("Argc", int),
                        ("Arguments", str)
                        ], self.generator(data))

    def generator(self, data):
        for proc in data:
            yield(0, [
                    int(proc.p_pid),
                    str(proc.p_comm),
                    str(proc.task.map.pmap.pm_task_map),
                    Address(proc.user_stack),
                    int(proc.p_argslen),
                    int(proc.p_argc),
                    str(proc.get_arguments()),
                    ])

    def render_text(self, outfd, data):

        self.table_header(outfd, [("Pid", "8"), 
                                  ("Name", "20"),
                                  ("Bits", "16"),
                                  ("Stack", "#018x"),
                                  ("Length", "8"),
                                  ("Argc", "8"),
                                  ("Arguments", "")])
        for proc in data:
            self.table_row(outfd, 
                           proc.p_pid, 
                           proc.p_comm, 
                           str(proc.task.map.pmap.pm_task_map or '')[9:],
                           proc.user_stack,
                           proc.p_argslen,
                           proc.p_argc,
                           proc.get_arguments())
