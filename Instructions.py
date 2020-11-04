from Converters import *
from MachineErrors import *
from Breakpoints import *
from FetchDecodeExecute import *
from Messages import *

# Registers for MARIE
AC = 0
IR = 1
MAR = 2
MBR = 3
PC = 4
InputREG = 5
OutputREG = 6

# Memory of MARIE words
MARIE_DEC_MAX = 32767
MARIE_DEC_MIN = -32768

# Output Change
Hex = 0
Dec = 1
ASCII = 2

# Memory Addresses
MARIE_ADDRESS = 4095

dictReference = {}

memArray = [[None] * 256] * 17


# Instructions for MARIE

# Load Instruction

def load():
    global AC
    global MBR
    AC = MBR
    return AC
    # TODO:  return AC, Event handler to insert.


# Store Instruction with operation to display var in memory table array
def store():
    global MBR
    global AC
    global errorCode
    global machine_error
    global memArray
    MBR = AC
    # if error
    if machine_error:
        return
    address = MAR
    memR = address / 16
    memC = address % 16 + 1
    # tries to store in memory table.
    try:
        memArray[memR][memC] = " " + convertDecToHex(MBR)
    # TODO: Rectangle rect = memoryTable.getCellRect(memoryRow, memoryCol, false);
    #        memoryTable.scrollRectToVisible(rect);
    except IndexError:
        errorCode = 3
        machine_error = True


# subtract instruction
def sub():
    global AC
    global MBR
    AC = AC - MBR
    return AC
    # TODO: return AC with event handler


# add instruction

def add():
    global AC
    global MBR
    AC = AC + MBR
    return AC
    # TODO: return AC with event handler


# jump and store instruction

def jnS():
    global MAR
    global memArray
    global PC
    global errorCode
    global machine_error
    address = MAR
    memR = address / 16
    memC = address % 16 + 1
    try:
        memArray[memR][memC] = " " + convertDecToHex(PC)
        PC = (MAR + 1)
        return PC  # TODO: PC post Action Event
    except IndexError:
        errorCode = 3
        machine_error = True


# skip condition instruction
def skipCond():
    global IR
    global machine_error
    global errorCode
    global PC
    instruction = IR
    comparison = (instruction & 3072) >> 10  # strip opcode
    # check if valid comparison
    if comparison == 3:
        machine_error = True
        errorCode = 2
        return
    acVal = AC  # store ac value in acVal variable
    op = instruction & 1023
    if comparison == 0:
        if acVal < op:
            PC = PC + 1
    elif comparison == 1:
        if acVal == op:
            PC = PC + 1
    elif comparison == 2:
        if acVal > op:
            PC = PC + 1
    if machine_error:
        return
    return PC  # TODO: return with post actionevent


# jump instruction
def jump():
    global IR
    global PC
    global machine_error

    address = IR
    address = address & 4095  # strip opcode
    PC = address
    if machine_error:
        return
    return PC  # TODO: return with postactionevent


def clear():
    global AC
    AC = 0
    return AC  # TODO: return with postaction event


# add intermediate instruction
def addI():
    global MAR
    global MBR
    global machine_error
    global memArray
    global errorCode
    MAR = MBR
    if machine_error:
        return
    address = MAR
    memR = address / 16
    memC = address % 16 + 1
    try:
        MBR = (" " + memArray[memR][memC])
        # TODO: return MAR with post action
        # TODO: return MBR with post action
        add()
    except IndexError:
        errorCode = 3
        machine_error = True
        return


# jump intermediate instruction
def jumpI():
    global PC
    global MBR
    global machine_error
    PC = MBR
    if machine_error:
        return
    return PC  # TODO: return PC with post action


# input instruction
def inputIns():
    global machine_state
    global Running
    global Input_Blocking
    global InputREG
    global machine_error
    global AC
    global stepping
    # TODO: status message, make print statements compatible with GUI
    if machine_state == Running:
        print("waiting for input")
        machine_state = Input_Blocking
        # TODO: set text for input -> InputREG = " "
        # TODO: backgrounds for input panel and input box mode?
        # TODO: InputREG.setEditable(True)
        # TODO: request focus so its on screen above other windows
    elif machine_state == Input_Blocking:
        InputREG = input()  # get input from user
        # TODO: close input from being edited until needed again(runStop)
        if machine_error:
            halt()
            return
        AC = InputREG
        if machine_error:
            halt()
            return
        machine_state = Running
        if stepping:
            print("Press [Step] to continue.")
        else:
            print(" ")
        # TODO: Implement BreakPoints
        #  if()
