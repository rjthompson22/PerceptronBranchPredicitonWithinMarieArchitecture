from tkinter import *
import tkinter as tk
from tkinter import font

class InstructionGUI(tk.Frame):
#GUI for the main memory of the marie architecture, where the user writes code


    def __init__(self, root, frame, col, row, cspan, rspan):
        super().__init__(master=root)
        self.grid()
        
        highlightFont = font.Font(family='Helvetica', size=12, weight='bold')
        
        
        self.entriesCanvas = tk.Canvas(frame, borderwidth=0, background="white")
        self.entriesFrame = tk.Frame(self.entriesCanvas, background="white")
        self.scrollbar = tk.Scrollbar(frame, command=self.entriesCanvas.yview)
        self.entriesCanvas.configure(yscrollcommand=self.scrollbar.set)

        
        
        #tk.Label(self.entriesCanvas, text="Main Memory", font = highlightFont).grid(column=col, row=row)
        self.entriesCanvas.grid(column=col, row=row, sticky=(N, W, E, S), columnspan = cspan, rowspan = rspan)
        self.scrollbar.grid(column=col+1, row=row, rowspan = rspan, sticky='nsw')
        
        self.entriesCanvas.create_window((0, 0), window=self.entriesFrame,
                                         anchor='nw', tags='self.entriesFrame')

        self.entriesCanvas.bind('<Configure>', self.onFrameConfigure)

        self.entries = []
        self.labels = []
        for i in range(100):
            self.labels.append(tk.Label(self.entriesFrame, text = str(i), width = 10))
            self.entries.append(tk.Entry(self.entriesFrame, font=('arial', 10)))
            self.labels[i].grid(column=0, row=i, sticky = (E))
            self.entries[i].grid(column=1, row=i)
            

    def onFrameConfigure(self, event):
        self.entriesCanvas.configure(scrollregion=self.entriesCanvas.bbox("all"), width=self.entriesFrame.winfo_width())
            
            
    def get_instructions(self):
        instructions = []
        for i in self.entries:
            instructions.append(i.get())
            
        return self.instructions
    
    
    def get_next_instruction(self):
        for i, k in enumerate(self.entries):
            yield (i, k.get())