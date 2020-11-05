from tkinter import *
from tkinter import ttk
from tkinter import font
#from GUI_style import *

class RegisterGUI:
#GUI for the main memory of the marie architecture, where the user writes code

    def __init__(self, root, col, row, cspan=1, rspan=1):
        
        highlightFont = font.Font(family='Helvetica', size=12, weight='bold')
        Regframe = ttk.Frame(root, padding="3 3 12 12")
        Regframe.grid(column=col, row=row, columnspan = cspan, rowspan = rspan, 
                      sticky=(N, W, E, S))
        ttk.Label(Regframe, text="CPU State", font = highlightFont).grid(column=0, row=0)
        
        PC = StringVar()
        IR = StringVar()
        MAR = StringVar()
        MBR = StringVar()
        AC = StringVar()
        IN = StringVar()
        OUT = StringVar()
        
        REG_C = 0   #Column for Register name
        ENTRY_C = 1  #Column for entry field
        
        PC_entry = ttk.Entry(Regframe, width=10, textvariable=PC)
        PC_entry.grid(column=ENTRY_C, row=1, sticky=(W, E))
        ttk.Label(Regframe, text="Program Counter").grid(column=REG_C, row=1, sticky=E)
        
        IR_entry = ttk.Entry(Regframe, width=10, textvariable=IR)
        IR_entry.grid(column=ENTRY_C, row=2, sticky=(W, E))
        ttk.Label(Regframe, text="Instruction Register").grid(column=REG_C, row=2, sticky=E)
        
        MAR_entry = ttk.Entry(Regframe, width=10, textvariable=MAR)
        MAR_entry.grid(column=ENTRY_C, row=3, sticky=(W, E))
        ttk.Label(Regframe, text="MAR Register").grid(column=REG_C, row=3, sticky=E)
        
        MBR_entry = ttk.Entry(Regframe, width=10, textvariable=MBR)
        MBR_entry.grid(column=ENTRY_C, row=4, sticky=(W, E))
        ttk.Label(Regframe, text="MBR Register").grid(column=REG_C, row=4, sticky=E)
        
        AC_entry = ttk.Entry(Regframe, width=10, textvariable=AC)
        AC_entry.grid(column=ENTRY_C, row=5, sticky=(W, E))
        ttk.Label(Regframe, text="Accumulator").grid(column=REG_C, row=5, sticky=E)
        
        IN_entry = ttk.Entry(Regframe, width=10, textvariable=IN)
        IN_entry.grid(column=ENTRY_C, row=6, sticky=(W, E))
        ttk.Label(Regframe, text="Input").grid(column=REG_C, row=6, sticky=E)
        
        OUT_entry = ttk.Entry(Regframe, width=10, textvariable=OUT)
        OUT_entry.grid(column=ENTRY_C, row=7, sticky=(W, E))
        ttk.Label(Regframe, text="Output").grid(column=REG_C, row=7, sticky=E)