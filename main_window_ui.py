# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '\\edu.local\public\studenthomes\22200322\Desktop\db_2\design\main_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1032, 685)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.leftTable = QtWidgets.QTableView(self.centralwidget)
        self.leftTable.setGeometry(QtCore.QRect(10, 10, 431, 471))
        self.leftTable.setObjectName("leftTable")
        self.rightTable = QtWidgets.QTableView(self.centralwidget)
        self.rightTable.setGeometry(QtCore.QRect(590, 10, 431, 471))
        self.rightTable.setObjectName("rightTable")
        self.send_to_right = QtWidgets.QPushButton(self.centralwidget)
        self.send_to_right.setGeometry(QtCore.QRect(470, 100, 91, 81))
        self.send_to_right.setStyleSheet("QPushButton:hover {\n"
"    background-color: #ffdbcc;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #fcb9aa;\n"
"}\n"
"QPushButton {\n"
"    ;\n"
"    background-color: rgb(49, 223, 211);\n"
"    border-radius: 31px;\n"
"}")
        self.send_to_right.setObjectName("send_to_right")
        self.send_to_left = QtWidgets.QPushButton(self.centralwidget)
        self.send_to_left.setGeometry(QtCore.QRect(470, 260, 91, 81))
        self.send_to_left.setStyleSheet("QPushButton:hover {\n"
"    background-color: #ffdbcc;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #fcb9aa;\n"
"}\n"
"QPushButton {\n"
"    ;\n"
"    background-color: rgb(49, 223, 211);\n"
"    border-radius: 31px;\n"
"}")
        self.send_to_left.setObjectName("send_to_left")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(230, 500, 571, 111))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.addButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.addButton.sizePolicy().hasHeightForWidth())
        self.addButton.setSizePolicy(sizePolicy)
        self.addButton.setStyleSheet("QPushButton:hover {\n"
"    background-color: #ffdbcc;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #fcb9aa;\n"
"}\n"
"QPushButton {\n"
"    ;\n"
"    background-color: rgb(49, 223, 211);\n"
"    border-radius: 31px;\n"
"}")
        self.addButton.setObjectName("addButton")
        self.horizontalLayout.addWidget(self.addButton)
        spacerItem = QtWidgets.QSpacerItem(65, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.delButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.delButton.sizePolicy().hasHeightForWidth())
        self.delButton.setSizePolicy(sizePolicy)
        self.delButton.setStyleSheet("QPushButton:hover {\n"
"    background-color: #ffdbcc;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #fcb9aa;\n"
"}\n"
"QPushButton {\n"
"    ;\n"
"    background-color: rgb(49, 223, 211);\n"
"    border-radius: 31px;\n"
"}")
        self.delButton.setObjectName("delButton")
        self.horizontalLayout.addWidget(self.delButton)
        spacerItem1 = QtWidgets.QSpacerItem(65, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.editButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.editButton.sizePolicy().hasHeightForWidth())
        self.editButton.setSizePolicy(sizePolicy)
        self.editButton.setStyleSheet("QPushButton:hover {\n"
"    background-color: #ffdbcc;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #fcb9aa;\n"
"}\n"
"QPushButton {\n"
"    ;\n"
"    background-color: rgb(49, 223, 211);\n"
"    border-radius: 31px;\n"
"}")
        self.editButton.setObjectName("editButton")
        self.horizontalLayout.addWidget(self.editButton)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.send_to_right.setText(_translate("MainWindow", "=>"))
        self.send_to_left.setText(_translate("MainWindow", "<="))
        self.addButton.setText(_translate("MainWindow", "Добавить"))
        self.delButton.setText(_translate("MainWindow", "Удалить"))
        self.editButton.setText(_translate("MainWindow", "Изменить"))
