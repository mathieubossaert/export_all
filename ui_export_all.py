# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_export_all.ui'
#
# Created: Fri May 16 20:47:58 2014
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Export_all(object):
    def setupUi(self, Export_all):
        Export_all.setObjectName(_fromUtf8("Export_all"))
        Export_all.resize(402, 108)
        self.buttonBox = QtGui.QDialogButtonBox(Export_all)
        self.buttonBox.setGeometry(QtCore.QRect(40, 70, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.lineEdit = QtGui.QLineEdit(Export_all)
        self.lineEdit.setGeometry(QtCore.QRect(11, 34, 311, 27))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.label = QtGui.QLabel(Export_all)
        self.label.setGeometry(QtCore.QRect(11, 11, 155, 17))
        self.label.setObjectName(_fromUtf8("label"))
        self.toolButton_Browse = QtGui.QToolButton(Export_all)
        self.toolButton_Browse.setGeometry(QtCore.QRect(330, 34, 70, 25))
        self.toolButton_Browse.setObjectName(_fromUtf8("toolButton_Browse"))

        self.retranslateUi(Export_all)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), Export_all.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), Export_all.reject)
        QtCore.QMetaObject.connectSlotsByName(Export_all)

    def retranslateUi(self, Export_all):
        Export_all.setWindowTitle(_translate("Export_all", "Export_all", None))
        self.label.setText(_translate("Export_all", "Choisissez le dossier cible", None))
        self.toolButton_Browse.setText(_translate("Export_all", "Parcourir", None))

