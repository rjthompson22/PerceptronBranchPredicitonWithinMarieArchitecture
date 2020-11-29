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
        
        self.PC = StringVar()
        self.IR = StringVar()
        self.MAR = StringVar()
        self.MBR = StringVar()
        self.AC = StringVar()
        self.IN = StringVar()
        self.OUT = StringVar()
        
        REG_C = 0   #Column for Register name
        ENTRY_C = 1  #Column for entry field
        
        PC_entry = ttk.Entry(Regframe, width=10, textvariable=self.PC)
        PC_entry.grid(column=ENTRY_C, row=1, sticky=(W, E))
        ttk.Label(Regframe, text="Program Counter").grid(column=REG_C, row=1, sticky=E)
        
        IR_entry = ttk.Entry(Regframe, width=10, textvariable=self.IR)
        IR_entry.grid(column=ENTRY_C, row=2, sticky=(W, E))
        ttk.Label(Regframe, text="Instruction Register").grid(column=REG_C, row=2, sticky=E)
        
        MAR_entry = ttk.Entry(Regframe, width=10, textvariable=self.MAR)
        MAR_entry.grid(column=ENTRY_C, row=3, sticky=(W, E))
        ttk.Label(Regframe, text="MAR Register").grid(column=REG_C, row=3, sticky=E)
        
        MBR_entry = ttk.Entry(Regframe, width=10, textvariable=self.MBR)
        MBR_entry.grid(column=ENTRY_C, row=4, sticky=(W, E))
        ttk.Label(Regframe, text="MBR Register").grid(column=REG_C, row=4, sticky=E)
        
        AC_entry = ttk.Entry(Regframe, width=10, textvariable=self.AC)
        AC_entry.grid(column=ENTRY_C, row=5, sticky=(W, E))
        ttk.Label(Regframe, text="Accumulator").grid(column=REG_C, row=5, sticky=E)
        
        IN_entry = ttk.Entry(Regframe, width=10, textvariable=self.IN)
        IN_entry.grid(column=ENTRY_C, row=6, sticky=(W, E))
        ttk.Label(Regframe, text="Input").grid(column=REG_C, row=6, sticky=E)
        
        OUT_entry = ttk.Entry(Regframe, width=10, textvariable=self.OUT)
        OUT_entry.grid(column=ENTRY_C, row=7, sticky=(W, E))
        ttk.Label(Regframe, text="Output").grid(column=REG_C, row=7, sticky=E)
      
        
    def set_PC(self, new_value):
        try:
            self.PC.set(new_value)
        except ValueError:
            self.status.set("value error")
            
    def set_IR(self, new_value):
        try:
            self.IR.set(new_value)
        except ValueError:
            self.status.set("value error")
            
    def set_AC(self, new_value):
        try:
            self.AC.set(new_value)
        except ValueError:
            self.status.set("value error")            
            
    def set_MAR(self, new_value):
        try:
            self.MAR.set(new_value)
        except ValueError:
            self.status.set("value error")            

    def set_MBR(self, new_value):
        try:
            self.AC.set(new_value)
        except ValueError:
            self.status.set("value error")
            
    def set_OUT(self, new_value):
        try:
            self.AC.set(new_value)
        except ValueError:
            self.status.set("value error")                  
            
    def get_PC(self):
        return(self.PC.get())
            
    def get_IR(self):
        return(self.IR.get())
            
    def get_AC(self):
        return(self.AC.get())          
            
    def get_MAR(self):
        return(self.MAR.get())            

    def get_MBR(self, new_value):
        return(self.MBR.get())
            
    def get_IN(self):
        return(self.IN.get())
            
            
            