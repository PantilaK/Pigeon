# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'notificationjBcPdx.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QPushButton,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)

class Ui_notificationUI(object):
    def setupUi(self, notificationUI):
        if not notificationUI.objectName():
            notificationUI.setObjectName(u"notificationUI")
        notificationUI.resize(422, 68)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(notificationUI.sizePolicy().hasHeightForWidth())
        notificationUI.setSizePolicy(sizePolicy)
        notificationUI.setStyleSheet(u"\n"
"QWidget#notification{\n"
"  background-color: #e7e7e7;\n"
"  border-radius: 20px;\n"
"  border: 0px;\n"
"}\n"
"\n"
"QPushButton{\n"
"  border: 0px;\n"
"  padding: 2px 2px;\n"
"  color: #ffffff;\n"
"  font-weight: 1000}\n"
"\n"
"QLabel {\n"
"  color: #464d55;\n"
"  font-weight: 600;\n"
"}")
        self.verticalLayout = QVBoxLayout(notificationUI)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.notification = QWidget(notificationUI)
        self.notification.setObjectName(u"notification")
        sizePolicy.setHeightForWidth(self.notification.sizePolicy().hasHeightForWidth())
        self.notification.setSizePolicy(sizePolicy)
        self.horizontalLayout = QHBoxLayout(self.notification)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.notificationLabel = QLabel(self.notification)
        self.notificationLabel.setObjectName(u"notificationLabel")

        self.horizontalLayout.addWidget(self.notificationLabel)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.dismissButton = QPushButton(self.notification)
        self.dismissButton.setObjectName(u"dismissButton")

        self.horizontalLayout.addWidget(self.dismissButton)


        self.verticalLayout.addWidget(self.notification)


        self.retranslateUi(notificationUI)

        QMetaObject.connectSlotsByName(notificationUI)
    # setupUi

    def retranslateUi(self, notificationUI):
        notificationUI.setWindowTitle(QCoreApplication.translate("notificationUI", u"Form", None))
        self.notificationLabel.setText(QCoreApplication.translate("notificationUI", u"#notificationsdetails", None))
        self.dismissButton.setText(QCoreApplication.translate("notificationUI", u"X", None))
    # retranslateUi

