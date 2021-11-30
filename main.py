from PyQt5.QtWidgets import QLabel, QPushButton, QWidget, QApplication, QInputDialog, QLineEdit, QVBoxLayout
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
        self.setFixedSize(1280, 720)

        self.info = QLabel('<font color="red">Введите корректные данные пользователя!', self)
        self.info.setFont(QFont('Arial', 10))
        self.info.move(50, 850)
        self.info.hide()

        self.log = QLineEdit(self)
        self.log.setPlaceholderText('Логин пользователя')
        self.log.move(50, 620)
        self.log.setFixedSize(500, 30)

        self.pas = QLineEdit(self)
        self.pas.setPlaceholderText('Пароль пользователя')
        self.pas.move(50, 655)
        self.pas.setFixedSize(500, 30)

        self.button = QPushButton('Нажми', self)
        self.button.setFixedSize(65, 65)
        self.button.move(555, 620)
        self.button.clicked.connect(self.check)
        self.button.setStyleSheet('background: rgb(255,204,0);')

        self.button1 = QPushButton('Регистрация', self)
        self.button1.setFixedSize(200, 30)
        self.button1.move(625, 655)
        self.button1.clicked.connect(self.register)
        self.button1.setStyleSheet('background: rgb(255,204,0);')

        self.button2 = QPushButton('Забыли пароль?', self)
        self.button2.setFixedSize(200, 30)
        self.button2.move(625, 620)
        self.button2.setStyleSheet('background: rgb(255,204,0);')

    def register(self):
        pass

    def check(self):
        self.login = self.log.text()
        self.password = self.pas.text()
        if not self.login or not self.password:
            self.info.show()
            self.log.setStyleSheet('background: rgb(255, 200, 200);')
            self.pas.setStyleSheet('background: rgb(255, 200, 200);')
        else:
            self.info.hide()
            self.log.setStyleSheet('background: rgb(200, 255, 200);')
            self.pas.setStyleSheet('background: rgb(200, 255, 200);')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    progarmm = Project()
    progarmm.show()
    sys.exit(app.exec())
