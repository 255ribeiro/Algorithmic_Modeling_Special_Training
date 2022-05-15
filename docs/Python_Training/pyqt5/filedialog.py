import sys
from PyQt5.QtWidgets import *


class DlgMain(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My GUI")
        self.resize(300, 300)

        self.btn1 = QPushButton('Open one file', self)
        self.btn1.move(100,35)
        self.btn1.clicked.connect(self.evt_btn1_clicked)

        self.btn2 = QPushButton('Open Multiple files', self)
        self.btn2.move(100,75)
        self.btn2.clicked.connect(self.evt_btn2_clicked)

        self.btn3 = QPushButton('New file', self)
        self.btn3.move(100,115)
        self.btn3.clicked.connect(self.evt_btn3_clicked)


    def evt_btn1_clicked(self):
        res = QFileDialog.getOpenFileName(self, "Open File", "C:/", "JPG File (*.jpg);;PNG Files (*.png);;ALL (*.*)")
        print(res)


    def evt_btn2_clicked(self):
        res = QFileDialog.getOpenFileNames(self, "Open Files", "C:/Users", "JPG File (*.jpg);;PNG Files (*.png);;ALL (*.*)")
        print(res)

    def evt_btn3_clicked(self):
        res = QFileDialog.getSaveFileName(self, "Save File", "D:/gitrepos", "JPG File (*.jpg);;PNG Files (*.png);;ALL (*.*)")
        print(res)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    dlgMain = DlgMain()
    dlgMain.show()
    sys.exit(app.exec_())
