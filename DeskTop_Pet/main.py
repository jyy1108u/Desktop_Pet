import sys; import random
from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QDialog, QFileDialog
from PyQt5.QtGui import QMovie, QCursor, QPixmap
from PyQt5.QtCore import Qt

import MainUI
from MainUI import Ui_MainGame
from SetUI import Ui_Setting

class Char(QtWidgets.QMainWindow):
    def __init__(self, xy, size=1.0, on_top=False):
        super(Char, self).__init__()
        self.timer = QtCore.QTimer(self)
        self.timer2 = QtCore.QTimer(self)

        self.Charname = "Name"

        self.img_pathL = "Resource/Default_L.gif"
        self.img_pathR = "Resource/Default_R.gif"
        self.img_pathC = "Resource/Default_C.gif"
        self.img_pathF = "Resource/Default_charImage.png"
        self.xy = xy
        self.to_xy = [0, 0]
        self.direction = [0,0]
        self.size = size
        self.on_top = on_top
        self.localPos = None

        self.setupUi()
        self.show()


    def setupUi(self):
        centralWidget = QtWidgets.QWidget(self)
        self.setCentralWidget(centralWidget)

        flags = QtCore.Qt.WindowFlags(QtCore.Qt.FramelessWindowHint | QtCore.Qt.WindowStaysOnTopHint if self.on_top else QtCore.Qt.FramelessWindowHint)
        self.setWindowFlags(flags)
        self.setAttribute(QtCore.Qt.WA_NoSystemBackground, True)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground, True)

        self.label = QtWidgets.QLabel(centralWidget)
        self.movie = QMovie(self.img_pathL)
        self.label.setMovie(self.movie)
        self.movie.start()
        self.movie.stop()

        w = int(self.movie.frameRect().size().width() * self.size)
        h = int(self.movie.frameRect().size().height() * self.size)
        self.movie.setScaledSize(QtCore.QSize(w, h))
        self.movie.start()

        self.setGeometry(self.xy[0], self.xy[1], w, h)

    # 캐릭터 임의로 이동
    def walk(self):
        self.timer = QtCore.QTimer(self)
        self.timer.timeout.connect(self.walkHandler)
        self.timer2.timeout.connect(self.walkHandler2)
        self.timer.start(10)
        self.timer2.start(100)

    def walkHandler2(self):
        self.to_xy[0] = random.randrange(500, 1800)
        self.to_xy[1] = random.randrange(400, 900)

    def walkHandler(self):

        if self.xy[0] >= 1800:
            self.direction[0] = 0

            self.movie.stop()
            self.movie.setFileName(self.img_pathL)
            self.movie.start()

        elif self.xy[0] < 0:
            self.direction[0] = 1

            self.movie.stop()
            self.movie.setFileName(self.img_pathR)
            self.movie.start()

        if self.direction[0] == 0: #왼쪽
            self.xy[0] -= random.randrange(1, 3)
        else:                   #오른쪽
            self.xy[0] += random.randrange(1, 3)

        if self.xy[1] >= self.to_xy[1]:
            self.direction[1] = 0
        elif self.xy[1] < 0:
            self.direction[1] = 1

        if self.direction[1] == 0:
            self.xy[1] -= random.randrange(0, 2)
        else:
            self.xy[1] += random.randrange(0, 2)

        self.move(*self.xy)

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.m_flag = True
            self.m_Position = event.globalPos() - self.pos()  # Get the position of the mouse relative to the window
            event.accept()
            self.setCursor(QCursor(Qt.OpenHandCursor))  # Change mouse icon

            self.movie.stop()
            self.movie.setFileName(self.img_pathC)
            self.movie.start()

            self.timer.stop()


    def mouseMoveEvent(self, QMouseEvent):
        if Qt.LeftButton and self.m_flag:
            self.move(QMouseEvent.globalPos() - self.m_Position)  # Change window position
            self.xy[0] = QMouseEvent.globalX()
            self.xy[1] = QMouseEvent.globalY()

            QMouseEvent.accept()

    def mouseReleaseEvent(self, QMouseEvent):
        self.m_flag = False
        self.setCursor(QCursor(Qt.ArrowCursor))

        self.movie.stop()
        if self.direction[0] == 0:
            self.movie.setFileName(self.img_pathL)
        elif self.direction[0] == 1:
            self.movie.setFileName(self.img_pathR)
        self.movie.start()

        self.timer.start()
        self.timer2.start()


class SetWindow(QDialog, Ui_Setting):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.gifChangeL.setPixmap(QtGui.QPixmap(s.img_pathL))
        self.gifChangeR.setPixmap(QtGui.QPixmap(s.img_pathR))
        self.gifChangeC.setPixmap(QtGui.QPixmap(s.img_pathC))
        self.Setface.setPixmap(QtGui.QPixmap(s.img_pathF))

        self.NotSelected = "Resource/trans.png"

        self.filenameL = "0"
        self.filenameR = "0"
        self.filenameC = "0"
        self.filenameF = "0"

        self.show()
        s.timer.stop()
        s.movie.stop() #일단 일시정지

    def loadimage(self, event):
        window = QFileDialog()
        self.filenameL = window.getOpenFileName(self, 'Open File', '', 'image File(*.gif)')
        self.gifChangeL.setPixmap(QtGui.QPixmap(self.filenameL[0]))

    def loadimage2(self, event):
        window = QFileDialog()
        self.filenameR = window.getOpenFileName(self, 'Open File', '', 'image File(*.gif)')
        self.gifChangeR.setPixmap(QtGui.QPixmap(self.filenameR[0]))

    def loadimage3(self, event):
        window = QFileDialog()
        self.filenameC = window.getOpenFileName(self, 'Open File', '', 'image File(*.gif)')
        self.gifChangeC.setPixmap(QtGui.QPixmap(self.filenameC[0]))

    def loadimage4(self, event):
        window = QFileDialog()
        self.filenameF = window.getOpenFileName(self, 'Open File', '', 'image File(*.png)')
        self.Setface.setPixmap(QtGui.QPixmap(self.filenameF[0]))


    def Showcheakbox(self):
        if self.filenameL[0] != "":
            s.img_pathL = self.filenameL[0]
        else: s.img_pathL = self.NotSelected

        if self.filenameR[0] != "":
            s.img_pathR = self.filenameR[0]
        else: s.img_pathR = self.NotSelected

        if self.filenameC[0] != "":
            s.img_pathC = self.filenameC[0]
        else: s.img_pathC = self.NotSelected

        if self.filenameF[0] != "":
            s.img_pathF = self.filenameF[0]
        else: s.img_pathF = self.NotSelected

        self.text = self.getName.toPlainText()

        if self.text == "":
            myWindow.CharName.setText(myWindow.name)
            myWindow.CharName.setAlignment(QtCore.Qt.AlignCenter)
        else:
            myWindow.name = self.text
            myWindow.CharName.setText(myWindow.name)
            myWindow.CharName.setAlignment(QtCore.Qt.AlignCenter)

        s.movie.setFileName(s.img_pathL)
        s.movie.start()
        s.movie.stop()

    def Showmeinfo(self):
        pass

    def closeEvent(self, a0: QtGui.QCloseEvent):
        myWindow.CharFace.setPixmap(QtGui.QPixmap(s.img_pathF))
        s.timer.start()
        s.movie.start() #타이머/무비 다시 시작


class mainWindow(QMainWindow, Ui_MainGame):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.name = "란국"
        self.CharName.setAlignment(QtCore.Qt.AlignCenter)
        self.CharName.setText(self.name)
        self.show()

    def ShowSetting(self):
        setWindow = SetWindow()
        setWindow.exec_()

    def closeEvent(self, event):
        quit()



if __name__ == "__main__":
    app = QApplication(sys.argv)

    s = Char(xy=[1800, 500], on_top=True)
    s.walk()
    myWindow = mainWindow()
    myWindow.show()
    app.exec_()



