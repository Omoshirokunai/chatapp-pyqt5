##--by myhsin Hameed--##
## to run this chat app you have to 
## run both servercall.py and clientcall.py

from PyQt5 import QtGui 
from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication, QDialog
from PyQt5.QtCore import QCoreApplication
import sys, time
import socket
from threading import Thread
from socketserver import ThreadingMixIn
conn = None
from chatserver import * 
#we import from our server template ui

class Window(QDialog):
    ## the GUI from server   
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.textEditMessages=self.ui.textEditMessages
        self.ui.pushButtonSend.clicked.connect(self.dispMessage)       
        self.show()
        
    def dispMessage(self): 
        text=self.ui.lineEditMessages.text() 
        global conn
        conn.send(text.encode("utf-8"))        
        self.ui.textEditMessages.append("Server>"+self.ui.lineEditMessages.text())        
        self.ui.lineEditMessages.setText("")
        
        
class serverthread(Thread):
    def __init__(self, window):
        Thread.__init__(self)
        self.window = window
        
    def run(self):
        #TCP_IP = '127.0.0.1'
        #TCP_PORT = 1234
        BUFFER_SIZE = 1024 #1mb
        tcp_server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        tcp_server.bind((socket.gethostname(), 1234))
        
        threads = []# a list of threads (t1)
        tcp_server.listen(4) # makes a socket ready for accepting connections with que size of 5
        while True:
            global conn
            (conn, (ip,port))= tcp_server.accept()
            t1 = ClientThread(ip,port,window) # a new thread
            t1.start()
            threads.append(t1)
            
        for t in threads:
            t.join()
            
class ClientThread(Thread):
    def __init__(self, ip,port,window):
        Thread.__init__(self)
        self.window=window
        self.ip=ip
        self.port=port
        
    def run(self):
        """each client waits for data received from the server and displays that data in the Text Edit widget"""
        while True:
            global conn
            data = conn.recv(1024)
            window.textEditMessages.append("Client> "+data.decode("utf-8"))#The received data is decoded because the data received is in the form of bytes, which haveto be converted into strings using UTF-8 encoding
        
if __name__=="__main__":    
    app = QApplication(sys.argv)
    window = Window()
    serverthread=serverthread(window)
    serverthread.start()    
    window.exec()
    sys.exit(app.exec_())