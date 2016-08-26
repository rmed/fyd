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

"""Start dialog."""

import texture
import six

INFO = """
FYD copyist by Rafael Medina García (https://github.com/rmed/fyd).

Released under GPLv2+ license.
"""

START = 'Type START to continue'

class Scenario(texture.BaseScenario):

    def load(self):
        texture.tprint(INFO)
        texture.tnewline()
        texture.tprint(START)

    def do_action(self, cmd):
        if cmd != 'START':
            texture.tprint(START)
            return texture.dotick

        # Load main dialog
        return texture.loader(six.u('main'))
