# Form implementation generated from reading ui file 'IA2_game_window.ui'
#
# Created by: PyQt6 UI code generator 6.3.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1254, 753)
        palette = QtGui.QPalette()
        gradient = QtGui.QLinearGradient(0.0, 0.0, 1.0, 1.0)
        gradient.setSpread(QtGui.QGradient.Spread.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.CoordinateMode.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(52, 110, 255))
        gradient.setColorAt(1.0, QtGui.QColor(255, 255, 255))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.Button, brush)
        gradient = QtGui.QLinearGradient(0.0, 0.0, 1.0, 1.0)
        gradient.setSpread(QtGui.QGradient.Spread.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.CoordinateMode.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(52, 110, 255))
        gradient.setColorAt(1.0, QtGui.QColor(255, 255, 255))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.Base, brush)
        gradient = QtGui.QLinearGradient(0.0, 0.0, 1.0, 1.0)
        gradient.setSpread(QtGui.QGradient.Spread.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.CoordinateMode.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(52, 110, 255))
        gradient.setColorAt(1.0, QtGui.QColor(255, 255, 255))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.Window, brush)
        gradient = QtGui.QLinearGradient(0.0, 0.0, 1.0, 1.0)
        gradient.setSpread(QtGui.QGradient.Spread.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.CoordinateMode.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(52, 110, 255))
        gradient.setColorAt(1.0, QtGui.QColor(255, 255, 255))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.Button, brush)
        gradient = QtGui.QLinearGradient(0.0, 0.0, 1.0, 1.0)
        gradient.setSpread(QtGui.QGradient.Spread.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.CoordinateMode.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(52, 110, 255))
        gradient.setColorAt(1.0, QtGui.QColor(255, 255, 255))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.Base, brush)
        gradient = QtGui.QLinearGradient(0.0, 0.0, 1.0, 1.0)
        gradient.setSpread(QtGui.QGradient.Spread.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.CoordinateMode.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(52, 110, 255))
        gradient.setColorAt(1.0, QtGui.QColor(255, 255, 255))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.Window, brush)
        gradient = QtGui.QLinearGradient(0.0, 0.0, 1.0, 1.0)
        gradient.setSpread(QtGui.QGradient.Spread.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.CoordinateMode.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(52, 110, 255))
        gradient.setColorAt(1.0, QtGui.QColor(255, 255, 255))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.Button, brush)
        gradient = QtGui.QLinearGradient(0.0, 0.0, 1.0, 1.0)
        gradient.setSpread(QtGui.QGradient.Spread.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.CoordinateMode.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(52, 110, 255))
        gradient.setColorAt(1.0, QtGui.QColor(255, 255, 255))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.Base, brush)
        gradient = QtGui.QLinearGradient(0.0, 0.0, 1.0, 1.0)
        gradient.setSpread(QtGui.QGradient.Spread.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.CoordinateMode.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(52, 110, 255))
        gradient.setColorAt(1.0, QtGui.QColor(255, 255, 255))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.Window, brush)
        MainWindow.setPalette(palette)
        MainWindow.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(52, 110, 255, 255), stop:1 rgba(255, 255, 255, 255));")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.player_img_lb = QtWidgets.QLabel(self.centralwidget)
        self.player_img_lb.setGeometry(QtCore.QRect(240, 180, 220, 320))
        self.player_img_lb.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.player_img_lb.setText("")
        self.player_img_lb.setObjectName("player_img_lb")
        self.ai_img_lb = QtWidgets.QLabel(self.centralwidget)
        self.ai_img_lb.setGeometry(QtCore.QRect(770, 180, 220, 320))
        self.ai_img_lb.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.ai_img_lb.setText("")
        self.ai_img_lb.setObjectName("ai_img_lb")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(160, 20, 191, 51))
        font = QtGui.QFont()
        font.setFamily("Futura")
        font.setPointSize(30)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(910, 20, 221, 51))
        font = QtGui.QFont()
        font.setFamily("Futura")
        font.setPointSize(30)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.player_name_lb = QtWidgets.QLabel(self.centralwidget)
        self.player_name_lb.setGeometry(QtCore.QRect(50, 120, 391, 40))
        font = QtGui.QFont()
        font.setFamily("Futura")
        font.setPointSize(13)
        self.player_name_lb.setFont(font)
        self.player_name_lb.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignTop)
        self.player_name_lb.setObjectName("player_name_lb")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(510, 100, 206, 321))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label = QtWidgets.QLabel(self.layoutWidget)
        self.label.setObjectName("label")
        self.verticalLayout_5.addWidget(self.label)
        self.stat_lb = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Futura")
        font.setPointSize(22)
        self.stat_lb.setFont(font)
        self.stat_lb.setText("")
        self.stat_lb.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.stat_lb.setObjectName("stat_lb")
        self.verticalLayout_5.addWidget(self.stat_lb)
        self.label_9 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Futura")
        font.setPointSize(30)
        self.label_9.setFont(font)
        self.label_9.setAlignment(QtCore.Qt.AlignmentFlag.AlignHCenter|QtCore.Qt.AlignmentFlag.AlignTop)
        self.label_9.setObjectName("label_9")
        self.verticalLayout_5.addWidget(self.label_9)
        self.win_lb = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Futura")
        font.setPointSize(24)
        self.win_lb.setFont(font)
        self.win_lb.setText("")
        self.win_lb.setAlignment(QtCore.Qt.AlignmentFlag.AlignHCenter|QtCore.Qt.AlignmentFlag.AlignTop)
        self.win_lb.setObjectName("win_lb")
        self.verticalLayout_5.addWidget(self.win_lb)
        self.label_4 = QtWidgets.QLabel(self.layoutWidget)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_5.addWidget(self.label_4)
        self.victory_lb = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Futura")
        font.setPointSize(30)
        self.victory_lb.setFont(font)
        self.victory_lb.setText("")
        self.victory_lb.setAlignment(QtCore.Qt.AlignmentFlag.AlignHCenter|QtCore.Qt.AlignmentFlag.AlignTop)
        self.victory_lb.setObjectName("victory_lb")
        self.verticalLayout_5.addWidget(self.victory_lb)
        self.ai_name_lb = QtWidgets.QLabel(self.centralwidget)
        self.ai_name_lb.setGeometry(QtCore.QRect(780, 120, 391, 40))
        font = QtGui.QFont()
        font.setFamily("Futura")
        font.setPointSize(13)
        self.ai_name_lb.setFont(font)
        self.ai_name_lb.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignTop)
        self.ai_name_lb.setObjectName("ai_name_lb")
        self.exit_btn = QtWidgets.QPushButton(self.centralwidget)
        self.exit_btn.setGeometry(QtCore.QRect(560, 540, 113, 32))
        self.exit_btn.setStyleSheet("background-color: rgb(255, 0, 0);\n"
"color: rgb(255, 255, 255);\n"
"font: 12pt \"MS Shell Dlg 2\";")
        self.exit_btn.setObjectName("exit_btn")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(30, 180, 201, 271))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.player_intel_btn = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.player_intel_btn.setStyleSheet("background-color: rgb(255, 85, 255);\n"
"font: 11pt \"MS Shell Dlg 2\";")
        self.player_intel_btn.setObjectName("player_intel_btn")
        self.verticalLayout.addWidget(self.player_intel_btn)
        self.player_str_btn = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.player_str_btn.setStyleSheet("background-color: rgb(255, 85, 0);\n"
"font: 11pt \"MS Shell Dlg 2\";\n"
"")
        self.player_str_btn.setObjectName("player_str_btn")
        self.verticalLayout.addWidget(self.player_str_btn)
        self.player_spd_btn = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.player_spd_btn.setStyleSheet("background-color: rgb(0, 255, 255);\n"
"font: 11pt \"MS Shell Dlg 2\";")
        self.player_spd_btn.setObjectName("player_spd_btn")
        self.verticalLayout.addWidget(self.player_spd_btn)
        self.player_dura_btn = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.player_dura_btn.setStyleSheet("background-color: rgb(255, 170, 127);\n"
"font: 11pt \"MS Shell Dlg 2\";")
        self.player_dura_btn.setObjectName("player_dura_btn")
        self.verticalLayout.addWidget(self.player_dura_btn)
        self.player_pwr_btn = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.player_pwr_btn.setStyleSheet("background-color: rgb(255, 255, 0);\n"
"font: 11pt \"MS Shell Dlg 2\";")
        self.player_pwr_btn.setObjectName("player_pwr_btn")
        self.verticalLayout.addWidget(self.player_pwr_btn)
        self.player_combat_btn = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.player_combat_btn.setStyleSheet("background-color: rgb(0, 255, 0);\n"
"font: 11pt \"MS Shell Dlg 2\";")
        self.player_combat_btn.setObjectName("player_combat_btn")
        self.verticalLayout.addWidget(self.player_combat_btn)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.player_intel_lb = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.player_intel_lb.setStyleSheet("font: 11pt \"MS Shell Dlg 2\";")
        self.player_intel_lb.setObjectName("player_intel_lb")
        self.verticalLayout_7.addWidget(self.player_intel_lb)
        self.player_str_lb = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.player_str_lb.setStyleSheet("font: 11pt \"MS Shell Dlg 2\";")
        self.player_str_lb.setObjectName("player_str_lb")
        self.verticalLayout_7.addWidget(self.player_str_lb)
        self.player_spd_lb = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.player_spd_lb.setStyleSheet("font: 11pt \"MS Shell Dlg 2\";")
        self.player_spd_lb.setObjectName("player_spd_lb")
        self.verticalLayout_7.addWidget(self.player_spd_lb)
        self.player_dura_lb = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.player_dura_lb.setStyleSheet("font: 11pt \"MS Shell Dlg 2\";")
        self.player_dura_lb.setObjectName("player_dura_lb")
        self.verticalLayout_7.addWidget(self.player_dura_lb)
        self.player_pwr_lb = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.player_pwr_lb.setStyleSheet("font: 11pt \"MS Shell Dlg 2\";")
        self.player_pwr_lb.setObjectName("player_pwr_lb")
        self.verticalLayout_7.addWidget(self.player_pwr_lb)
        self.player_combat_lb = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.player_combat_lb.setStyleSheet("font: 11pt \"MS Shell Dlg 2\";")
        self.player_combat_lb.setObjectName("player_combat_lb")
        self.verticalLayout_7.addWidget(self.player_combat_lb)
        self.horizontalLayout.addLayout(self.verticalLayout_7)
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(1020, 180, 201, 261))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.a = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.a.setStyleSheet("background-color: rgb(255, 85, 255);\n"
"font: 11pt \"MS Shell Dlg 2\";")
        self.a.setObjectName("a")
        self.verticalLayout_2.addWidget(self.a)
        self.b = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.b.setStyleSheet("background-color: rgb(255, 85, 0);\n"
"font: 11pt \"MS Shell Dlg 2\";\n"
"")
        self.b.setObjectName("b")
        self.verticalLayout_2.addWidget(self.b)
        self.c = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.c.setStyleSheet("background-color: rgb(0, 255, 255);\n"
"font: 11pt \"MS Shell Dlg 2\";")
        self.c.setObjectName("c")
        self.verticalLayout_2.addWidget(self.c)
        self.d = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.d.setStyleSheet("background-color: rgb(255, 170, 127);\n"
"font: 11pt \"MS Shell Dlg 2\";")
        self.d.setObjectName("d")
        self.verticalLayout_2.addWidget(self.d)
        self.e = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.e.setStyleSheet("background-color: rgb(255, 255, 0);\n"
"font: 11pt \"MS Shell Dlg 2\";")
        self.e.setObjectName("e")
        self.verticalLayout_2.addWidget(self.e)
        self.f = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.f.setStyleSheet("background-color: rgb(0, 255, 0);\n"
"font: 11pt \"MS Shell Dlg 2\";")
        self.f.setObjectName("f")
        self.verticalLayout_2.addWidget(self.f)
        self.horizontalLayout_2.addLayout(self.verticalLayout_2)
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.ai_int_lb = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.ai_int_lb.setStyleSheet("font: 11pt \"MS Shell Dlg 2\";")
        self.ai_int_lb.setObjectName("ai_int_lb")
        self.verticalLayout_8.addWidget(self.ai_int_lb)
        self.ai_str_lb = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.ai_str_lb.setStyleSheet("font: 11pt \"MS Shell Dlg 2\";")
        self.ai_str_lb.setObjectName("ai_str_lb")
        self.verticalLayout_8.addWidget(self.ai_str_lb)
        self.ai_spd_lb = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.ai_spd_lb.setStyleSheet("font: 11pt \"MS Shell Dlg 2\";")
        self.ai_spd_lb.setObjectName("ai_spd_lb")
        self.verticalLayout_8.addWidget(self.ai_spd_lb)
        self.ai_dura_lb = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.ai_dura_lb.setStyleSheet("font: 11pt \"MS Shell Dlg 2\";")
        self.ai_dura_lb.setObjectName("ai_dura_lb")
        self.verticalLayout_8.addWidget(self.ai_dura_lb)
        self.ai_pwr_lb = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.ai_pwr_lb.setStyleSheet("font: 11pt \"MS Shell Dlg 2\";")
        self.ai_pwr_lb.setObjectName("ai_pwr_lb")
        self.verticalLayout_8.addWidget(self.ai_pwr_lb)
        self.ai_cmbt_lb = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.ai_cmbt_lb.setStyleSheet("font: 11pt \"MS Shell Dlg 2\";")
        self.ai_cmbt_lb.setObjectName("ai_cmbt_lb")
        self.verticalLayout_8.addWidget(self.ai_cmbt_lb)
        self.horizontalLayout_2.addLayout(self.verticalLayout_8)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">Player</p></body></html>"))
        self.label_3.setText(_translate("MainWindow", "Computer"))
        self.player_name_lb.setText(_translate("MainWindow", "Super Hero"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt;\">STAT CHOSEN:</span></p></body></html>"))
        self.label_9.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt;\">Round Winner:</span></p></body></html>"))
        self.label_4.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt;\">Match Winner:</span></p></body></html>"))
        self.ai_name_lb.setText(_translate("MainWindow", "Super Hero"))
        self.exit_btn.setText(_translate("MainWindow", "Exit"))
        self.player_intel_btn.setText(_translate("MainWindow", "Intelligence"))
        self.player_str_btn.setText(_translate("MainWindow", "Strength"))
        self.player_spd_btn.setText(_translate("MainWindow", "Speed"))
        self.player_dura_btn.setText(_translate("MainWindow", "Durability"))
        self.player_pwr_btn.setText(_translate("MainWindow", "Power"))
        self.player_combat_btn.setText(_translate("MainWindow", "Combat"))
        self.player_intel_lb.setText(_translate("MainWindow", "###"))
        self.player_str_lb.setText(_translate("MainWindow", "###"))
        self.player_spd_lb.setText(_translate("MainWindow", "###"))
        self.player_dura_lb.setText(_translate("MainWindow", "###"))
        self.player_pwr_lb.setText(_translate("MainWindow", "###"))
        self.player_combat_lb.setText(_translate("MainWindow", "###"))
        self.a.setText(_translate("MainWindow", "Intelligence"))
        self.b.setText(_translate("MainWindow", "Strength"))
        self.c.setText(_translate("MainWindow", "Speed"))
        self.d.setText(_translate("MainWindow", "Durability"))
        self.e.setText(_translate("MainWindow", "Power"))
        self.f.setText(_translate("MainWindow", "Combat"))
        self.ai_int_lb.setText(_translate("MainWindow", "###"))
        self.ai_str_lb.setText(_translate("MainWindow", "###"))
        self.ai_spd_lb.setText(_translate("MainWindow", "###"))
        self.ai_dura_lb.setText(_translate("MainWindow", "###"))
        self.ai_pwr_lb.setText(_translate("MainWindow", "###"))
        self.ai_cmbt_lb.setText(_translate("MainWindow", "###"))
