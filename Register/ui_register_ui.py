# Form implementation generated from reading ui file 'c:\Users\AlexP\PycharmProjects\pythonProject\Exim_Device_Management_System_V3\Register\ui_register.ui'
#
# Created by: PyQt6 UI code generator 6.7.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayoutWidget = QtWidgets.QWidget(parent=self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(150, 110, 461, 80))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(parent=self.horizontalLayoutWidget)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.txt_firstname = QtWidgets.QLineEdit(parent=self.horizontalLayoutWidget)
        self.txt_firstname.setObjectName("txt_firstname")
        self.horizontalLayout.addWidget(self.txt_firstname)
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(parent=self.centralwidget)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(150, 200, 461, 80))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(parent=self.horizontalLayoutWidget_2)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.txt_surname = QtWidgets.QLineEdit(parent=self.horizontalLayoutWidget_2)
        self.txt_surname.setObjectName("txt_surname")
        self.horizontalLayout_2.addWidget(self.txt_surname)
        self.horizontalLayoutWidget_3 = QtWidgets.QWidget(parent=self.centralwidget)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(150, 290, 461, 80))
        self.horizontalLayoutWidget_3.setObjectName("horizontalLayoutWidget_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_3 = QtWidgets.QLabel(parent=self.horizontalLayoutWidget_3)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)
        self.txt_username = QtWidgets.QLineEdit(parent=self.horizontalLayoutWidget_3)
        self.txt_username.setObjectName("txt_username")
        self.horizontalLayout_3.addWidget(self.txt_username)
        self.horizontalLayoutWidget_4 = QtWidgets.QWidget(parent=self.centralwidget)
        self.horizontalLayoutWidget_4.setGeometry(QtCore.QRect(150, 380, 461, 80))
        self.horizontalLayoutWidget_4.setObjectName("horizontalLayoutWidget_4")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_4)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_4 = QtWidgets.QLabel(parent=self.horizontalLayoutWidget_4)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_4.addWidget(self.label_4)
        self.txt_password = QtWidgets.QLineEdit(parent=self.horizontalLayoutWidget_4)
        self.txt_password.setMaximumSize(QtCore.QSize(397, 22))
        self.txt_password.setObjectName("txt_password")
        self.horizontalLayout_4.addWidget(self.txt_password)
        self.btn_register = QtWidgets.QPushButton(parent=self.centralwidget)
        self.btn_register.setGeometry(QtCore.QRect(150, 460, 221, 81))
        self.btn_register.setObjectName("btn_register")
        self.btn_close = QtWidgets.QPushButton(parent=self.centralwidget)
        self.btn_close.setGeometry(QtCore.QRect(380, 460, 221, 81))
        self.btn_close.setObjectName("btn_close")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Firstname"))
        self.label_2.setText(_translate("MainWindow", "Surname"))
        self.label_3.setText(_translate("MainWindow", "Username"))
        self.label_4.setText(_translate("MainWindow", "Password"))
        self.btn_register.setText(_translate("MainWindow", "Register"))
        self.btn_close.setText(_translate("MainWindow", "Close"))
