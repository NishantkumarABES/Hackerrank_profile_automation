from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtGui import QMovie 
from format_gui import Ui_Form
import pandas as pd
from dashboard import dashboard_MainWindow

import time

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        self.filename = None
        
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(380, 460)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 40, 381, 261))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("image/bot_image.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(0, 0, 381, 41))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("image/header.JPG"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(20, 380, 75, 23))
        self.pushButton.setDefault(False)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.browseFile)
        
        
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(20, 350, 141, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(150, 350, 221, 21))
        self.label_4.setObjectName("label_4")
        
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(100, 380, 91, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.setEnabled(0)
        self.pushButton_2.clicked.connect(self.open_dashboard)
        
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(20, 310, 101, 21))
        self.label_5.setObjectName("label_5")
        
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(120, 310, 75, 23))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.clicked.connect(self.openFormat)

        
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 380, 21))
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
        self.pushButton.setText(_translate("MainWindow", "Browse"))
        self.label_3.setText(_translate("MainWindow", "Upload Excel File:"))
        self.label_4.setText(_translate("MainWindow", "No file is selected"))
        self.pushButton_2.setText(_translate("MainWindow", "Open Dashboard"))
        self.label_5.setText(_translate("MainWindow", "Format of excel file:"))
        self.pushButton_3.setText(_translate("MainWindow", "Check"))
        

    def browseFile(self):
        self.filename = QFileDialog.getOpenFileName()
        self.label_4.setText(self.filename[0][-self.filename[0][::-1].find("/")::])
        self.pushButton_2.setEnabled(1)


    def openFormat(self):
        self.window = QtWidgets.QWidget()
        self.format_window = Ui_Form()
        self.format_window.setupUi(self.window)
        self.window.show()
        
    def formatChecker(self,path):
        excel_file = pd.read_csv(path)
        if len(excel_file.columns)!=4: return False
        if 


        return True
        
        
    def open_dashboard(self):
        path = self.filename[0]
        self.window_1 = QtWidgets.QMainWindow()
        self.dashboard = dashboard_MainWindow()
        self.dashboard.setupUi(self.window_1)
        self.window_1.show()
        
    
        
        

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
