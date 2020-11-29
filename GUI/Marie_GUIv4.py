# TODO: Complete run and step function calls to the backend in ActionGUI

from tkinter import *
from tkinter import ttk
from tkinter import font
from InstructionGUI import *
from RegisterGUI import *
from CycleGUI import *
from ActionGUI import *

#Window Configuration
root = Tk()
root.title("Marie Architecture")

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))

highlightFont = font.Font(family='Helvetica', size=12, weight='bold')

#MARIE Instructions
ttk.Label(mainframe, text="Main Memory", font = highlightFont).grid(column=0, row=0, columnspan = 1)
InstructionGUI(root, mainframe, 0,1,1,2)

#MARIE Registers
ttk.Label(mainframe, text="CPU State", font = highlightFont).grid(column=2, row=0)
RegisterGUI(mainframe,2,1,1,1)


#Instruction Cycle
CycleGUI(mainframe, 0, 4, 3, 1)


#Buttons
ActionGUI(mainframe, 2, 2, 1, 1)


for child in mainframe.winfo_children(): 
    child.grid_configure(padx=5, pady=5)


root.mainloop()