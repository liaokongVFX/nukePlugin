# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MovToExcel.ui'
#
# Created: Mon Mar 20 13:57:48 2017
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_MovToExcel(object):
    def setupUi(self, MovToExcel):
        MovToExcel.setObjectName("MovToExcel")
        MovToExcel.resize(572, 123)
        self.verticalLayout_2 = QtGui.QVBoxLayout(MovToExcel)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtGui.QLabel(MovToExcel)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.path_line = QtGui.QLineEdit(MovToExcel)
        self.path_line.setObjectName("path_line")
        self.horizontalLayout.addWidget(self.path_line)
        self.path_btn = QtGui.QToolButton(MovToExcel)
        self.path_btn.setMinimumSize(QtCore.QSize(30, 20))
        self.path_btn.setObjectName("path_btn")
        self.horizontalLayout.addWidget(self.path_btn)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtGui.QLabel(MovToExcel)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.excel_path_line = QtGui.QLineEdit(MovToExcel)
        self.excel_path_line.setObjectName("excel_path_line")
        self.horizontalLayout_2.addWidget(self.excel_path_line)
        self.excel_path_btn = QtGui.QToolButton(MovToExcel)
        self.excel_path_btn.setMinimumSize(QtCore.QSize(30, 20))
        self.excel_path_btn.setObjectName("excel_path_btn")
        self.horizontalLayout_2.addWidget(self.excel_path_btn)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3.addLayout(self.verticalLayout)
        self.to_excel_btn = QtGui.QPushButton(MovToExcel)
        self.to_excel_btn.setMinimumSize(QtCore.QSize(0, 57))
        self.to_excel_btn.setObjectName("to_excel_btn")
        self.horizontalLayout_3.addWidget(self.to_excel_btn)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.label_3 = QtGui.QLabel(MovToExcel)
        self.label_3.setMinimumSize(QtCore.QSize(0, 0))
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.verticalLayout_2.addWidget(self.label_3)
        self.progressBar = QtGui.QProgressBar(MovToExcel)
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.verticalLayout_2.addWidget(self.progressBar)

        self.retranslateUi(MovToExcel)
        QtCore.QMetaObject.connectSlotsByName(MovToExcel)

    def retranslateUi(self, MovToExcel):
        MovToExcel.setWindowTitle(QtGui.QApplication.translate("MovToExcel", "项目Excel生成工具", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("MovToExcel", "素材路径: ", None, QtGui.QApplication.UnicodeUTF8))
        self.path_btn.setText(QtGui.QApplication.translate("MovToExcel", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("MovToExcel", "生成位置: ", None, QtGui.QApplication.UnicodeUTF8))
        self.excel_path_btn.setText(QtGui.QApplication.translate("MovToExcel", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.to_excel_btn.setText(QtGui.QApplication.translate("MovToExcel", "生成Excel", None, QtGui.QApplication.UnicodeUTF8))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MovToExcel = QtGui.QDialog()
    ui = Ui_MovToExcel()
    ui.setupUi(MovToExcel)
    MovToExcel.show()
    sys.exit(app.exec_())

