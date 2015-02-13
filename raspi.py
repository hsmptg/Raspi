import time #sleep
import sys #exit
import signal #signal
import server
import adxl345

def signal_handler(signal, frame):
    app.exit()

class App():
    def __init__(self):
        self.version = "v1.0 ADXL345"
        print(self.version)
        signal.signal(signal.SIGINT, signal_handler)
            
        self.server = server.Server()   
        self.server.onCmd = self.onCmd
        self.acel = adxl345.ADXL345()

        while True:
            time.sleep(.1)
    
    def onCmd(self, cmd):
        if cmd[0:3] == "log":
            self.server.log = True if cmd[3:4] == "1" else False       
        elif cmd[0] == "v":
            print(self.version)
            self.server.send(self.version)       
        elif cmd[0] == "i":
            id = self.acel.ID()
            msg = "ID= {0:02X}".format(id)
            print(msg)
            self.server.send(msg)       
        elif cmd[0] == "a":
            v = self.acel.getData()
#            print "X=0x%0.4X Y=0x%0.4X Z=0x%0.4X" % (v.x, v.y, v.z)
            print("a {0} {1} {2}").format(v.x, v.y, v.z)
        
    def exit(self):
        print("\rYou pressed Ctrl+C!")
        self.server.exit()
        sys.exit(0)
        
if __name__ == '__main__':
    app = App()