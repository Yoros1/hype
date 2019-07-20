# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './ui/login_form.ui'
#
# Created by: PyQt5 UI code generator 5.12.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_login_form(object):
    def setupUi(self, login_form):
        login_form.setObjectName("login_form")
        login_form.setWindowModality(QtCore.Qt.ApplicationModal)
        login_form.resize(800, 300)
        login_form.setMinimumSize(QtCore.QSize(800, 300))
        login_form.setMaximumSize(QtCore.QSize(800, 300))
        login_form.setStyleSheet("background-color:white;\n"
"")
        login_form.setSizeGripEnabled(False)
        login_form.setModal(True)
        self.btn_enter_acnt = QtWidgets.QPushButton(login_form)
        self.btn_enter_acnt.setEnabled(True)
        self.btn_enter_acnt.setGeometry(QtCore.QRect(337, 222, 171, 41))
        font = QtGui.QFont()
        font.setFamily("IRANSans")
        font.setPointSize(11)
        font.setKerning(False)
        self.btn_enter_acnt.setFont(font)
        self.btn_enter_acnt.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_enter_acnt.setMouseTracking(True)
        self.btn_enter_acnt.setFocusPolicy(QtCore.Qt.TabFocus)
        self.btn_enter_acnt.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.btn_enter_acnt.setStyleSheet("border-radius: 5px;\n"
"background-color:rgb(58, 178, 151);")
        self.btn_enter_acnt.setFlat(False)
        self.btn_enter_acnt.setObjectName("btn_enter_acnt")
        self.btn_cancel_login = QtWidgets.QPushButton(login_form)
        self.btn_cancel_login.setEnabled(True)
        self.btn_cancel_login.setGeometry(QtCore.QRect(237, 222, 81, 41))
        font = QtGui.QFont()
        font.setFamily("IRANSans")
        font.setPointSize(11)
        font.setKerning(False)
        self.btn_cancel_login.setFont(font)
        self.btn_cancel_login.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_cancel_login.setMouseTracking(True)
        self.btn_cancel_login.setFocusPolicy(QtCore.Qt.TabFocus)
        self.btn_cancel_login.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.btn_cancel_login.setStyleSheet("border-radius: 5px;\n"
"background-color:rgb(178, 55, 77);")
        self.btn_cancel_login.setFlat(False)
        self.btn_cancel_login.setObjectName("btn_cancel_login")
        self.btn_sign_up = QtWidgets.QPushButton(login_form)
        self.btn_sign_up.setEnabled(True)
        self.btn_sign_up.setGeometry(QtCore.QRect(170, 232, 51, 20))
        font = QtGui.QFont()
        font.setFamily("B Yekan")
        font.setPointSize(11)
        font.setKerning(False)
        self.btn_sign_up.setFont(font)
        self.btn_sign_up.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_sign_up.setMouseTracking(True)
        self.btn_sign_up.setFocusPolicy(QtCore.Qt.TabFocus)
        self.btn_sign_up.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.btn_sign_up.setStyleSheet("border:0px;\n"
"color:blue;")
        self.btn_sign_up.setFlat(False)
        self.btn_sign_up.setObjectName("btn_sign_up")
        self.gbox_user_pass = QtWidgets.QGroupBox(login_form)
        self.gbox_user_pass.setGeometry(QtCore.QRect(170, 48, 461, 141))
        font = QtGui.QFont()
        font.setFamily("IRANSans")
        font.setPointSize(9)
        self.gbox_user_pass.setFont(font)
        self.gbox_user_pass.setStyleSheet("border: 1px solid rgb(58, 178, 151);")
        self.gbox_user_pass.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTop|QtCore.Qt.AlignTrailing)
        self.gbox_user_pass.setObjectName("gbox_user_pass")
        self.lineEdit_password = QtWidgets.QLineEdit(self.gbox_user_pass)
        self.lineEdit_password.setGeometry(QtCore.QRect(40, 81, 261, 35))
        self.lineEdit_password.setMinimumSize(QtCore.QSize(0, 35))
        self.lineEdit_password.setStyleSheet("border:solid 5px;\n"
"background-color:rgb(204, 204, 204);\n"
"border-radius:5px;\n"
"font: 11pt \"B Homa\";")
        self.lineEdit_password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_password.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_password.setObjectName("lineEdit_password")
        self.lineEdit_username = QtWidgets.QLineEdit(self.gbox_user_pass)
        self.lineEdit_username.setGeometry(QtCore.QRect(40, 36, 261, 35))
        self.lineEdit_username.setMinimumSize(QtCore.QSize(0, 35))
        self.lineEdit_username.setStyleSheet("border:solid 5px;\n"
"background-color:rgb(204, 204, 204);\n"
"border-radius:5px;\n"
"font: 10pt \"B Homa\";")
        self.lineEdit_username.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_username.setObjectName("lineEdit_username")
        self.label = QtWidgets.QLabel(self.gbox_user_pass)
        self.label.setGeometry(QtCore.QRect(311, 44, 71, 21))
        font = QtGui.QFont()
        font.setFamily("IRANSans")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setStyleSheet("font: 10pt \"IRANSans\";\n"
"border: 0px;")
        self.label.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label.setLineWidth(0)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.gbox_user_pass)
        self.label_2.setGeometry(QtCore.QRect(307, 88, 121, 21))
        font = QtGui.QFont()
        font.setFamily("IRANSans")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("font: 10pt \"IRANSans\";\n"
"border: 0px;")
        self.label_2.setObjectName("label_2")
        self.btn_request_temp_pass = QtWidgets.QPushButton(login_form)
        self.btn_request_temp_pass.setEnabled(True)
        self.btn_request_temp_pass.setGeometry(QtCore.QRect(520, 232, 111, 20))
        font = QtGui.QFont()
        font.setFamily("B Yekan")
        font.setPointSize(10)
        font.setKerning(False)
        self.btn_request_temp_pass.setFont(font)
        self.btn_request_temp_pass.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_request_temp_pass.setMouseTracking(True)
        self.btn_request_temp_pass.setFocusPolicy(QtCore.Qt.TabFocus)
        self.btn_request_temp_pass.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.btn_request_temp_pass.setStyleSheet("border:0px;\n"
"color:blue;")
        self.btn_request_temp_pass.setFlat(False)
        self.btn_request_temp_pass.setObjectName("btn_request_temp_pass")

        self.retranslateUi(login_form)
        QtCore.QMetaObject.connectSlotsByName(login_form)
        login_form.setTabOrder(self.lineEdit_username, self.lineEdit_password)
        login_form.setTabOrder(self.lineEdit_password, self.btn_enter_acnt)
        login_form.setTabOrder(self.btn_enter_acnt, self.btn_request_temp_pass)
        login_form.setTabOrder(self.btn_request_temp_pass, self.btn_sign_up)
        login_form.setTabOrder(self.btn_sign_up, self.btn_cancel_login)

    def retranslateUi(self, login_form):
        _translate = QtCore.QCoreApplication.translate
        login_form.setWindowTitle(_translate("login_form", "ورود به سیستم"))
        self.btn_enter_acnt.setText(_translate("login_form", "ورود به حساب کاربری"))
        self.btn_cancel_login.setText(_translate("login_form", "انصراف"))
        self.btn_sign_up.setText(_translate("login_form", "ثبت نام"))
        self.gbox_user_pass.setTitle(_translate("login_form", "شماره تلفن همراه و رمز عبور خود را وارد کنید "))
        self.lineEdit_username.setPlaceholderText(_translate("login_form", "حروف انگلیسی یا عدد ..."))
        self.label.setText(_translate("login_form", "تلفن همراه :"))
        self.label_2.setText(_translate("login_form", "رمز عبور / رمز موقت :"))
        self.btn_request_temp_pass.setText(_translate("login_form", "درخواست رمز موقت"))


