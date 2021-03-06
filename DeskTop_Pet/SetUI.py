# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Temp\SetUI.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Setting(object):
    def setupUi(self, Setting):
        Setting.setObjectName("Setting")
        Setting.resize(300, 300)
        Setting.setMinimumSize(QtCore.QSize(300, 300))
        Setting.setMaximumSize(QtCore.QSize(300, 300))
        Setting.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        Setting.setModal(True)
        self.Background = QtWidgets.QLabel(Setting)
        self.Background.setGeometry(QtCore.QRect(0, 0, 300, 300))
        self.Background.setMinimumSize(QtCore.QSize(300, 300))
        self.Background.setMaximumSize(QtCore.QSize(300, 300))
        self.Background.setStyleSheet("")
        self.Background.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.Background.setFrameShadow(QtWidgets.QFrame.Plain)
        self.Background.setText("")
        self.Background.setPixmap(QtGui.QPixmap(":/newPrefix/Resource/SettingWin.png"))
        self.Background.setScaledContents(False)
        self.Background.setIndent(0)
        self.Background.setObjectName("Background")
        self.Setface = QtWidgets.QLabel(Setting)
        self.Setface.setGeometry(QtCore.QRect(27, 89, 46, 45))
        self.Setface.setText("")
        self.Setface.setPixmap(QtGui.QPixmap(":/newPrefix/Resource/SetCharface.png"))
        self.Setface.setObjectName("Setface")
        self.getName = QtWidgets.QTextBrowser(Setting)
        self.getName.setGeometry(QtCore.QRect(28, 163, 67, 20))
        font = QtGui.QFont()
        font.setFamily("카페24 고운밤")
        self.getName.setFont(font)
        self.getName.setStyleSheet("background-color: rgb(247, 231, 224)")
        self.getName.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.getName.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.getName.setReadOnly(False)
        self.getName.setObjectName("getName")
        self.Facechange = QtWidgets.QPushButton(Setting)
        self.Facechange.setGeometry(QtCore.QRect(76, 91, 41, 41))
        font = QtGui.QFont()
        font.setFamily("카페24 고운밤")
        font.setPointSize(8)
        self.Facechange.setFont(font)
        self.Facechange.setStyleSheet("background-color: rgb(247, 231, 224)")
        self.Facechange.setObjectName("Facechange")
        self.gifChangeL = QtWidgets.QLabel(Setting)
        self.gifChangeL.setGeometry(QtCore.QRect(134, 97, 34, 39))
        self.gifChangeL.setText("")
        self.gifChangeL.setPixmap(QtGui.QPixmap(":/newPrefix/Resource/SetChargif.png"))
        self.gifChangeL.setObjectName("gifChangeL")
        self.gifChangeR = QtWidgets.QLabel(Setting)
        self.gifChangeR.setGeometry(QtCore.QRect(177, 97, 34, 39))
        self.gifChangeR.setText("")
        self.gifChangeR.setPixmap(QtGui.QPixmap(":/newPrefix/Resource/SetChargif.png"))
        self.gifChangeR.setObjectName("gifChangeR")
        self.gifChangeC = QtWidgets.QLabel(Setting)
        self.gifChangeC.setGeometry(QtCore.QRect(221, 97, 34, 39))
        self.gifChangeC.setText("")
        self.gifChangeC.setPixmap(QtGui.QPixmap(":/newPrefix/Resource/SetChargif.png"))
        self.gifChangeC.setObjectName("gifChangeC")
        self.BgifCL = QtWidgets.QPushButton(Setting)
        self.BgifCL.setGeometry(QtCore.QRect(131, 152, 41, 21))
        font = QtGui.QFont()
        font.setFamily("카페24 고운밤")
        font.setPointSize(8)
        self.BgifCL.setFont(font)
        self.BgifCL.setStyleSheet("background-color: rgb(252, 227, 216)")
        self.BgifCL.setObjectName("BgifCL")
        self.BgifCR = QtWidgets.QPushButton(Setting)
        self.BgifCR.setGeometry(QtCore.QRect(174, 152, 41, 21))
        font = QtGui.QFont()
        font.setFamily("카페24 고운밤")
        font.setPointSize(8)
        self.BgifCR.setFont(font)
        self.BgifCR.setStyleSheet("background-color: rgb(252, 227, 216)")
        self.BgifCR.setObjectName("BgifCR")
        self.BgifCC = QtWidgets.QPushButton(Setting)
        self.BgifCC.setGeometry(QtCore.QRect(218, 152, 41, 21))
        font = QtGui.QFont()
        font.setFamily("카페24 고운밤")
        font.setPointSize(8)
        self.BgifCC.setFont(font)
        self.BgifCC.setStyleSheet("background-color: rgb(252, 227, 216)")
        self.BgifCC.setObjectName("BgifCC")
        self.BgifCL_2 = QtWidgets.QPushButton(Setting)
        self.BgifCL_2.setGeometry(QtCore.QRect(208, 183, 71, 21))
        font = QtGui.QFont()
        font.setFamily("카페24 고운밤")
        font.setPointSize(8)
        self.BgifCL_2.setFont(font)
        self.BgifCL_2.setAutoFillBackground(False)
        self.BgifCL_2.setStyleSheet("background-color: rgb(248, 207, 210)")
        self.BgifCL_2.setObjectName("BgifCL_2")
        self.label = QtWidgets.QLabel(Setting)
        self.label.setGeometry(QtCore.QRect(50, 227, 41, 16))
        font = QtGui.QFont()
        font.setFamily("카페24 고운밤")
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.BgifCL_3 = QtWidgets.QPushButton(Setting)
        self.BgifCL_3.setGeometry(QtCore.QRect(130, 227, 61, 41))
        font = QtGui.QFont()
        font.setFamily("카페24 고운밤")
        font.setPointSize(8)
        self.BgifCL_3.setFont(font)
        self.BgifCL_3.setStyleSheet("background-color: rgb(252, 227, 216)")
        self.BgifCL_3.setObjectName("BgifCL_3")
        self.BgifCL_4 = QtWidgets.QPushButton(Setting)
        self.BgifCL_4.setGeometry(QtCore.QRect(205, 227, 61, 41))
        font = QtGui.QFont()
        font.setFamily("카페24 고운밤")
        font.setPointSize(8)
        self.BgifCL_4.setFont(font)
        self.BgifCL_4.setStyleSheet("background-color: rgb(252, 227, 216);\n"
"color: rgb(207, 0, 0)")
        self.BgifCL_4.setObjectName("BgifCL_4")

        self.retranslateUi(Setting)
        self.Facechange.clicked.connect(Setting.loadimage4)
        self.BgifCR.clicked.connect(Setting.loadimage2)
        self.BgifCL.clicked.connect(Setting.loadimage)
        self.BgifCC.clicked.connect(Setting.loadimage3)
        self.BgifCL_2.clicked.connect(Setting.Showcheakbox)
        self.BgifCL_3.clicked.connect(Setting.Showmeinfo)
        self.BgifCL_4.clicked.connect(Setting.Showcheakbox)
        QtCore.QMetaObject.connectSlotsByName(Setting)

    def retranslateUi(self, Setting):
        _translate = QtCore.QCoreApplication.translate
        Setting.setWindowTitle(_translate("Setting", "Setting"))
        self.Facechange.setText(_translate("Setting", "변경"))
        self.BgifCL.setText(_translate("Setting", "변경"))
        self.BgifCR.setText(_translate("Setting", "변경"))
        self.BgifCC.setText(_translate("Setting", "변경"))
        self.BgifCL_2.setText(_translate("Setting", "적용하기"))
        self.BgifCL_3.setText(_translate("Setting", "도움말"))
        self.BgifCL_4.setText(_translate("Setting", "초기화"))
import SetRes


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Setting = QtWidgets.QWidget()
    ui = Ui_Setting()
    ui.setupUi(Setting)
    Setting.show()
    sys.exit(app.exec_())
