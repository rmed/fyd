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

"""File copy dialog."""

import os
import texture
import time
import six
from pykeyboard import PyKeyboard

class Scenario(texture.BaseScenario):

    def load(self):
        text = """
        FILE COPY
        =========

        Current file: %s

        You will have 10 seconds to switch to the window in which the contents
        will be copied and make sure a writable widget is focused

        Write START to copy or CANCEL to go back
        """ % self.state.get('current_file', 'None')

        texture.tprint(text)

    def do_action(self, cmd):
        # Need a file to work with
        if not self.state.get('current_file', ''):
            texture.tprint('No file specified, set one using the LOAD command')
            return texture.loader(six.u('main'))


        if cmd == 'START':
            texture.tprint('Preparing to copy')

            file_path = self.state['current_file']

            # File must exist
            if not os.path.isfile(file_path):
                texture.tprint('File does not exist, cancelling...')
                return texture.loader(six.u('main'))

            # Countdown
            for i in reversed(range(10)):
                texture.tprint(str(i))
                time.sleep(1)

            # Write file
            texture.tnewline()
            texture.tprint('Copying...')
            keyboard = PyKeyboard()

            with open(file_path, 'r') as f:
                for line in f:
                    # Mind newline
                    keyboard.type_string(line.rstrip('\n'))
                    keyboard.tap_key(keyboard.enter_key)

            texture.tprint('Done!')
            return texture.loader(six.u('main'))

        texture.tprint('Write START to copy or CANCEL to go back')
