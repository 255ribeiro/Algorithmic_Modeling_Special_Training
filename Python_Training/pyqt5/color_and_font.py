import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *


# Main Class
class DlgMain(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My App")
        self.resize(200, 200)

        # First Button
        self.btn1 = QPushButton("Color Picker", self)
        self.btn1.move(40, 20)
        self.btn1.clicked.connect(self.evt_btn1_clicked)

        # Second Button
        self.btn2 = QPushButton("Set font", self)
        self.btn2.move(40, 50)
        self.btn2.clicked.connect(self.evt_btn2_clicked)

        # Label
        self.nameLabel = QLabel('Example Text',self)
        self.nameLabel.move(40,100)
        self.nameLabel.resize(500,20)

    # Button 1 event
    def evt_btn1_clicked(self):

        color = QColorDialog.getColor(QColor("indigo"), self, "Choose Color")
        p = self.palette()
        p.setColor(self.backgroundRole(), color)
        self.setPalette(p)
        print(color.getRgbF())

    # Button 2 event
    def evt_btn2_clicked(self):
        font, bool_res = QFontDialog.getFont()
        if bool_res:
            print(font.family())
            print(font.italic())
            print(font.bold())
            print(font.weight())
            print(font.pointSize())
            self.nameLabel.setFont(font)

        else:
            font = QFont("Times New Roman", 24, 81, True)
            print(font.family())
            print(font.italic())
            print(font.bold())
            print(font.weight())
            print(font.pointSize())
            self.nameLabel.setFont(font)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    dlgMain = DlgMain()
    dlgMain.show()
    sys.exit(app.exec_())