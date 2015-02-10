import platform

if platform.uname()[4] == "armv6l":
    import RPi.GPIO as GPIO # @UnresolvedImport @UnusedImport
else:
    import virtualGPIO as GPIO # @Reimport
    
class LedBut():
    def __init__(self, server, parent=None):
        self.server = server
        
        #to disable RuntimeWarning: This channel is already in use
        GPIO.setwarnings(False)
        
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(4, GPIO.OUT)
        GPIO.output(4, True)
        GPIO.setup(17, GPIO.IN)
    
        self.but = not GPIO.input(17)
    
    def procBut(self):
        b = not GPIO.input(17)
        if b != self.but:
            self.but = b
            self.server.send("b1" if b else "b0")
        
    def cmdLed(self, cmd):
        GPIO.output(4, cmd[1] == "1")
    
    def cmdBut(self, cmd):
        b = not GPIO.input(17)
        self.server.send("b1" if b else "b0")