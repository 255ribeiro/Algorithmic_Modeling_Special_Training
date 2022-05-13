import sys
from PyQt5.QtWidgets import *

# Create class
class DlgMain(QDialog):

    # __init__ function
    def __init__(self):
        super().__init__()
        # configure main window
        self.setWindowTitle("My App")
        self.resize(300,200)

        # Buttons
        self.btn1 = QPushButton('Critial button', self)
        self.btn1.move(100,35)
        self.btn1.clicked.connect(self.evt_btn1_clicked)

        self.btn2 = QPushButton('Warning Button', self)
        self.btn2.move(100,75)
        self.btn2.clicked.connect(self.evt_btn2_clicked)

        self.btn3 = QPushButton('Question Button', self)
        self.btn3.move(100,115)
        self.btn3.clicked.connect(self.evt_btn3_clicked)

    # Buttons events

    def evt_btn1_clicked(self):
        res = QMessageBox.critical(self,'Disk Full', 'Your disk is almost full')
        print(res)

    def evt_btn2_clicked(self):
        res = QMessageBox.warning(self,'Disk Full', 'Your disk is almost full')
        print(res)

    def evt_btn3_clicked(self):
        res = QMessageBox.question(self,'Disk Full', 'Your disk is almost full')
        print(res)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    dlgMain = DlgMain()
    # show main window
    dlgMain.show()
    # execute app
    sys.exit(app.exec_())