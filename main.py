"""
discription: this is a basic programm that let's you start mutiple programms with diffrent mode's
Author:Samuel B.
Version: 1.0
"""
import start_programms

open = start_programms.Open_programms()
modes = ""
for mode in open.modes:
    if modes == "":
        modes = mode
    else:
        modes += "/" + mode
while True:
    mode = input(f"what mode ({modes})?")
    if mode == "exit":
        exit()
    if (mode in open.modes):
        break
    else:
        print(f'"{mode}" is not a valid mode! Please enter one of these modes: {open.modes}')

open.setup(mode)
print(f"starting programms...")
open.startProgramms()
