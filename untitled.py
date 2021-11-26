# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Sample_synth(object):
    def setupUi(self, Sample_synth):
        Sample_synth.setObjectName("Sample_synth")
        Sample_synth.setWindowModality(QtCore.Qt.ApplicationModal)
        Sample_synth.resize(640, 480)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Sample_synth.sizePolicy().hasHeightForWidth())
        Sample_synth.setSizePolicy(sizePolicy)
        self.horizontalLayoutWidget = QtWidgets.QWidget(Sample_synth)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 340, 621, 131))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.layoutWidget = QtWidgets.QWidget(Sample_synth)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 240, 621, 91))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_1 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.label_1.setFont(font)
        self.label_1.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_1.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_1.setAlignment(QtCore.Qt.AlignCenter)
        self.label_1.setObjectName("label_1")
        self.verticalLayout.addWidget(self.label_1)
        self.reverb_dial = QtWidgets.QDial(self.layoutWidget)
        self.reverb_dial.setMaximum(127)
        self.reverb_dial.setWrapping(False)
        self.reverb_dial.setNotchTarget(2.7)
        self.reverb_dial.setNotchesVisible(True)
        self.reverb_dial.setObjectName("reverb_dial")
        self.verticalLayout.addWidget(self.reverb_dial)
        self.horizontalLayout_2.addLayout(self.verticalLayout)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_4 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.label_4.setFont(font)
        self.label_4.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_4.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_4.addWidget(self.label_4)
        self.vibrato_dial = QtWidgets.QDial(self.layoutWidget)
        self.vibrato_dial.setMaximum(127)
        self.vibrato_dial.setWrapping(False)
        self.vibrato_dial.setNotchTarget(2.7)
        self.vibrato_dial.setNotchesVisible(True)
        self.vibrato_dial.setObjectName("vibrato_dial")
        self.verticalLayout_4.addWidget(self.vibrato_dial)
        self.horizontalLayout_2.addLayout(self.verticalLayout_4)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_5 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.label_5.setFont(font)
        self.label_5.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_5.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_5.addWidget(self.label_5)
        self.pan_dial = QtWidgets.QDial(self.layoutWidget)
        self.pan_dial.setMaximum(127)
        self.pan_dial.setSingleStep(1)
        self.pan_dial.setProperty("value", 65)
        self.pan_dial.setWrapping(False)
        self.pan_dial.setNotchTarget(2.7)
        self.pan_dial.setNotchesVisible(True)
        self.pan_dial.setObjectName("pan_dial")
        self.verticalLayout_5.addWidget(self.pan_dial)
        self.horizontalLayout_2.addLayout(self.verticalLayout_5)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label_6 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.label_6.setFont(font)
        self.label_6.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_6.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_6.addWidget(self.label_6)
        self.expression_dial = QtWidgets.QDial(self.layoutWidget)
        self.expression_dial.setMaximum(127)
        self.expression_dial.setWrapping(False)
        self.expression_dial.setNotchTarget(2.7)
        self.expression_dial.setNotchesVisible(True)
        self.expression_dial.setObjectName("expression_dial")
        self.verticalLayout_6.addWidget(self.expression_dial)
        self.horizontalLayout_2.addLayout(self.verticalLayout_6)
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.label_7 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.label_7.setFont(font)
        self.label_7.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_7.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_7.addWidget(self.label_7)
        self.sustain_dial = QtWidgets.QDial(self.layoutWidget)
        self.sustain_dial.setMaximum(127)
        self.sustain_dial.setWrapping(False)
        self.sustain_dial.setNotchTarget(2.7)
        self.sustain_dial.setNotchesVisible(True)
        self.sustain_dial.setObjectName("sustain_dial")
        self.verticalLayout_7.addWidget(self.sustain_dial)
        self.horizontalLayout_2.addLayout(self.verticalLayout_7)
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.label_8 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.label_8.setFont(font)
        self.label_8.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_8.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.verticalLayout_8.addWidget(self.label_8)
        self.volume_dial = QtWidgets.QDial(self.layoutWidget)
        self.volume_dial.setMaximum(127)
        self.volume_dial.setWrapping(False)
        self.volume_dial.setNotchTarget(2.7)
        self.volume_dial.setNotchesVisible(True)
        self.volume_dial.setObjectName("volume_dial")
        self.verticalLayout_8.addWidget(self.volume_dial)
        self.horizontalLayout_2.addLayout(self.verticalLayout_8)
        self.verticalLayout_9 = QtWidgets.QVBoxLayout()
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.label_9 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.label_9.setFont(font)
        self.label_9.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_9.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setObjectName("label_9")
        self.verticalLayout_9.addWidget(self.label_9)
        self.chorus_dial = QtWidgets.QDial(self.layoutWidget)
        self.chorus_dial.setMaximum(127)
        self.chorus_dial.setWrapping(False)
        self.chorus_dial.setNotchTarget(2.7)
        self.chorus_dial.setNotchesVisible(True)
        self.chorus_dial.setObjectName("chorus_dial")
        self.verticalLayout_9.addWidget(self.chorus_dial)
        self.horizontalLayout_2.addLayout(self.verticalLayout_9)
        self.layoutWidget1 = QtWidgets.QWidget(Sample_synth)
        self.layoutWidget1.setGeometry(QtCore.QRect(370, 10, 258, 221))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.label = QtWidgets.QLabel(self.layoutWidget1)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout_10.addWidget(self.label)
        self.fonts_list = QtWidgets.QListWidget(self.layoutWidget1)
        self.fonts_list.setObjectName("fonts_list")
        self.verticalLayout_10.addWidget(self.fonts_list)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.add_to_db = QtWidgets.QPushButton(self.layoutWidget1)
        self.add_to_db.setObjectName("add_to_db")
        self.horizontalLayout_3.addWidget(self.add_to_db)
        self.delete_from_db = QtWidgets.QPushButton(self.layoutWidget1)
        self.delete_from_db.setObjectName("delete_from_db")
        self.horizontalLayout_3.addWidget(self.delete_from_db)
        self.verticalLayout_10.addLayout(self.horizontalLayout_3)

        self.retranslateUi(Sample_synth)
        QtCore.QMetaObject.connectSlotsByName(Sample_synth)

    def retranslateUi(self, Sample_synth):
        _translate = QtCore.QCoreApplication.translate
        Sample_synth.setWindowTitle(_translate("Sample_synth", "Form"))
        self.label_1.setText(_translate("Sample_synth", "Reverb"))
        self.label_4.setText(_translate("Sample_synth", "Vibrato"))
        self.label_5.setText(_translate("Sample_synth", "Pan"))
        self.label_6.setText(_translate("Sample_synth", "Expression"))
        self.label_7.setText(_translate("Sample_synth", "Sustain"))
        self.label_8.setText(_translate("Sample_synth", "Volume"))
        self.label_9.setText(_translate("Sample_synth", "Chorus"))
        self.label.setText(_translate("Sample_synth", "Музыкальный шрифт"))
        self.add_to_db.setText(_translate("Sample_synth", "Загрузить в бд"))
        self.delete_from_db.setText(_translate("Sample_synth", "Выгрузить из бд"))
