# -*- coding: utf-8 -*-
#
# FYD copyist - https://github.com/rmed/fyd
# Copyright (C) 2016  Rafael Medina García <rafamedgar@gmail.com>
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along
# # with this program; if not, write to the Free Software Foundation, Inc.,
# 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.

"""File confirmation dialog."""

import texture
import six

class Scenario(texture.BaseScenario):

    def load(self):
        text = """
        CONFIRM FILE
        ============

        Will use file %s
        """ % self.state.get('new_file', '')

        texture.tprint(text)
        texture.tnewline()
        texture.tprint('Is this correct? (YES / NO)')

    def do_action(self, cmd):
        if not cmd or cmd not in ['YES', 'NO']:
            texture.tprint('Is this correct? (YES / NO)')
            return texture.dotick

        if cmd == 'YES':
            # Update file
            self.state['current_file'] = self.state.get('new_file', '')
            self.state['new_file'] = ''

            return texture.loader(six.u('main'))

        # Ask for file again
        return texture.loader(six.u('loader'))
