import Crypto
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import sys
import PyQt5
from Crypto.Protocol.KDF import scrypt
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import * 
from PyQt5.QtGui import * 
from PyQt5.QtCore import *
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QPushButton, QAction, QLineEdit, QMessageBox, QRadioButton
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import (QLabel, QRadioButton, QPushButton, QVBoxLayout, QApplication, QWidget)
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QVBoxLayout, QWidget
import os 
from os import path

password = "password"

class loginWindow(QMainWindow):     
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("Login Page")
       
        self.label = QLabel("Enter username and password")
        self.textbox1 = QLineEdit(self)
        self.textbox2 = QLineEdit(self)

        self.textbox1.move(10,10)
        self.textbox1.resize(100,50)

        self.textbox2.move(10,80)
        self.textbox2.resize(100,50)

        self.label.move(500,200)
        self.label.resize(100,100)

        self.program = None  # No external window yet.
        self.button = QPushButton("Submit", self)
        self.button.move(100,200)
        self.button.clicked.connect(self.show_new_window)
        self.show()
    

        

        
    
    def show_new_window(self, checked):
        if self.textbox2.text() == password:
            self.program = Window()
            self.program.show()
        else:
            print("Password incorrect")   

class generateKey():
    salt = get_random_bytes(16)
    key = scrypt(password, salt, 16, N=2**14, r=8, p=1) 
    print(key)
       

class Window(QWidget): 
    def __init__(self): 
        super().__init__() 
        
       
        self.init_ui()
        
    def init_ui(self):
        # setting title 
        self.setWindowTitle("Encryption/Password Manager ") 
        # creating radio buttons 
        self.label = QLabel('What would you like to do?')
        self.rbtn1 = QRadioButton('Create File?')
        self.rbtn2 = QRadioButton('Delete File?')
        self.label2 = QLabel("")

        self.label2.move(100,100)
        #Creating textbox for filename 
        self.textbox = QLineEdit(self)
        self.textbox.move(200,200)
        self.textbox.resize(80,50)
        self.textbox.hide()

        #Toggling radiobuttons
        self.rbtn1.toggled.connect(self.rbtn1toggle)
        self.rbtn2.toggled.connect(self.rbtn2toggle)

        #Creating submit button
        button = QPushButton('Submit', self)
        button.clicked.connect(self.buttonclicked)
        ##button.resize(100,100)
       ## button.move(400,400)

        #Layout for appereance
        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.rbtn1)
        layout.addWidget(self.rbtn2)
        layout.addWidget(self.label2) 

        self.setGeometry(500, 500, 500, 500)
        
        self.setLayout(layout)
        self.show()
       
    


  
    # action method 
    def rbtn1toggle(self): 
        radioBtn = self.sender()
        if radioBtn.isChecked():
            self.label2.setText("Enter file to create")            
            self.textbox.show()
            

    def rbtn2toggle(self):
        radioBtn = self.sender()
        if radioBtn.isChecked():
            self.label2.setText("Enter file to delete")
            self.textbox.show()
            
            

    def buttonclicked(self):
            if(self.rbtn1.isChecked()):
                fileCreate = open(self.textbox.text(), "wb")
                print("File created successfully")
            else:
                if((self.rbtn2.isChecked()) and os.path.exists(self.textbox.text())):
                    os.remove(self.textbox.text())
                    print("File deleted")
                else:
                    print("The file does not exist")

    




if __name__ == '__main__':
    app = QApplication(sys.argv)
    program = loginWindow()
    program.show()
    app.exec_()








