#!/usr/bin/env python3

import os
import gi
import subprocess
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gdk , GObject
from subprocess import Popen, PIPE
import fcntl

class MyWindow(Gtk.Window):

    def __init__(self):
        super(MyWindow, self).__init__()

        self.init_ui()

    def init_ui(self):    

        grid = Gtk.Grid()
        grid.set_column_spacing(5)
        self.add(grid)        

        entry = Gtk.Entry()
        entry.connect("key-release-event", self.on_key_release)
        entry.set_text("192.168.")

        button1 = Gtk.Button("Send NRO")
        button1.connect("clicked", self.whenbutton1_clicked)

        grid.attach(entry, 0, 0, 1, 1)
        grid.attach(button1, 2, 0, 1, 1)

        self.label = Gtk.Label("")
        self.label.set_width_chars(15)

        #grid.attach(self.label, 0, 1, 1, 1)

        self.set_border_width(5)

        self.set_title("NxLink PUI by KranK/KuranKu")
        self.set_default_size(350, 100)
        self.connect("destroy", Gtk.main_quit)

        

    def on_key_release(self, widget, event):
        self.label.set_text(widget.get_text())

    def whenbutton1_clicked(self, button):
        print (self.label.get_label())
        os.system("nxlink -s -a " + self.label.get_label() + " Atmosphere_ToolBox.nro")


win = MyWindow()
win.show_all()
Gtk.main()
