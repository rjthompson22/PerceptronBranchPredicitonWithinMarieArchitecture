from enum import Enum
from Instructions import *
from Breakpoints import *
from FetchDecodeExecute import *
from MachineErrors import *
from Messages import *


# Function to insert string in location of another string

def insert_sequence(str1, str2, int):
    str1_split1 = str1[:int]
    str1_split2 = str1[int:]
    new_string = str1_split1 + str2 + str1_split2
    return new_string


# Conversion of  decimal to hexadecimal in 2's complement(represents negative numbers)
# Range of MARIE word values
def convertDecToHex(decimal):
    if decimal < 0:
        decimal = decimal
        decimal = (1 << 16) + decimal
    else:
        if (decimal & (1 << (16 - 1))) != 0:
            decimal = decimal - (1 << 16)
    decimal = hex(decimal)  # converts to hexadecimal format after calculating 2's complement
    # If statements pad zeros to display proper formatting of hexadecimal (0x0000 - 0xFFFF)
    if len(decimal) == 3:
        return insert_sequence(decimal, '000', 2)
    if len(decimal) == 4:
        return insert_sequence(decimal, '00', 2)
    if len(decimal) == 5:
        return insert_sequence(decimal, '0', 2)
    if len(decimal) == 6:
        return decimal
    if len(decimal) > 6:
        return decimal[0:6]


# Converts decimal to hexadecimal for address values.
# If statements pad zeros top display proper formatting of hexadecimal addressing(0x000- 0xFFF)
def convertAddressToHex(address):
    if address < 0:
        address = address
        address = (1 << 20) + address
    else:
        if (address & (1 << (20 - 1))) != 0:
            address = address - (1 << 20)
    address = hex(address)  # converts to hexadecimal format after calculating 2's complement
    if len(address) == 3:
        return insert_sequence(address, '00', 2)
    if len(address) == 4:
        return insert_sequence(address, '0', 2)
    if len(address) == 5:
        return address
    if len(address) > 5:
        return address[0:5]

# translates integer to HEX/DEC and outputs GUI
# TODO: implement this function
# def reformat():
