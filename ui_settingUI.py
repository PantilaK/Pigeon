# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'settingUIpuhKZz.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QLabel,
    QLineEdit, QPushButton, QScrollArea, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(520, 565)
        Form.setStyleSheet(u"background-color: #464d55;")
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.widget = QWidget(Form)
        self.widget.setObjectName(u"widget")
        self.widget.setStyleSheet(u"QWidget {\n"
"  background-color: #fff;\n"
"}\n"
"QWidget#widget{\n"
"  border-radius: 12px;\n"
"}\n"
"QComboBox{\n"
"   background-color: #fff;\n"
"  font-weight: 600;\n"
"   border: 1px solid #ced4da;\n"
"   border-radius: 5px;\n"
"   color: #464d55;\n"
"   padding-left: 15px;\n"
"}\n"
"QComboBox::placeholder{\n"
"  color: #767e89;\n"
"}\n"
"QComboBox::on{\n"
"   border: 3px solid #d0e3ff;\n"
"}\n"
"QComboBox::drop-down{\n"
"   border: 0px;\n"
"}\n"
"QComboBox::down-arrow{\n"
"   image: url(:/dropdown/dropdownPNG.png);\n"
"   width: 12px;\n"
"   height: 12px;\n"
"   margin-right: 15px;\n"
"}\n"
"QComboBox QListView{\n"
"  color: #464d55;\n"
"  font-weight: 600;\n"
"   border: 1px solid rgba(0,0,0, 10%);\n"
"   padding: 5px;\n"
"   background-color: #fff;\n"
"   outline: 0px;\n"
"}\n"
"QComboBox QListView:item {\n"
"   padding-left: 10px;\n"
"   background-color: #fff;\n"
"}\n"
"\n"
"QLabel {\n"
"  color: #464d55;\n"
"  font-weight: 600;\n"
"}\n"
"QLabel#usernameErrorLabel, #passwordErrorLabel {\n"
"  color: "
                        "#e6583c;\n"
"  font-weight: 600;\n"
"  font-size: 10px;\n"
"}\n"
"\n"
"QLabel#passwordHeaderLabel, #usernameHeaderLabel{  \n"
"  font-size: 24px;\n"
"  margin-bottom: 10px;\n"
"}\n"
"\n"
"QLineEdit {\n"
"  color: #464d55;\n"
"  font-weight: 600;\n"
"  border-radius: 8px;\n"
"  border: 1px solid #e0e4e7;\n"
"  padding: 5px 15px;\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"  border: 1px solid #d0e3ff;\n"
"}\n"
"\n"
"QLineEdit::placeholder {\n"
"  color: #767e89;\n"
"}\n"
"QPushButton {\n"
"  background-color: #464d55;\n"
"  color: #fff;\n"
"  font-weight: 600;\n"
"  border-radius: 12px;\n"
"  border: 1px solid #464d55;\n"
"  padding: 5px 15px;\n"
"  outline: 0px;\n"
"}\n"
"QPushButton:hover {\n"
"  border: 3px solid #767e89;\n"
"}\n"
"QPushButton:focus {\n"
"  border: 3px solid #767e89;\n"
"}\n"
"QCheckBox {\n"
"  color: #464d55;\n"
"  font-weight: 600;\n"
"}\n"
"QDateTimeEdit{\n"
"  color: #464d55;\n"
"  font-weight: 600;\n"
"  border-radius: 8px;\n"
"  border: 1px solid #e0e4e7;\n"
"  padding: 5px 15px;}\n"
"QDateTim"
                        "eEdit::on{\n"
"   border: 3px solid #d0e3ff;\n"
"}\n"
"QDateTimeEdit::drop-down{\n"
"   border: 0px;\n"
"}\n"
"QDateTimeEdit::down-arrow{\n"
"   image: url(:/dropdown/dropdownPNG.png);\n"
"   width: 12px;\n"
"   height: 12px;\n"
"   margin-right: 15px;\n"
"}\n"
"\n"
"QTextEdit {\n"
"  color: #464d55;\n"
"  font-weight: 600;\n"
"  border-radius: 8px;\n"
"  border: 1px solid #e0e4e7;\n"
"  padding: 5px 15px;\n"
"}\n"
"\n"
"QTextEdit:focus {\n"
"  border: 1px solid #d0e3ff;\n"
"}\n"
"\n"
"QTextEdit::placeholder {\n"
"  color: #767e89;\n"
"}\n"
"\n"
"QCalendarWidget QAbstractItemView\n"
"{ \n"
"selection-background-color: #042944; \n"
"selection-color: white;\n"
"selection-border:10px solid red;\n"
"\n"
"}\n"
"QCalendarWidget QWidget \n"
"{\n"
"  color:grey;\n"
"}\n"
"QCalendarWidget QTableView{\n"
"border-width:0px;\n"
"background-color:lightgrey;\n"
"}\n"
"\n"
"\n"
"QScrollBar:vertical {\n"
"\n"
"  border-color: rgb(227, 227, 227);\n"
"  border-width: 1px;\n"
"  border-style: solid;\n"
"  border-radius: 8px;\n"
""
                        "\n"
"  background-color: rgb(240, 240, 240);\n"
"  width: 8px;\n"
"  margin: 21px 0 21px 0;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical {\n"
"\n"
"  background-color: rgb(200, 200, 200);\n"
"  min-height: 25px;\n"
"\n"
"}\n"
"\n"
" QScrollBar::add-line:vertical {\n"
"    height: 0px;\n"
"}\n"
"\n"
"QScrollBar::sub-line:vertical {\n"
"    height: 0px;\n"
"}\n"
"\n"
"\n"
"  QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"      background: none;\n"
"   height: 0px;\n"
"  }")
        self.verticalLayout_2 = QVBoxLayout(self.widget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.scrollArea = QScrollArea(self.widget)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setStyleSheet(u"QWidget#scrollArea{\n"
"border: 0px;\n"
"}")
        self.scrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 472, 517))
        self.scrollAreaWidgetContents.setStyleSheet(u".QWidget {\n"
"border: 2px solid #464d55;\n"
"border-radius: 12px;}")
        self.verticalLayout_3 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.editUsernameWidget = QWidget(self.scrollAreaWidgetContents)
        self.editUsernameWidget.setObjectName(u"editUsernameWidget")
        self.gridLayout_2 = QGridLayout(self.editUsernameWidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.usernameHeaderLabel = QLabel(self.editUsernameWidget)
        self.usernameHeaderLabel.setObjectName(u"usernameHeaderLabel")
        self.usernameHeaderLabel.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_2.addWidget(self.usernameHeaderLabel, 0, 1, 1, 1)

        self.label_5 = QLabel(self.editUsernameWidget)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout_2.addWidget(self.label_5, 1, 0, 1, 1)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(-1, 10, -1, -1)
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_3)

        self.changeUsernameButton = QPushButton(self.editUsernameWidget)
        self.changeUsernameButton.setObjectName(u"changeUsernameButton")

        self.horizontalLayout_3.addWidget(self.changeUsernameButton)


        self.gridLayout_2.addLayout(self.horizontalLayout_3, 3, 0, 1, 2)

        self.usernameLineEdit = QLineEdit(self.editUsernameWidget)
        self.usernameLineEdit.setObjectName(u"usernameLineEdit")

        self.gridLayout_2.addWidget(self.usernameLineEdit, 1, 1, 1, 1)

        self.usernameErrorLabel = QLabel(self.editUsernameWidget)
        self.usernameErrorLabel.setObjectName(u"usernameErrorLabel")
        self.usernameErrorLabel.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.usernameErrorLabel, 2, 0, 1, 2)


        self.verticalLayout_3.addWidget(self.editUsernameWidget)

        self.editPasswordWidget = QWidget(self.scrollAreaWidgetContents)
        self.editPasswordWidget.setObjectName(u"editPasswordWidget")
        self.gridLayout = QGridLayout(self.editPasswordWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.enterPreviousPasswordLineEdit = QLineEdit(self.editPasswordWidget)
        self.enterPreviousPasswordLineEdit.setObjectName(u"enterPreviousPasswordLineEdit")
        self.enterPreviousPasswordLineEdit.setEchoMode(QLineEdit.Password)

        self.gridLayout.addWidget(self.enterPreviousPasswordLineEdit, 1, 1, 1, 1)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(-1, 10, -1, -1)
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)

        self.pushButton_2 = QPushButton(self.editPasswordWidget)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.horizontalLayout_2.addWidget(self.pushButton_2)


        self.gridLayout.addLayout(self.horizontalLayout_2, 5, 0, 1, 2)

        self.reEnterNewPasswordLineEdit = QLineEdit(self.editPasswordWidget)
        self.reEnterNewPasswordLineEdit.setObjectName(u"reEnterNewPasswordLineEdit")
        self.reEnterNewPasswordLineEdit.setEchoMode(QLineEdit.Password)

        self.gridLayout.addWidget(self.reEnterNewPasswordLineEdit, 3, 1, 1, 1)

        self.label_3 = QLabel(self.editPasswordWidget)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 3, 0, 1, 1)

        self.label = QLabel(self.editPasswordWidget)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)

        self.label_2 = QLabel(self.editPasswordWidget)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 1)

        self.enterNewPasswordLineEdit = QLineEdit(self.editPasswordWidget)
        self.enterNewPasswordLineEdit.setObjectName(u"enterNewPasswordLineEdit")
        self.enterNewPasswordLineEdit.setEchoMode(QLineEdit.Password)

        self.gridLayout.addWidget(self.enterNewPasswordLineEdit, 2, 1, 1, 1)

        self.passwordHeaderLabel = QLabel(self.editPasswordWidget)
        self.passwordHeaderLabel.setObjectName(u"passwordHeaderLabel")
        self.passwordHeaderLabel.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.passwordHeaderLabel, 0, 1, 1, 1)

        self.passwordErrorLabel = QLabel(self.editPasswordWidget)
        self.passwordErrorLabel.setObjectName(u"passwordErrorLabel")
        self.passwordErrorLabel.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.passwordErrorLabel, 4, 0, 1, 2)


        self.verticalLayout_3.addWidget(self.editPasswordWidget)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(-1, 10, -1, -1)
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.doneButton = QPushButton(self.scrollAreaWidgetContents)
        self.doneButton.setObjectName(u"doneButton")

        self.horizontalLayout.addWidget(self.doneButton)


        self.verticalLayout_3.addLayout(self.horizontalLayout)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_2.addWidget(self.scrollArea)


        self.verticalLayout.addWidget(self.widget)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.usernameHeaderLabel.setText(QCoreApplication.translate("Form", u"Username", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"New Username:", None))
        self.changeUsernameButton.setText(QCoreApplication.translate("Form", u"Change Username", None))
        self.usernameLineEdit.setPlaceholderText(QCoreApplication.translate("Form", u"Enter new username", None))
        self.usernameErrorLabel.setText(QCoreApplication.translate("Form", u"error", None))
        self.enterPreviousPasswordLineEdit.setPlaceholderText(QCoreApplication.translate("Form", u"Enter previous password", None))
        self.pushButton_2.setText(QCoreApplication.translate("Form", u"Change Password", None))
        self.reEnterNewPasswordLineEdit.setPlaceholderText(QCoreApplication.translate("Form", u"Re-enter new password", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"Re-enter Password:", None))
        self.label.setText(QCoreApplication.translate("Form", u"Previous Password:", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"New Password:", None))
        self.enterNewPasswordLineEdit.setPlaceholderText(QCoreApplication.translate("Form", u"Enter new password", None))
        self.passwordHeaderLabel.setText(QCoreApplication.translate("Form", u"Password", None))
        self.passwordErrorLabel.setText(QCoreApplication.translate("Form", u"error", None))
        self.doneButton.setText(QCoreApplication.translate("Form", u"Done", None))
    # retranslateUi

