"""
Author: Samuel B.
discription: this is to start programms that are listed in a json file properly
Version: 1.0
"""

import os
import subprocess
import webbrowser
import platform

import json


class Open_programms():
    def __init__(self):
        self.os = platform.system()
        dir = os.listdir("json")
        self.modes = []
        self.files = []
        for mode in dir:
            if (mode.endswith(".json")):
                self.files.append(mode)
                self.modes.append(mode.replace(".json", ""))

    def update(self):
        dir = os.listdir("json")
        self.modes = []
        self.files = []
        for mode in dir:
            if (mode.endswith(".json")):
                self.files.append(mode)
                self.modes.append(mode.replace(".json", ""))

    def setup(self, mode):
        self.mode = mode
        self.file = "json/" + mode + ".json"

    def checkForMode(self):
        if (not os.path.exists(self.file)):
            print(f'You idiot "{self.mode}" isn\'t a supported mode!')
        return os.path.exists(self.file)

    def startProgramms(self):
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
                if(self.os.lower() == "windows"):
                    os.startfile(json_object[item])
                else:
                    subprocess.Popen(json_object[item])
