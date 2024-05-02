from data_featcher import get_users_data
from PyQt5 import QtCore, QtGui, QtWidgets
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
from PyQt5.QtWidgets import QVBoxLayout
import matplotlib.pyplot as plt
from matplotlib.figure import Figure


class Ui_MainWindow(object):
    def setupUi(self, MainWindow, path):
        self.path = path
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(900, 540)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 60, 171, 31))
        self.label.setObjectName("label")
        
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(190, 70, 47, 13))
        self.label_2.setObjectName("label_2")
        
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(20, 90, 121, 16))
        self.label_3.setObjectName("label_3")
        
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(150, 90, 51, 16))
        self.label_4.setObjectName("label_4")
        
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(20, 30, 141, 16))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")



        self.layout = QVBoxLayout(self.centralwidget)
        self.layout.setGeometry(QtCore.QRect(400, 400, 100, 100))
        self.figure, self.axes = plt.subplots()
        self.canvas = FigureCanvas(self.figure)  
        self.layout.addWidget(self.canvas)
        

        

	

        
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 890, 21))
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
        self.label.setText(_translate("MainWindow", "Number of student in given sheet:"))
        self.label_2.setText(_translate("MainWindow", "None"))
        self.label_3.setText(_translate("MainWindow", "Successful data retrieval:"))
        self.label_4.setText(_translate("MainWindow", "None"))
        self.label_5.setText(_translate("MainWindow", "DASHBOARD"))
        
    def featch_data(self):
        get_user_data(path)
        

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow,"nishant")
    MainWindow.show()
    sys.exit(app.exec_())
