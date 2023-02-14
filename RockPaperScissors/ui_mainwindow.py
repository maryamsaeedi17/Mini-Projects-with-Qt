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
from PySide6.QtWidgets import (QApplication, QLabel, QMainWindow, QMenuBar,
    QPushButton, QSizePolicy, QStatusBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(422, 472)
        MainWindow.setStyleSheet(u"background-color: rgb(85, 255, 0);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.btn_paper = QPushButton(self.centralwidget)
        self.btn_paper.setObjectName(u"btn_paper")
        self.btn_paper.setGeometry(QRect(20, 340, 101, 91))
        font = QFont()
        font.setPointSize(20)
        self.btn_paper.setFont(font)
        self.btn_paper.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius: 5px;\n"
"border-image:url(C:/Users/ara/Desktop/MyProjects1/PyLearningWorks1/Mini-Project2/Mini-Projects-with-Qt/RockPaperScissors/paper.png);\n"
"")
        self.btn_rock = QPushButton(self.centralwidget)
        self.btn_rock.setObjectName(u"btn_rock")
        self.btn_rock.setGeometry(QRect(160, 340, 101, 91))
        self.btn_rock.setFont(font)
        self.btn_rock.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius: 5px;\n"
"border-image:url(C:/Users/ara/Desktop/MyProjects1/PyLearningWorks1/Mini-Project2/Mini-Projects-with-Qt/RockPaperScissors/rock.png);\n"
"\n"
"")
        self.btn_scissors = QPushButton(self.centralwidget)
        self.btn_scissors.setObjectName(u"btn_scissors")
        self.btn_scissors.setGeometry(QRect(300, 340, 101, 91))
        self.btn_scissors.setFont(font)
        self.btn_scissors.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius: 5px;\n"
"border-image:url(C:/Users/ara/Desktop/MyProjects1/PyLearningWorks1/Mini-Project2/Mini-Projects-with-Qt/RockPaperScissors/scissors.png);\n"
"")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(170, 0, 71, 31))
        font1 = QFont()
        font1.setPointSize(12)
        self.label.setFont(font1)
        self.label.setAlignment(Qt.AlignCenter)
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(150, 310, 101, 31))
        font2 = QFont()
        font2.setPointSize(12)
        font2.setBold(True)
        self.label_2.setFont(font2)
        self.label_2.setStyleSheet(u"color: rgb(85, 85, 0);")
        self.label_2.setAlignment(Qt.AlignCenter)
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(170, 170, 71, 31))
        self.label_3.setFont(font1)
        self.label_3.setAlignment(Qt.AlignCenter)
        self.result = QLabel(self.centralwidget)
        self.result.setObjectName(u"result")
        self.result.setGeometry(QRect(20, 140, 381, 31))
        font3 = QFont()
        font3.setPointSize(11)
        self.result.setFont(font3)
        self.result.setStyleSheet(u"background-color: rgb(255, 255, 0);\n"
"border-radius: 5px;")
        self.result.setAlignment(Qt.AlignCenter)
        self.player_score = QLabel(self.centralwidget)
        self.player_score.setObjectName(u"player_score")
        self.player_score.setGeometry(QRect(250, 310, 49, 31))
        font4 = QFont()
        font4.setPointSize(13)
        font4.setBold(True)
        self.player_score.setFont(font4)
        self.player_score.setStyleSheet(u"color: rgb(85, 85, 0);")
        self.player_choice = QPushButton(self.centralwidget)
        self.player_choice.setObjectName(u"player_choice")
        self.player_choice.setGeometry(QRect(160, 200, 101, 101))
        self.player_choice.setStyleSheet(u"border-color: rgb(0, 85, 0);\n"
"border-width: 2px;\n"
"border-style : dashed")
        self.computer_choice = QPushButton(self.centralwidget)
        self.computer_choice.setObjectName(u"computer_choice")
        self.computer_choice.setGeometry(QRect(160, 30, 101, 101))
        self.computer_choice.setStyleSheet(u"border-color: rgb(0, 85, 0);\n"
"border-width: 2px;\n"
"border-style : dashed")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 422, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"RockPaperScissors-Game", None))
        self.btn_paper.setText("")
        self.btn_rock.setText("")
        self.btn_scissors.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"Computer", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Your Score:", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Player", None))
        self.result.setText(QCoreApplication.translate("MainWindow", u"Result", None))
        self.player_score.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.player_choice.setText("")
        self.computer_choice.setText("")
    # retranslateUi

