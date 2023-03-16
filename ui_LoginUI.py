# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'LoginUIXGYIZp.ui'
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
    QLayout, QLineEdit, QPushButton, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(460, 988)
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        Form.setStyleSheet(u"background-color: rgb(82, 158, 218)")
        self.gridLayout = QGridLayout(Form)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.gridLayout.setContentsMargins(20, 20, 20, 20)
        self.loginWidget = QWidget(Form)
        self.loginWidget.setObjectName(u"loginWidget")
        self.loginWidget.setStyleSheet(u"QWidget {\n"
"  background-color: #fff;\n"
"  border-radius: 12px;\n"
"}\n"
"QLabel {\n"
"  color: #464d55;\n"
"  font-weight: 600;\n"
"}\n"
"QLabel#heading {\n"
"  color: #0f1925;\n"
"  font-size: 18px;\n"
"  margin-bottom: 10px;\n"
"}\n"
"\n"
"QLabel#subheading {\n"
"  color: #0f1925;\n"
"  font-size: 12px;\n"
"  font-weight: normal;\n"
"  margin-bottom: 10px;\n"
"}\n"
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
"  background-color: rgb(82, 158, 218);\n"
"  color: #fff;\n"
"  font-weight: 600;\n"
"  border-radius: 8px;\n"
"  border: 1px solid rgb(82, 158, 218);\n"
"  padding: 5px 15px;\n"
"  margin-top: 10px;\n"
"  outline: 0px;\n"
"}\n"
"QPushButton:hover {\n"
"  border: 3px solid #9ac3fe;\n"
"}\n"
"QPushButton:focus {\n"
"  border: 3px solid #9ac3fe;\n"
"}")
        self.verticalLayout_2 = QVBoxLayout(self.loginWidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(20, 20, 20, 20)
        self.label = QLabel(self.loginWidget)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"")

        self.verticalLayout_2.addWidget(self.label)

        self.usernameLineEdit = QLineEdit(self.loginWidget)
        self.usernameLineEdit.setObjectName(u"usernameLineEdit")
        self.usernameLineEdit.setMinimumSize(QSize(300, 0))
        self.usernameLineEdit.setStyleSheet(u"")

        self.verticalLayout_2.addWidget(self.usernameLineEdit)

        self.passwordLabel = QLabel(self.loginWidget)
        self.passwordLabel.setObjectName(u"passwordLabel")
        self.passwordLabel.setStyleSheet(u"")

        self.verticalLayout_2.addWidget(self.passwordLabel)

        self.passwordLineEdit = QLineEdit(self.loginWidget)
        self.passwordLineEdit.setObjectName(u"passwordLineEdit")
        self.passwordLineEdit.setMinimumSize(QSize(300, 0))
        self.passwordLineEdit.setStyleSheet(u"")
        self.passwordLineEdit.setEchoMode(QLineEdit.Password)

        self.verticalLayout_2.addWidget(self.passwordLineEdit)

        self.verticalSpacer_3 = QSpacerItem(0, 20, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_2.addItem(self.verticalSpacer_3)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.loginButton = QPushButton(self.loginWidget)
        self.loginButton.setObjectName(u"loginButton")
        self.loginButton.setMinimumSize(QSize(0, 50))

        self.horizontalLayout.addWidget(self.loginButton)

        self.cancelButton = QPushButton(self.loginWidget)
        self.cancelButton.setObjectName(u"cancelButton")
        self.cancelButton.setMinimumSize(QSize(0, 50))

        self.horizontalLayout.addWidget(self.cancelButton)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.createAccountButton = QPushButton(self.loginWidget)
        self.createAccountButton.setObjectName(u"createAccountButton")
        self.createAccountButton.setMinimumSize(QSize(0, 50))

        self.verticalLayout_2.addWidget(self.createAccountButton)


        self.gridLayout.addWidget(self.loginWidget, 1, 2, 1, 1)

        self.createAccountWidget = QWidget(Form)
        self.createAccountWidget.setObjectName(u"createAccountWidget")
        self.createAccountWidget.setEnabled(True)
        self.createAccountWidget.setStyleSheet(u"QWidget {\n"
"  background-color: #fff;\n"
"  border-radius: 12px;\n"
"}\n"
"QLabel {\n"
"  color: #464d55;\n"
"  font-weight: 600;\n"
"}\n"
"QLabel#CAcreateAccountLabel {\n"
"  color: #0f1925;\n"
"  font-size: 18px;\n"
"  margin-bottom: 10px;\n"
"  text-align: center;\n"
"}\n"
"\n"
"QLabel#subheading {\n"
"  color: #0f1925;\n"
"  font-size: 12px;\n"
"  font-weight: normal;\n"
"  margin-bottom: 10px;\n"
"}\n"
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
"  background-color: rgb(82, 158, 218);\n"
"  color: #fff;\n"
"  font-weight: 600;\n"
"  border-radius: 8px;\n"
"  border: 1px solid rgb(82, 158, 218);\n"
"  padding: 5px 15px;\n"
"  margin-top: 10px;\n"
"  outline: 0px;\n"
"}\n"
"QPushButton:hover {\n"
"  border: 3px solid #9ac3fe;\n"
"}\n"
"QPushButton:focus {\n"
""
                        "  border: 3px solid #9ac3fe;\n"
"}")
        self.verticalLayout_4 = QVBoxLayout(self.createAccountWidget)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(20, 20, 20, 20)
        self.CAcreateAccountLabel = QLabel(self.createAccountWidget)
        self.CAcreateAccountLabel.setObjectName(u"CAcreateAccountLabel")
        self.CAcreateAccountLabel.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.CAcreateAccountLabel)

        self.label_3 = QLabel(self.createAccountWidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setStyleSheet(u"")

        self.verticalLayout_4.addWidget(self.label_3)

        self.CAusernameLineEdit = QLineEdit(self.createAccountWidget)
        self.CAusernameLineEdit.setObjectName(u"CAusernameLineEdit")
        self.CAusernameLineEdit.setMinimumSize(QSize(300, 0))
        self.CAusernameLineEdit.setStyleSheet(u"")

        self.verticalLayout_4.addWidget(self.CAusernameLineEdit)

        self.passwordLabel_3 = QLabel(self.createAccountWidget)
        self.passwordLabel_3.setObjectName(u"passwordLabel_3")
        self.passwordLabel_3.setStyleSheet(u"")

        self.verticalLayout_4.addWidget(self.passwordLabel_3)

        self.CApasswordLineEdit = QLineEdit(self.createAccountWidget)
        self.CApasswordLineEdit.setObjectName(u"CApasswordLineEdit")
        self.CApasswordLineEdit.setMinimumSize(QSize(300, 0))
        self.CApasswordLineEdit.setStyleSheet(u"")
        self.CApasswordLineEdit.setEchoMode(QLineEdit.Password)

        self.verticalLayout_4.addWidget(self.CApasswordLineEdit)

        self.label_4 = QLabel(self.createAccountWidget)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout_4.addWidget(self.label_4)

        self.CAconfirmPasswordLineEdit = QLineEdit(self.createAccountWidget)
        self.CAconfirmPasswordLineEdit.setObjectName(u"CAconfirmPasswordLineEdit")
        self.CAconfirmPasswordLineEdit.setEchoMode(QLineEdit.Password)

        self.verticalLayout_4.addWidget(self.CAconfirmPasswordLineEdit)

        self.verticalSpacer_4 = QSpacerItem(0, 20, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_4.addItem(self.verticalSpacer_4)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.CAcreateAccountButton = QPushButton(self.createAccountWidget)
        self.CAcreateAccountButton.setObjectName(u"CAcreateAccountButton")
        self.CAcreateAccountButton.setMinimumSize(QSize(0, 50))

        self.horizontalLayout_3.addWidget(self.CAcreateAccountButton)

        self.CAcancelButton = QPushButton(self.createAccountWidget)
        self.CAcancelButton.setObjectName(u"CAcancelButton")
        self.CAcancelButton.setMinimumSize(QSize(0, 50))

        self.horizontalLayout_3.addWidget(self.CAcancelButton)


        self.verticalLayout_4.addLayout(self.horizontalLayout_3)


        self.gridLayout.addWidget(self.createAccountWidget, 2, 2, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 200, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 3, 2, 1, 1)

        self.pigeonLabel = QLabel(Form)
        self.pigeonLabel.setObjectName(u"pigeonLabel")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.pigeonLabel.sizePolicy().hasHeightForWidth())
        self.pigeonLabel.setSizePolicy(sizePolicy1)
        self.pigeonLabel.setMinimumSize(QSize(0, 80))
        font = QFont()
        font.setFamilies([u"Helvetica"])
        font.setPointSize(51)
        font.setBold(True)
        self.pigeonLabel.setFont(font)
        self.pigeonLabel.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.pigeonLabel, 0, 2, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_2, 1, 3, 2, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 1, 1, 2, 1)

        QWidget.setTabOrder(self.usernameLineEdit, self.passwordLineEdit)
        QWidget.setTabOrder(self.passwordLineEdit, self.loginButton)
        QWidget.setTabOrder(self.loginButton, self.cancelButton)
        QWidget.setTabOrder(self.cancelButton, self.createAccountButton)

        self.retranslateUi(Form)
        self.createAccountButton.clicked.connect(self.loginWidget.hide)
        self.createAccountButton.clicked.connect(self.createAccountWidget.show)
        self.CAcancelButton.clicked.connect(self.createAccountWidget.hide)
        self.CAcancelButton.clicked.connect(self.loginWidget.show)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText(QCoreApplication.translate("Form", u"Username:", None))
        self.usernameLineEdit.setInputMask("")
        self.usernameLineEdit.setText("")
        self.usernameLineEdit.setPlaceholderText(QCoreApplication.translate("Form", u"Enter your username", None))
        self.passwordLabel.setText(QCoreApplication.translate("Form", u"Password:", None))
        self.passwordLineEdit.setInputMask("")
        self.passwordLineEdit.setPlaceholderText(QCoreApplication.translate("Form", u"Enter your password", None))
        self.loginButton.setText(QCoreApplication.translate("Form", u"Login", None))
        self.cancelButton.setText(QCoreApplication.translate("Form", u"Cancel", None))
        self.createAccountButton.setText(QCoreApplication.translate("Form", u"Create an account", None))
        self.CAcreateAccountLabel.setText(QCoreApplication.translate("Form", u"Create Account", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"Username:", None))
        self.CAusernameLineEdit.setInputMask("")
        self.CAusernameLineEdit.setText("")
        self.CAusernameLineEdit.setPlaceholderText(QCoreApplication.translate("Form", u"Enter your username", None))
        self.passwordLabel_3.setText(QCoreApplication.translate("Form", u"Password:", None))
        self.CApasswordLineEdit.setInputMask("")
        self.CApasswordLineEdit.setPlaceholderText(QCoreApplication.translate("Form", u"Enter your password", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"Confirm Password:", None))
        self.CAconfirmPasswordLineEdit.setPlaceholderText(QCoreApplication.translate("Form", u"Re-enter your password", None))
        self.CAcreateAccountButton.setText(QCoreApplication.translate("Form", u"Create Account", None))
        self.CAcancelButton.setText(QCoreApplication.translate("Form", u"Cancel", None))
        self.pigeonLabel.setText(QCoreApplication.translate("Form", u"Pigeon", None))
    # retranslateUi

