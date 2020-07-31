import sys
from PyQt5.QtWidgets import QApplication, QDialog
import socket
from threading import Thread
from socketserver import ThreadingMixIn
from chatsclient import *

## username = input("username: ") ##testing
client1 = None
#Gui logic
class Window(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.textEditMessages=self.ui.textEditMessages
        self.ui.pushButtonSend.clicked.connect(self.dispMessage)
        self.show()
        
    def dispMessage(self):
        text=self.ui.lineEditMessages.text()
        self.ui.textEditMessages.append("Client> "+self.ui.lineEditMessages.text())
        client1.send(text.encode("utf-8"))
        self.ui.lineEditMessages.setText("")
        

#chatapp logic        
class ClientThread(Thread):
    def __init__(self,window):
        Thread.__init__(self)
        self.window=window
    def run(self):
        #get the IP address of the server by invoking the hostname method on the socket class and, using port 80, 
        # the client tries to connect to the server.
        host = socket.gethostname()
        port = 1234
        BUFFER_SIZE = 1024 #so we can read 1mb 
        global client1
        client1 = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        client1.connect((host, port))
        
        
        while True:
            #if connection is made the client will try to recieve data 
            data = client1.recv(BUFFER_SIZE)
            window.textEditMessages.append("Server>"+data.decode("utf-8")) 
            
            
            #client1.close() 
            ### still not sure how to properly pick a time close 
            ## cause imediatly clossing leads to a bug where client cant send message
            
            
if __name__=="__main__":
    app = QApplication(sys.argv)
    window = Window()
    clientThread=ClientThread(window)
    clientThread.start()
    window.exec()
    sys.exit(app.exec_())      
