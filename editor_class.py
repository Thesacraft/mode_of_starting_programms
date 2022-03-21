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
        self.editor_modes_list = ["create","delete","edit"]
        self.plugin = start_programms.Open_programms()
        self.files = self.plugin.files
        self.modes = self.plugin.modes
    def getEntrys(self,file):
        with open(file) as json_file:
            json_object = json.load(json_file)
            json_file.close()
        entrys = []
        for item in json_object:
            entrys.append(item)
        return entrys
    def checkIfNewEntry(self,file,entry):
        entrys = self.getEntrys(file)
        if(entry in entrys):
            return False
        else:
            return True
    def exitEditor(self):
        exit()
    def checkIfExit(self,mode):
        if(mode.strip().lower() == "exit"):
            self.exitEditor()
    def checkIfchange(self,mode):
        self.checkIfExit(mode)
        if(mode.strip().lower() == "change"):
            return True
        else:
            return False
    def checkIfModeIsEditormode(self,mode):
        self.checkIfExit(mode)
        if(mode.strip().lower() in self.editor_modes_list):
            return True
        else:
            return False
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
        filepath = f"json/{file}"
        return filepath


    def updateVars(self):
        self.plugin.update()
        self.files = self.plugin.files
        self.modes = self.plugin.modes
    def handleCreate(self,mode):
        if(not mode in self.modes and not mode == ""):
            pass
        else:
            return False,TypeError(f'"{mode}" is already created!')
        file = self.jsonFilePath(mode)
        with open(file,"w+") as fh:
            fh.write(json.dumps({}))
            fh.close()
        self.updateVars()
        return True,f'"{mode.replace(".json","")}" was succesfully created!'
    def handleDelete(self,mode):
        if(mode in self.modes or mode in self.files):
            file = self.jsonFilePath(mode)
            try:
                os.remove(file)
                return True,f'"{mode.replace(".json","")}" was succesfuly removed!'
            except:
                return False,TypeError("Is not a mode you can delete!")
        return False,TypeError(f"\"{mode}\"Is not a mode! Please choose out of this list of modes: {self.modes}")
    def handleEditCreate(self,name,entry,mode):
        file = self.jsonFilePath(mode)
        with open(file) as json_file:
            json_object = json.load(json_file)
            json_file.close()
        if(self.checkIfNewEntry(file,name)):
            json_object[name] = entry
            with open(file,"w") as fh:
                fh.write(json.dumps(json_object))
            return True, f'"{mode}" was sucessfully created!'
        else:
            return False, f'"{mode}" could\'t be created because it already exists!'
    def handleEditDelete(self,name,mode):
        file = self.jsonFilePath(mode)
        with open(file) as json_file:
            json_object = json.load(json_file)
            json_file.close()
        if(not self.checkIfNewEntry(file,name)):
            json_object.pop(name)
        else:
            return False,TypeError(f'"{name}" is not a entry! please choose one of these to delete: {self.getEntrys(file)}')
        with open(file,"w") as fh:
            fh.write(json.dumps(json_object))
            fh.close()
        return True, f'"{name}" was succesfully deleted!'



