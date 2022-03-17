"""
Author: Samuel B.
discription: editor for using the main.py and making it easy to add and remove programms and modes
Version:1.0
"""
import json

import editor_class
import start_programms

editor = editor_class.Editor()


editor_modes = "create/delete/edit"

while True:
    while True:
        editor_mode = input(f'Choose What you wanna do({editor_modes})(exit to exit)!').strip().lower()
        if(editor.checkIfModeIsEditormode(editor_mode)):
            break
        else:
            print(f'"{editor_mode}" is not a valid mode! Please choose one of these modes({editor_modes}) or exit to exit!')
    if(editor_mode == "edit"):
        while True:
            mode = input(f"What mode do you wanna edit({editor.modes})(exit to exit)(change to change)!").strip().lower()
            editor.checkIfExit(mode)
            if(mode in editor.modes):
                file = editor.jsonFilePath(mode)
                with open(file) as json_file:
                    json_object = json.load(json_file)
                    json_file.close()
                while True:
                    mode = input(f'Do You Wanna create or wanna delete a entry(entrys: {editor.getEntrys(file)})?(exit to exit)(change to change)').strip().lower()
                    editor.checkIfExit(mode)
                    if(mode == "create" or mode == "delete"):
                        while True:
                            pass



