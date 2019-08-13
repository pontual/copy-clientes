from time import sleep
from pyautogui import click, hotkey, keyDown, keyUp, dragTo, press, typewrite
from tkinter import Tk, TclError
import sys

LAST_VAL = ""

def getfield(x1, x2, y):
    dt = 0.15
    click(x2, y)
    dragTo(x1, y, dt, button="left")
    hotkey("ctrl", "c")
    

def getcli(n):
    tk = Tk()
    out = []

    out.append(str(n))
    def ctrlv():
        global LAST_VAL
        nonlocal tk, out
        try:
            val = tk.selection_get(selection="CLIPBOARD").strip()
            if val == LAST_VAL:
                val = ""
            out.append(val)
            LAST_VAL = val
        except TclError:
            print("nothing to copy")
        
        
    # row y-coords
    r1 = 140
    r2 = 180
    r3 = 220
    r4 = 260

    # top bar
    click(25, 10)

    # select cli
    press("f3")
    sleep(0.5)
    typewrite(str(n) + '\n')
    
    getfield(14, 405, r1)
    ctrlv()
    
    getfield(422, 566, r1)
    ctrlv()

    getfield(671, 764, r1)
    ctrlv()

    # row 2
    getfield(14, 408, r2)
    ctrlv()

    getfield(422, 567, r2)
    ctrlv()

    getfield(581, 741, r2)
    ctrlv()

    getfield(756, 784, r2)
    ctrlv()

    getfield(14, 82, r3)
    ctrlv()

    getfield(117, 295, r3)
    ctrlv()

    getfield(310, 456, r3)
    ctrlv()

    getfield(493, 616, r3)
    ctrlv()

    getfield(14, 262, r4)
    ctrlv()
    
    tk.destroy()

    return '"' + '","'.join(out) + '"'
 

if __name__ == "__main__":
    fname = sys.argv[1]
    outname = sys.argv[2]
    input("Bring Cliente to front and press Enter")
    with open(fname) as f, open(outname, 'w', encoding="utf-8") as o:
        for line in f:
            line = line.strip()
            print(line)
            if len(line) > 0:
                print(getcli(line), file=o)
