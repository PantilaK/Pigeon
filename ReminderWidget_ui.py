# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ReminderWidget.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QHBoxLayout, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(425, 84)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        Form.setStyleSheet(u"QWidget{\n"
"  background-color: #fff;\n"
"}\n"
"QLabel{\n"
"  color: #464d55;\n"
"  font-weight: 400;\n"
"  font-size: 14px;\n"
"  padding: 5px 5px;\n"
"}\n"
"QCheckBox{\n"
"  color: #464d55;\n"
"  font-weight: 400;\n"
"  font-size: 14px;\n"
"  padding: 5px 0px;\n"
"}\n"
"QPushButton {\n"
"  background-color: #464d55;\n"
"  color: #fff;\n"
"  font-weight: 600;\n"
"  border-radius: 10px;\n"
"  border: 1px solid #464d55;\n"
"  padding: 5px 15px;\n"
"  outline: 0px;\n"
"}\n"
"QLineEdit {\n"
"  color: #464d55;\n"
"  font-weight: 600;\n"
"  border-radius: 8px;\n"
"  border: 1px solid #e0e4e7;\n"
"  padding: 5px 15px;\n"
"}\n"
"")
        self.horizontalLayout = QHBoxLayout(Form)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.reminderShowWidget = QWidget(Form)
        self.reminderShowWidget.setObjectName(u"reminderShowWidget")
        self.horizontalLayout_3 = QHBoxLayout(self.reminderShowWidget)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(12, 1, 12, 1)
        self.showReminderCheckbox = QCheckBox(self.reminderShowWidget)
        self.showReminderCheckbox.setObjectName(u"showReminderCheckbox")

        self.horizontalLayout_3.addWidget(self.showReminderCheckbox)

        self.showReminderLabel = QLabel(self.reminderShowWidget)
        self.showReminderLabel.setObjectName(u"showReminderLabel")

        self.horizontalLayout_3.addWidget(self.showReminderLabel)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)

        self.showEditButton = QPushButton(self.reminderShowWidget)
        self.showEditButton.setObjectName(u"showEditButton")

        self.horizontalLayout_3.addWidget(self.showEditButton)

        self.showDeleteButton = QPushButton(self.reminderShowWidget)
        self.showDeleteButton.setObjectName(u"showDeleteButton")

        self.horizontalLayout_3.addWidget(self.showDeleteButton)


        self.verticalLayout.addWidget(self.reminderShowWidget)

        self.reminderEditWidget = QWidget(Form)
        self.reminderEditWidget.setObjectName(u"reminderEditWidget")
        self.horizontalLayout_2 = QHBoxLayout(self.reminderEditWidget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(-1, 1, -1, 1)
        self.editReminderCheckBox = QCheckBox(self.reminderEditWidget)
        self.editReminderCheckBox.setObjectName(u"editReminderCheckBox")

        self.horizontalLayout_2.addWidget(self.editReminderCheckBox)

        self.editReminderLineEdit = QLineEdit(self.reminderEditWidget)
        self.editReminderLineEdit.setObjectName(u"editReminderLineEdit")

        self.horizontalLayout_2.addWidget(self.editReminderLineEdit)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)

        self.editOKButton = QPushButton(self.reminderEditWidget)
        self.editOKButton.setObjectName(u"editOKButton")

        self.horizontalLayout_2.addWidget(self.editOKButton)

        self.editDeleteButton = QPushButton(self.reminderEditWidget)
        self.editDeleteButton.setObjectName(u"editDeleteButton")

        self.horizontalLayout_2.addWidget(self.editDeleteButton)


        self.verticalLayout.addWidget(self.reminderEditWidget)


        self.horizontalLayout.addLayout(self.verticalLayout)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.showReminderCheckbox.setText("")
        self.showReminderLabel.setText(QCoreApplication.translate("Form", u"Reminder", None))
        self.showEditButton.setText(QCoreApplication.translate("Form", u"Edit", None))
        self.showDeleteButton.setText(QCoreApplication.translate("Form", u"Delete", None))
        self.editReminderCheckBox.setText("")
        self.editReminderLineEdit.setPlaceholderText(QCoreApplication.translate("Form", u"Reminder Text", None))
        self.editOKButton.setText(QCoreApplication.translate("Form", u"OK", None))
        self.editDeleteButton.setText(QCoreApplication.translate("Form", u"Delete", None))
    # retranslateUi

