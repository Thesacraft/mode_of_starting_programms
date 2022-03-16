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
                    mode_edit = input(f"Do you wanna create or wanna delete a programm(change to change the mode)?")
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
                        elif(mode_edit == "create"):
                            while True:
                                with open("json/"+file) as json_file:
                                    json_object = json.load(json_file)

                                    entrys = []
                                    for item in json_object:
                                        entrys.append(item)
                                    json_file.close()
                                    while True:
                                        key = input("Enter the name of the programm if it should bring up the webbrowser please type webbrowser(change to change the mode)!")
                                        if not key == "change" and not key == "exit" and not key in json_object:
                                            break
                                        elif key == "change":
                                            break_again = True
                                            break
                                        else:
                                            print("You can't input a name like change or exit and their cannot be the same programm twice!")
                                    if break_again:
                                        break

                                    programm_path = input("Enter the path of the programm if it should bring up the webbrowser please enter the full adress it should bring up!(change to change the mode)")
                                    if(programm_path == "change"):
                                        break
                                    json_object[key] = programm_path
                                    with open("json/"+file,"w") as fh:
                                        fh.write(json.dumps(json_object))
                                        fh.close()
                                    break



            else:
                print(f'"{file}" is not a file! You must create it first!')
    if(edit_mode == "create"):
        while True:
            name = input("Enter the name of the mode with .json(change to change the mode)")
            if name == "change":
                break
            elif(name.endswith(".json")):
                if(not name.startswith(".json") and not name.startswith("exit") and not name.startswith("change")):
                    if(os.path.exists("json/"+name)):
                        print("This mode already exist!")
                    else:
                        with open("json/"+name,"w+") as fh:
                            fh.write(json.dumps({}))
                            fh.close()
                            print(f'"{name}" was created!')
                            break
                else:
                    print(f'"{name}" is not a valid Filename! it cannot be empty or start with change or exit')
            else:
                print(f'The mode must be ended with ".json"(for example "{name}.json")')




