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
highlightFont = font.Font(family='Helvetica', name='appHighlightFont', size=12, weight='bold')

#MARIE Instructions
ttk.Label(mainframe, text="Main Memory", font = highlightFont).grid(column=1, row=1, columnspan = 2)
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

I0_entry = ttk.Entry(mainframe, width=7, textvariable=instructions[0]).grid(column=2, row=2, sticky=(W, E), columnspan = 2)
I1_entry = ttk.Entry(mainframe, width=7, textvariable=instructions[1]).grid(column=2, row=3, sticky=(W, E), columnspan = 2)
I2_entry = ttk.Entry(mainframe, width=7, textvariable=instructions[2]).grid(column=2, row=4, sticky=(W, E), columnspan = 2)
I3_entry = ttk.Entry(mainframe, width=7, textvariable=instructions[3]).grid(column=2, row=5, sticky=(W, E), columnspan = 2)
I4_entry = ttk.Entry(mainframe, width=7, textvariable=instructions[4]).grid(column=2, row=6, sticky=(W, E), columnspan = 2)
I5_entry = ttk.Entry(mainframe, width=7, textvariable=instructions[5]).grid(column=2, row=7, sticky=(W, E), columnspan = 2)
I6_entry = ttk.Entry(mainframe, width=7, textvariable=instructions[6]).grid(column=2, row=8, sticky=(W, E), columnspan = 2)
I7_entry = ttk.Entry(mainframe, width=7, textvariable=instructions[7]).grid(column=2, row=9, sticky=(W, E), columnspan = 2)
I8_entry = ttk.Entry(mainframe, width=7, textvariable=instructions[8]).grid(column=2, row=10, sticky=(W, E), columnspan = 2)
I9_entry = ttk.Entry(mainframe, width=7, textvariable=instructions[9]).grid(column=2, row=11, sticky=(W, E), columnspan = 2)

for i, k in enumerate(instructions):
    label = "Instruction " + str(i) + ":"
    ttk.Label(mainframe, text=label).grid(column=1, row=i+2, sticky=E)




#MARIE Registers
ttk.Label(mainframe, text="CPU State", font = highlightFont).grid(column=5, row=1, columnspan = 2)
PC = StringVar()
IR = StringVar()
MAR = StringVar()
MBR = StringVar()
AC = StringVar()
IN = StringVar()
OUT = StringVar()

REG_C = 5   #Column for Register name
ENTRY_C = 6  #Column for entry field

PC_entry = ttk.Entry(mainframe, width=7, textvariable=PC)
PC_entry.grid(column=ENTRY_C, row=2, sticky=(W, E))
ttk.Label(mainframe, text="Program Counter").grid(column=REG_C, row=2, sticky=E)

IR_entry = ttk.Entry(mainframe, width=7, textvariable=IR)
IR_entry.grid(column=ENTRY_C, row=3, sticky=(W, E))
ttk.Label(mainframe, text="Instruction Register").grid(column=REG_C, row=3, sticky=E)

MAR_entry = ttk.Entry(mainframe, width=7, textvariable=MAR)
MAR_entry.grid(column=ENTRY_C, row=4, sticky=(W, E))
ttk.Label(mainframe, text="MAR Register").grid(column=REG_C, row=4, sticky=E)

MBR_entry = ttk.Entry(mainframe, width=7, textvariable=MBR)
MBR_entry.grid(column=ENTRY_C, row=5, sticky=(W, E))
ttk.Label(mainframe, text="MBR Register").grid(column=REG_C, row=5, sticky=E)

AC_entry = ttk.Entry(mainframe, width=7, textvariable=AC)
AC_entry.grid(column=ENTRY_C, row=6, sticky=(W, E))
ttk.Label(mainframe, text="Accumulator").grid(column=REG_C, row=6, sticky=E)

IN_entry = ttk.Entry(mainframe, width=7, textvariable=IN)
IN_entry.grid(column=ENTRY_C, row=7, sticky=(W, E))
ttk.Label(mainframe, text="Input").grid(column=REG_C, row=7, sticky=E)

OUT_entry = ttk.Entry(mainframe, width=7, textvariable=OUT)
OUT_entry.grid(column=ENTRY_C, row=8, sticky=(W, E))
ttk.Label(mainframe, text="Output").grid(column=REG_C, row=8, sticky=E)


fetch = StringVar()
decode = StringVar()
execute = StringVar()

ttk.Label(mainframe, text="Fetch").grid(column=1, row=12, columnspan = 2, sticky = W)
ttk.Label(mainframe, text="Decode").grid(column=3, row=12, columnspan = 2, sticky = W)
ttk.Label(mainframe, text="Execute").grid(column=5, row=12, columnspan = 2, sticky = W)
ttk.Label(mainframe, textvariable=fetch).grid(column=1, row=13, sticky=(W, E))
ttk.Label(mainframe, textvariable=decode).grid(column=3, row=13, sticky=(W, E))
ttk.Label(mainframe, textvariable=execute).grid(column=5, row=13, sticky=(W, E))



for child in mainframe.winfo_children(): 
    child.grid_configure(padx=5, pady=5)
PC_entry.focus()


root.mainloop()
