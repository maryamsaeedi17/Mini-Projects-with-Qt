# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QMainWindow,
    QMenuBar, QPushButton, QSizePolicy, QStatusBar,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(484, 407)
        MainWindow.setStyleSheet(u"background-color: rgb(255, 253, 185);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(50, 10, 381, 61))
        font = QFont()
        font.setFamilies([u"Segoe Print"])
        font.setPointSize(20)
        font.setBold(True)
        font.setStrikeOut(False)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet(u"color: rgb(255, 85, 0);\n"
"background-color: rgb(255, 255, 0);\n"
"border-color:rgb(255, 85, 0);\n"
"border-radius: 10px;")
        self.input = QLineEdit(self.centralwidget)
        self.input.setObjectName(u"input")
        self.input.setGeometry(QRect(280, 120, 71, 51))
        font1 = QFont()
        font1.setPointSize(26)
        self.input.setFont(font1)
        self.input.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 120, 241, 61))
        font2 = QFont()
        font2.setPointSize(13)
        self.label.setFont(font2)
        self.label.setAlignment(Qt.AlignCenter)
        self.btn_sub = QPushButton(self.centralwidget)
        self.btn_sub.setObjectName(u"btn_sub")
        self.btn_sub.setGeometry(QRect(380, 130, 81, 31))
        font3 = QFont()
        font3.setPointSize(16)
        self.btn_sub.setFont(font3)
        self.btn_sub.setStyleSheet(u"background-color: rgb(85, 170, 255);")
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(30, 220, 61, 31))
        font4 = QFont()
        font4.setPointSize(15)
        self.label_2.setFont(font4)
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(20, 260, 201, 31))
        font5 = QFont()
        font5.setPointSize(12)
        self.label_3.setFont(font5)
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(20, 310, 201, 31))
        self.label_4.setFont(font5)
        self.grt = QLineEdit(self.centralwidget)
        self.grt.setObjectName(u"grt")
        self.grt.setGeometry(QRect(220, 250, 51, 41))
        font6 = QFont()
        font6.setPointSize(20)
        self.grt.setFont(font6)
        self.lss = QLineEdit(self.centralwidget)
        self.lss.setObjectName(u"lss")
        self.lss.setGeometry(QRect(200, 300, 51, 41))
        self.lss.setFont(font6)
        self.btn_str = QPushButton(self.centralwidget)
        self.btn_str.setObjectName(u"btn_str")
        self.btn_str.setGeometry(QRect(350, 230, 121, 51))
        self.btn_str.setFont(font3)
        self.btn_str.setStyleSheet(u"background-color: rgb(255, 170, 255);")
        self.btn_res = QPushButton(self.centralwidget)
        self.btn_res.setObjectName(u"btn_res")
        self.btn_res.setGeometry(QRect(350, 300, 121, 51))
        self.btn_res.setFont(font3)
        self.btn_res.setStyleSheet(u"background-color: rgb(85, 255, 0);")
        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(290, 180, 111, 31))
        font7 = QFont()
        font7.setPointSize(9)
        self.label_5.setFont(font7)
        self.ch_remain = QLineEdit(self.centralwidget)
        self.ch_remain.setObjectName(u"ch_remain")
        self.ch_remain.setGeometry(QRect(400, 180, 31, 31))
        font8 = QFont()
        font8.setPointSize(10)
        self.ch_remain.setFont(font8)
        self.ch_remain.setAlignment(Qt.AlignCenter)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 484, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Number Guessing Game", None))
        self.input.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"Enter your guess: \n"
"(a number between 1 and 100)", None))
        self.btn_sub.setText(QCoreApplication.translate("MainWindow", u"Submit", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Hints:", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"The number is greater than:", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"The number is less than:", None))
        self.grt.setText("")
        self.lss.setText("")
        self.btn_str.setText(QCoreApplication.translate("MainWindow", u"Start Game", None))
        self.btn_res.setText(QCoreApplication.translate("MainWindow", u"Reset Game", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Chance remaining:", None))
        self.ch_remain.setText("")
    # retranslateUi

