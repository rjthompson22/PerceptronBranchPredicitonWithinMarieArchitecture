from tkinter import *
from tkinter import ttk
from tkinter import font

class CycleGUI:
#GUI for the main memory of the marie architecture, where the user writes code

    
    def __init__(self, root, col, row, cspan=1, rspan=1):

        #Instruction Cycle
        self.ICframe = ttk.Frame(root, padding="3 3 12 12")
        self.ICframe.grid(column=col, row=row, columnspan = cspan, rowspan = rspan,
                     sticky=(N, W, E, S))
        
        #Default Display
        self.default_disp = ttk.Frame(self.ICframe)
        self.fetch = StringVar()
        self.decode = StringVar()
        self.execute = StringVar()
        default_disp = self.default_disp
        self.fetch_label = ttk.Label(default_disp, text="Fetch", width = 20)
        self.decode_label = ttk.Label(default_disp, text="Decode", width = 20)
        self.execute_label = ttk.Label(default_disp, text="Execute", width = 20)
        self.fetch_disp = ttk.Label(default_disp, textvariable=self.fetch, background = 'white')
        self.decode_disp = ttk.Label(default_disp, textvariable=self.decode, background = 'white')
        self.execute_disp = ttk.Label(default_disp, textvariable=self.execute, background = 'white')
        
        self.fetch_label.grid(column=0, row=1, padx = 5)
        self.decode_label.grid(column=1, row=1, padx = 5)
        self.execute_label.grid(column=2, row=1, padx = 5)
        self.fetch_disp.grid(column=0, row=2, sticky=(W, E), padx = 5)
        self.decode_disp.grid(column=1, row=2, sticky=(W, E), padx = 5)
        self.execute_disp.grid(column=2, row=2, sticky=(W, E), padx = 5)
        
        #Pipelined Display
        self.pipeline_disp = ttk.Frame(self.ICframe)
        x_labels = ["C1", "C2", "C3", "C4", "C5", "C6", "C7", "C8", "C9", "C10"]
        y_labels = ["I1", "I2", "I3", "I4", "I5", "I6", "I7", "I8", "I9", "I10"]
        row_entries = [StringVar(),StringVar(),StringVar(),StringVar(),
                        StringVar(),StringVar(),StringVar(),StringVar(),
                        StringVar(), StringVar()]
        self.rows = []
        for i in range(10):
            self.rows.append(row_entries)
            
        self.X = []
        self.Y = []
        self.XY = []
        
        for i in range(10):
            self.X.append(ttk.Label(self.pipeline_disp, text = x_labels[i], width = 5))
            self.Y.append(ttk.Label(self.pipeline_disp, text = y_labels[i]))
            self.XY.append([ttk.Label(self.pipeline_disp, textvariable = self.rows[i][j], 
                                      background = 'white', width = 5, borderwidth="2", relief="groove")
                            for j in range(10)])
        for i in range(10):
            self.X[i].grid(column = 1+i, row = 1, sticky = (W))
            self.Y[i].grid(column = 0, row = 2+i)
            for j in range(10):
                self.XY[i][j].grid(column = 1+i, row = 2+j)
        
        self.default_disp.grid(column = 0, row = 1, columnspan = 3)
        
        
        #Radio Button
        #For Pipeline Options
        self.v = IntVar()
        v = self.v
        v.set(0)
        pipelineOptions = [
            ("Non-Pipelined"),
            ("Pipelined")
        ]
        for val, pipelineOptions in enumerate(pipelineOptions):
            Radiobutton(self.ICframe, 
                  text=pipelineOptions,
                  padx = 20, 
                  variable=self.v, 
                  command=self.disp_change,
                  value=val).grid(column = val, row = 0, sticky = (W))
        
    
    def disp_default(self):
        self.default_disp.grid(column = 0, row = 1, columnspan = 3)
        
    def disp_pipeline(self):
        self.pipeline_disp.grid(column = 0, row = 1, columnspan = 3, sticky = 'ew')
        
    def disp_change(self):
        if (self.v.get() == 0):
            self.pipeline_disp.grid_forget()
            self.disp_default()
        else:
            self.default_disp.grid_forget()
            self.disp_pipeline()
    
    
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
            

    def set_XY(self, new_value):
        #new_value input needs to be a 9x9 array
        try:
            for i in range(10):
                for j in range(10):
                    self.XY[i][j].set(new_value[i][j])
        except ValueError:
            for i in range(10):
                for j in range(10):
                    self.XY[i][j].set("err") 