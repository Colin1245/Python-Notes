# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tumja.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 0, 771, 471))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("imgs/tum.png"))
        self.label.setScaledContents(False)
        self.label.setObjectName("label")

        self.TUM = QtWidgets.QPushButton(self.centralwidget)
        self.TUM.setGeometry(QtCore.QRect(0, 500, 381, 31))
        self.TUM.setObjectName("TUM")
    
        self.JA = QtWidgets.QPushButton(self.centralwidget)
        self.JA.setGeometry(QtCore.QRect(380, 500, 421, 31))
        self.JA.setObjectName("JA")

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

        self.TUM.clicked.connect(self.show_tum)
        self.JA.clicked.connect(self.show_ja)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.TUM.setText(_translate("MainWindow", "Technical University of Munich"))
        self.JA.setText(_translate("MainWindow", "Junge Akademie"))

    def show_tum(self):
        self.label.setPixmap(QtGui.QPixmap("imgs/tum.png"))

    def show_ja(self):
        self.label.setPixmap(QtGui.QPixmap("imgs/ja.jpeg"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

