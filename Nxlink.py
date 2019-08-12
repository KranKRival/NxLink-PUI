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

        box = Gtk.Box(spacing=6)
        self.add(box)


        self.set_title("NxLink PUI by KranK/KuranKu")
        self.set_default_size(300, 30)
        self.connect("destroy", Gtk.main_quit)

        OpenNroButtonn = Gtk.Button("Choose File")
        OpenNroButtonn.connect("clicked", self.on_file_clicked)
        box.add(OpenNroButtonn)

        IpAdressBox = Gtk.Entry()
        IpAdressBox.connect("key-release-event", self.on_key_release)
        IpAdressBox.set_text("192.168.")
        box.add(IpAdressBox)

        SendNroButton = Gtk.Button("Send NRO")
        SendNroButton.connect("clicked", self.SendNroButton_clicked)
        box.add(SendNroButton)

        self.NROlabel = Gtk.Label("")
        self.NROlabel.set_width_chars(12)

        self.IpAdress = Gtk.Label("")
        self.IpAdress.set_width_chars(12)



    def on_file_clicked(self, widget):
        dialog = Gtk.FileChooserDialog("Please choose a file", self,
            Gtk.FileChooserAction.OPEN,
            (Gtk.STOCK_CANCEL, Gtk.ResponseType.CANCEL,
             Gtk.STOCK_OPEN, Gtk.ResponseType.OK))
             
        
        self.add_filters(dialog)

        response = dialog.run()
        if response == Gtk.ResponseType.OK:
            print("Open clicked")
            print("File selected: " + dialog.get_filename())
            self.NROlabel.set_text(dialog.get_filename())
        elif response == Gtk.ResponseType.CANCEL:
            print("Cancel clicked")

        dialog.destroy()

    def add_filters(self, dialog):

        filter_any = Gtk.FileFilter()
        filter_any.set_name("Switch ? (.NRO)")
        filter_any.add_pattern("*.[Nn][Rr][Oo]")
        dialog.add_filter(filter_any)

    def on_key_release(self, widget, event):
        self.IpAdress.set_text(widget.get_text())

    def SendNroButton_clicked(self, button):
        print ("Ip Adress is: " + self.IpAdress.get_label())
        print ("Sent Command: " + "nxlink -s -a " + self.IpAdress.get_label() + self.NROlabel.get_label())
        os.system("nxlink -s -a " + self.IpAdress.get_label() + " " + self.NROlabel.get_label())


win = MyWindow()
win.show_all()
Gtk.main()
