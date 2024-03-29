# Form implementation generated from reading ui file '.\ui\finding_user.ui'
#
# Created by: PyQt6 UI code generator 6.6.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Found_Users_Page(object):
    def setupUi(self, Found_Users_Page):
        Found_Users_Page.setObjectName("Found_Users_Page")
        Found_Users_Page.resize(1074, 555)
        self.centralwidget = QtWidgets.QWidget(parent=Found_Users_Page)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayoutWidget_5 = QtWidgets.QWidget(parent=self.centralwidget)
        self.horizontalLayoutWidget_5.setGeometry(QtCore.QRect(440, 460, 169, 31))
        self.horizontalLayoutWidget_5.setObjectName("horizontalLayoutWidget_5")
        self.exit_page = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_5)
        self.exit_page.setContentsMargins(0, 0, 0, 0)
        self.exit_page.setObjectName("exit_page")
        self.apply_button = QtWidgets.QPushButton(parent=self.horizontalLayoutWidget_5)
        self.apply_button.setStyleSheet("color: rgb(0, 0, 127);\n"
"background-color: rgb(255, 255, 255);\n"
"font: 700 9pt \"Segoe UI\";")
        self.apply_button.setObjectName("apply_button")
        self.exit_page.addWidget(self.apply_button)
        self.cancel_button = QtWidgets.QPushButton(parent=self.horizontalLayoutWidget_5)
        self.cancel_button.setStyleSheet("color: rgb(170, 0, 0);\n"
"background-color: rgb(255, 255, 255);\n"
"font: 700 9pt \"Segoe UI\";")
        self.cancel_button.setObjectName("cancel_button")
        self.exit_page.addWidget(self.cancel_button)
        self.title_label = QtWidgets.QLabel(parent=self.centralwidget)
        self.title_label.setGeometry(QtCore.QRect(360, 0, 344, 27))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.title_label.setFont(font)
        self.title_label.setMouseTracking(True)
        self.title_label.setStyleSheet("background-color: qconicalgradient(cx:0, cy:0, angle:135, stop:0 rgba(255, 255, 0, 69), stop:0.375 rgba(255, 255, 0, 69), stop:0.423533 rgba(251, 255, 0, 145), stop:0.45 rgba(247, 255, 0, 208), stop:0.477581 rgba(255, 244, 71, 130), stop:0.518717 rgba(255, 218, 71, 130), stop:0.55 rgba(255, 255, 0, 255), stop:0.57754 rgba(255, 203, 0, 130), stop:0.625 rgba(255, 255, 0, 69), stop:1 rgba(255, 255, 0, 69));\n"
"color: rgb(0, 0, 0);")
        self.title_label.setObjectName("title_label")
        self.found_users_info = QtWidgets.QGroupBox(parent=self.centralwidget)
        self.found_users_info.setGeometry(QtCore.QRect(20, 50, 1031, 391))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(9)
        font.setBold(True)
        font.setItalic(False)
        self.found_users_info.setFont(font)
        self.found_users_info.setStyleSheet("color: rgb(170, 0, 0);\n"
"font: 700 9pt \"Segoe UI\";")
        self.found_users_info.setFlat(False)
        self.found_users_info.setCheckable(False)
        self.found_users_info.setObjectName("found_users_info")
        self.horizontalLayoutWidget = QtWidgets.QWidget(parent=self.found_users_info)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(30, 60, 203, 30))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.name_users = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.name_users.setContentsMargins(0, 0, 0, 0)
        self.name_users.setObjectName("name_users")
        self.ho_ten_label = QtWidgets.QLabel(parent=self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(9)
        font.setBold(True)
        font.setItalic(False)
        self.ho_ten_label.setFont(font)
        self.ho_ten_label.setStyleSheet("color: rgb(0, 0, 0);\n"
"font: 700 9pt \"Segoe UI\";")
        self.ho_ten_label.setObjectName("ho_ten_label")
        self.name_users.addWidget(self.ho_ten_label)
        self.ho_ten_box = QtWidgets.QLineEdit(parent=self.horizontalLayoutWidget)
        self.ho_ten_box.setStyleSheet("color: rgb(0, 0, 0);\n"
"font: 9pt \"Segoe UI\";")
        self.ho_ten_box.setObjectName("ho_ten_box")
        self.name_users.addWidget(self.ho_ten_box)
        self.horizontalLayoutWidget_3 = QtWidgets.QWidget(parent=self.found_users_info)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(30, 120, 982, 28))
        self.horizontalLayoutWidget_3.setObjectName("horizontalLayoutWidget_3")
        self.age_range = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.age_range.setContentsMargins(0, 0, 0, 0)
        self.age_range.setObjectName("age_range")
        self.age_measures = QtWidgets.QLabel(parent=self.horizontalLayoutWidget_3)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(9)
        font.setBold(True)
        font.setItalic(False)
        self.age_measures.setFont(font)
        self.age_measures.setStyleSheet("color: rgb(0, 0, 0);\n"
"font: 700 9pt \"Segoe UI\";")
        self.age_measures.setObjectName("age_measures")
        self.age_range.addWidget(self.age_measures)
        self.age_1 = QtWidgets.QRadioButton(parent=self.horizontalLayoutWidget_3)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        self.age_1.setFont(font)
        self.age_1.setStyleSheet("color: rgb(0, 0, 0);\n"
"font: 9pt \"Segoe UI\";")
        self.age_1.setObjectName("age_1")
        self.age_range.addWidget(self.age_1)
        self.age_2 = QtWidgets.QRadioButton(parent=self.horizontalLayoutWidget_3)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        self.age_2.setFont(font)
        self.age_2.setStyleSheet("color: rgb(0, 0, 0);\n"
"font: 9pt \"Segoe UI\";")
        self.age_2.setObjectName("age_2")
        self.age_range.addWidget(self.age_2)
        self.age_3 = QtWidgets.QRadioButton(parent=self.horizontalLayoutWidget_3)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        self.age_3.setFont(font)
        self.age_3.setStyleSheet("color: rgb(0, 0, 0);\n"
"font: 9pt \"Segoe UI\";")
        self.age_3.setObjectName("age_3")
        self.age_range.addWidget(self.age_3)
        self.age_4 = QtWidgets.QRadioButton(parent=self.horizontalLayoutWidget_3)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        self.age_4.setFont(font)
        self.age_4.setStyleSheet("color: rgb(0, 0, 0);\n"
"font: 9pt \"Segoe UI\";")
        self.age_4.setObjectName("age_4")
        self.age_range.addWidget(self.age_4)
        self.age_5 = QtWidgets.QRadioButton(parent=self.horizontalLayoutWidget_3)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        self.age_5.setFont(font)
        self.age_5.setStyleSheet("color: rgb(0, 0, 0);\n"
"font: 9pt \"Segoe UI\";")
        self.age_5.setObjectName("age_5")
        self.age_range.addWidget(self.age_5)
        self.age_6 = QtWidgets.QRadioButton(parent=self.horizontalLayoutWidget_3)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        self.age_6.setFont(font)
        self.age_6.setStyleSheet("color: rgb(0, 0, 0);\n"
"font: 9pt \"Segoe UI\";")
        self.age_6.setObjectName("age_6")
        self.age_range.addWidget(self.age_6)
        self.age_7 = QtWidgets.QRadioButton(parent=self.horizontalLayoutWidget_3)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        self.age_7.setFont(font)
        self.age_7.setStyleSheet("color: rgb(0, 0, 0);\n"
"font: 9pt \"Segoe UI\";")
        self.age_7.setObjectName("age_7")
        self.age_range.addWidget(self.age_7)
        self.age_8 = QtWidgets.QRadioButton(parent=self.horizontalLayoutWidget_3)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        self.age_8.setFont(font)
        self.age_8.setStyleSheet("color: rgb(0, 0, 0);\n"
"font: 9pt \"Segoe UI\";")
        self.age_8.setObjectName("age_8")
        self.age_range.addWidget(self.age_8)
        self.age_9 = QtWidgets.QRadioButton(parent=self.horizontalLayoutWidget_3)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        self.age_9.setFont(font)
        self.age_9.setStyleSheet("color: rgb(0, 0, 0);\n"
"font: 9pt \"Segoe UI\";")
        self.age_9.setObjectName("age_9")
        self.age_range.addWidget(self.age_9)
        self.age_10 = QtWidgets.QRadioButton(parent=self.horizontalLayoutWidget_3)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        self.age_10.setFont(font)
        self.age_10.setStyleSheet("color: rgb(0, 0, 0);\n"
"font: 9pt \"Segoe UI\";")
        self.age_10.setObjectName("age_10")
        self.age_range.addWidget(self.age_10)
        self.age_11 = QtWidgets.QRadioButton(parent=self.horizontalLayoutWidget_3)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        self.age_11.setFont(font)
        self.age_11.setStyleSheet("color: rgb(0, 0, 0);\n"
"font: 9pt \"Segoe UI\";")
        self.age_11.setObjectName("age_11")
        self.age_range.addWidget(self.age_11)
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(parent=self.found_users_info)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(580, 60, 132, 30))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.sex_users = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.sex_users.setContentsMargins(0, 0, 0, 0)
        self.sex_users.setObjectName("sex_users")
        self.gioi_tinh_label = QtWidgets.QLabel(parent=self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(9)
        font.setBold(True)
        font.setItalic(False)
        self.gioi_tinh_label.setFont(font)
        self.gioi_tinh_label.setStyleSheet("color: rgb(0, 0, 0);\n"
"font: 700 9pt \"Segoe UI\";")
        self.gioi_tinh_label.setObjectName("gioi_tinh_label")
        self.sex_users.addWidget(self.gioi_tinh_label)
        self.gioi_tinh = QtWidgets.QComboBox(parent=self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        self.gioi_tinh.setFont(font)
        self.gioi_tinh.setStyleSheet("color: rgb(0, 0, 0);\n"
"font: 9pt \"Segoe UI\";")
        self.gioi_tinh.setInsertPolicy(QtWidgets.QComboBox.InsertPolicy.NoInsert)
        self.gioi_tinh.setSizeAdjustPolicy(QtWidgets.QComboBox.SizeAdjustPolicy.AdjustToContents)
        self.gioi_tinh.setObjectName("gioi_tinh")
        self.gioi_tinh.addItem("")
        self.gioi_tinh.addItem("")
        icon = QtGui.QIcon.fromTheme("accessories-calculator")
        self.gioi_tinh.addItem(icon, "")
        self.gioi_tinh.setItemText(2, "")
        self.sex_users.addWidget(self.gioi_tinh)
        self.horizontalLayoutWidget_4 = QtWidgets.QWidget(parent=self.found_users_info)
        self.horizontalLayoutWidget_4.setGeometry(QtCore.QRect(30, 240, 441, 121))
        self.horizontalLayoutWidget_4.setObjectName("horizontalLayoutWidget_4")
        self.face_feature = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_4)
        self.face_feature.setContentsMargins(0, 0, 0, 0)
        self.face_feature.setObjectName("face_feature")
        self.face_characteristics = QtWidgets.QLabel(parent=self.horizontalLayoutWidget_4)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(9)
        font.setBold(True)
        font.setItalic(False)
        self.face_characteristics.setFont(font)
        self.face_characteristics.setStyleSheet("color: rgb(0, 0, 0);\n"
"font: 700 9pt \"Segoe UI\";")
        self.face_characteristics.setObjectName("face_characteristics")
        self.face_feature.addWidget(self.face_characteristics)
        self.info_face = QtWidgets.QTextEdit(parent=self.horizontalLayoutWidget_4)
        self.info_face.setStyleSheet("color: rgb(0, 0, 0);\n"
"font: 9pt \"Segoe UI\";")
        self.info_face.setOverwriteMode(True)
        self.info_face.setObjectName("info_face")
        self.face_feature.addWidget(self.info_face)
        self.horizontalLayoutWidget_6 = QtWidgets.QWidget(parent=self.found_users_info)
        self.horizontalLayoutWidget_6.setGeometry(QtCore.QRect(580, 290, 366, 31))
        self.horizontalLayoutWidget_6.setObjectName("horizontalLayoutWidget_6")
        self.pic = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_6)
        self.pic.setContentsMargins(0, 0, 0, 0)
        self.pic.setObjectName("pic")
        self.upload_avatar_label = QtWidgets.QLabel(parent=self.horizontalLayoutWidget_6)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(9)
        font.setBold(True)
        font.setItalic(False)
        self.upload_avatar_label.setFont(font)
        self.upload_avatar_label.setStyleSheet("color: rgb(0, 0, 0);\n"
"font: 700 9pt \"Segoe UI\";")
        self.upload_avatar_label.setObjectName("upload_avatar_label")
        self.pic.addWidget(self.upload_avatar_label)
        self.pushButton = QtWidgets.QPushButton(parent=self.horizontalLayoutWidget_6)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("color: rgb(0, 0, 0);\n"
"font: 9pt \"Segoe UI\";")
        self.pushButton.setObjectName("pushButton")
        self.pic.addWidget(self.pushButton)
        self.horizontalLayoutWidget_7 = QtWidgets.QWidget(parent=self.found_users_info)
        self.horizontalLayoutWidget_7.setGeometry(QtCore.QRect(30, 180, 164, 30))
        self.horizontalLayoutWidget_7.setObjectName("horizontalLayoutWidget_7")
        self.nation_place = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_7)
        self.nation_place.setSizeConstraint(QtWidgets.QLayout.SizeConstraint.SetFixedSize)
        self.nation_place.setContentsMargins(0, 0, 0, 0)
        self.nation_place.setSpacing(2)
        self.nation_place.setObjectName("nation_place")
        self.nation = QtWidgets.QLabel(parent=self.horizontalLayoutWidget_7)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(9)
        font.setBold(True)
        font.setItalic(False)
        self.nation.setFont(font)
        self.nation.setStyleSheet("color: rgb(0, 0, 0);\n"
"font: 700 9pt \"Segoe UI\";")
        self.nation.setObjectName("nation")
        self.nation_place.addWidget(self.nation)
        self.nation_box = QtWidgets.QComboBox(parent=self.horizontalLayoutWidget_7)
        self.nation_box.setStyleSheet("color: rgb(0, 0, 0);\n"
"font: 9pt \"Segoe UI\";")
        self.nation_box.setInsertPolicy(QtWidgets.QComboBox.InsertPolicy.InsertAtBottom)
        self.nation_box.setSizeAdjustPolicy(QtWidgets.QComboBox.SizeAdjustPolicy.AdjustToContents)
        self.nation_box.setDuplicatesEnabled(True)
        self.nation_box.setObjectName("nation_box")
        self.nation_box.addItem("")
        self.nation_place.addWidget(self.nation_box)
        self.horizontalLayoutWidget_9 = QtWidgets.QWidget(parent=self.found_users_info)
        self.horizontalLayoutWidget_9.setGeometry(QtCore.QRect(220, 180, 269, 30))
        self.horizontalLayoutWidget_9.setObjectName("horizontalLayoutWidget_9")
        self.city_place = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_9)
        self.city_place.setSizeConstraint(QtWidgets.QLayout.SizeConstraint.SetFixedSize)
        self.city_place.setContentsMargins(0, 0, 0, 0)
        self.city_place.setSpacing(2)
        self.city_place.setObjectName("city_place")
        self.city = QtWidgets.QLabel(parent=self.horizontalLayoutWidget_9)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(9)
        font.setBold(True)
        font.setItalic(False)
        self.city.setFont(font)
        self.city.setStyleSheet("color: rgb(0, 0, 0);\n"
"font: 700 9pt \"Segoe UI\";")
        self.city.setObjectName("city")
        self.city_place.addWidget(self.city)
        self.city_box = QtWidgets.QComboBox(parent=self.horizontalLayoutWidget_9)
        self.city_box.setStyleSheet("color: rgb(0, 0, 0);\n"
"font: 9pt \"Segoe UI\";")
        self.city_box.setInsertPolicy(QtWidgets.QComboBox.InsertPolicy.NoInsert)
        self.city_box.setSizeAdjustPolicy(QtWidgets.QComboBox.SizeAdjustPolicy.AdjustToContents)
        self.city_box.setObjectName("city_box")
        self.city_place.addWidget(self.city_box)
        self.horizontalLayoutWidget_10 = QtWidgets.QWidget(parent=self.found_users_info)
        self.horizontalLayoutWidget_10.setGeometry(QtCore.QRect(790, 180, 205, 30))
        self.horizontalLayoutWidget_10.setObjectName("horizontalLayoutWidget_10")
        self.ward_place = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_10)
        self.ward_place.setSizeConstraint(QtWidgets.QLayout.SizeConstraint.SetFixedSize)
        self.ward_place.setContentsMargins(0, 0, 0, 0)
        self.ward_place.setSpacing(2)
        self.ward_place.setObjectName("ward_place")
        self.ward = QtWidgets.QLabel(parent=self.horizontalLayoutWidget_10)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(9)
        font.setBold(True)
        font.setItalic(False)
        self.ward.setFont(font)
        self.ward.setStyleSheet("color: rgb(0, 0, 0);\n"
"font: 700 9pt \"Segoe UI\";")
        self.ward.setObjectName("ward")
        self.ward_place.addWidget(self.ward)
        self.ward_box = QtWidgets.QComboBox(parent=self.horizontalLayoutWidget_10)
        self.ward_box.setStyleSheet("color: rgb(0, 0, 0);\n"
"font: 9pt \"Segoe UI\";")
        self.ward_box.setInsertPolicy(QtWidgets.QComboBox.InsertPolicy.NoInsert)
        self.ward_box.setSizeAdjustPolicy(QtWidgets.QComboBox.SizeAdjustPolicy.AdjustToContents)
        self.ward_box.setObjectName("ward_box")
        self.ward_place.addWidget(self.ward_box)
        self.horizontalLayoutWidget_8 = QtWidgets.QWidget(parent=self.found_users_info)
        self.horizontalLayoutWidget_8.setGeometry(QtCore.QRect(530, 180, 223, 30))
        self.horizontalLayoutWidget_8.setObjectName("horizontalLayoutWidget_8")
        self.district_place = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_8)
        self.district_place.setSizeConstraint(QtWidgets.QLayout.SizeConstraint.SetFixedSize)
        self.district_place.setContentsMargins(0, 0, 0, 0)
        self.district_place.setSpacing(2)
        self.district_place.setObjectName("district_place")
        self.district = QtWidgets.QLabel(parent=self.horizontalLayoutWidget_8)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(9)
        font.setBold(True)
        font.setItalic(False)
        self.district.setFont(font)
        self.district.setStyleSheet("color: rgb(0, 0, 0);\n"
"font: 700 9pt \"Segoe UI\";")
        self.district.setObjectName("district")
        self.district_place.addWidget(self.district)
        self.district_box = QtWidgets.QComboBox(parent=self.horizontalLayoutWidget_8)
        self.district_box.setEnabled(True)
        self.district_box.setStyleSheet("color: rgb(0, 0, 0);\n"
"font: 9pt \"Segoe UI\";")
        self.district_box.setInsertPolicy(QtWidgets.QComboBox.InsertPolicy.NoInsert)
        self.district_box.setSizeAdjustPolicy(QtWidgets.QComboBox.SizeAdjustPolicy.AdjustToContents)
        self.district_box.setObjectName("district_box")
        self.district_place.addWidget(self.district_box)
        Found_Users_Page.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=Found_Users_Page)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1074, 25))
        self.menubar.setObjectName("menubar")
        Found_Users_Page.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=Found_Users_Page)
        self.statusbar.setObjectName("statusbar")
        Found_Users_Page.setStatusBar(self.statusbar)

        self.retranslateUi(Found_Users_Page)
        QtCore.QMetaObject.connectSlotsByName(Found_Users_Page)

    def retranslateUi(self, Found_Users_Page):
        _translate = QtCore.QCoreApplication.translate
        Found_Users_Page.setWindowTitle(_translate("Found_Users_Page", "MainWindow"))
        self.apply_button.setText(_translate("Found_Users_Page", "APPLY"))
        self.cancel_button.setText(_translate("Found_Users_Page", "CANCEL"))
        self.title_label.setText(_translate("Found_Users_Page", "<html><head/><body><p align=\"center\">ỨNG DỤNG TÌM NGƯỜI MUỐN GẶP</p></body></html>"))
        self.found_users_info.setTitle(_translate("Found_Users_Page", "THÔNG TIN NGƯỜI CẦN TÌM"))
        self.ho_ten_label.setText(_translate("Found_Users_Page", "Họ và Tên"))
        self.ho_ten_box.setPlaceholderText(_translate("Found_Users_Page", "Họ và Tên"))
        self.age_measures.setText(_translate("Found_Users_Page", "Mốc tuổi"))
        self.age_1.setText(_translate("Found_Users_Page", "0 - 10"))
        self.age_2.setText(_translate("Found_Users_Page", "10 - 20"))
        self.age_3.setText(_translate("Found_Users_Page", "21 - 30"))
        self.age_4.setText(_translate("Found_Users_Page", "31 - 40"))
        self.age_5.setText(_translate("Found_Users_Page", "41 - 50"))
        self.age_6.setText(_translate("Found_Users_Page", "51 - 60"))
        self.age_7.setText(_translate("Found_Users_Page", "61 - 70"))
        self.age_8.setText(_translate("Found_Users_Page", "71 - 80"))
        self.age_9.setText(_translate("Found_Users_Page", "81 - 90"))
        self.age_10.setText(_translate("Found_Users_Page", "91 - 100"))
        self.age_11.setText(_translate("Found_Users_Page", "101 - 110"))
        self.gioi_tinh_label.setText(_translate("Found_Users_Page", "Giới tính"))
        self.gioi_tinh.setItemText(0, _translate("Found_Users_Page", "Nam"))
        self.gioi_tinh.setItemText(1, _translate("Found_Users_Page", "Nữ"))
        self.face_characteristics.setText(_translate("Found_Users_Page", "Đặc điểm nhận dạng"))
        self.info_face.setDocumentTitle(_translate("Found_Users_Page", "Đặc điểm gương mặt"))
        self.info_face.setPlaceholderText(_translate("Found_Users_Page", "Nêu các đặc điểm gương mặt của bạn"))
        self.upload_avatar_label.setText(_translate("Found_Users_Page", "Upload hình ảnh cá nhân"))
        self.pushButton.setText(_translate("Found_Users_Page", "Download"))
        self.nation.setText(_translate("Found_Users_Page", "Quốc gia"))
        self.nation_box.setPlaceholderText(_translate("Found_Users_Page", "Quốc gia"))
        self.nation_box.setItemText(0, _translate("Found_Users_Page", "Việt Nam"))
        self.city.setText(_translate("Found_Users_Page", "Thành phố / Tỉnh"))
        self.city_box.setPlaceholderText(_translate("Found_Users_Page", "Thành phố / Tỉnh"))
        self.ward.setText(_translate("Found_Users_Page", "Phường / Xã"))
        self.ward_box.setPlaceholderText(_translate("Found_Users_Page", "Phường / Xã"))
        self.district.setText(_translate("Found_Users_Page", "Quận / Huyện"))
        self.district_box.setPlaceholderText(_translate("Found_Users_Page", "Quận / Huyện"))
