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
"""The basic simplegui API - all package-level calls go through here.

The returned objects from these functions all implement their own APIs defined in their respective classes."""

import os
from typing import Callable, Optional
from unittest.mock import Mock

from ._canvas import Canvas
from ._frame import Frame
from ._image import Image
from ._keys import KEY_MAP
from ._timer import Timer
from ._widgets import Control

# Import Qt Multimedia libraries causes problems on cloud test runners, so this is mocked if necessary
if os.getenv('NO_AUDIO', False):
    Sound = Mock()
else:
    from ._sound import Sound

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


def create_frame(title, canvas_width, canvas_height, control_width=None):
    # type: (str, int, int, Optional[int]) -> Frame
    """Creates a new frame for interactive programs.

    The frame's window has the given title, a string.
    The frame consists of two parts: a control panel on the left and a canvas on the right.
    The control panel's width in pixels can be specified by the number control_width.
    The canvas width in pixels is the number canvas_width.
    The height in pixels of both the control panel and canvas is the number canvas_height.

    :param title: the title of the frame window
    :param canvas_width: the width of the drawing area, in pixels
    :param canvas_height: the height of the drawing area, in pixels
    :param control_width: the width of the control area of the frame, in pixels
    :return: a :class:`~simplequi._frame.Frame` that can be used to setup (most of) the rest of the program
    """
    return Frame(title, canvas_width, canvas_height, control_width)


def create_timer(interval, timer_handler):
    # type: (int, Callable[[], None]) -> Timer
    """Creates a timer.

    Once started, it will repeatedly call the given event handler at the specified interval, which is given in ms.
    The handler should be defined with no arguments.

    :param interval: the interval at which to call the timer handler, in milliseconds
    :param timer_handler: a function to call after each interval
    :return: a :class:`~simplequi._timer.Timer` that calls ``timer_handler`` every ``interval`` ms (once started)
    """
    return Timer(interval, timer_handler)


def load_image(url):
    # type: (str) -> Image
    """
    Loads an image from the specified URL.

    The image can be in any format supported by PySide2.
    No error is raised if the file isn't found or is of an unsupported format.

    :param url: the URL of the image to load
    :return: an :class:`~simplequi._image.Image` that can be passed to :meth:`~simplequi._canvas.Canvas.draw_image`
    """
    return Image(url)


def load_sound(url):
    # type: (str) -> Sound
    """
    Loads a sound from the specified URL.

    Supports whatever audio formats that PySide2 supports.
    No error is raised if the file isn't found or is of an unsupported format.

    :param url: the URL of the sound to load
    :return: a :class:`~simplequi._sound.Sound` that can be played, paused etc.
    """
    return Sound(url)
