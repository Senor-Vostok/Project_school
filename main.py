from PyQt5.QtWidgets import QLabel, QPushButton, QWidget, QApplication, QInputDialog, QLineEdit, QVBoxLayout, QGroupBox, QHBoxLayout, QFileDialog, QRadioButton, QMessageBox
from PyQt5.QtGui import QPixmap, QFont, QIcon, QFontDatabase, QCursor, QCloseEvent
from PyQt5.QtCore import QSize, QTimer
from PyQt5.Qt import Qt
from random import choice
import sys

personality_answer = None


class YN(QWidget):
    def __init__(self):
        super().__init__()
        self.UI()

    def UI(self):
        self.setFixedSize(250, 100)
        self.setWindowTitle('Подтверждение')
        self.mainstick = QVBoxLayout(self)
        self.label = QLabel('Вы уверены, что хотите завершить тест?\nНекоторые задание не сделаны', self)
        self.stick = QHBoxLayout(self)
        self.ybt = QPushButton('Да', self)
        self.nbt = QPushButton('Нет', self)
        self.ybt.clicked.connect(self.choice1)
        self.nbt.clicked.connect(self.choice2)
        self.stick.addWidget(self.ybt, alignment=Qt.AlignCenter)
        self.stick.addWidget(self.nbt, alignment=Qt.AlignCenter)
        self.mainstick.addWidget(self.label, alignment=Qt.AlignCenter)
        self.mainstick.addLayout(self.stick)

    def choice1(self):
        global personality_answer
        personality_answer = True
        self.close()

    def choice2(self):
        self.close()


class Smotr(QWidget):
    def __init__(self, bd, sf=False, local=None):
        super().__init__()
        self.sf = sf
        if bd[0] != 'FINAL':
            self.fon = QLabel(self)
            self.fon.setFixedSize(960, 540)
            self.fon.setPixmap(QPixmap('add/fon/fon_stud.png'))
            self.wh = False
            self.bd = bd
            self.local = local
            self.yanswers = [i[2] for i in self.bd]
            for i in range(len(self.yanswers)):
                if self.bd[i][1] == 'True':
                    self.yanswers[i] = self.bd[i][2][-1]
            self.answers = [None] * len(self.bd)
            self.moved = 64
            self.timer = QTimer(self)
            self.timer.setInterval(10)
            self.timer.timeout.connect(self.animation)
            self.timer.stop()
            self.llen = 960 // len(self.answers)
            self.mainpolz = QLabel(self)
            self.mainpolz.setFixedSize(self.llen, 25)
            self.mainpolz.setStyleSheet('background: #F2E3D5;')
            self.polz = list()
            for i in range(len(self.answers)):
                s = QLabel(self)
                s.setFixedSize(self.llen, 20)
                s.setStyleSheet('background: rgb(200, 200, 200);')
                s.move(self.llen * i, 0)
                self.polz.append(s)
            self.UI()
        else:
            self.setWindowTitle('Lös-ученик')
            self.setFixedSize(960, 540)
            self.fon = QLabel(self)
            self.fon.setFixedSize(960, 540)
            self.fon.setPixmap(QPixmap('add/fon/fon_stud_final.png'))
            self.mainstick = QVBoxLayout(self)
            self.rezul = QLabel(bd[1], self)
            self.rezul.setFont(QFont(font, 70))
            self.rezul.setStyleSheet('color: #F2E3D5;')
            self.mainstick.addWidget(self.rezul, alignment=Qt.AlignCenter)
            self.opovesh = QLabel('Покажи учителю свой результат', self)
            self.opovesh.setFixedSize(500, 30)
            self.opovesh.setFont(QFont(font, 25))
            self.opovesh.move(275, 505)
            self.opovesh.setStyleSheet('color: #F2E3D5;')

    def animation(self):
        if self.mainpolz.x() < self.llen * self.number and not self.wh:
            self.mainpolz.move(self.mainpolz.x() + self.moved, 0)
            if self.moved > 16:
                self.moved = self.moved // 2
        elif self.mainpolz.x() > self.llen * self.number and self.wh:
            self.mainpolz.move(self.mainpolz.x() - self.moved, 0)
            if self.moved > 16:
                self.moved = self.moved // 2
        else:
            self.moved = 64
            self.mainpolz.move(self.llen * self.number, 0)
            self.wh = False
            self.timer.stop()

    def check(self):
        if self.bd[self.number][1] == 'False':
            self.answer = QLineEdit(self)
            self.answer.show()
            self.answer.setFixedSize(500, 20)
            self.mainstick.addWidget(self.answer, alignment=Qt.AlignCenter)
            if self.answers[self.number] != None:
                self.answer.setText(self.answers[self.number])
        else:
            self.gb = QGroupBox('Варианты', self)
            self.gb.setStyleSheet('color: rgb(255, 255, 255);')
            self.gb.setFont(QFont(font, 13))
            self.gb.setFixedSize(500, 300)
            self.sp = ['None'] * (len(self.bd[self.number][2]) - 1)
            self.ms = QVBoxLayout(self)
            for i in range(len(self.bd[self.number][2]) - 1):
                self.sp[i] = QRadioButton(self.bd[self.number][2][i], self)
                self.sp[i].setStyleSheet('color: rgb(0, 0, 0);')
                self.sp[i].setFont(QFont(font, 12))
                if self.sp[i].text() == self.answers[self.number]:
                    self.sp[i].setChecked(True)
                self.sp[i].show()
                self.ms.addWidget(self.sp[i])
            self.gb.setLayout(self.ms)
            self.gb.show()
            self.mainstick.addWidget(self.gb, alignment=Qt.AlignCenter)

    def clck(self):
        if self.bd[self.number][1] == 'True':
            for i in self.sp:
                if i.isChecked():
                    self.polz[self.number].setStyleSheet('background: #24a319;')
                    self.answers[self.number] = i.text()
        else:
            if len(self.answer.text()) != 0:
                self.polz[self.number].setStyleSheet('background: #24a319;')
                self.answers[self.number] = self.answer.text()

    def leftb(self):
        self.clck()
        self.right.setEnabled(True)
        self.number -= 1
        self.wh = True
        self.timer.start()
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
        self.clck()
        self.left.setEnabled(True)
        self.number += 1
        self.timer.start()
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
        self.setFixedSize(960, 540)
        self.number = 0
        self.left = QPushButton('<', self)
        self.right = QPushButton('>', self)
        self.left.setFont(QFont('', 20))
        self.right.setFont(QFont('', 20))
        self.left.setFixedSize(30, 200)
        self.right.setFixedSize(30, 200)
        self.left.move(0, 170)
        self.right.move(930, 170)
        self.left.clicked.connect(self.leftb)
        self.right.clicked.connect(self.rightb)
        self.left.setEnabled(False)
        if len(self.bd) == 1:
            self.right.setEnabled(False)
        self.listnumber = QLabel(f'Страница: {self.number + 1}/{len(self.bd)}', self)
        self.listnumber.setFont(QFont(font, 15))
        self.listnumber.move(10, 505)
        self.listnumber.setFixedSize(200, 30)
        self.mainstick = QVBoxLayout(self)
        self.qwestion = QLabel(self.bd[self.number][0], self)
        self.qwestion.setStyleSheet('color: rgb(255, 255, 255);')
        self.qwestion.setFont(QFont(font, 15))
        self.mainstick.addWidget(self.qwestion, alignment=Qt.AlignCenter)
        self.complete = QPushButton('Завершить', self)
        self.complete.setFont(QFont(font, 15))
        self.complete.setFixedSize(150, 30)
        self.complete.move(800, 500)
        self.complete.setStyleSheet('background: #F2E3D5;')
        self.complete.clicked.connect(self.completele)
        self.rezul = QLabel('100', self)
        self.rezul.setFont(QFont(font, 70))
        self.rezul.setStyleSheet('color: #F2E3D5;')
        self.mainstick.addWidget(self.rezul, alignment=Qt.AlignCenter)
        self.rezul.hide()
        self.check()

    def procent(self):
        allans = len(self.answers)
        seclan = 0
        for i in range(len(self.answers)):
            if self.answers[i] == self.yanswers[i]:
                seclan += 1
        return str((seclan * 100) // allans)

    def completele(self):
        global personality_answer
        self.clck()
        if personality_answer == None:
            if None in self.answers:
                self.win = YN()
                self.win.show()
            else:
                self.final()
        else:
            personality_answer = None
            self.final()

    def final(self):
        self.qwestion.deleteLater()
        self.complete.deleteLater()
        self.listnumber.deleteLater()
        try:
            self.answer.deleteLater()
        except Exception:
            self.gb.deleteLater()
        self.left.deleteLater()
        self.right.deleteLater()
        for i in self.polz:
            i.deleteLater()
        self.mainpolz.deleteLater()
        self.fon.setPixmap(QPixmap('add/fon/fon_stud_final.png'))
        self.rezul.show()
        self.rezul.setText(self.procent())
        self.opovesh = QLabel('Покажи учителю свой результат', self)
        self.opovesh.setFixedSize(500, 30)
        self.opovesh.setFont(QFont(font, 25))
        self.opovesh.move(275, 505)
        self.opovesh.setStyleSheet('color: #F2E3D5;')
        if self.sf:
            file = open(self.local, mode='w')
            file.write(f'FINAL\n{self.procent()}')
            file.close()
        self.opovesh.show()


class Create_work(QWidget):
    def __init__(self):
        super().__init__()
        self.UI()

    def UI(self):
        self.setWindowTitle('Lös-учитель')
        self.setFixedSize(1280, 720)
        self.fon = QLabel(self)
        pix = choice(['add/fon/fon4.png', 'add/fon/fon5.png', 'add/fon/fon6.png'])
        self.fon.setPixmap(QPixmap(pix))
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
        self.createqw.setFont(QFont(font, 15))
        self.createqw.setFixedSize(500, 30)
        self.createqw.move(50, 50)
        self.wr = QLabel(' Ответ ученика', self)
        self.wr.setFont(QFont(font, 15))
        self.wr.move(50, 130)
        self.wr.setStyleSheet('color: rgb(255, 255, 255);')
        self.choice1 = QRadioButton('Тестовый ответ', self)
        self.choice1.setFont(QFont(font, 15))
        self.choice1.move(50, 180)
        self.choice1.clicked.connect(self.manychoice)
        self.choice1.setStyleSheet('color: rgb(255, 255, 255);')
        self.choice2 = QRadioButton('Ручной ввод', self)
        self.choice2.setFont(QFont(font, 15))
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
        self.predsmotr.setStyleSheet('background: #F2E3D5;')
        self.predsmotr.clicked.connect(self.smotr)
        self.predsmotr.setEnabled(False)
        self.savetests = QPushButton('Сохранить тест', self)
        self.savetests.setFont(QFont(font, 15))
        self.savetests.setFixedSize(200, 30)
        self.savetests.move(825, 670)
        self.savetests.setStyleSheet('background: #F2E3D5;')
        self.savetests.clicked.connect(self.savetest)
        self.bd = [['None', 'None', 'None']]
        self.create = QPushButton('Добавить в тест', self)
        self.create.setFont(QFont(font, 15))
        self.create.setFixedSize(200, 30)
        self.create.move(1030, 670)
        self.create.clicked.connect(self.adli)
        self.create.setStyleSheet('background: #F2E3D5;')
        self.select = 'None'
        self.deletelist = QPushButton('Удалить страницу', self)
        self.deletelist.setFont(QFont(font, 15))
        self.deletelist.setFixedSize(200, 30)
        self.deletelist.move(415, 670)
        self.deletelist.setStyleSheet('background: #F2E3D5;')
        self.deletelist.setEnabled(False)
        self.deletelist.clicked.connect(self.dellist)

    def dellist(self):
        print(self.bd)
        self.bd.remove(self.bd[self.li - 1])
        print(self.bd)
        print(self.li)
        if self.li > 1:
            self.li += 1
            self.backlist()
        else:
            self.li -= 1
            self.nextlist()
            self.back.setEnabled(False)
            self.back.setStyleSheet('background: #808080;')

    def check_smotr(self):
        if ['None', 'None', 'None'] in self.bd:
            self.predsmotr.setEnabled(False)
        else:
            self.predsmotr.setEnabled(True)

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
        if ['None', 'None', 'None'] in self.bd:
            self.bd = self.bd[:-1]
        name = QFileDialog.getSaveFileName(self, 'Сохраните файл', None, '.los')
        name = name[0] + name[1]
        if name:
            with open(name, mode='w') as file:
                file.write(self.preob())

    def adli(self):
        if self.select != 'None':
            yn = True
            if len(self.createqw.text()) > 0:
                self.bd[self.li - 1][0] = self.createqw.text()
                self.createqw.setStyleSheet('background: rgb(255, 255, 255);')
            else:
                self.createqw.setStyleSheet('background: rgb(255, 150, 150);')
                yn = False
            self.bd[self.li - 1][1] = self.select
            if self.select == 'True':
                sp = list()
                try:
                    for i in self.spisok:
                        if len(i.text()) > 0:
                            sp.append(i.text())
                            i.setStyleSheet('background: rgb(255, 255, 255);')
                        else:
                            i.setStyleSheet('background: rgb(255, 150, 150);')
                            yn = False
                    if len(self.yanswer.text()) > 0:
                        sp.append(self.yanswer.text())
                        self.yanswer.setStyleSheet('background: rgb(255, 255, 255);')
                    else:
                        self.yanswer.setStyleSheet('background: rgb(255, 150, 150);')
                        yn = False
                    self.bd[self.li - 1][2] = sp
                    self.many.setStyleSheet('background: rgb(255, 255, 255);')
                except Exception:
                    self.many.setStyleSheet('background: rgb(255, 150, 150);')
                    yn = False
            elif self.select == 'False':
                if len(self.otvet.text()) > 0:
                    self.bd[self.li - 1][2] = self.otvet.text()
                    self.otvet.setStyleSheet('background: rgb(255, 255, 255);')
                else:
                    self.otvet.setStyleSheet('background: rgb(255, 150, 150);')
                    yn = False
            print(self.bd)
            print('----------')
            if yn:
                self.next.setEnabled(True)
                self.next.setStyleSheet('background: #F2E3D5;')
                if self.li != 1:
                    self.back.setEnabled(True)
                    self.back.setStyleSheet('background: #F2E3D5;')
            else:
                self.bd[self.li - 1] = ['None', 'None', 'None']
            self.predsmotr.setEnabled(True)
            print(self.bd)

    def backlist(self):
        self.li -= 1
        self.check_smotr()
        self.number.setText(f'Страница {self.li}')
        if self.li == 1:
            self.back.setEnabled(False)
            self.back.setStyleSheet('background: #808080;')
        self.next.setEnabled(True)
        self.next.setStyleSheet('background: #F2E3D5;')
        if len(self.bd) == 1:
            self.deletelist.setEnabled(False)
        else:
            self.deletelist.setEnabled(True)
        self.checklist()

    def checklist(self):
        try:
            for i in self.spisok:
                i.hide()
            self.many.hide()
            self.ok.hide()
            self.yanswer.hide()
        except Exception:
            self.otvet.hide()
        if self.bd[self.li - 1][1] == 'True':
            self.createqw.setText(self.bd[self.li - 1][0])
            try:
                self.otvet.hide()
            except Exception:
                pass
            self.many.setText(str(len(self.bd[self.li - 1][2]) - 1))
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
                    self.ch = QLineEdit(self.bd[self.li - 1][2][i], self)
                    self.ch.setFixedSize(400, 25)
                    self.ch.move(830, 50 + i * 50)
                    self.ch.show()
                    self.ch.setFont(QFont(font, 15))
                    self.spisok.append(self.ch)
                self.yanswer.setText(self.bd[self.li - 1][2][-1])
                self.yanswer.setFont(QFont(font, 15))
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
        self.deletelist.setEnabled(True)
        if self.li == len(self.bd):
            self.bd.append(['None', 'None', 'None'])
        self.li += 1
        self.check_smotr()
        self.back.setEnabled(True)
        self.back.setStyleSheet('background: #F2E3D5;')
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
        self.otvet.setFont(QFont(font, 15))
        self.otvet.setFixedSize(300, 25)
        self.otvet.move(300, 180)
        self.otvet.show()

    def manychoice(self):
        self.select = 'True'
        self.many = QLineEdit(self)
        self.many.setPlaceholderText('Количество вопросов')
        self.many.setFont(QFont(font, 15))
        self.many.setFixedSize(300, 25)
        self.many.move(300, 180)
        self.many.show()
        self.ok = QPushButton('Ввод', self)
        self.ok.setFont(QFont(font, 15))
        self.ok.setFixedSize(60, 25)
        self.ok.move(600, 180)
        self.ok.show()
        self.ok.clicked.connect(self.createqwestions)
        self.ok.setStyleSheet('background: #F2E3D5;')

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
                    self.ch.setFont(QFont(font, 15))
                    self.spisok.append(self.ch)
                else:
                    break
            self.yanswer = QLineEdit(self)
            self.yanswer.setPlaceholderText('Правильный ответ')
            self.yanswer.setFixedSize(400, 25)
            self.yanswer.move(830, 550)
            self.yanswer.setFont(QFont(font, 15))
            self.yanswer.show()
        except Exception:
            pass


class Project(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def preob(self, texts):
        texts = texts.split('\n')
        if texts[0] == 'FINAL':
            return texts
        else:
            bd = list()
            for i in texts:
                tx = i.split('~~~~~')
                if tx[1] == 'True':
                    bd.append([tx[0], tx[1], tx[2].split('-----')])
                else:
                    bd.append(tx)
            return bd

    def start_kit(self):
        self.bt1 = QPushButton('Главная', self)
        self.bt1.setFixedSize(200, 30)
        self.bt1.setFont(QFont(font, 15))
        self.bt1.move(40, 610)
        self.bt2 = QPushButton('Ваши данные', self)
        self.bt2.setFont(QFont(font, 15))
        self.bt2.setFixedSize(200, 30)
        self.bt2.move(240, 610)
        self.bt3 = QPushButton('Ошибка?', self)
        self.bt3.setFont(QFont(font, 15))
        self.bt3.setFixedSize(200, 30)
        self.bt3.move(440, 610)
        self.bt_create = QPushButton('Создать', self)
        self.bt_create.setFont(QFont(font, 20))
        self.bt_create.setFixedSize(600, 40)
        self.bt_create.move(40, 645)
        self.bt_create.clicked.connect(self.doit)
        self.main_widget = [self.bt1, self.bt2, self.bt3, self.bt_create]
        for i in self.main_widget:
            i.setStyleSheet('background: #F2E3D5;')
        self.bt1.clicked.connect(self.menu)

    def doit(self):
        if self.bt_create.text().lower() == 'решить':
            name = QFileDialog.getOpenFileName(self, "Выберите файл", ".")
            try:
                file = open(name[0], mode='rt')
                file = self.preob(file.read())
                self.work = Smotr(file, True, name[0])
                self.work.show()
            except Exception:
                pass
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
        self.student.setFont(QFont(font, 20))
        self.student.setFixedSize(300, 50)
        self.student.move(50, 620)
        self.student.clicked.connect(self.stude)
        self.student.setStyleSheet('background: #F2E3D5;')

        self.teacher = QPushButton('Учитель', self)
        self.teacher.setFont(QFont(font, 20))
        self.teacher.setFixedSize(300, 50)
        self.teacher.move(355, 620)
        self.teacher.clicked.connect(self.teach)
        self.teacher.setStyleSheet('background: #F2E3D5;')

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
        self.fon.setPixmap(QPixmap('add/fon/fon2.png'))
        self.bt_create.setText('Решить')
        for i in self.main_widget:
            i.show()
        self.teacher_or_student = True

    def teach(self):
        for i in self.all_widget:
            i.hide()
        self.fon.setPixmap(QPixmap('add/fon/fon3.png'))
        self.bt_create.setText('Создать')
        for i in self.main_widget:
            i.show()
        self.teacher_or_student = True


if __name__ == '__main__':
    app = QApplication(sys.argv)
    font = 'FuturaBookC'
    QFontDatabase.addApplicationFont('FuturaBookC-Italic.ttf')
    progarm = Project()
    progarm.show()
    sys.exit(app.exec())
