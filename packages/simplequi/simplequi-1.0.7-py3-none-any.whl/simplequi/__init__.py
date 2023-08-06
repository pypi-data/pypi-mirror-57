# -----------------------------------------------------------------------------
# Copyright ©2019 Arthur Gordon-Wright
# <https://github.com/ArthurGW/simplequi>
# <simplequi.codeskulptor@gmail.com>
#
# This file is part of simplequi.
#
# simplequi is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# simplequi is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with simplequi.  If not, see <https://www.gnu.org/licenses/>.
# -----------------------------------------------------------------------------

from . import _api
from ._api import (KEY_MAP, create_frame, create_timer, load_image, load_sound,
                   Frame, Canvas, Control, Image, Sound, Timer)

__all__ = [
    'KEY_MAP',
    'create_frame',
    'create_timer',
    'load_image',
    'load_sound',
    'Frame',
    'Canvas',
    'Control',
    'Image',
    'Sound',
    'Timer',
   ]
__doc__ = _api.__doc__

__version__ = '1.0.7'
