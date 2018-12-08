import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtWidgets import QLCDNumber, QLabel, QLineEdit
from PyQt5.QtGui import QPixmap

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        self.setGeometry(300, 300, 300, 400)
        self.setWindowTitle('Img')

        self.btn = QPushButton('Показать', self)
        self.btn.resize(self.btn.sizeHint())
        self.btn.move(100, 80)
        self.btn.clicked.connect(self.hello)


        # _________input1____________________#
        self.name_label = QLabel(self)
        self.name_label.setText("Имя файла:  ")
        self.name_label.move(40, 50)

        self.name_input = QLineEdit(self)
        self.name_input.move(130, 50)

        self.pix_label = QLabel(self)
        self.pix_label.setText("testtesttesttesttesttesttesttest \n srfgwrfgwerf")
        self.pix_label.setGeometry(40, 150, 200, 200)

    def hello(self):
        a = self.name_input.text()
        pixmap = QPixmap(a)
        self.pix_label.setPixmap(pixmap)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
