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



#MARIE Instructions
InstructionGUI(mainframe,0,0,1,2)

#MARIE Registers
RegisterGUI(mainframe,1,0,1,1)


#Instruction Cycle
CycleGUI(mainframe, 0, 2, 2, 1)


#Buttons
ActionGUI(mainframe, 1, 1, 1, 1)


for child in mainframe.winfo_children(): 
    child.grid_configure(padx=5, pady=5)





root.mainloop()