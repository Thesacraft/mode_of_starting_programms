"""
Author: Samuel B.
discription: editor for using the main.py and making it easy to add and remove programms and modes
Version: 1.0
"""

import json
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
        mode+=".json"
        return mode
    def updateVars(self):
        self.plugin.update()
        self.files = self.plugin.files
        self.modes = self.plugin.modes
    def handleCreate(self,mode):
        if(not mode in self.modes and not mode == ""):
            if(not mode.endswith(".json")):
                mode = self.modeToFile(mode)
        else:
            return TypeError("Not A Valid Mode")
        with open(mode,"w+") as fh:
            fh.write(json.dumps({}))
            fh.close()
        self.updateVars()
    def handleDelete(self,mode):
        if(self.checkIfModeorFile(mode)):
            pass

