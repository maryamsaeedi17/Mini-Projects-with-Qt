import random
from functools import partial
import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox
from PySide6.QtCore import QFile
from PySide6.QtGui import *
from ui_mainwindow import Ui_MainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.btn_paper.clicked.connect(partial(self.play, 1))
        self.ui.btn_rock.clicked.connect(partial(self.play, 2))
        self.ui.btn_scissors.clicked.connect(partial(self.play, 3))
        self.u_score=0
        self.c_score=0
        self.ties=0
    



    def play(self, x):
        if x==1:
            self.ui.player_choice.setIcon(QIcon("RockPaperScissors\paper.png"))
        elif x==2:
            self.ui.player_choice.setIcon(QIcon("RockPaperScissors/rock.png"))
        elif x==3:
            self.ui.player_choice.setIcon(QIcon("RockPaperScissors\scissors.png"))
        c=random.randint(1,3)
        if c==1:
            self.ui.computer_choice.setIcon(QIcon("RockPaperScissors\c-paper.png"))
        elif c==2:
            self.ui.computer_choice.setIcon(QIcon("RockPaperScissors\c-rock.png"))
        elif c==3:
            self.ui.computer_choice.setIcon(QIcon("RockPaperScissors\c-scissors.png"))
        if (x==1 and c==1) or (x==1 and c==1) or (x==1 and c==1):
            self.ties += 1
        elif (x==1 and c==2) or (x==2 and c==3) or (x==3 and c==1):
            self.u_score += 1
        elif (x==2 and c==1) or (x==3 and c==2) or (x==3 and c==1):
            self.c_score += 1
        
        self.ui.player_score.setText(str(self.u_score))      
        self.checkscore()




    def checkscore(self):
        if self.u_score==5:
            self.ui.result.setText("You win! 🎉")
        elif self.c_score==5:
            self.ui.result.setText("Computer won.")
        elif self.ties==5:
            self.ui.result.setText("Ties!")
            





app=QApplication(sys.argv)

main_window=MainWindow()
main_window.show()

app.exec()