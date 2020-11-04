from Instructions import *
from MachineErrors import *
from FetchDecodeExecute import *
from Converters import *
from Breakpoints import *

statusMsg = None
outputHolder = [[None] * 2] * 2


# sets status message, needs to be integrated

def setMessage(msg):
    global statusMsg
    statusMsg = msg
    # TODO: set message field to status message
    # return statusMsg TODO: message field post action event


