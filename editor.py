import start_programms
import json
import os

plugin = start_programms.open_programms()
modes = plugin.modes
edit_modes = "edit/delete/create"
json_files = plugin.files
modes_edit = "delete/create"
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
                    mode_edit = input(f"Do you wanna create or wanna delete a programm?")
                    if(mode_edit in modes_edit):
                        if(mode_edit == "delete"):
                            while True:
                                with open("json/"+file) as json_file:
                                    json_object = json.load(json_file)

                                    entrys = []
                                    for item in json_object:
                                        entrys.append(item)
                                    json_file.close()

                                    entry = input(f"Choose a entry to delete(entrys:{entrys})!")
                                    if entry in entrys:
                                        try:
                                            json_object.pop(entry)
                                            print(json_object)
                                            with open("json/"+file,"w") as fh:
                                                fh.write(json.dumps(json_object))
                                                fh.close()

                                            break
                                        except:
                                            print("Thats not a Valid entry!")
                                    elif entry == "change":

                                        break
                    break

            else:
                print(f'"{file}" is not a file! You must create it first!')