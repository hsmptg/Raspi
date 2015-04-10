import pigpio

#import platform
#if platform.uname()[4] == "armv6l":
#    import RPi.GPIO as GPIO # @UnresolvedImport @UnusedImport
#else:
#    import virtualGPIO as GPIO # @Reimport
    
class LedBut():
    def __init__(self, server, parent=None):
        self.server = server
        
        self.pi = pigpio.pi()
        self.pi.set_mode( 4, pigpio.OUTPUT) # LED
        self.pi.set_mode(17, pigpio.INPUT)  # BUT
    
        self.but = not self.pi.read(17)
    
    def procBut(self):
        b = not self.pi.read(17)
        if b != self.but:
            self.but = b
            self.server.send("b1" if b else "b0")
        
    def cmdLed(self, cmd):
        self.pi.write(4, cmd[1] == "1")
    
    def cmdBut(self, cmd):
        b = not self.pi.read(17)
        self.server.send("b1" if b else "b0")