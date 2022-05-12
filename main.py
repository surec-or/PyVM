
# "PyVM" by surec-or on github #

# BLOCK 1 #
# Set Up #
import random

savedata = open("savedata.txt", "r")
data = savedata.readlines()
savedata.close

pointer = 0
cells = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,int(data[0]),int(data[1])]   # Last 2 cells for game saved data
go = True
strsav = "BLANK"
writtenprogram = "BLANK"

savedata = open("savedprogram.txt", "r")
data = savedata.read()
if data == "":
    savedprogram = "BLANK"
else:
    savedprogram = data
savedata.close
data = "BLANK"

# BLOCK 2 #
# Command Index #
def setpointer(location):                               # setpnt: "Set Pointer": Sets the pointer to a specific location.
    global pointer
    pointer = (location)
    if pointer >= 19:
        pointer = 19
    if pointer <= 0:
        pointer = 0
def getpointer():                                       # spoint: "Show Pointer": Shows the where the pointer is.
    print(f"Current Pointer is at location c{pointer}")
def getcell():                                          # shcell: "Show Cell": Shows the cell that the pointer is on.
    print(f"Cell c{pointer} is {cells[pointer]}")
    print(cells[pointer])
def changecell(position, change):                       # change(input): "Change to (input)": Changes the cell that the pointer is on to a number that is inputted or changes the cell in a specific idex.
    cells[position] = change
    print(f"Wrote {change} to location c{position}")
def showall():                                          # shoall: "Show All": Shows every cell at once.
    print(f"Drive 1: {cells}")
    print(f"Drive 2: [{savedprogram}]")
def pointerright():                                     # pointr: "Point Right": Moves the pointer one to the right.
    global pointer
    pointer +=1
    if pointer >= 19:
        pointer = 0
def pointerleft():                                      # pointl: "Point Left": Moves the pointer one to the left.
    global pointer
    pointer -=1
    if pointer <= 0:
        pointer = 19
def printcell():                                        # prcell: "Print Cell": Prints the cell the pointer is pointing at.
    global pointer
    print(f"Cell at c{pointer} is ascii:")
    print(chr(cells[pointer]))
def stringsave(string):                                 # string: "String": Uses memory to commit a string to a cell for each character in the string.
    global strsav
    print(f"Saved '{string}' to memory")
    for x in range(len(string)):
        changecell(x, ord(string[x]))
def endpc():                                            # endall: "End All": Ends the program.
    savedata = open("savedata.txt", "w")
    savedata.write(f"{cells[20]}\n{cells[21]}")
    savedata.close
    quit()
def printall():                                         # prallc: "Print All Cells": Prints all cells in the order that they are in the cell list as a string.
    forstring = ""
    
    # SMALL BRAIN SOLUTION: CONVERT THE ENTIRE LIST INTO ASCII 🡫
    cellsascii = [chr(cells[0]),chr(cells[1]),chr(cells[2]),chr(cells[3]),chr(cells[4]),chr(cells[5]),chr(cells[6]),chr(cells[7]),
    chr(cells[8]),chr(cells[9]),chr(cells[10]),chr(cells[11]),chr(cells[12]),chr(cells[13]),chr(cells[14]),chr(cells[15]),chr(cells[16]),chr(cells[17]),
    chr(cells[18]),chr(cells[19]),]
    # SMALL BRAIN SOLUTION: CONVERT THE ENTIRE LIST INTO ASCII 🡩
    
    print(forstring.join(cellsascii))
def writeprogram(program):                              # prgram(program to write OR type "saved" for saved program): "Program": Write a brainfuck style program. Uses >(Move pointer right)<(Move pointer left)+(Add 1 to pointed cell)-(Subtract 1 from pointed cell)p(Prints the pointed cell)a(Adds 10 to pointed cell)s(Subtracts 10 from pointed cell)w(Saves the written program to be used again, overwrites the saved program).(Prints all memory to the console.)
    global savedprogram
    global writtenprogram
    print("Running program through brainfuck application")
    if writtenprogram == "saved":
        print("Running saved program")
        writtenprogram = savedprogram
    else:
        writtenprogram = program
    for x in writtenprogram:
        global pointer
        global cells 
        if ">" in x:
            pointer +=1
            if pointer >= 19:
                pointer = 0
        if "<" in x:
            pointer -=1
            if pointer <= 0:
                pointer = 19
        if "+" in x:
            changecell(pointer, cells[pointer] + 1)
        if "a" in x:
            changecell(pointer, cells[pointer] + 10)
        if "-" in x:
            changecell(pointer, cells[pointer] - 1)
            if cells[pointer] >= 0:
                cells[pointer] = 0
        if "s" in x:
            changecell(pointer, cells[pointer] - 10)
            if cells[pointer] >= 0:
                cells[pointer] = 0
        if "p" in x:
            print(chr(cells[pointer]))
        if "w" in x:
            savedprogram = writtenprogram
            savedata = open("savedprogram.txt", "w")
            savedata.write(savedprogram)
            savedata.close
        if "." in x:
            printall()
def wash():

    global savedprogram
    global cells
    
    print("Clearing memory and save data...")
    cells = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    savedprogram = "BLANK"
    savedata = open("savedata.txt", "w")
    savedata.write(f"0\n0")
    savedata.close
    savedata = open("savedprogram.txt", "w")
    savedata.write("")
    savedata.close
def runrps():                                         # gameft: "Game Fight": Play rock paper sciccors  
    print(f"You have {cells[21]} wins.")
    enemy = random.randint(1,3)
    player = int(input("Choose:\n1. Sword\n2. Gun\n3. Bomb\nEnter answer: "))
    print("\n")
    if enemy == 1:
        if player == 2:
            print("Win!")
            cells[21] +=1
        else:
            if player == 3:
                print("Lose!")
            else:
                if player == 1:
                    print("Stalemate!")
    if enemy == 2:
        if player == 3:
            print("Win!")
            cells[21] +=1
        else:
            if player == 1:
                print("Lose!")
            else:
                if player == 2:
                    print("Stalemate!")
    if enemy == 3:
        if player == 1:
            print("Win!")
            cells[21] +=1
        else:
            if player == 2:
                print("Lose!")
            else:
                if player == 3:
                    print("Stalemate!")
def runslots():                                    # gamesl: "Game Slots": Play a slots game.
    
    global cells

    if cells[20] <= 1:
        print("Welcome to slots. The game detects a new save file.\n\nTo play, type a bet that is equal or lower to your starting money, which is 10.\n")
        cells[20] = 10
    else:
        print(f"Your balance is {cells[20]}")
    bet = int(input("What is your bet?: "))
    if bet >= (cells[20] + 1):
        print("Try again. Bet must be lower than balance.")
    else:
        print("Spinning...")
        bet *=random.randint(-1,2)
        print(f"Result: {bet}")
        cells[20] += bet
        if cells[20] <= 1:
            print("Your balance is zero! Try again.")
                    
# BLOCK 3 #
# Command Request #
def runcmd():
    
    global pointer
    
    cmdcheck = cmd[:6]
    if cmdcheck == "Change":
        cmdnum = int(cmd[6:])
        changecell(pointer, cmdnum)
    if cmdcheck == "Shcell":
        getcell()
    if cmdcheck == "Spoint":
        getpointer()
    if cmdcheck == "Shoall":
        showall()
    if cmdcheck == "Pointr":
        pointerright()
        print("Moved the pointer 1 to the right.")
    if cmdcheck == "Pointl":
        pointerleft()
        print("Moved the pointer 1 to the left.")
    if cmdcheck == "Prcell":
        printcell()
    if cmdcheck == "Prallc":
        printall()
    if cmdcheck == "Endall":
        endpc()
    if cmdcheck == "Hiworl":
        print("Hello World!")
    if cmdcheck == "String":
        global strsav
        strsav = str(cmd[6:])
        if (len(cmd[6:])) >= 20:
            print(f"ERROR: Memory can only store 20 characters!")
        else:
            stringsave(strsav)
    if cmdcheck == "Setpnt":
        
        global setpoint
        
        setpoint = int(cmd[6:])
        print(f"Set pointer to location c{setpoint}")
        setpointer(setpoint)
    if cmdcheck == "Prgram":
        global writtenprogram
        writtenprogram = str(cmd[6:])
        writeprogram(writtenprogram)
    if cmdcheck == "Wrtall":
        stringsave("»»»»»»»»»»»»»»»»»»»»")
        print("Wrote all accessable cells as 187")
    if cmdcheck == "Adwash":
        wash()
    if cmdcheck == "Gameft":
        print("Running game 'Fight'...")
        print("\nWelcome to the fight! Sword beats bomb, gun beats sword, bomb beats gun!")
        runrps()
    if cmdcheck == "Gamesl":
        print("Running game 'Slots'...")
        runslots()
    if cmdcheck == "Savedp":
        print(savedprogram)

def reqcmd():
    global cmd
    cmd = input("\nEnter a Command: ").capitalize()
    runcmd()

while go == True:
    reqcmd()
