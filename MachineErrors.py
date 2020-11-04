from Instructions import *
from Breakpoints import *
from FetchDecodeExecute import *
from Converters import *
from Messages import *

# Step mode
stepping = False

# status of machine
Normal_Halt = 0
Running = 1
Paused = 2
Input_Blocking = 3
Abnormal_Halt = -1
User_Halt = -2
No_Program = -3
Uninitialized = 0xDEAD
machine_state = 0xDEAD
machine_error = False
errorExists = False

# Error Codes and Messages
errorCode = 0
error_messages = ["Program Terminated Normally",
                  "Illegal Instruction/Opcode",
                  "Illegal conditional operand",
                  "Out of Range Address Value",
                  "Invalid Formatting of Machine Code",
                  "IO Exception",
                  "Invalid Register",
                  "Numeric Value Illegal in Register",
                  "Max statements reached"]


# function to halt MARIE in case of error
def halt():
    global machine_state
    global IR
    global Abnormal_Halt
    global machine_error
    global errorCode
    global error_messages
    exit_status = IR & 4095
    # TODO: disable stepping mode
    # TODO: disable runStop
    if machine_error:
        machine_state = Abnormal_Halt
        if errorCode < error_messages.len():
            print("Machine halted abnormally. Error:" + error_messages[errorCode] + ". Exit Status: " + exit_status)
        else:
            print("Machine halted abnormally. Exit Status:" + exit_status)
    else:
        machine_state = Normal_Halt
        print("Machine halted normally. Exit status:" + exit_status)


# restarts display and PC to original states
def restart():
    global machine_state
    global Uninitialized
    global No_Program
    global machine_error
    global errorCode
    global InputREG
    global PC
