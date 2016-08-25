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

"""Main dialog."""

import texture
import six

class Scenario(texture.BaseScenario):

    def load(self):
        text = """
        MAIN DIALOG
        ===========

        Current file: %s

        ------------------

        Commands:

        - LOAD: set file to work with
        - COPY: start a 5 second countdown and copy file contents when done
        - CANCEL: cancel current operation
        - EXIT: leave program
        """ % self.state.get('current_file', 'None')

        texture.tprint(text)

    def do_action(self, cmd):
        if cmd == 'LOAD':
            return texture.loader(six.u('loader'))

        elif cmd == 'COPY':
            return texture.loader(six.u('copy'))
