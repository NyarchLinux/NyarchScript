# window.py
#
# Copyright 2023 Francesco Caracciolo
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# SPDX-License-Identifier: GPL-3.0-or-later

from gi.repository import Adw
from gi.repository import Gtk
import subprocess
from .scripts import SCRIPTS
@Gtk.Template(resource_path='/moe/nyarchlinux/scripts/window.ui')
class NyarchscriptWindow(Adw.ApplicationWindow):
    __gtype_name__ = 'NyarchscriptWindow'

    stack = Gtk.Template.Child("stack")

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.commands = {}
        self.generate_pages()

    def generate_pages(self):
        for page in SCRIPTS:
            adwpage = Adw.ViewStackPage()
            content = Adw.PreferencesPage()
            for section in page["sections"]:
                content.add(self.generate_section(section))
            self.stack.add_titled_with_icon(content, page["title"], page["title"], page["icon-name"])

    def generate_section(self, section):
        adwsection = Adw.PreferencesGroup()
        adwsection.set_title(section["title"])
        if section["subtitle"] is not None:
            adwsection.set_subtitle(section["subtitle"])
        for script in section["scripts"]:
            print(script)
            row = self.generate_row(script)
            adwsection.add(row)
        return adwsection

    def generate_row(self, script):
        row = Adw.ExpanderRow()
        button = Gtk.Button()
        button.set_icon_name("media-playback-start-symbolic")
        button.add_css_class("flat")
        button.set_margin_top(15)
        button.set_margin_bottom(15)
        self.commands[button] = script["command"]
        button.connect("clicked", self.button_clicked)
        row.set_title(script["title"])
        if script["subtitle"] is not None:
            row.set_subtitle(script["subtitle"])
        label = self.code_label(script["description"])
        row.add_row(label)
        row.add_action(button)
        return row

    def button_clicked(self, button):
        self.background_process(self.commands[button])
    def code_label(self, text):
        label = Gtk.Label()
        label.set_use_markup(True)
        label.set_selectable(True)
        label.set_halign(Gtk.Align.START)
        label.set_margin_top(4)
        label.set_margin_bottom(4)
        label.set_margin_start(4)
        label.set_label("<span font_family='monospace'>" + text + "</span>")
        return label

    def background_process(self, command):
    	subprocess.Popen(["flatpak-spawn",  "--host", "kitty", "bash", "-c", command])
