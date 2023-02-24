"""
Author: Samuel B.
discription: editor for using the main.py and making it easy to add and remove programms and modes
Version: 1.0
"""

import os
import json
import start_programms


class Editor():
    def __init__(self):
        self.editor_modes_list = ["create", "delete", "edit"]
        self.plugin = start_programms.OpenProgramms()
        self.files = self.plugin.files
        self.modes = self.plugin.modes

    def get_entrys(self, file):
        with open(file) as json_file:
            json_object = json.load(json_file)
            json_file.close()
        entrys = []
        for item in json_object:
            entrys.append(item)
        return entrys

    def check_if_new_entry(self, file, entry):
        entrys = self.get_entrys(file)
        if entry in entrys:
            return False
        else:
            return True

    def check_if_exit(self, mode):
        if mode.strip().lower() == "exit":
            exit()

    def check_if_change(self, mode):
        self.check_if_exit(mode)
        if mode.strip().lower() == "change":
            return True
        else:
            return False

    def check_if_mode_is_editormode(self, mode):
        self.check_if_exit(mode)
        if mode.strip().lower() in self.editor_modes_list:
            return True
        else:
            return False

    def check_if_mode_or_file(self, mode):
        if mode.endswith(".json"):
            return False
        else:
            return True

    def mode_to_file(self, mode):
        if self.check_if_mode_or_file(mode):
            mode += ".json"
        return mode

    def json_file_path(self, file):
        file = self.mode_to_file(file)
        filepath = f"json/{file}"
        return filepath

    def update_vars(self):
        self.plugin.update()
        self.files = self.plugin.files
        self.modes = self.plugin.modes

    def handle_create(self, mode):
        if not mode in self.modes and not mode == "" and not self.mode_to_file(mode) in self.files:
            pass
        else:
            return False, TypeError(f'"{mode}" is already created!')
        file = self.json_file_path(mode)
        with open(file, "w+") as fh:
            fh.write(json.dumps({}))
            fh.close()
        self.update_vars()
        return True, f'"{mode.replace(".json", "")}" was succesfully created!'

    def handle_delete(self, mode):
        if mode in self.modes or mode in self.files:
            file = self.json_file_path(mode)
            try:
                os.remove(file)
                return True, f'"{mode.replace(".json", "")}" was succesfuly removed!'
            except:
                return False, TypeError("Is not a mode you can delete!")
        return False, TypeError(f"\"{mode}\"Is not a mode! Please choose out of this list of modes: {self.modes}")

    def handle_edit_create(self, name, entry, mode):
        file = self.json_file_path(mode)
        with open(file) as json_file:
            json_object = json.load(json_file)
            json_file.close()
        if self.check_if_new_entry(file, name):
            json_object[name] = entry
            with open(file, "w") as fh:
                fh.write(json.dumps(json_object))
            return True, f'"{name}" was sucessfully created!'
        else:
            return False, f'"{name}" could\'t be created because it already exists!'

    def handle_edit_delete(self, name, mode):
        file = self.json_file_path(mode)
        with open(file) as json_file:
            json_object = json.load(json_file)
            json_file.close()
        if not self.check_if_new_entry(file, name):
            json_object.pop(name)
        else:
            return False, TypeError(
                f'"{name}" is not a entry! please choose one of these to delete: {self.get_entrys(file)}')
        with open(file, "w") as fh:
            fh.write(json.dumps(json_object))
            fh.close()
        return True, f'"{name}" was succesfully deleted!'
