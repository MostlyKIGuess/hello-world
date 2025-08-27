# Copyright 2009 Simon Schampijer
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
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA  02110-1301  USA

"""HelloWorld Activity: A case study for developing an activity."""

import gi
gi.require_version('Gtk', '4.0')
from gi.repository import Gtk

from gettext import gettext as _

from sugar.activity.activity import Activity
from sugar.graphics.toolbarbox import ToolbarBox
from sugar.activity.widgets import StopButton, ActivityToolbarButton


class HelloWorldActivity(Activity):
    """HelloWorldActivity class as specified in activity.info"""

    def __init__(self, handle, application=None):
        """Set up the HelloWorld activity."""
        Activity.__init__(self, handle, application=application)

        # we do not have collaboration features
        # make the share option insensitive
        self.max_participants = 1

        # toolbar with the new toolbar redesign
        toolbar_box = ToolbarBox()

        activity_button = ActivityToolbarButton(self)
        # GTK4: use append on the toolbar container
        toolbar_box.toolbar.append(activity_button)

        # spacer to push stop button to the right
        separator = Gtk.Box()
        separator.set_hexpand(True)
        toolbar_box.toolbar.append(separator)

        stop_button = StopButton(self)
        toolbar_box.toolbar.append(stop_button)

        self.set_toolbar_box(toolbar_box)

        # label with the text, make the string translatable
        label = Gtk.Label(label=_("Hello World!"))
        # GTK4: set canvas directly with widgets
        self.set_canvas(label)
