import threading
from FetchDecodeExecute import *
from Instructions import *
from MachineErrors import *
from Messages import *



#breakpointOn = False
#lastStatement = 0
#aString = ""
#programArray = [0][0]

# thread function


def runIt():
    global programArray
    isBreakpoint = bool(programArray[lastStatement][24])


# starts breakpoint in program
def startBreakPoint():
    t1 = threading.Thread
