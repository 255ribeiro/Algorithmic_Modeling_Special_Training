import sys
from PyQt5.QtWidgets import *


class DlgMain(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My GUI")
        self.resize(300, 200)

        self.btn1 = QPushButton('Name', self)
        self.btn1.move(100,35)
        self.btn1.clicked.connect(self.evt_btn1_clicked)

        self.btn2 = QPushButton('Age', self)
        self.btn2.move(100,75)
        self.btn2.clicked.connect(self.evt_btn2_clicked)

        self.btn3 = QPushButton('height', self)
        self.btn3.move(100,115)
        self.btn3.clicked.connect(self.evt_btn3_clicked)

        self.btn4 = QPushButton('Profession', self)
        self.btn4.move(100,155)
        self.btn4.clicked.connect(self.evt_btn4_clicked)


    def evt_btn1_clicked(self):
        
        str_name, bool_res = QInputDialog.getText(self, "Text", "Enter your name: ")
        if bool_res:
            QMessageBox.information(self, 'Name', 'Your name is {}'.format(str_name))
        else:
            QMessageBox.warning(self,'Canceled', 'Canceled by user' )

    def evt_btn2_clicked(self):
        
        i_age, bool_res = QInputDialog.getInt(self, "Age", "Enter your age: ", 20, 0, 120, 1)
        if bool_res:
            QMessageBox.information(self, 'Age', 'Your age is {} years old'.format(str(i_age)))
        else:
            QMessageBox.warning(self,'Canceled', 'Canceled by user' )

    def evt_btn3_clicked(self):
        
        d_height, bool_res = QInputDialog.getDouble(self, "Height", "Enter your height: ", 1.70, .50, 3.00, 2)
        if bool_res:
            QMessageBox.information(self, 'Height', 'Your height is {}m'.format(str(d_height)))
        else:
            QMessageBox.warning(self,'Canceled', 'Canceled by user' )
        

    def evt_btn4_clicked(self):
        lst_profession = ["Architect", "Engineer", "Programmer"]
        str_profession, bool_res = QInputDialog.getItem(self, "Text", "Enter your profession: ", lst_profession, editable=False)
        if bool_res:
            QMessageBox.information(self, "Name", "Your profession is "+ str_profession)
        else:
            QMessageBox.critical(self, "Canceled", "User canceled")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    dlgMain = DlgMain()
    dlgMain.show()
    sys.exit(app.exec_())
