"""
Author: Samuel B.
discription: editor for using the main.py and making it easy to add and remove programms and modes
Version:1.0
"""

import editor_class

editor = editor_class.Editor()

editor_modes = "create/delete/edit"

while True:
    while True:
        editor_mode = input(f'Choose What you wanna do({editor_modes})(exit to exit)!').strip().lower()
        if (editor.checkIfModeIsEditormode(editor_mode)):
            break
        else:
            print(
                f'"{editor_mode}" is not a valid mode! Please choose one of these modes({editor_modes}) or exit to exit!')
    if (editor_mode == "edit"):
        while True:
            mode = input(
                f"What mode do you wanna edit({editor.modes})(exit to exit)(change to change)!").strip().lower()
            if (editor.checkIfchange(mode)):
                break
            if (mode in editor.modes):
                file = editor.jsonFilePath(mode)
                while True:
                    mode_editor = input(
                        f'Do You Wanna create or wanna delete a entry(entrys: {editor.getEntrys(file)})?(exit to exit)(change to change)').strip().lower()
                    if (editor.checkIfchange(mode_editor)):
                        break
                    if (mode_editor == "create" or mode_editor == "delete"):
                        if (mode_editor == "create"):
                            while True:
                                name = input(
                                    "Prompt a name for the Programm or for a webbrowser \"webbrowser\" (exit to exit)(change to change)!").strip().lower()
                                if (editor.checkIfchange(name)):
                                    break
                                entry = input(
                                    "Prompt the path to the programm or the websites seperatet by \";\" (exit to exit)(change to change)!")
                                [success, error] = editor.handleEditCreate(name, entry, mode)
                                if (success):
                                    print(error)
                                    break
                                else:
                                    print(error)
                        elif (mode_editor == "delete"):
                            while True:
                                entrys = editor.getEntrys(file)
                                entry = input(
                                    f"Choose one of ({entrys}) these to delete(exit to exit)(change to change)!").strip().lower()
                                if (editor.checkIfchange(entry)):
                                    break
                                [success, error] = editor.handleEditDelete(entry, mode)
                                if (success):
                                    print(error)
                                    break
                                else:
                                    print(error)
    elif (editor_mode == "create"):
        while True:
            mode = input(f"Input the name of the mode(exit to exit)(change to change)!")
            if (editor.checkIfchange(mode)):
                break
            [success, error] = editor.handleCreate(mode)
            if (success):
                print(error)
                editor.updateVars()
                break
            else:
                print(error)
    elif (editor_mode == "delete"):
        while True:
            mode = input(
                f"Input the mode that should be deleted(currently availabel modes:{editor.modes})(exit to exit)(change to change)!")
            if (editor.checkIfchange(mode)):
                break
            [success, error] = editor.handleDelete(mode)
            if (success):
                print(error)
                editor.updateVars()
                break
            else:
                print(error)
