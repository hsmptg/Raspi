BCM = 0
OUT = 0
IN = 1

def setwarnings(flag):
    pass

def setmode(mode):
    pass

def setup(pin, direction):
    pass

def input(pin):  # @ReservedAssignment
    return True

def output(pin, value):
    print("pin {0} = {1}".format(pin, value))
