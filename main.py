from PyQt5.QtWidgets import QLabel, QPushButton, QWidget, QApplication, QInputDialog, QLineEdit, QVBoxLayout, QGroupBox, QHBoxLayout, QFileDialog, QRadioButton
from PyQt5.QtGui import QPixmap, QFont, QIcon, QFontDatabase, QCursor, QCloseEvent
from PyQt5.QtCore import QSize, QTimer
from PyQt5.Qt import Qt
import sys


class Create_work(QWidget):
    def __init__(self):
        super().__init__()
        self.UI()

    def UI(self):
        self.setWindowTitle('Lös-учитель')
        self.setFixedSize(1280, 720)
        self.back = QPushButton('<', self)
        self.back.setFont(QFont('', 20))
        self.back.setFixedSize(30, 200)
        self.back.move(0, 260)
        self.back.clicked.connect(self.backlist)
        self.back.setEnabled(False)
        self.next = QPushButton('>', self)
        self.next.setFont(QFont('', 20))
        self.next.setFixedSize(30, 200)
        self.next.move(1250, 260)
        self.next.clicked.connect(self.nextlist)
        self.next.setEnabled(False)
        self.createqw = QLineEdit(self)
        self.createqw.setPlaceholderText('Создать вопрос')
        self.createqw.setFont(QFont('Intro Cond Black Free', 10))
        self.createqw.setFixedSize(500, 30)
        self.createqw.move(50, 50)
        self.wr = QLabel('Ответ ученика', self)
        self.wr.setFont(QFont('Intro Cond Black Free', 10))
        self.wr.move(50, 130)
        self.choice1 = QRadioButton('Тестовый ответ', self)
        self.choice1.setFont(QFont('Intro Cond Black Free', 10))
        self.choice1.move(50, 180)
        self.choice1.clicked.connect(self.manychoice)
        self.choice2 = QRadioButton('Ручной ввод', self)
        self.choice2.setFont(QFont('Intro Cond Black Free', 10))
        self.choice2.move(50, 230)
        self.choice2.clicked.connect(self.onechoice)
        self.li = 1
        self.number = QLabel(f'Страница {self.li}', self)
        self.number.setFont(QFont('Intro Cond Black Free', 15))
        self.number.setFixedSize(500, 30)
        self.number.move(50, 670)
        self.bd = [[None, None, None]]
        self.create = QPushButton('Добавить', self)
        self.create.setFont(QFont('Intro Cond Black Free', 15))
        self.create.setFixedSize(200, 30)
        self.create.move(1030, 670)
        self.create.clicked.connect(self.adli)
        self.select = 'None'

    def adli(self):
        if self.select != 'None':
            self.bd[self.li - 1][0] = self.createqw.text()
            self.bd[self.li - 1][1] = self.select
            if self.select == 'True':
                sp = list()
                print(self.spisok)
                for i in self.spisok:
                    sp.append(i.text())
                sp.append(self.yanswer.text())
                self.bd[self.li - 1][2] = sp
            elif self.select == 'False':
                self.bd[self.li - 1][2] = self.otvet.text()
            print(self.bd)
            self.next.setEnabled(True)

    def backlist(self):
        self.li -= 1
        self.number.setText(f'Страница {self.li}')
        if self.li == 1:
            self.back.setEnabled(False)
        self.next.setEnabled(True)
        self.checklist()

    def checklist(self):
        if self.bd[self.li - 1][1] == 'True':
            self.createqw.setText(self.bd[self.li - 1][0])
            try:
                self.otvet.hide()
            except Exception:
                pass
            self.many.setText(str(len(self.bd[self.li - 1][2])))
            self.many.show()
            self.ok.show()
            self.yanswer.show()
            try:
                for i in self.spisok:
                    i.hide()
            except Exception:
                pass
            try:
                self.spisok = list()
                for i in range(int(self.many.text())):
                    if i <= 9 and i != int(self.many.text()) - 1:
                        self.ch = QLineEdit(self.bd[self.li - 1][2][i], self)
                        self.ch.setFixedSize(400, 25)
                        self.ch.move(830, 50 + i * 50)
                        self.ch.show()
                        self.spisok.append(self.ch)
                self.yanswer.setText(self.bd[self.li - 1][2][-1])
            except Exception:
                pass
        elif self.bd[self.li - 1][1] == 'False':
            self.createqw.setText(self.bd[self.li - 1][0])
            try:
                self.many.hide()
                self.ok.hide()
                self.yanswer.hide()
            except Exception:
                pass
            try:
                for i in self.spisok:
                    i.hide()
            except Exception:
                pass
            self.otvet.setText(self.bd[self.li - 1][2])
            self.otvet.show()
        elif self.select == 'True':
            self.createqw.setText('')
            self.many.setText('')
            for i in self.spisok:
                i.hide()
            self.yanswer.hide()
        elif self.select == 'False':
            self.createqw.setText('')
            self.otvet.setText('')

    def nextlist(self):
        if self.li == len(self.bd):
            self.bd.append(['None', 'None', 'None'])
        self.li += 1
        self.back.setEnabled(True)
        self.number.setText(f'Страница {self.li}')
        self.next.setEnabled(False)
        self.checklist()


    def onechoice(self):
        self.select = 'False'
        try:
            self.many.hide()
            self.ok.hide()
            for i in self.spisok:
                i.hide()
        except Exception:
            pass
        self.otvet = QLineEdit(self)
        self.otvet.setPlaceholderText('Правильный ответ')
        self.otvet.setFont(QFont('Intro Cond Black Free', 10))
        self.otvet.setFixedSize(300, 25)
        self.otvet.move(300, 180)
        self.otvet.show()

    def manychoice(self):
        self.select = 'True'
        self.many = QLineEdit(self)
        self.many.setPlaceholderText('Количество вопросов')
        self.many.setFont(QFont('Intro Cond Black Free', 10))
        self.many.setFixedSize(300, 25)
        self.many.move(300, 180)
        self.many.show()
        self.ok = QPushButton('Ввод', self)
        self.ok.setFont(QFont('Intro Cond Black Free', 10))
        self.ok.setFixedSize(60, 25)
        self.ok.move(600, 180)
        self.ok.show()
        self.ok.clicked.connect(self.createqwestions)

    def createqwestions(self):
        try:
            for i in self.spisok:
                i.hide()
        except Exception:
            pass
        try:
            self.spisok = list()
            for i in range(int(self.many.text())):
                if i <= 9:
                    self.ch = QLineEdit(self)
                    self.ch.setPlaceholderText(f'Вариант ответа {i + 1}')
                    self.ch.setFixedSize(400, 25)
                    self.ch.move(830, 50 + i * 50)
                    self.ch.show()
                    self.spisok.append(self.ch)
            self.yanswer = QLineEdit(self)
            self.yanswer.setPlaceholderText('Правильный ответ')
            self.yanswer.setFont(QFont('Intro Cond Black Free', 10))
            self.yanswer.setFixedSize(400, 25)
            self.yanswer.move(830, 550)
            self.yanswer.show()
        except Exception:
            pass


class Project(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def start_kit(self):
        self.bt1 = QPushButton('Главная', self)
        self.bt1.setFixedSize(200, 30)
        self.bt1.setFont(QFont('Intro Cond Black Free', 10))
        self.bt1.move(40, 610)
        self.bt2 = QPushButton('Ваши данные', self)
        self.bt2.setFont(QFont('Intro Cond Black Free', 10))
        self.bt2.setFixedSize(200, 30)
        self.bt2.move(240, 610)
        self.bt3 = QPushButton('Ошибка?', self)
        self.bt3.setFont(QFont('Intro Cond Black Free', 10))
        self.bt3.setFixedSize(200, 30)
        self.bt3.move(440, 610)
        self.bt_create = QPushButton('Создать', self)
        self.bt_create.setFont(QFont('Intro Cond Black Free', 20))
        self.bt_create.setFixedSize(600, 40)
        self.bt_create.move(40, 645)
        self.bt_create.clicked.connect(self.doit)
        self.main_widget = [self.bt1, self.bt2, self.bt3, self.bt_create]
        for i in self.main_widget:
            i.setStyleSheet('background: #FFDD33;')
        self.bt1.clicked.connect(self.menu)

    def doit(self):
        if self.bt_create.text().lower() == 'решить':
            name = QFileDialog.getOpenFileName(self, "Выберите файл", ".")
            print(name)
        else:
            self.redactor = Create_work()
            self.redactor.show()

    def initUI(self):
        self.setWindowTitle('Lös')
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
        self.button.setStyleSheet('background: #FFDD33;')

        self.button1 = QPushButton('Регистрация', self)
        self.button1.setFont(QFont('Intro Cond Black Free', 10))
        self.button1.setFixedSize(200, 30)
        self.button1.move(625, 655)
        self.button1.clicked.connect(self.register)
        self.button1.setStyleSheet('background: #FFDD33;')

        self.button2 = QPushButton('Забыли пароль?', self)
        self.button2.setFont(QFont('Intro Cond Black Free', 10))
        self.button2.setFixedSize(200, 30)
        self.button2.move(625, 620)
        self.button2.setStyleSheet('background: #FFDD33;')

        self.teacher_or_student = None

        self.all_widget = [self.log, self.pas, self.button, self.button1, self.button2]

        self.start_kit()
        self.menu()

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
            if self.login.lower() == '1':
                self.stude()
            elif self.login.lower() == '2':
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
        self.fon.setPixmap(QPixmap('add/fon/fon2.png'))
        self.bt_create.setText('Решить')
        for i in self.main_widget:
            i.show()
        self.teacher_or_student = True

    def teach(self):
        self.fon.setPixmap(QPixmap('add/fon/fon2.png'))
        self.bt_create.setText('Создать')
        for i in self.main_widget:
            i.show()
        self.teacher_or_student = True


if __name__ == '__main__':
    app = QApplication(sys.argv)
    QFontDatabase.addApplicationFont('IntroCondBlackFree.ttf')
    progarm = Project()
    progarm.show()
    sys.exit(app.exec())
