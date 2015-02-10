import time #sleep
import sys #exit
import signal #signal
import server

def signal_handler(signal, frame):
    app.exit()

class App():
    def __init__(self):
        print("Raspi")
        signal.signal(signal.SIGINT, signal_handler)
            
        self.server = server.Server()   
        self.server.onCmd = self.onCmd

        while True:
            time.sleep(.1)
    
    def onCmd(self, cmd):
        if cmd[0:3] == "log":
            self.server.log = True if cmd[3:4] == "1" else False       
        elif cmd[0] == "v":
            version = "v1.0 Raspi"
            print(version)
            self.server.send(version)       
        
    def exit(self):
        print("\rYou pressed Ctrl+C!")
        self.server.exit()
        sys.exit(0)
        
if __name__ == '__main__':
    app = App()