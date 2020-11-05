from tkinter import *
from tkinter import ttk
from tkinter import font

class InstructionGUI:
#GUI for the main memory of the marie architecture, where the user writes code

    def __init__(self, root, col, row, cspan, rspan):
        
        highlightFont = font.Font(family='Helvetica', size=12, weight='bold')
        
        Instframe = ttk.Frame(root, padding="3 3 12 12")
        Instframe.grid(column=col, row=row, sticky=(N, W, E, S), columnspan = cspan, rowspan = rspan)
        
        ttk.Label(Instframe, text="Main Memory", font = highlightFont).grid(column=1, row=1, columnspan = 2)
        I0 = StringVar()
        I1 = StringVar()
        I2 = StringVar()
        I3 = StringVar()
        I4 = StringVar()
        I5 = StringVar()
        I6 = StringVar()
        I7 = StringVar()
        I8 = StringVar()
        I9 = StringVar()
        instructions = [I0, I1, I2, I3, I4, I5, I6, I7, I8, I9]
        
        I0_entry = ttk.Entry(Instframe, width=20, textvariable=instructions[0])
        I0_entry.grid(column=2, row=2, sticky=(W, E), columnspan = 2)
        
        I1_entry = ttk.Entry(Instframe, width=20, textvariable=instructions[1])
        I1_entry.grid(column=2, row=3, sticky=(W, E), columnspan = 2)
        
        I2_entry = ttk.Entry(Instframe, width=20, textvariable=instructions[2])
        I2_entry.grid(column=2, row=4, sticky=(W, E), columnspan = 2)
        
        I3_entry = ttk.Entry(Instframe, width=20, textvariable=instructions[3])
        I3_entry.grid(column=2, row=5, sticky=(W, E), columnspan = 2)
        
        I4_entry = ttk.Entry(Instframe, width=20, textvariable=instructions[4])
        I4_entry.grid(column=2, row=6, sticky=(W, E), columnspan = 2)
        
        I5_entry = ttk.Entry(Instframe, width=20, textvariable=instructions[5])
        I5_entry.grid(column=2, row=7, sticky=(W, E), columnspan = 2)
        
        I6_entry = ttk.Entry(Instframe, width=20, textvariable=instructions[6])
        I6_entry.grid(column=2, row=8, sticky=(W, E), columnspan = 2)
        
        I7_entry = ttk.Entry(Instframe, width=20, textvariable=instructions[7])
        I7_entry.grid(column=2, row=9, sticky=(W, E), columnspan = 2)
        
        I8_entry = ttk.Entry(Instframe, width=20, textvariable=instructions[8])
        I8_entry.grid(column=2, row=10, sticky=(W, E), columnspan = 2)
        
        I9_entry = ttk.Entry(Instframe, width=20, textvariable=instructions[9])
        I9_entry.grid(column=2, row=11, sticky=(W, E), columnspan = 2)

        for i, k in enumerate(instructions):
            label = "Instruction " + str(i) + ":"
            ttk.Label(Instframe, text=label).grid(column=1, row=i+2, sticky=E)