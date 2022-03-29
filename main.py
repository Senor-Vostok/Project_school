from PyQt5.QtWidgets import QLabel, QPushButton, QWidget, QApplication, QInputDialog, QLineEdit, QVBoxLayout, QGroupBox, QHBoxLayout, QFileDialog, QRadioButton
from PyQt5.QtGui import QPixmap, QFont, QIcon, QFontDatabase, QCursor, QCloseEvent
from PyQt5.QtCore import QSize, QTimer
from PyQt5.Qt import Qt
import sys


class Smotr(QWidget):
    def __init__(self, bd):
        super().__init__()
        self.left = QPushButton('<', self)
        self.right = QPushButton('>', self)
        self.left.setFont(QFont('', 20))
        self.right.setFont(QFont('', 20))
        self.left.setFixedSize(30, 200)
        self.right.setFixedSize(30, 200)
        self.left.move(0, 120)
        self.right.move(610, 120)
        self.left.clicked.connect(self.leftb)
        self.right.clicked.connect(self.rightb)
        self.left.setEnabled(False)
        self.number = 0

        self.bd = bd
        if len(self.bd) == 1:
            self.right.setEnabled(False)
        self.UI()

    def check(self):
        if self.bd[self.number][1] == 'False':
            self.answer = QLineEdit(self)
            self.answer.show()
            self.answer.setFixedSize(500, 20)
            self.mainstick.addWidget(self.answer, alignment=Qt.AlignCenter)
        else:
            self.gb = QGroupBox('варианты', self)
            self.gb.setFixedSize(500, 300)
            self.sp = ['None'] * (len(self.bd[self.number][2]) - 1)
            self.ms = QVBoxLayout(self)
            for i in range(len(self.bd[self.number][2]) - 1):
                self.sp[i] = QRadioButton(self.bd[self.number][2][i])
                self.sp[i].show()
                self.ms.addWidget(self.sp[i])
            self.gb.setLayout(self.ms)
            self.gb.show()
            self.mainstick.addWidget(self.gb, alignment=Qt.AlignCenter)


    def leftb(self):
        self.right.setEnabled(True)
        self.number -= 1
        self.qwestion.setText(self.bd[self.number][0])
        self.listnumber.setText(f'Страница: {self.number + 1}/{len(self.bd)}')
        try:
            self.answer.deleteLater()
        except Exception:
            self.gb.deleteLater()
        self.check()
        if self.number + 1 == 1:
            self.left.setEnabled(False)

    def rightb(self):
        self.left.setEnabled(True)
        self.number += 1
        self.qwestion.setText(self.bd[self.number][0])
        self.listnumber.setText(f'Страница: {self.number + 1}/{len(self.bd)}')
        try:
            self.answer.deleteLater()
        except Exception:
            self.gb.deleteLater()
        self.check()
        if self.number + 1 == len(self.bd):
            self.right.setEnabled(False)

    def UI(self):
        self.setWindowTitle('Lös-ученик')
        self.setFixedSize(640, 360)
        self.listnumber = QLabel(f'Страница: {self.number + 1}/{len(self.bd)}', self)
        self.listnumber.setFont(QFont(font, 10))
        self.listnumber.move(10, 10)
        self.mainstick = QVBoxLayout(self)
        self.qwestion = QLabel(self.bd[self.number][0], self)
        self.qwestion.setFont(QFont(font, 10))
        self.mainstick.addWidget(self.qwestion, alignment=Qt.AlignCenter)
        self.check()


class Create_work(QWidget):
    def __init__(self):
        super().__init__()
        self.UI()

    def UI(self):
        self.setWindowTitle('Lös-учитель')
        self.setFixedSize(1280, 720)
        self.fon = QLabel(self)
        self.fon.setPixmap(QPixmap('add/fon/fon1.png'))
        self.fon.setFixedSize(1280, 720)
        self.back = QPushButton('<', self)
        self.back.setFont(QFont('', 20))
        self.back.setFixedSize(30, 200)
        self.back.move(0, 260)
        self.back.setStyleSheet('background: #808080;')
        self.back.clicked.connect(self.backlist)
        self.back.setEnabled(False)
        self.next = QPushButton('>', self)
        self.next.setFont(QFont('', 20))
        self.next.setFixedSize(30, 200)
        self.next.move(1250, 260)
        self.next.clicked.connect(self.nextlist)
        self.next.setEnabled(False)
        self.next.setStyleSheet('background: #808080;')
        self.createqw = QLineEdit(self)
        self.createqw.setPlaceholderText('Создать вопрос')
        self.createqw.setFont(QFont(font, 10))
        self.createqw.setFixedSize(500, 30)
        self.createqw.move(50, 50)
        self.wr = QLabel('Ответ ученика', self)
        self.wr.setFont(QFont(font, 10))
        self.wr.move(50, 130)
        self.wr.setStyleSheet('color: rgb(255, 255, 255);')
        self.choice1 = QRadioButton('Тестовый ответ', self)
        self.choice1.setFont(QFont(font, 10))
        self.choice1.move(50, 180)
        self.choice1.clicked.connect(self.manychoice)
        self.choice1.setStyleSheet('color: rgb(255, 255, 255);')
        self.choice2 = QRadioButton('Ручной ввод', self)
        self.choice2.setFont(QFont(font, 10))
        self.choice2.move(50, 230)
        self.choice2.clicked.connect(self.onechoice)
        self.choice2.setStyleSheet('color: rgb(255, 255, 255);')
        self.li = 1
        self.number = QLabel(f'Страница {self.li}', self)
        self.number.setFont(QFont(font, 15))
        self.number.setFixedSize(500, 30)
        self.number.move(50, 670)
        self.number.setStyleSheet('color: rgb(255, 255, 255);')
        self.predsmotr = QPushButton('Предпросмотр', self)
        self.predsmotr.setFont(QFont(font, 15))
        self.predsmotr.setFixedSize(200, 30)
        self.predsmotr.move(620, 670)
        self.predsmotr.setStyleSheet('background: #FFDD33;')
        self.predsmotr.clicked.connect(self.smotr)
        self.savetests = QPushButton('Сохранить тест', self)
        self.savetests.setFont(QFont(font, 15))
        self.savetests.setFixedSize(200, 30)
        self.savetests.move(825, 670)
        self.savetests.setStyleSheet('background: #FFDD33;')
        self.savetests.clicked.connect(self.savetest)
        self.bd = [['None', 'None', 'None']]
        self.create = QPushButton('Добавить в тест', self)
        self.create.setFont(QFont(font, 15))
        self.create.setFixedSize(200, 30)
        self.create.move(1030, 670)
        self.create.clicked.connect(self.adli)
        self.create.setStyleSheet('background: #FFDD33;')
        self.select = 'None'

    def smotr(self):
        self.smotret = Smotr(self.bd)
        self.smotret.show()

    def preob(self):
        sp2 = list()
        for i in self.bd:
            sp1 = list()
            for j in i:
                try:
                    j.append('0')
                    j.pop(-1)
                    sp3 = list()
                    for l in j:
                        sp3.append(l)
                    sp1.append('-----'.join(sp3))
                except Exception:
                    sp1.append(j)
            sp2.append('~~~~~'.join(sp1))
        sp2 = '\n'.join(sp2)
        return sp2

    def savetest(self):
        name = QFileDialog.getSaveFileName(self, 'Сохраните файл', None, '.los')
        name = name[0] + name[1]
        if name:
            with open(name, mode='w') as file:
                file.write(self.preob())

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
            self.next.setStyleSheet('background: #FFDD33;')
            if self.li != 1:
                self.back.setEnabled(True)
                self.back.setStyleSheet('background: #FFDD33;')

    def backlist(self):
        self.li -= 1
        self.number.setText(f'Страница {self.li}')
        if self.li == 1:
            self.back.setEnabled(False)
            self.back.setStyleSheet('background: #808080;')
        self.next.setEnabled(True)
        self.next.setStyleSheet('background: #FFDD33;')
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
        self.back.setStyleSheet('background: #FFDD33;')
        self.number.setText(f'Страница {self.li}')
        if self.li == len(self.bd):
            self.next.setEnabled(False)
            self.next.setStyleSheet('background: #808080;')
        self.checklist()

    def onechoice(self):
        self.select = 'False'
        try:
            self.many.hide()
            self.ok.hide()
            self.yanswer.hide()
            for i in self.spisok:
                i.hide()
        except Exception:
            pass
        self.otvet = QLineEdit(self)
        self.otvet.setPlaceholderText('Правильный ответ')
        self.otvet.setFont(QFont(font, 10))
        self.otvet.setFixedSize(300, 25)
        self.otvet.move(300, 180)
        self.otvet.show()

    def manychoice(self):
        self.select = 'True'
        self.many = QLineEdit(self)
        self.many.setPlaceholderText('Количество вопросов')
        self.many.setFont(QFont(font, 10))
        self.many.setFixedSize(300, 25)
        self.many.move(300, 180)
        self.many.show()
        self.ok = QPushButton('Ввод', self)
        self.ok.setFont(QFont(font, 10))
        self.ok.setFixedSize(60, 25)
        self.ok.move(600, 180)
        self.ok.show()
        self.ok.clicked.connect(self.createqwestions)
        self.ok.setStyleSheet('background: #FFDD33;')

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
                    self.ch.setFont(QFont(font, 10))
                    self.spisok.append(self.ch)
            self.yanswer = QLineEdit(self)
            self.yanswer.setPlaceholderText('Правильный ответ')
            self.yanswer.setFixedSize(400, 25)
            self.yanswer.move(830, 550)
            self.yanswer.setFont(QFont(font, 10))
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
        self.bt1.setFont(QFont(font, 10))
        self.bt1.move(40, 610)
        self.bt2 = QPushButton('Ваши данные', self)
        self.bt2.setFont(QFont(font, 10))
        self.bt2.setFixedSize(200, 30)
        self.bt2.move(240, 610)
        self.bt3 = QPushButton('Ошибка?', self)
        self.bt3.setFont(QFont(font, 10))
        self.bt3.setFixedSize(200, 30)
        self.bt3.move(440, 610)
        self.bt_create = QPushButton('Создать', self)
        self.bt_create.setFont(QFont(font, 20))
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
        self.fon.setPixmap(QPixmap('add/fon/fon.png'))
        self.fon.setFixedSize(1280, 720)

        self.student = QPushButton('Ученик', self)
        self.student.setFont(QFont(font, 15))
        self.student.setFixedSize(300, 50)
        self.student.move(50, 620)
        self.student.clicked.connect(self.stude)
        self.student.setStyleSheet('background: #FFDD33;')

        self.teacher = QPushButton('Учитель', self)
        self.teacher.setFont(QFont(font, 15))
        self.teacher.setFixedSize(300, 50)
        self.teacher.move(355, 620)
        self.teacher.clicked.connect(self.teach)
        self.teacher.setStyleSheet('background: #FFDD33;')

        self.teacher_or_student = None

        self.all_widget = [self.student, self.teacher]

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

    def menu(self):
        for i in self.main_widget:
            i.hide()
        self.hide_menu(False, self.all_widget)
        self.fon.setPixmap(QPixmap('add/fon/fon1.png'))

    def stude(self):
        for i in self.all_widget:
            i.hide()
        self.fon.setPixmap(QPixmap('add/fon/fon1.png'))
        self.bt_create.setText('Решить')
        for i in self.main_widget:
            i.show()
        self.teacher_or_student = True

    def teach(self):
        for i in self.all_widget:
            i.hide()
        self.fon.setPixmap(QPixmap('add/fon/fon1.png'))
        self.bt_create.setText('Создать')
        for i in self.main_widget:
            i.show()
        self.teacher_or_student = True


if __name__ == '__main__':
    app = QApplication(sys.argv)
    font = 'Ruberoid Semi Bold'
    QFontDatabase.addApplicationFont('Ruberoid-SemiBold.ttf')
    progarm = Project()
    progarm.show()
    sys.exit(app.exec())
