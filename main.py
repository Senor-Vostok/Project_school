from PyQt5.QtWidgets import QLabel, QPushButton, QWidget, QApplication, QInputDialog, QLineEdit
from PyQt5.QtGui import QPixmap, QFont, QIcon, QFontDatabase, QCursor, QCloseEvent
from PyQt5.QtCore import QSize, QTimer
from PyQt5.Qt import Qt
import sys


class Project(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Project')
        self.setFixedSize(1600, 900)

        self.test = QLabel('Регистрация/вход', self)
        self.test.move(100, 100)
        self.test.setFont(QFont('Arial', 72))

        self.button = QPushButton('Нажми', self)
        self.button.move(750, 450)
        self.button.setFixedSize(100, 50)
        self.button.clicked.connect(self.prr)

        self.win = QLineEdit(self)
        self.win.setFixedSize(200, 30)
        self.win.move(700, 400)


    def prr(self):
        self.test.setText('Успешно')
        self.test.setFont(QFont('Arial', 72))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    progarmm = Project()
    progarmm.show()
    sys.exit(app.exec())
