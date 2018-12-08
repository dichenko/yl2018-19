import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtWidgets import QLCDNumber, QLabel, QLineEdit


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 300, 400)
        self.setWindowTitle('Calc')

        self.btn = QPushButton('Рассчитать', self)
        self.btn.resize(self.btn.sizeHint())
        self.btn.move(100, 300)
        self.btn.clicked.connect(self.hello)

        self.label = QLabel(self)
        self.label.setText("Введите два числа")
        self.label.move(80, 20)

        # _________input1____________________#
        self.name_label = QLabel(self)
        self.name_label.setText("a =  ")
        self.name_label.move(40, 50)

        self.name_input = QLineEdit(self)
        self.name_input.move(80, 50)

        #_________input2____________________#
        self.name_label2 = QLabel(self)
        self.name_label2.setText("b =  ")
        self.name_label2.move(40, 100)

        self.name_input2 = QLineEdit(self)
        self.name_input2.move(80, 100)

        # _________LCD1____________________#
        self.LCD_count1 = QLCDNumber(self)
        self.LCD_count1.move(110, 140)
        # _________LCD2____________________#
        self.LCD_count2 = QLCDNumber(self)
        self.LCD_count2.move(110, 170)
        # _________LCD3____________________#
        self.LCD_count3 = QLCDNumber(self)
        self.LCD_count3.move(110, 200)
        # _________LCD4____________________#
        self.LCD_count4 = QLCDNumber(self)
        self.LCD_count4.move(110, 230)

    def hello(self):
        a = self.name_input.text()
        b = self.name_input2.text()
        self.LCD_count1.display(str(int(a) + int(b)))
        self.LCD_count2.display(str(int(a) - int(b)))
        self.LCD_count3.display(str(int(a) * int(b)))
        if b == '0':
            self.LCD_count4.display('error')
        else:
            self.LCD_count4.display(str(int(a) / int(b)))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())