import random
from functools import partial
import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox
from PySide6.QtCore import QFile
from ui_mainwindow import Ui_MainWindow



class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.btn_str.clicked.connect(self.reset_and_start_game)
        self.ui.btn_sub.clicked.connect(self.checkplay)
        self.ui.btn_res.clicked.connect(self.reset_and_start_game)
        self.goal=random.randint(1,100)
        self.chance=7
        self.ui.ch_remain.setText(str(self.chance))
        print(self.goal)
    

    def checkplay(self):
        if self.ui.input.text()=="":
            QMessageBox.warning(self, "Attention", "You have not entered a number yet!")
            return
        if self.chance>1:
            if int(self.ui.input.text())==self.goal:
                msg_box=QMessageBox(windowTitle="Congratulations", text="You hit the target!🎉")
                msg_box.exec()
                self.reset_and_start_game()
            elif int(self.ui.input.text()) < self.goal:
                self.chance -= 1
                msg_box=QMessageBox(windowTitle="Wrong Guess", text="Go Up! Number of your chances left:" + str(self.chance))
                msg_box.exec()
                self.ui.grt.setText(self.ui.input.text())
            elif int(self.ui.input.text()) > self.goal:
                self.chance -= 1
                msg_box=QMessageBox(windowTitle="Wrong Guess", text="Go Down! Number of your chances left:" + str(self.chance))
                msg_box.exec()
                self.ui.lss.setText(self.ui.input.text())
        elif self.chance <= 1:
            msg_box=QMessageBox(windowTitle="Sorry!", text="You did not succeed. The true number was:" + str(self.goal))
            msg_box.exec()
            self.reset_and_start_game()

        self.ui.ch_remain.setText(str(self.chance))

        

    def reset_and_start_game(self):
        self.goal=random.randint(1,100)
        self.ui.input.setText("")
        self.ui.grt.setText("")
        self.ui.lss.setText("")






app=QApplication(sys.argv)

main_window=MainWindow()
main_window.show()

app.exec()