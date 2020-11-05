from tkinter import *
from tkinter import ttk
from tkinter import font

class ActionGUI:
#GUI for the main memory of the marie architecture, where the user writes code

    def __init__(self, root, col, row, cspan=1, rspan=1):
        
        #Buttons to run the program
        Runframe = ttk.Frame(root, padding="3 3 12 12")
        Runframe.grid(column=col, row=row, columnspan = cspan, rowspan = rspan, 
                      sticky=(N, W, E, S))
        
        RunComplete = ttk.Button(Runframe, text='Run')
        RunComplete.grid(column=0, row = 0)
        
        RunStep = ttk.Button(Runframe, text='Step')
        RunStep.grid(column=0, row = 1)