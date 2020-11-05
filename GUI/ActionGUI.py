# TODO: Complete run and step function calls to the backend

from tkinter import *
from tkinter import ttk
from tkinter import font
from InstructionGUI import *

class ActionGUI:
#GUI for the main memory of the marie architecture, where the user writes code

    

    def __init__(self, root, col, row, cspan=1, rspan=1):
        
        #Buttons to run the program
        Runframe = ttk.Frame(root, padding="3 3 12 12")
        Runframe.grid(column=col, row=row, columnspan = cspan, rowspan = rspan, 
                      sticky=(N, W, E, S))
        
        self.status = StringVar()
        ttk.Label(Runframe, text="System Status: ").grid(column=0, row=2, pady = 5, sticky = (E))      
        ttk.Label(Runframe, textvariable=self.status, background = 'white', width = 20).grid(
            column=1, row=2, pady = 5, sticky=(W))
        
        RunComplete = ttk.Button(Runframe, text='Run', command = self.run)
        RunComplete.grid(column=0, row = 0, columnspan = 2)
        
        RunStep = ttk.Button(Runframe, text='Step', command = self.step)
        RunStep.grid(column=0, row = 1, columnspan = 2)
        
    
    def set_status(self, status_update):
        
        try:
            self.status.set(status_update)
        except ValueError:
            self.status.set("error")
        
    def run(self):
        pass
    
    def step(self):
        pass