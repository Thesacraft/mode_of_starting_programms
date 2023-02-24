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
        if (editor.check_if_mode_is_editormode(editor_mode)):
            break
        else:
            print(
                f'"{editor_mode}" is not a valid mode! Please choose one of these modes({editor_modes}) or exit to exit!')
    if (editor_mode == "edit"):
        while True:
            mode = input(
                f"What mode do you wanna edit({editor.modes})(exit to exit)(change to change)!").strip().lower()
            if (editor.check_if_change(mode)):
                break
            if (mode in editor.modes):
                file = editor.json_file_path(mode)
                while True:
                    mode_editor = input(
                        f'Do You Wanna create or wanna delete a entry(entrys: {editor.get_entrys(file)})?(exit to exit)(change to change)').strip().lower()
                    if (editor.check_if_change(mode_editor)):
                        break
                    if (mode_editor == "create" or mode_editor == "delete"):
                        if (mode_editor == "create"):
                            while True:
                                name = input(
                                    "Prompt a name for the Programm or for a webbrowser \"webbrowser\" (exit to exit)(change to change)!").strip().lower()
                                if (editor.check_if_change(name)):
                                    break
                                entry = input(
                                    "Prompt the path to the programm or the websites seperatet by \";\" (exit to exit)(change to change)!")
                                [success, error] = editor.handle_edit_create(name, entry, mode)
                                if (success):
                                    print(error)
                                    break
                                else:
                                    print(error)
                        elif (mode_editor == "delete"):
                            while True:
                                entrys = editor.get_entrys(file)
                                entry = input(
                                    f"Choose one of ({entrys}) these to delete(exit to exit)(change to change)!").strip().lower()
                                if (editor.check_if_change(entry)):
                                    break
                                [success, error] = editor.handle_edit_delete(entry, mode)
                                if (success):
                                    print(error)
                                    break
                                else:
                                    print(error)
    elif (editor_mode == "create"):
        while True:
            mode = input(f"Input the name of the mode(exit to exit)(change to change)!")
            if (editor.check_if_change(mode)):
                break
            [success, error] = editor.handle_create(mode)
            if (success):
                print(error)
                editor.update_vars()
                break
            else:
                print(error)
    elif (editor_mode == "delete"):
        while True:
            mode = input(
                f"Input the mode that should be deleted(currently availabel modes:{editor.modes})(exit to exit)(change to change)!")
            if (editor.check_if_change(mode)):
                break
            [success, error] = editor.handle_delete(mode)
            if (success):
                print(error)
                editor.update_vars()
                break
            else:
                print(error)
