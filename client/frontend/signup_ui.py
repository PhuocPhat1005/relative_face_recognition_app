# Form implementation generated from reading ui file '.\ui\signup.ui'
#
# Created by: PyQt6 UI code generator 6.6.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Sign_Up_Page(object):
    def setupUi(self, Sign_Up_Page):
        Sign_Up_Page.setObjectName("Sign_Up_Page")
        Sign_Up_Page.resize(1074, 555)
        self.centralwidget = QtWidgets.QWidget(parent=Sign_Up_Page)
        self.centralwidget.setObjectName("centralwidget")
        self.info_account = QtWidgets.QGroupBox(parent=self.centralwidget)
        self.info_account.setGeometry(QtCore.QRect(310, 90, 461, 318))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(9)
        font.setBold(True)
        font.setItalic(False)
        self.info_account.setFont(font)
        self.info_account.setStyleSheet("color: rgb(170, 0, 0);\n"
"border-color: rgb(255, 255, 127);\n"
"font: 700 9pt \"Segoe UI\";")
        self.info_account.setObjectName("info_account")
        self.verticalLayoutWidget = QtWidgets.QWidget(parent=self.info_account)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(40, 60, 181, 171))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(parent=self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(9)
        font.setBold(True)
        font.setItalic(False)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(0, 0, 0);\n"
"font: 700 9pt \"Segoe UI\";")
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(parent=self.verticalLayoutWidget)
        self.label_2.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.label_4 = QtWidgets.QLabel(parent=self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(9)
        font.setBold(True)
        font.setItalic(False)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)
        self.label_5 = QtWidgets.QLabel(parent=self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(9)
        font.setBold(True)
        font.setItalic(False)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_5.setObjectName("label_5")
        self.verticalLayout.addWidget(self.label_5)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(parent=self.info_account)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(220, 60, 201, 171))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.account_name = QtWidgets.QLineEdit(parent=self.verticalLayoutWidget_2)
        self.account_name.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);\n"
"font: 9pt \"Segoe UI\";")
        self.account_name.setObjectName("account_name")
        self.verticalLayout_2.addWidget(self.account_name)
        self.account_email = QtWidgets.QLineEdit(parent=self.verticalLayoutWidget_2)
        self.account_email.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);\n"
"font: 9pt \"Segoe UI\";")
        self.account_email.setObjectName("account_email")
        self.verticalLayout_2.addWidget(self.account_email)
        self.account_password = QtWidgets.QLineEdit(parent=self.verticalLayoutWidget_2)
        self.account_password.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);\n"
"font: 9pt \"Segoe UI\";")
        self.account_password.setObjectName("account_password")
        self.verticalLayout_2.addWidget(self.account_password)
        self.confirm_password = QtWidgets.QLineEdit(parent=self.verticalLayoutWidget_2)
        self.confirm_password.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);\n"
"font: 9pt \"Segoe UI\";")
        self.confirm_password.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        self.confirm_password.setObjectName("confirm_password")
        self.verticalLayout_2.addWidget(self.confirm_password)
        self.horizontalLayoutWidget = QtWidgets.QWidget(parent=self.info_account)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(40, 230, 381, 28))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_6 = QtWidgets.QLabel(parent=self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(9)
        font.setBold(True)
        font.setItalic(False)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("color: rgb(0, 0, 0);\n"
"font: 700 9pt \"Segoe UI\";")
        self.label_6.setObjectName("label_6")
        self.horizontalLayout.addWidget(self.label_6)
        self.check_robot = QtWidgets.QCheckBox(parent=self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(9)
        font.setBold(True)
        font.setItalic(False)
        self.check_robot.setFont(font)
        self.check_robot.setStyleSheet("color: rgb(170, 0, 0);\n"
"font: 700 9pt \"Segoe UI\";")
        self.check_robot.setObjectName("check_robot")
        self.horizontalLayout.addWidget(self.check_robot)
        self.title_label = QtWidgets.QLabel(parent=self.centralwidget)
        self.title_label.setGeometry(QtCore.QRect(370, 20, 344, 27))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.title_label.setFont(font)
        self.title_label.setMouseTracking(True)
        self.title_label.setStyleSheet("background-color: qconicalgradient(cx:0, cy:0, angle:135, stop:0 rgba(255, 255, 0, 69), stop:0.375 rgba(255, 255, 0, 69), stop:0.423533 rgba(251, 255, 0, 145), stop:0.45 rgba(247, 255, 0, 208), stop:0.477581 rgba(255, 244, 71, 130), stop:0.518717 rgba(255, 218, 71, 130), stop:0.55 rgba(255, 255, 0, 255), stop:0.57754 rgba(255, 203, 0, 130), stop:0.625 rgba(255, 255, 0, 69), stop:1 rgba(255, 255, 0, 69));\n"
"color: rgb(0, 0, 0);")
        self.title_label.setObjectName("title_label")
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(parent=self.centralwidget)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(460, 420, 169, 31))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.apply_button = QtWidgets.QPushButton(parent=self.horizontalLayoutWidget_2)
        self.apply_button.setStyleSheet("color: rgb(0, 0, 127);\n"
"background-color: rgb(255, 255, 255);\n"
"font: 700 9pt \"Segoe UI\";")
        self.apply_button.setObjectName("apply_button")
        self.horizontalLayout_4.addWidget(self.apply_button)
        self.cancel_button = QtWidgets.QPushButton(parent=self.horizontalLayoutWidget_2)
        self.cancel_button.setStyleSheet("color: rgb(170, 0, 0);\n"
"background-color: rgb(255, 255, 255);\n"
"font: 700 9pt \"Segoe UI\";")
        self.cancel_button.setObjectName("cancel_button")
        self.horizontalLayout_4.addWidget(self.cancel_button)
        Sign_Up_Page.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=Sign_Up_Page)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1074, 25))
        self.menubar.setObjectName("menubar")
        Sign_Up_Page.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=Sign_Up_Page)
        self.statusbar.setObjectName("statusbar")
        Sign_Up_Page.setStatusBar(self.statusbar)

        self.retranslateUi(Sign_Up_Page)
        QtCore.QMetaObject.connectSlotsByName(Sign_Up_Page)

    def retranslateUi(self, Sign_Up_Page):
        _translate = QtCore.QCoreApplication.translate
        Sign_Up_Page.setWindowTitle(_translate("Sign_Up_Page", "MainWindow"))
        self.info_account.setTitle(_translate("Sign_Up_Page", "THÔNG TIN ĐĂNG KÝ TÀI KHOẢN"))
        self.label.setText(_translate("Sign_Up_Page", "<html><head/><body><p><span style=\" font-weight:700;\">TÊN ĐĂNG KÝ</span></p></body></html>"))
        self.label_2.setText(_translate("Sign_Up_Page", "<html><head/><body><p>EMAIL ĐĂNG KÝ</p></body></html>"))
        self.label_4.setText(_translate("Sign_Up_Page", "<html><head/><body><p><span style=\" font-weight:700;\">NHẬP MẬT KHẨU</span></p></body></html>"))
        self.label_5.setText(_translate("Sign_Up_Page", "<html><head/><body><p><span style=\" font-weight:700;\">XÁC NHẬN MẬT KHẨU</span></p></body></html>"))
        self.account_name.setPlaceholderText(_translate("Sign_Up_Page", "Ten Dang Ky"))
        self.account_email.setPlaceholderText(_translate("Sign_Up_Page", "Tai khoan Email"))
        self.account_password.setPlaceholderText(_translate("Sign_Up_Page", "Password"))
        self.confirm_password.setPlaceholderText(_translate("Sign_Up_Page", "Confirm Password"))
        self.label_6.setText(_translate("Sign_Up_Page", "<html><head/><body><p>BẠN CÓ PHẢI <span style=\" color:#aa0000;\">ROBOT</span> KHÔNG ?</p></body></html>"))
        self.check_robot.setText(_translate("Sign_Up_Page", "Not Robot"))
        self.title_label.setText(_translate("Sign_Up_Page", "<html><head/><body><p align=\"center\">ỨNG DỤNG TÌM NGƯỜI MUỐN GẶP</p></body></html>"))
        self.apply_button.setText(_translate("Sign_Up_Page", "APPLY"))
        self.cancel_button.setText(_translate("Sign_Up_Page", "CANCEL"))