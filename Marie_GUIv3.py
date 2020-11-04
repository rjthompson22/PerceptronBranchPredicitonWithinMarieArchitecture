from tkinter import *
from tkinter import ttk
from tkinter import font

#Window Configuration
root = Tk()
root.title("Marie Architecture")

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=1)
root.columnconfigure(2, weight=1)
root.columnconfigure(3, weight=1)
root.columnconfigure(4, weight=1)
root.columnconfigure(5, weight=1)
root.columnconfigure(6, weight=1)
root.rowconfigure(0, weight=1)	

ttk.Label(mainframe, text="                                 ").grid(column=2, row=1)
highlightFont = font.Font(family='Helvetica', size=12, weight='bold')

#MARIE Instructions
Instframe = ttk.Frame(mainframe, padding="3 3 12 12")
Instframe.grid(column=0, row=0, sticky=(N, W, E, S), columnspan = 2)
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

I0_entry = ttk.Entry(Instframe, width=20, textvariable=instructions[0]).grid(column=2, row=2, sticky=(W, E), columnspan = 2)
I1_entry = ttk.Entry(Instframe, width=20, textvariable=instructions[1]).grid(column=2, row=3, sticky=(W, E), columnspan = 2)
I2_entry = ttk.Entry(Instframe, width=20, textvariable=instructions[2]).grid(column=2, row=4, sticky=(W, E), columnspan = 2)
I3_entry = ttk.Entry(Instframe, width=20, textvariable=instructions[3]).grid(column=2, row=5, sticky=(W, E), columnspan = 2)
I4_entry = ttk.Entry(Instframe, width=20, textvariable=instructions[4]).grid(column=2, row=6, sticky=(W, E), columnspan = 2)
I5_entry = ttk.Entry(Instframe, width=20, textvariable=instructions[5]).grid(column=2, row=7, sticky=(W, E), columnspan = 2)
I6_entry = ttk.Entry(Instframe, width=20, textvariable=instructions[6]).grid(column=2, row=8, sticky=(W, E), columnspan = 2)
I7_entry = ttk.Entry(Instframe, width=20, textvariable=instructions[7]).grid(column=2, row=9, sticky=(W, E), columnspan = 2)
I8_entry = ttk.Entry(Instframe, width=20, textvariable=instructions[8]).grid(column=2, row=10, sticky=(W, E), columnspan = 2)
I9_entry = ttk.Entry(Instframe, width=20, textvariable=instructions[9]).grid(column=2, row=11, sticky=(W, E), columnspan = 2)

for i, k in enumerate(instructions):
    label = "Instruction " + str(i) + ":"
    ttk.Label(Instframe, text=label).grid(column=1, row=i+2, sticky=E)


#MARIE Registers
Regframe = ttk.Frame(mainframe, padding="3 3 12 12")
Regframe.grid(column=2, row=0, sticky=(N, W, E, S), columnspan = 2)
ttk.Label(Regframe, text="CPU State", font = highlightFont).grid(column=0, row=0, columnspan = 2)
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


#Instruction Cycle
ICframe = ttk.Frame(mainframe, padding="3 3 12 12")
ICframe.grid(column=0, row=1, sticky=(N, W, E, S), columnspan = 4)

fetch = StringVar()
decode = StringVar()
execute = StringVar()

ttk.Label(ICframe, text="Fetch", width = 20).grid(column=1, row=0)
ttk.Label(ICframe, text="Decode", width = 20).grid(column=2, row=0)
ttk.Label(ICframe, text="Execute", width = 20).grid(column=3, row=0)
ttk.Label(ICframe, textvariable=fetch, background = 'white').grid(column=1, row=1, sticky=(W, E), padx = 5)
ttk.Label(ICframe, textvariable=decode, background = 'white').grid(column=2, row=1, sticky=(W, E), padx = 5)
ttk.Label(ICframe, textvariable=execute, background = 'white').grid(column=3, row=1, sticky=(W, E), padx = 5)


for child in mainframe.winfo_children(): 
    child.grid_configure(padx=5, pady=5)
PC_entry.focus()


root.mainloop()