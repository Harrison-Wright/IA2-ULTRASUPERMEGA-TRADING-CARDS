# Form implementation generated from reading ui file 'IA2_create_account.ui'
#
# Created by: PyQt6 UI code generator 6.3.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.

import email
import sqlite3
import sys
from PyQt6 import QtCore, QtGui, QtWidgets
from User import UserDB


class Ui_create_userWindow(object):
    def __init__(self):
        self.file = "Users.db"
        self.connection = sqlite3.connect(self.file)
        self.cursor = self.connection.cursor()
        self.login = False
        self.username = ""
        self.uc = UserDB()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(282, 257)
        MainWindow.setStyleSheet("color: rgb(0, 0, 0);\n"
"")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.formLayout = QtWidgets.QFormLayout(self.centralwidget)
        self.formLayout.setObjectName("formLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.create_user_title = QtWidgets.QLabel(self.centralwidget)
        self.create_user_title.setStyleSheet("font: 18pt \"MS Shell Dlg 2\";")
        self.create_user_title.setObjectName("create_user_title")
        self.verticalLayout.addWidget(self.create_user_title)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.username_lb = QtWidgets.QLabel(self.centralwidget)
        self.username_lb.setMinimumSize(QtCore.QSize(71, 0))
        self.username_lb.setStyleSheet("")
        self.username_lb.setObjectName("username_lb")
        self.horizontalLayout.addWidget(self.username_lb)
        self.username_entry_le = QtWidgets.QLineEdit(self.centralwidget)
        self.username_entry_le.setObjectName("username_entry_le")
        self.horizontalLayout.addWidget(self.username_entry_le)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.email_lb = QtWidgets.QLabel(self.centralwidget)
        self.email_lb.setMinimumSize(QtCore.QSize(71, 0))
        self.email_lb.setStyleSheet("")
        self.email_lb.setObjectName("email_lb")
        self.horizontalLayout_2.addWidget(self.email_lb)
        self.email_entry_le = QtWidgets.QLineEdit(self.centralwidget)
        self.email_entry_le.setObjectName("email_entry_le")
        self.horizontalLayout_2.addWidget(self.email_entry_le)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.password_lb = QtWidgets.QLabel(self.centralwidget)
        self.password_lb.setMinimumSize(QtCore.QSize(71, 0))
        self.password_lb.setStyleSheet("")
        self.password_lb.setObjectName("password_lb")
        self.horizontalLayout_3.addWidget(self.password_lb)
        self.password_entry_le = QtWidgets.QLineEdit(self.centralwidget)
        self.password_entry_le.setObjectName("password_entry_le")
        self.horizontalLayout_3.addWidget(self.password_entry_le)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.return_lb = QtWidgets.QLabel(self.centralwidget)
        self.return_lb.setText("")
        self.return_lb.setObjectName("return_lb")
        self.verticalLayout.addWidget(self.return_lb)
        self.enter_btn = QtWidgets.QPushButton(self.centralwidget)
        self.enter_btn.setObjectName("enter_btn")
        self.verticalLayout.addWidget(self.enter_btn)
        self.formLayout.setLayout(0, QtWidgets.QFormLayout.ItemRole.LabelRole, self.verticalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.enter_btn.clicked.connect(lambda: self.create_user())
        

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.create_user_title.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">Create Account</p></body></html>"))
        self.username_lb.setText(_translate("MainWindow", "Username:"))
        self.email_lb.setText(_translate("MainWindow", "Email:"))
        self.password_lb.setText(_translate("MainWindow", "Password:"))
        self.enter_btn.setText(_translate("MainWindow", "enter"))

    uc = UserDB()
    
    def create_user(self):
        recentUsername = self.username_entry_le.text()
        recent_email = self.email_entry_le.text()
        recentPassword = self.password_entry_le.text()
        self.return_lb.setText(UserDB.create_user(self, username = recentUsername, email = recent_email, password = recentPassword))

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_create_userWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())