# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'tripComponentSZCLdg.ui'
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

class Ui_tripWidget(object):
    def setupUi(self, tripWidget):
        if not tripWidget.objectName():
            tripWidget.setObjectName(u"tripWidget")
        tripWidget.resize(490, 421)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(tripWidget.sizePolicy().hasHeightForWidth())
        tripWidget.setSizePolicy(sizePolicy)
        tripWidget.setStyleSheet(u"QWidget#headerWidget{\n"
"  background-color: #fff;\n"
"  border-radius: 20px;\n"
"  border: 2px solid #464d55;;\n"
"}\n"
"\n"
"QWidget{\n"
"    background-color: #fff;\n"
"}\n"
"\n"
"QLabel {\n"
"  color: #464d55;\n"
"  font-weight: 600;\n"
"  font-size: 24px\n"
"}\n"
"\n"
"QPushButton {\n"
"  background-color: #464d55;\n"
"  color: #fff;\n"
"  font-weight: 600;\n"
"  border-radius: 12px;\n"
"  border: 1px solid #464d55;\n"
"  padding: 5px 15px;\n"
"  outline: 0px;\n"
"}\n"
"")
        self.verticalLayout = QVBoxLayout(tripWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.headerWidget = QWidget(tripWidget)
        self.headerWidget.setObjectName(u"headerWidget")
        self.headerWidget.setMinimumSize(QSize(400, 0))
        self.verticalLayout_2 = QVBoxLayout(self.headerWidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.tripTitle = QLabel(self.headerWidget)
        self.tripTitle.setObjectName(u"tripTitle")

        self.horizontalLayout.addWidget(self.tripTitle)

        self.tripTime = QLabel(self.headerWidget)
        self.tripTime.setObjectName(u"tripTime")
        self.tripTime.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout.addWidget(self.tripTime)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.tripExpandButton = QPushButton(self.headerWidget)
        self.tripExpandButton.setObjectName(u"tripExpandButton")

        self.horizontalLayout_2.addWidget(self.tripExpandButton)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.tripEditButton = QPushButton(self.headerWidget)
        self.tripEditButton.setObjectName(u"tripEditButton")

        self.horizontalLayout_2.addWidget(self.tripEditButton)

        self.tripDeleteButton = QPushButton(self.headerWidget)
        self.tripDeleteButton.setObjectName(u"tripDeleteButton")

        self.horizontalLayout_2.addWidget(self.tripDeleteButton)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)


        self.verticalLayout.addWidget(self.headerWidget)

        self.tripSubWidget = QWidget(tripWidget)
        self.tripSubWidget.setObjectName(u"tripSubWidget")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.tripSubWidget.sizePolicy().hasHeightForWidth())
        self.tripSubWidget.setSizePolicy(sizePolicy1)
        self.tripSubWidget.setStyleSheet(u"QWidget#sidebarWidget{\n"
"  background-color: #464d55;\n"
"  border-radius: 2px\n"
"}")
        self.horizontalLayout_3 = QHBoxLayout(self.tripSubWidget)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(-1, 0, 0, -1)
        self.sidebarWidget = QWidget(self.tripSubWidget)
        self.sidebarWidget.setObjectName(u"sidebarWidget")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.sidebarWidget.sizePolicy().hasHeightForWidth())
        self.sidebarWidget.setSizePolicy(sizePolicy2)
        self.sidebarWidget.setMinimumSize(QSize(3, 0))

        self.horizontalLayout_3.addWidget(self.sidebarWidget)

        self.tripDetailWidget = QWidget(self.tripSubWidget)
        self.tripDetailWidget.setObjectName(u"tripDetailWidget")
        sizePolicy3 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.tripDetailWidget.sizePolicy().hasHeightForWidth())
        self.tripDetailWidget.setSizePolicy(sizePolicy3)
        self.tripDetailWidget.setStyleSheet(u"QLabel#detailHeaderLabel{\n"
"  color: #464d55;\n"
"  font-weight: 600;\n"
"  font-size: 20px\n"
"}\n"
"QLabel#reminderHeaderLabel{\n"
"  color: #464d55;\n"
"  font-weight: 600;\n"
"  font-size: 20px\n"
"}\n"
"QLabel{\n"
"  color: #464d55;\n"
"  font-weight: 400;\n"
"  font-size: 14px\n"
"}\n"
"QCheckBox{\n"
"  color: #464d55;\n"
"  font-weight: 400;\n"
"  font-size: 14px\n"
"}\n"
"")
        self.verticalLayout_3 = QVBoxLayout(self.tripDetailWidget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, -1, 0, -1)
        self.tripDetailsWidget = QWidget(self.tripDetailWidget)
        self.tripDetailsWidget.setObjectName(u"tripDetailsWidget")
        self.verticalLayout_4 = QVBoxLayout(self.tripDetailsWidget)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.detailHeaderLabel = QLabel(self.tripDetailsWidget)
        self.detailHeaderLabel.setObjectName(u"detailHeaderLabel")
        self.detailHeaderLabel.setAlignment(Qt.AlignRight|Qt.AlignTop|Qt.AlignTrailing)

        self.verticalLayout_4.addWidget(self.detailHeaderLabel)

        self.label = QLabel(self.tripDetailsWidget)
        self.label.setObjectName(u"label")

        self.verticalLayout_4.addWidget(self.label)


        self.verticalLayout_3.addWidget(self.tripDetailsWidget)

        self.tripReminderWidget = QWidget(self.tripDetailWidget)
        self.tripReminderWidget.setObjectName(u"tripReminderWidget")
        self.verticalLayout_5 = QVBoxLayout(self.tripReminderWidget)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.reminderHeaderLabel = QLabel(self.tripReminderWidget)
        self.reminderHeaderLabel.setObjectName(u"reminderHeaderLabel")
        self.reminderHeaderLabel.setAlignment(Qt.AlignRight|Qt.AlignTop|Qt.AlignTrailing)

        self.verticalLayout_5.addWidget(self.reminderHeaderLabel)

        self.checkboxLayout = QVBoxLayout()
        self.checkboxLayout.setObjectName(u"checkboxLayout")

        self.verticalLayout_5.addLayout(self.checkboxLayout)


        self.verticalLayout_3.addWidget(self.tripReminderWidget)

        self.tripComponentControlWidget = QWidget(self.tripDetailWidget)
        self.tripComponentControlWidget.setObjectName(u"tripComponentControlWidget")
        self.horizontalLayout_4 = QHBoxLayout(self.tripComponentControlWidget)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.addComponentButton = QPushButton(self.tripComponentControlWidget)
        self.addComponentButton.setObjectName(u"addComponentButton")

        self.horizontalLayout_4.addWidget(self.addComponentButton)


        self.verticalLayout_3.addWidget(self.tripComponentControlWidget)

        self.componentWidget = QWidget(self.tripDetailWidget)
        self.componentWidget.setObjectName(u"componentWidget")
        self.horizontalLayout_5 = QHBoxLayout(self.componentWidget)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, -1, 0, -1)
        self.componentLayout = QVBoxLayout()
        self.componentLayout.setObjectName(u"componentLayout")

        self.horizontalLayout_5.addLayout(self.componentLayout)


        self.verticalLayout_3.addWidget(self.componentWidget)


        self.horizontalLayout_3.addWidget(self.tripDetailWidget)


        self.verticalLayout.addWidget(self.tripSubWidget)


        self.retranslateUi(tripWidget)

        QMetaObject.connectSlotsByName(tripWidget)
    # setupUi

    def retranslateUi(self, tripWidget):
        tripWidget.setWindowTitle(QCoreApplication.translate("tripWidget", u"Form", None))
        self.tripTitle.setText(QCoreApplication.translate("tripWidget", u"trip", None))
        self.tripTime.setText(QCoreApplication.translate("tripWidget", u"Time", None))
        self.tripExpandButton.setText(QCoreApplication.translate("tripWidget", u"Expand", None))
        self.tripEditButton.setText(QCoreApplication.translate("tripWidget", u"Edit", None))
        self.tripDeleteButton.setText(QCoreApplication.translate("tripWidget", u"Delete", None))
        self.detailHeaderLabel.setText(QCoreApplication.translate("tripWidget", u"Details", None))
        self.label.setText(QCoreApplication.translate("tripWidget", u"tripDetails1\n"
"tripDetails2", None))
        self.reminderHeaderLabel.setText(QCoreApplication.translate("tripWidget", u"Reminder", None))
        self.addComponentButton.setText(QCoreApplication.translate("tripWidget", u"Add Components", None))
    # retranslateUi

