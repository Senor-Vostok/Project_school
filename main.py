from PyQt5.QtWidgets import QLabel, QPushButton, QWidget, QApplication, QInputDialog, QLineEdit, QVBoxLayout, QGroupBox, QHBoxLayout
from PyQt5.QtGui import QPixmap, QFont, QIcon, QFontDatabase, QCursor, QCloseEvent
from PyQt5.QtCore import QSize, QTimer
from PyQt5.Qt import Qt
import sys


class Project(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def start_kit(self):
        self.bt1 = QPushButton('Главная', self)
        self.bt1.setFont(QFont('Intro Cond Black Free', 20))
        self.bt1.move(1200, 0)
        self.bt2 = QPushButton('Ваши данные', self)
        self.bt2.setFont(QFont('Intro Cond Black Free', 20))
        self.bt3 = QPushButton('Ошибка?', self)
        self.bt3.setFont(QFont('Intro Cond Black Free', 20))
        self.bt_create = QPushButton('Создать', self)
        self.bt_create.setFont(QFont('Intro Cond Black Free', 30))
        self.bt_create.setFixedSize(462, 140)
        self.bt_create.move(-462, 216)
        self.bt_bd = QPushButton('Данные учеников', self)
        self.bt_bd.setFont(QFont('Intro Cond Black Free', 30))
        self.bt_bd.setFixedSize(462, 140)
        self.bt_bd.move(-462, 360)
        self.bt_result = QPushButton('Оценки учеников \nза работы', self)
        self.bt_result.setFont(QFont('Intro Cond Black Free', 30))
        self.bt_result.setFixedSize(462, 140)
        self.bt_result.move(-462, 504)
        self.main_widget = [self.bt1, self.bt2, self.bt3, self.bt_create, self.bt_bd, self.bt_result]
        for i in self.main_widget:
            i.setStyleSheet('background: #19A3F5;')
        self.bt1.clicked.connect(self.menu)

    def initUI(self):
        self.setWindowTitle('Project')
        self.setFixedSize(1280, 720)

        self.fon = QLabel(self)
        self.fon.setPixmap(QPixmap('add/fon/fon2.png'))
        self.fon.setFixedSize(1280, 720)

        self.info = QLabel('<font color="red">Введите корректные данные пользователя!', self)
        self.info.setFont(QFont('Intro Cond Black Free', 10))
        self.info.move(50, 690)
        self.info.hide()

        self.log = QLineEdit(self)
        self.log.setPlaceholderText('Логин пользователя')
        self.log.setFont(QFont('Intro Cond Black Free', 10))
        self.log.move(50, 620)
        self.log.setFixedSize(500, 30)

        self.pas = QLineEdit(self)
        self.pas.setPlaceholderText('Пароль пользователя')
        self.pas.setFont(QFont('Intro Cond Black Free', 10))
        self.pas.move(50, 655)
        self.pas.setFixedSize(500, 30)

        self.button = QPushButton('Ввод', self)
        self.button.setFont(QFont('Intro Cond Black Free', 10))
        self.button.setFixedSize(65, 65)
        self.button.move(555, 620)
        self.button.clicked.connect(self.check)
        self.button.setStyleSheet('background: #19A3F5;')

        self.button1 = QPushButton('Регистрация', self)
        self.button1.setFont(QFont('Intro Cond Black Free', 10))
        self.button1.setFixedSize(200, 30)
        self.button1.move(625, 655)
        self.button1.clicked.connect(self.register)
        self.button1.setStyleSheet('background: #19A3F5;')

        self.button2 = QPushButton('Забыли пароль?', self)
        self.button2.setFont(QFont('Intro Cond Black Free', 10))
        self.button2.setFixedSize(200, 30)
        self.button2.move(625, 620)
        self.button2.setStyleSheet('background: #19A3F5;')

        self.teacher_or_student = None

        self.all_widget = [self.log, self.pas, self.button, self.button1, self.button2]

        self.timer_anim = QTimer(self)
        self.timer_anim.setInterval(1)
        self.cord0 = -462
        self.timer_anim.timeout.connect(self.animation)

        self.start_kit()
        self.menu()

    def animation(self):
        self.timer_anim.start()
        if self.cord0 < 10:
            self.cord0 += 2
            for i in [self.bt_create, self.bt_bd, self.bt_result]:
                i.move(self.cord0, i.pos().y())
        else:
            self.timer_anim.stop()
            self.cord0 = -462

    def hide_menu(self, flag, spisok):
        if flag:
            for i in spisok:
                i.hide()
        else:
            for i in spisok:
                i.show()

    def register(self):
        pass

    def check(self):
        self.login = self.log.text()
        self.password = self.pas.text()
        if not self.login or not self.password:
            self.info.show()
        else:
            self.info.hide()
            self.hide_menu(True, self.all_widget)
            if self.login.lower() == 'ученик':
                self.stude()
            elif self.login.lower() == 'учитель':
                self.teach()
            else:
                self.info.show()
                self.hide_menu(False, self.all_widget)

    def menu(self):
        for i in self.main_widget:
            i.hide()
        self.hide_menu(False, self.all_widget)
        self.fon.setPixmap(QPixmap('add/fon/fon2.png'))

    def stude(self):
        self.animation()
        self.fon.setPixmap(QPixmap('add/fon/fon3.png'))
        self.bt_create.setText('Решить')
        self.bt_bd.setText('Предметы')
        self.bt_result.setText('Решенные')
        for i in self.main_widget:
            i.show()
        self.teacher_or_student = True

    def teach(self):
        self.animation()
        self.fon.setPixmap(QPixmap('add/fon/fon3.png'))
        self.bt_create.setText('Создать')
        self.bt_bd.setText('Данные учеников')
        self.bt_result.setText('Результаты учеников\nпо работе')
        for i in self.main_widget:
            i.show()
        self.teacher_or_student = True


if __name__ == '__main__':
    app = QApplication(sys.argv)
    QFontDatabase.addApplicationFont('IntroCondBlackFree.ttf')
    progarm = Project()
    progarm.show()
    sys.exit(app.exec())
