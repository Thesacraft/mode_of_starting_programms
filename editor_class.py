"""
Author: Samuel B.
discription: editor for using the main.py and making it easy to add and remove programms and modes
Version: 1.0
"""

import json
import os
import start_programms

class Editor():
    def __init__(self):
        self.plugin = start_programms.Open_programms()
        self.files = self.plugin.files
        self.modes = self.plugin.modes
    def checkIfModeorFile(self,mode):
        if(mode.endswith(".json")):
            return False
        else:
            return True
    def modeToFile(self,mode):
        if (self.checkIfModeorFile(mode)):
            mode+=".json"
        return mode
    def jsonFilePath(self,file):
        file = self.modeToFile(file)
        filepath = f"/json/{file}"
        return filepath


    def updateVars(self):
        self.plugin.update()
        self.files = self.plugin.files
        self.modes = self.plugin.modes
    def handleCreate(self,mode):
        if(not mode in self.modes and not mode == ""):
            if(not mode.endswith(".json")):
                mode = self.modeToFile(mode)
        else:
            return False,TypeError(f'"{mode}"Not A Valid Mode! Enter one of these modes: {self.modes}')
        with open(mode,"w+") as fh:
            fh.write(json.dumps({}))
            fh.close()
        self.updateVars()
        return True,f'"{mode.replace(".json","")}" was succesfully created!'
    def handleDelete(self,mode):
        if(mode in self.modes or mode in self.files):
            if(self.checkIfModeorFile(mode)):
                mode += ".json"
            try:
                os.remove(mode)
                return True,f'"{mode.replace(".json","")}" was succesfuly removed!'
            except:
                return False,TypeError("Is not a mode you can delete!")
        return False,TypeError(f"\"{mode}\"Is not a mode! Please choose out of this list of modes: {self.modes}")
    def handleEditCreate(self,name,entry,mode):
        file = self.jsonFilePath(mode)
        with open(file) as json_file:
            json_object = json.load(json_file)
            json_file.close()
        if(not name in json_object):
            json_object[name] = entry
            return True, f'"{mode}" was sucessfully created!'
        else:
            return False, f'"{mode}" could\'t be created because it already exists!'
    def handleEditDelete(self,mode):
        pass

