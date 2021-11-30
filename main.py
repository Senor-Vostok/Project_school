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
        self.button.setFixedSize(100, 30)
        self.button.clicked.connect(self.check)
        self.button.setStyleSheet('background: rgb(255,204,0);')

        self.info = QLabel('Введите корректные данные пользователя!', self)
        self.info.setStyleSheet('background: rgb(255,0,0);')
        self.info.setFont(QFont('Arial', 10))
        self.info.move(50, 850)
        self.info.hide()

        self.win = QLineEdit(self)
        self.win.setFixedSize(200, 30)
        self.win.move(700, 400)


    def check(self):
        self.text = self.win.text()
        if not self.text:
            self.info.show()
            self.win.setStyleSheet('background: rgb(255, 200, 200);')
        else:
            self.info.hide()
            self.win.setStyleSheet('background: rgb(200, 255, 200);')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    progarmm = Project()
    progarmm.show()
    sys.exit(app.exec())
