"""
Author: Samuel B.
discription: this is to start programms that are listed in a json file properly
Version: 1.0
"""

import os
import webbrowser

import json


class open_programms():
    def __init__(self):
        dir = os.listdir("json")
        self.modes = []
        self.files = []
        for mode in dir:
            if(mode.endswith(".json")):
                self.files.append(mode)
                self.modes.append(mode.replace(".json",""))
    def update(self):
        dir = os.listdir("json")
        self.modes = []
        self.files = []
        for mode in dir:
            if(mode.endswith(".json")):
                self.files.append(mode)
                self.modes.append(mode.replace(".json",""))
    def setup(self,mode):
        self.mode = mode
        self.file = "json/" + mode + ".json"

    def check_for_mode(self):
        if(not os.path.exists(self.file)):
            print(f'You idiot "{self.mode}" isn\'t a supported mode!')
        return os.path.exists(self.file)


    def start(self):
        with open(self.file) as json_file:
            json_object = json.load(json_file)
            json_file.close()
        for item in json_object:
            if item == "webbrowser":
                webbrowser.open(json_object[item])
            elif os.path.exists(json_object[item]):
                os.startfile(json_object[item])

