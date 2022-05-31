# Form implementation generated from reading ui file 'IA2_help_window.ui'
#
# Created by: PyQt6 UI code generator 6.3.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.

import sys
from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_HelpWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.formLayout = QtWidgets.QFormLayout(self.centralwidget)
        self.formLayout.setObjectName("formLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.title_lb = QtWidgets.QLabel(self.centralwidget)
        self.title_lb.setObjectName("title_lb")
        self.verticalLayout.addWidget(self.title_lb)
        self.help_text = QtWidgets.QLabel(self.centralwidget)
        self.help_text.setWordWrap(True)
        self.help_text.setObjectName("help_text")
        self.verticalLayout.addWidget(self.help_text)
        self.return_menu = QtWidgets.QPushButton(self.centralwidget)
        self.return_menu.setObjectName("return_menu")
        self.verticalLayout.addWidget(self.return_menu)
        self.formLayout.setLayout(0, QtWidgets.QFormLayout.ItemRole.LabelRole, self.verticalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.title_lb.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:36pt;\">Game Guide</span></p></body></html>"))
        self.help_text.setText(_translate("MainWindow", "<html><head/><body><p>Ultra Super Mega Cards: Top Trumps is a single player, card based strategy game against AI. In order to use the game you must create an account with a username, email and password. To login you must enter your username and password. To play you must first select a deck size to be evenly split in a random order of cards between you and the AI. You must then select the difficulty of the AI you are playing against to suite your level of playing. Now you are ready to play, by pressing play you start the game, where you get to view the card on the op of your deck and select one of its (highest) stats to try and beat the AI in the given stat field for its card. If you win then you get your card and their card added to your deck, but if you lose the AI gets both cards added to its deck. The Aim of the game is to collect all the cards in play. If you do this the win is recorded to your statistics, but if the AI gets all the cards a loss is recorded. These player statistics can be viewed from menu to see all the matches you have played, the AI difficulty of the match and whether you won or lost the match. Goodluck and enjoy the game!</p></body></html>"))
        self.return_menu.setText(_translate("MainWindow", "return to menu"))



if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_HelpWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())