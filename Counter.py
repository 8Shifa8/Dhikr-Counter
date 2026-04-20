from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys


class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.setGeometry(200, 200, 300, 300)
        self.setWindowTitle("Dhikr Counter")
        self.count = 0
        self.initUI()

    def initUI(self):
        self.label = QtWidgets.QLabel(self)
        self.label.setText("0")
        self.label.move(130, 100)

        self.b1 = QtWidgets.QPushButton(self)
        self.b1.setText("Increase")
        self.b1.move(100, 150)
        self.b1.clicked.connect(self.increase)

        self.b2 = QtWidgets.QPushButton(self)
        self.b2.setText("Reset")
        self.b1.move(100, 190)
        self.b2.clicked.connect(self.reset)

    def increase(self):
        self.count += 1
        self.label.setText(str(self.count))
        self.label.adjustSize()

    def reset(self):
        self.count = 0
        self.label.setText(str(self.count))
        self.label.adjustSize()


def window():
    app = QApplication(sys.argv)
    win = MyWindow()
    win.show()
    sys.exit(app.exec_())


window()
