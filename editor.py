import start_programms
import json
import os

plugin = start_programms.open_programms()
modes = plugin.modes
edit_modes = "edit/delete/create"
json_files = plugin.files
while True:
    while True:
        edit_mode = input(f"Choose what you wanna do({edit_modes})!")
        if(edit_mode in edit_modes):
            break
        print(f'"{edit_mode}" is not a Valid mode! Please enter one of these modes: {edit_modes}')
    if(edit_mode == "edit"):
        while True:
            file = input(f"please enter one of these files to edit ({json_files})(change to change the mode)!")
            if file == "change":
                break
            if(file in json_files):
                with open("json/"+file) as json_file:
                    temp = []
                    for item in json.load(json_file):
                        temp.append(item)
                    print(f'There currently are these programms to start in this mode: {temp}')
                    del(temp)
                    json_file.close()
                while True:
                    break
            else:
                print(f'"{file}" is not a file! You must create it first!')