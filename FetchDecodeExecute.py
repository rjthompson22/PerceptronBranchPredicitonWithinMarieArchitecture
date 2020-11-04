from Instructions import *
from Instructions import add
from MachineErrors import *
from Converters import *
from Breakpoints import *
from Messages import *

instructionCode = 0  # machine code
programFocusRow = 0  # current order in gui
operandRequired = [True, True, True, True, True, False, False, False, False, False, False, True, True]
memCell = 0  # current mem location


# fetches
def fetchNextInstruction():
    global machine_error
    global MAR
    global PC
    global IR
    global MBR
    global errorCode
    global dictReference
    global programFocusRow
    global instructionCode
    global operandRequired
    global memCell
    global memArray
    global MARIE_ADDRESS
    global errorExists
    global Running
    global machine_state
    aString = ""
    memR = 0
    memC = 0
    if machine_error:
        halt()
        return
    MAR = PC
    # TODO:SET VALUES, post action event
    address = MAR
    memR = address / 16
    memC = address % 16 + 1
    try:
        IR = (" " + str((memArray[memR][memC].trim())))
    except IndexError:
        errorCode = 3
        machine_error = True
        return
    aString = str(PC.trim())
    if aString in dictReference:
        programFocusRow = int(dictReference.get(aString))
        # TODO: Rectangle rect = programTable.getCellRect(programFocusRow, 5, false);
        # TODO: programTable.scrollRectToVisible(rect);
    aString = str(IR.trim())
    try:
        instructionCode = int(aString[0:1], base=16)
        if instructionCode >= operandRequired.len():
            raise ValueError()
    except ValueError:
        machine_error = True
        errorCode = 1
        return
    if operandRequired[instructionCode]:
        MAR = str(IR[1:4].trim())
        # TODO: MAR postaction
        address = MAR
        memR = address / 16
        memC = address % 16 + 1
        memCell = address
    try:  # TODO: Rectangle rect = memoryTable.getCellRect(memoryRow, memoryCol, false); memoryTable.scrollRectToVisible(rect);
        MBR = (" " + (memArray[memR][memC].trim()))
        if machine_error:
            return
        # MBR post action event
    except IndexError:
        errorCode = 3
        machine_error = True
        return
    PC = PC + 1
    if PC > MARIE_ADDRESS:
        errorCode = 8
        machine_error = True
    if machine_error:
        return
    # TODO: PC.postActionEvent()
    errorExists = False
    machine_state = Running


# Executes instructions
def execute():
    global machine_error
    global errorCode
    global instructionCode
    if instructionCode == 0:
        jnS()
    elif instructionCode == 1:
        load()
    elif instructionCode == 2:
        store()
    elif instructionCode == 3:
        add()
    elif instructionCode == 4:
        sub()
    elif instructionCode == 5:
        inputIns()
    elif instructionCode == 6:
        outputIns()
    elif instructionCode == 7:
        halt()
    elif instructionCode == 8:
        skipCond()
    elif instructionCode == 9:
        jump()
    elif instructionCode == 10:
        clear()
    elif instructionCode == 11:
        addI()
    elif instructionCode == 12:
        jumpI();
    else:
        machine_error = True
        errorCode = 1
