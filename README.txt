Hey, this is my faux virtual machine written in python. It's my first real completed project, so hopefully there won't be too many bugs!
I tried my best to make as much memory as possible stored in the main.py file alone, but I had to had savedata.txt and savedprogram.txt so you wont lose your saved data
after doing endall to finish what you are doing.

COMMANDS

Manual
pointr: "Point Right": Moves the pointer one to the right.
pointl: "Point Left": Moves the pointer one to the left.
change(input): "Change to (input)": Changes the cell that the pointer is on to a number.
prcell: "Print Cell": Prints the cell the pointer is pointing at.
shcell: "Show Cell": Shows the cell that the pointer is on.

Automatic
string(input): "String": Uses memory to commit a string to a cell for each character in the string.
prallc: "Print All Cells": Prints all cells in the order that they are in the cell list as a string.
shoall: "Show All": Shows every cell at once.

Other
endall: "End All": Ends the program. Saves all saved game data to a file.
wrtall: "Write all": Sets all avalible cells to 187.
adwash: "Admin Wash": Sets all cells to 0. Also removes all saved data.

Applications:
gameft: "Game Fight": Play rock paper sciccors.
gamesl: "Game Slots": Play a slots game.
prgram(program to write OR type "saved" for saved program): "Program": Write a brainfuck style program. Uses >(Move pointer right)<(Move pointer left)+(Add 1 to pointed cell)-(Subtract 1 from pointed cell)p(Prints the pointed cell)a(Adds 10 to pointed cell)s(Subtracts 10 from pointed cell)w(Saves the written program to be used again, overwrites the saved program).(Prints all memory to the console.)
