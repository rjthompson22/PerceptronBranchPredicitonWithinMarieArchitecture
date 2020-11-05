from tkinter import *
from tkinter import ttk
from tkinter import font

class CycleGUI:
#GUI for the main memory of the marie architecture, where the user writes code

    def __init__(self, root, col, row, cspan=1, rspan=1):

        #Instruction Cycle
        ICframe = ttk.Frame(root, padding="3 3 12 12")
        ICframe.grid(column=col, row=row, columnspan = cspan, rowspan = rspan,
                     sticky=(N, W, E, S))
        
        self.fetch = StringVar()
        self.decode = StringVar()
        self.execute = StringVar()
        
        ttk.Label(ICframe, text="Fetch", width = 20).grid(column=1, row=0, padx = 5)
        ttk.Label(ICframe, text="Decode", width = 20).grid(column=2, row=0, padx = 5)
        ttk.Label(ICframe, text="Execute", width = 20).grid(column=3, row=0, padx = 5)
        
        ttk.Label(ICframe, textvariable=self.fetch, background = 'white').grid(
            column=1, row=1, sticky=(W, E), padx = 5)
        ttk.Label(ICframe, textvariable=self.decode, background = 'white').grid(
            column=2, row=1, sticky=(W, E), padx = 5)
        ttk.Label(ICframe, textvariable=self.execute, background = 'white').grid(
            column=3, row=1, sticky=(W, E), padx = 5)
        
    def set_fetch(self, new_value):
        try:
            self.fetch.set(new_value)
        except ValueError:
            self.fetch.set("value error")  
            
    def set_decode(self, new_value):
        try:
            self.decode.set(new_value)
        except ValueError:
            self.decode.set("value error")  
            
    def set_execute(self, new_value):
        try:
            self.execute.set(new_value)
        except ValueError:
            self.execute.set("value error") 