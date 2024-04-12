from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QMovie
from data_featcher import get_users_data,get_stars_data,get_certificate_data

class dashboard_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(910, 490)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 905, 21))
        self.menubar.setObjectName("menubar")

        self.label = QtWidgets.QLabel(self.centralwidget) 
        self.label.setGeometry(QtCore.QRect(360, 25, 200, 200)) 
        #self.label.setMinimumSize(QtCore.QSize(250, 250)) 
        #self.label.setMaximumSize(QtCore.QSize(250, 250)) 
        self.label.setObjectName("lb1") 
        self.movie = QMovie("media/loader.gif") 
        self.label.setMovie(self.movie) 
        self.startAnimation()        
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(413, 255, 94, 30))
        self.pushButton.setDefault(False)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.startFeatchingData)


        

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        self.pushButton.setText(_translate("MainWindow", "Start Processing"))
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))

    def startFeatchingData(self):
        get_users_data()
  
    def startAnimation(self): 
        self.movie.start() 
 
    def stopAnimation(self): 
        self.movie.stop()
        self.label.setMovie(None)



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = dashboard_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
