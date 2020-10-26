import passwordManager
import utilities
from PyQt5 import QtCore, QtGui, QtWidgets

class Controller():
    def __init__(self):
        pass

    def ShowLogin(self):
        self.login = Login()
        self.login.switchWindow.connect(self.ShowMain)
        self.login.failure.connect(self.ShowFailure)
        self.login.show()

    def ShowMain(self):
        self.mainWindow = MainWindow(self.login.key)
        self.login.close()
        self.mainWindow.show()

    def ShowFailure(self):
        self.error = Error()
        self.login.close()
        self.error.show()

class Login(QtWidgets.QWidget):
    switchWindow = QtCore.pyqtSignal()
    failure = QtCore.pyqtSignal()

    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        
        self.setWindowTitle("Datalocker Login")
        self.setFixedSize(300, 100)

        fullLayout = QtWidgets.QVBoxLayout()
        firstRowLayout = QtWidgets.QHBoxLayout()
        secondRowLayout = QtWidgets.QHBoxLayout()
        
        self.lblPassword = QtWidgets.QLabel("Master Password")
        self.lblPassword.setGeometry(QtCore.QRect(40, 70, 47, 13))
        self.lblPassword.setObjectName("lblPassword")
        secondRowLayout.addWidget(self.lblPassword)

        self.txtPassword = QtWidgets.QLineEdit()
        self.txtPassword.setGeometry(QtCore.QRect(130, 30, 113, 20))
        self.txtPassword.setEchoMode(QtWidgets.QLineEdit.Password)
        self.txtPassword.setObjectName("txtPassword")
        secondRowLayout.addWidget(self.txtPassword)

        fullLayout.addLayout(firstRowLayout)
        fullLayout.addLayout(secondRowLayout)

        self.pushButton = QtWidgets.QPushButton("Login")
        self.pushButton.setGeometry(QtCore.QRect(140, 100, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.login)
        
        fullLayout.addWidget(self.pushButton)
        
        self.setLayout(fullLayout)

    def login(self):
        plainPass = self.txtPassword.text()

        if(utilities.AuthenticatePassword(plainPass)):
            self.key = utilities.GenerateKey(plainPass)
            self.switchWindow.emit()   

        else:
            self.failure.emit()


class Error(QtWidgets.QWidget):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        
        self.setWindowTitle("Datalocker Login Error")
        self.setFixedSize(300, 100)

        self.layout = QtWidgets.QVBoxLayout()

        self.lblPassword = QtWidgets.QLabel("Authenticaion Failed - Invalid Password.")
        self.lblPassword.setObjectName("lblPassword")
        self.lblPassword.setAlignment(QtCore.Qt.AlignCenter)
        self.layout.addWidget(self.lblPassword)

        self.btnClose = QtWidgets.QPushButton("Close")
        self.btnClose.setObjectName("btnClose")
        self.btnClose.clicked.connect(self.Close)

        self.layout.addWidget(self.btnClose)

        self.setLayout(self.layout)

    def Close(self):
        QtCore.QCoreApplication.instance().quit()


class MainWindow(QtWidgets.QWidget):
    switchWindow = QtCore.pyqtSignal()

    def __init__(self, key):
        QtWidgets.QWidget.__init__(self)
        
        self.setWindowTitle("Datalocker - Home")
        self.setFixedSize(800, 360)

        self.key = key

        self.tabs = QtWidgets.QTabWidget(self)
        self.tabs.setGeometry(QtCore.QRect(10, 10, 790, 340))
        self.tabs.setObjectName("tabs")

        self.tabFile = QtWidgets.QWidget()
        self.tabFile.setObjectName("tabFile")

        self.tabs.addTab(self.tabFile, "File Manager")

        self.tabPword = QtWidgets.QWidget()
        self.tabPword.setObjectName("tabPword")

        self.verticalLayoutWidget = QtWidgets.QWidget(self.tabPword)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(30, 30, 200, 100))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")

        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")

        self.btnNewEntry = QtWidgets.QPushButton("New Entry", self.verticalLayoutWidget)
        self.btnNewEntry.setObjectName("btnNewEntry")
        self.btnNewEntry.clicked.connect(self.AddNewEntry)
        self.verticalLayout.addWidget(self.btnNewEntry)

        self.btnUpdateEntry = QtWidgets.QPushButton("Update Entry", self.verticalLayoutWidget)
        self.btnUpdateEntry.setObjectName("btnUpdateEntry")
        self.btnUpdateEntry.clicked.connect(self.UpdateEntries)
        self.verticalLayout.addWidget(self.btnUpdateEntry)

        self.btnGenerate = QtWidgets.QPushButton("Generate Entry", self.verticalLayoutWidget)
        self.btnGenerate.setObjectName("btnGenerate")
        self.btnGenerate.clicked.connect(self.GeneratePassword)
        self.verticalLayout.addWidget(self.btnGenerate)

        self.gridLayoutWidget = QtWidgets.QWidget(self.tabPword)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(30, 130, 200, 150))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")

        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")

        self.lblSevice = QtWidgets.QLabel("Service", self.gridLayoutWidget)
        self.lblSevice.setAlignment(QtCore.Qt.AlignLeft)
        self.lblSevice.setObjectName("lblSevice")
        self.gridLayout.addWidget(self.lblSevice, 0, 0, 1, 1)

        self.lblUsername = QtWidgets.QLabel("Username", self.gridLayoutWidget)
        self.lblUsername.setAlignment(QtCore.Qt.AlignLeft)
        self.lblUsername.setObjectName("lblUsername")
        self.gridLayout.addWidget(self.lblUsername, 1, 0, 1, 1)

        self.lblPassword = QtWidgets.QLabel("Password", self.gridLayoutWidget)
        self.lblPassword.setAlignment(QtCore.Qt.AlignLeft)
        self.lblPassword.setObjectName("lblPassword")
        self.gridLayout.addWidget(self.lblPassword, 2, 0, 1, 1)

        self.txtService = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.txtService.setObjectName("txtService")
        self.gridLayout.addWidget(self.txtService, 0, 1, 1, 1)

        self.txtUsername = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.txtUsername.setObjectName("txtUsername")
        self.gridLayout.addWidget(self.txtUsername, 1, 1, 1, 1)

        self.txtPassword = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.txtPassword.setObjectName("txtPassword")
        self.txtPassword.setEchoMode(QtWidgets.QLineEdit.Password)
        self.gridLayout.addWidget(self.txtPassword, 2, 1, 1, 1)

        self.btnVisible = QtWidgets.QPushButton("Toggle Visibility", self.gridLayoutWidget)
        self.btnVisible.setObjectName("btnVisible")
        self.btnVisible.clicked.connect(self.ToggleVisibility)
        self.gridLayout.addWidget(self.btnVisible, 3, 1, 1, 1)
        
        self.tableWidget = QtWidgets.QTableWidget(self.tabPword)
        self.tableWidget.setGeometry(QtCore.QRect(290, 30, 452, 250))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setRowCount(0)

        item = QtWidgets.QTableWidgetItem("Service")
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem("Username")
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem("Password")

        self.tableWidget.setHorizontalHeaderItem(2, item)
        self.tableWidget.horizontalHeader().setVisible(True)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(150)
        self.tableWidget.horizontalHeader().setMaximumSectionSize(150)
        self.tableWidget.horizontalHeader().setMinimumSectionSize(150)

        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.verticalHeader().setDefaultSectionSize(25)
        self.tableWidget.verticalHeader().setMinimumSectionSize(25)
        
        self.tabs.addTab(self.tabPword, "Password Manager")
        self.tabs.setCurrentIndex(0)

        self.FillPasswordTable()

    def GeneratePassword(self):
        self.txtPassword.setText(passwordManager.GeneratePassword())

    def AddNewEntry(self):
        if(len(self.txtService.text()) > 0 and (len(self.txtUsername.text()) > 0) and (len(self.txtPassword.text()) > 0)):
            service = self.txtService.text()
            username = self.txtUsername.text()
            password = self.txtPassword.text()

            newEntry = {
                "service" : service,
                "username" : username,
                "password" : password
            }

            passwordManager.CreateNewPasswordEntry(self.key, newEntry)
            self.FillPasswordTable()
            self.ClearInput()

    def FillPasswordTable(self):
        data, exists = passwordManager.GetFileData(self.key)

        if(exists):
            self.tableWidget.setRowCount(0)
            for i in range(len(data["entries"])):
                rowPosition = self.tableWidget.rowCount()
                self.tableWidget.insertRow(rowPosition)    

                self.tableWidget.setItem(rowPosition, 0, QtWidgets.QTableWidgetItem(data["entries"][i]["service"]))
                self.tableWidget.setItem(rowPosition, 1, QtWidgets.QTableWidgetItem(data["entries"][i]["username"]))
                self.tableWidget.setItem(rowPosition, 2, QtWidgets.QTableWidgetItem(data["entries"][i]["password"]))

    def UpdateEntries(self):
        found = False

        data, exists = passwordManager.GetFileData(self.key)

        if(exists):
            for i in range(self.tableWidget.rowCount()):
                data["entries"][i]["service"] = self.tableWidget.item(i, 0).text()
                data["entries"][i]["username"] = self.tableWidget.item(i, 1).text()
                data["entries"][i]["password"] = self.tableWidget.item(i, 2).text()

        passwordManager.StoreFileData(self.key, data)
        self.FillPasswordTable()
        self.ClearInput()
    
    def ToggleVisibility(self):
        if(self.txtPassword.echoMode() == QtWidgets.QLineEdit.Password):
            self.txtPassword.setEchoMode(QtWidgets.QLineEdit.Normal)

        else:
            self.txtPassword.setEchoMode(QtWidgets.QLineEdit.Password)

    def ClearInput(self):
        self.txtService.setText("")
        self.txtUsername.setText("")
        self.txtPassword.setText("")