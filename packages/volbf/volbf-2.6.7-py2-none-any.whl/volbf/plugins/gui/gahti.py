# volbf
# Copyright (C) 2007-2013 volbf Foundation
# Copyright (C) 2010,2011,2012 Michael Hale Ligh <michael.ligh@mnin.org>
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
from volbf import renderers
from volbf.renderers.basic import Address
from volbf.renderers.text import TextRenderer

import volbf.utils as utils
import volbf.debug as debug
import volbf.plugins.gui.constants as consts
import volbf.plugins.gui.sessions as sessions

class Gahti(sessions.Sessions):
    """Dump the USER handle type information"""

    def unified_output(self, data):

        return renderers.TreeGrid(
            [("Session", str),
             ("Type", str),
             ("Tag", str),
             ("fnDestroy", Address),
             ("Flags", str),
            ], self.generator(data))

    def generator(self, data):
        profile = utils.load_as(self._config).profile

        # Get the OS version being analyzed
        version = (profile.metadata.get('major', 0),
                   profile.metadata.get('minor', 0))

        # Choose which USER handle enum to use
        if version >= (6, 1):
            handle_types = consts.HANDLE_TYPE_ENUM_SEVEN
        else:
            handle_types = consts.HANDLE_TYPE_ENUM

        for session in data:
            gahti = session.find_gahti()
            if gahti:
                for i, h in handle_types.items():
                    yield (0,
                                    [str(session.SessionId),
                                     str(h),
                                     str(gahti.types[i].dwAllocTag),
                                     Address(gahti.types[i].fnDestroy),
                                     str(gahti.types[i].bObjectCreateFlags)])

    def render_text(self, outfd, data):
        output = self.unified_output(data)

        if isinstance(output, renderers.TreeGrid):
            tr = TextRenderer(self.text_cell_renderers, sort_column = self.text_sort_column)
            tr.render(outfd, output)
        else:
            raise TypeError("Unified Output must return a TreeGrid object")
