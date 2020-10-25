import passwordManager
from PyQt5 import QtCore, QtGui, QtWidgets

class PasswordManager(object):
    def setupUi(self, MainWindow, key):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(800, 378)

        self.key = key

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabs = QtWidgets.QTabWidget(self.centralwidget)
        self.tabs.setGeometry(QtCore.QRect(10, 10, 771, 351))
        self.tabs.setObjectName("tabs")
        self.tabFile = QtWidgets.QWidget()
        self.tabFile.setObjectName("tabFile")
        self.tabs.addTab(self.tabFile, "")
        self.tabPword = QtWidgets.QWidget()
        self.tabPword.setObjectName("tabPword")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.tabPword)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(30, 200, 231, 111))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")

        self.btnNewEntry = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.btnNewEntry.setObjectName("btnNewEntry")
        self.btnNewEntry.clicked.connect(self.AddNewEntry)
        self.verticalLayout.addWidget(self.btnNewEntry)

        self.btnUpdateEntry = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.btnUpdateEntry.setObjectName("btnUpdateEntry")
        self.btnUpdateEntry.clicked.connect(self.UpdateEntries)
        self.verticalLayout.addWidget(self.btnUpdateEntry)

        self.btnGenerate = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.btnGenerate.setObjectName("btnGenerate")
        self.btnGenerate.clicked.connect(self.GeneratePassword)
        self.verticalLayout.addWidget(self.btnGenerate)

        self.gridLayoutWidget = QtWidgets.QWidget(self.tabPword)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(30, 31, 229, 161))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")

        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")

        self.lblSevice = QtWidgets.QLabel(self.gridLayoutWidget)
        self.lblSevice.setAlignment(QtCore.Qt.AlignLeft)
        self.lblSevice.setObjectName("lblSevice")
        self.gridLayout.addWidget(self.lblSevice, 0, 0, 1, 1)

        self.lblUsername = QtWidgets.QLabel(self.gridLayoutWidget)
        self.lblUsername.setAlignment(QtCore.Qt.AlignLeft)
        self.lblUsername.setObjectName("lblUsername")
        self.gridLayout.addWidget(self.lblUsername, 1, 0, 1, 1)

        self.lblPassword = QtWidgets.QLabel(self.gridLayoutWidget)
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

        self.btnVisible = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.btnVisible.setObjectName("btnVisible")
        self.btnVisible.clicked.connect(self.ToggleVisibility)
        self.gridLayout.addWidget(self.btnVisible, 3, 1, 1, 1)

        self.tableWidget = QtWidgets.QTableWidget(self.tabPword)
        self.tableWidget.setGeometry(QtCore.QRect(290, 30, 452, 280))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        self.tableWidget.horizontalHeader().setVisible(True)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(150)
        self.tableWidget.horizontalHeader().setMaximumSectionSize(150)
        self.tableWidget.horizontalHeader().setMinimumSectionSize(150)
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.verticalHeader().setDefaultSectionSize(25)
        self.tableWidget.verticalHeader().setMinimumSectionSize(25)
        #self.tableWidget.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)
        self.tabs.addTab(self.tabPword, "")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.tabs.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.FillPasswordTable()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Data Locker"))
        self.tabs.setTabText(self.tabs.indexOf(self.tabFile), _translate("MainWindow", "File Manager"))

        self.btnNewEntry.setText(_translate("MainWindow", "New Entry"))
        self.btnUpdateEntry.setText(_translate("MainWindow", "Update Entry"))
        self.btnGenerate.setText(_translate("MainWindow", "Generate Password"))

        self.lblUsername.setText(_translate("MainWindow", "Username"))
        self.lblSevice.setText(_translate("MainWindow", "Service"))
        self.lblPassword.setText(_translate("MainWindow", "Password"))

        self.btnVisible.setText(_translate("MainWindow", "Toggle Password"))

        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Service"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Username"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Password"))

        self.tabs.setTabText(self.tabs.indexOf(self.tabPword), _translate("MainWindow", "Password Manager"))

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