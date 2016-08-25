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

from __future__ import absolute_import

import texture
import dialogs
import six
import sys

def cancel(state):
    """Cancel current operation and return to main dialog."""
    return texture.loader(six.u('main'))

def exit(state):
    """Exit program"""
    sys.exit('Bye!')

if __name__ == '__main__':
    # It's just a game!
    gm = texture.GameMaster(scenarios='dialogs')

    gm.register_command('EXIT', exit)
    gm.register_command('CANCEL', cancel)

    gm.start_game()
