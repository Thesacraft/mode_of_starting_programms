"""
Author: Samuel B.
description: this is to start programms that are listed in a json file properly
Version: 1.0
"""

import os
import platform
import subprocess
import tkinter
import webbrowser

import json


class OpenProgramms():
    def update(self):
        dir_list = os.listdir("json")
        self.modes = []
        self.files = []
        for mode in dir_list:
            if mode.endswith(".json"):
                self.files.append(mode)
                self.modes.append(mode.replace(".json", ""))

    def __init__(self):
        self.file = None
        self.mode = None
        self.modes = None
        self.files = None
        self.os = platform.system()
        self.update()  # creates variables

    def setup(self, mode):
        self.mode = mode
        self.file = "json/" + mode + ".json"

    def check_for_mode(self):
        if not os.path.exists(self.file):
            print(f'You idiot "{self.mode}" isn\'t a supported mode!')
        return os.path.exists(self.file)

    def start_programms(self):
        with open(self.file) as json_file:
            json_object = json.load(json_file)
            json_file.close()
        for item in json_object:
            if item == "webbrowser":
                lst = json_object[item].split(';')
                print(lst)
                for i in lst:
                    webbrowser.open(i)
            elif os.path.exists(json_object[item]):
                if (self.os.lower() == "windows"):
                    os.startfile(json_object[item])
                else:
                    subprocess.Popen(json_object[item])


class OpenProgrammsTkinter():
    def __init__(self):
        self.root = tkinter.Tk()
        self.root.title("Start Programms")
        self.logic_class = OpenProgramms()

    def _items_selected(self, event):
        # get all selected indices
        selected_mode = self.listbox.get(self.listbox.curselection()[0])
        self.logic_class.setup(selected_mode)
        self.logic_class.start_programms()
        self.root.quit()

    def _setup(self):
        var = tkinter.Variable(value=self.logic_class.modes)
        self.listbox = tkinter.Listbox(self.root, listvariable=var, height=15, width=50, selectmode=tkinter.SINGLE,
                                       justify="center")
        self.listbox.pack()
        self.listbox.bind('<Double-1>', self._items_selected)

    def run(self):
        self._setup()
        self.root.mainloop()
