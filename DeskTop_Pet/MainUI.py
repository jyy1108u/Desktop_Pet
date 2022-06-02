# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Temp\MainUI.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainGame(object):
    def setupUi(self, MainGame):
        MainGame.setObjectName("MainGame")
        MainGame.resize(400, 300)
        MainGame.setMinimumSize(QtCore.QSize(400, 300))
        MainGame.setMaximumSize(QtCore.QSize(400, 300))
        palette = QtGui.QPalette()
        MainGame.setPalette(palette)
        MainGame.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        MainGame.setMouseTracking(False)
        MainGame.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        MainGame.setAutoFillBackground(False)
        MainGame.setStyleSheet("")
        MainGame.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        MainGame.setAnimated(True)
        MainGame.setDocumentMode(False)
        MainGame.setUnifiedTitleAndToolBarOnMac(False)
        self.Gamemain = QtWidgets.QWidget(MainGame)
        self.Gamemain.setStyleSheet("windowtitle: rgb(255, 170, 0)")
        self.Gamemain.setObjectName("Gamemain")
        self.Setting = QtWidgets.QPushButton(self.Gamemain)
        self.Setting.setGeometry(QtCore.QRect(360, 10, 31, 31))
        self.Setting.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Setting.setAutoFillBackground(False)
        self.Setting.setStyleSheet("border-image: url(:/newPrefix/Resource/setting1.png)")
        self.Setting.setText("")
        self.Setting.setObjectName("Setting")
        self.background = QtWidgets.QLabel(self.Gamemain)
        self.background.setGeometry(QtCore.QRect(0, 0, 400, 300))
        self.background.setText("")
        self.background.setPixmap(QtGui.QPixmap(":/newPrefix/Resource/background.png"))
        self.background.setObjectName("background")
        self.CharName = QtWidgets.QLabel(self.Gamemain)
        self.CharName.setGeometry(QtCore.QRect(91, 20, 64, 15))
        font = QtGui.QFont()
        font.setFamily("카페24 고운밤")
        self.CharName.setFont(font)
        self.CharName.setObjectName("CharName")
        self.CharFace = QtWidgets.QLabel(self.Gamemain)
        self.CharFace.setGeometry(QtCore.QRect(13, 13, 46, 45))
        self.CharFace.setText("")
        self.CharFace.setPixmap(QtGui.QPixmap(":/newPrefix/Resource/charImage.png"))
        self.CharFace.setObjectName("CharFace")
        self.H1 = QtWidgets.QLabel(self.Gamemain)
        self.H1.setGeometry(QtCore.QRect(10, 70, 15, 13))
        self.H1.setText("")
        self.H1.setPixmap(QtGui.QPixmap(":/newPrefix/Resource/trans.png"))
        self.H1.setObjectName("H1")
        self.H2 = QtWidgets.QLabel(self.Gamemain)
        self.H2.setGeometry(QtCore.QRect(30, 70, 15, 13))
        self.H2.setText("")
        self.H2.setPixmap(QtGui.QPixmap(":/newPrefix/Resource/trans.png"))
        self.H2.setObjectName("H2")
        self.H3 = QtWidgets.QLabel(self.Gamemain)
        self.H3.setGeometry(QtCore.QRect(50, 70, 15, 13))
        self.H3.setText("")
        self.H3.setPixmap(QtGui.QPixmap(":/newPrefix/Resource/trans.png"))
        self.H3.setObjectName("H3")
        self.H4 = QtWidgets.QLabel(self.Gamemain)
        self.H4.setGeometry(QtCore.QRect(70, 70, 15, 13))
        self.H4.setText("")
        self.H4.setPixmap(QtGui.QPixmap(":/newPrefix/Resource/trans.png"))
        self.H4.setObjectName("H4")
        self.H5 = QtWidgets.QLabel(self.Gamemain)
        self.H5.setGeometry(QtCore.QRect(90, 70, 15, 13))
        self.H5.setText("")
        self.H5.setPixmap(QtGui.QPixmap(":/newPrefix/Resource/trans.png"))
        self.H5.setObjectName("H5")
        self.background.raise_()
        self.Setting.raise_()
        self.CharName.raise_()
        self.CharFace.raise_()
        self.H1.raise_()
        self.H2.raise_()
        self.H3.raise_()
        self.H4.raise_()
        self.H5.raise_()
        MainGame.setCentralWidget(self.Gamemain)

        self.retranslateUi(MainGame)
        self.Setting.clicked.connect(MainGame.ShowSetting)
        QtCore.QMetaObject.connectSlotsByName(MainGame)

    def retranslateUi(self, MainGame):
        _translate = QtCore.QCoreApplication.translate
        MainGame.setWindowTitle(_translate("MainGame", "DesktopLF"))
        MainGame.setStatusTip(_translate("MainGame", "what"))
        self.CharName.setText(_translate("MainGame", "Charname"))
import MainRes

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainGame = QtWidgets.QMainWindow()
    ui = Ui_MainGame()
    ui.setupUi(MainGame)
    MainGame.show()
    sys.exit(app.exec_())
