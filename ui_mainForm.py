# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainFormjcNfnv.ui'
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
from PySide6.QtWidgets import (QAbstractScrollArea, QApplication, QHBoxLayout, QLabel,
    QLayout, QPushButton, QScrollArea, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)

class Ui_mainWidget(object):
    def setupUi(self, mainWidget):
        if not mainWidget.objectName():
            mainWidget.setObjectName(u"mainWidget")
        mainWidget.setWindowModality(Qt.ApplicationModal)
        mainWidget.resize(799, 651)
        mainWidget.setStyleSheet(u"background-color: rgb(82, 158, 218);\n"
"\n"
"QWidget {\n"
"  background-color: #fff;\n"
"  border-radius: 12px;\n"
"}\n"
"\n"
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
"QPushBut"
                        "ton:focus {\n"
"  border: 3px solid #9ac3fe;\n"
"}")
        self.horizontalLayout = QHBoxLayout(mainWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.controllerWidget = QWidget(mainWidget)
        self.controllerWidget.setObjectName(u"controllerWidget")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.controllerWidget.sizePolicy().hasHeightForWidth())
        self.controllerWidget.setSizePolicy(sizePolicy)
        self.controllerWidget.setStyleSheet(u"QWidget {\n"
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
"  padding: 15px 30px;\n"
"  margin-top: 10px;\n"
"  outline: 0px;\n"
"}\n"
"QPushButton:hover {\n"
"  border: 3px solid #9ac3fe;\n"
"}\n"
"QPushButton:focus {\n"
"  border: 3px solid #9ac3fe;\n"
"}")
        self.verticalLayout = QVBoxLayout(self.controllerWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setSizeConstraint(QLayout.SetMinimumSize)
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)
        self.currentTripButton = QPushButton(self.controllerWidget)
        self.currentTripButton.setObjectName(u"currentTripButton")

        self.verticalLayout.addWidget(self.currentTripButton)

        self.futureTripButton = QPushButton(self.controllerWidget)
        self.futureTripButton.setObjectName(u"futureTripButton")

        self.verticalLayout.addWidget(self.futureTripButton)

        self.pastTripButton = QPushButton(self.controllerWidget)
        self.pastTripButton.setObjectName(u"pastTripButton")

        self.verticalLayout.addWidget(self.pastTripButton)

        self.verticalSpacer = QSpacerItem(20, 50, QSizePolicy.Minimum, QSizePolicy.MinimumExpanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.accountWidget = QWidget(self.controllerWidget)
        self.accountWidget.setObjectName(u"accountWidget")
        self.horizontalLayout_2 = QHBoxLayout(self.accountWidget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.acountDetailsLabel = QLabel(self.accountWidget)
        self.acountDetailsLabel.setObjectName(u"acountDetailsLabel")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.acountDetailsLabel.sizePolicy().hasHeightForWidth())
        self.acountDetailsLabel.setSizePolicy(sizePolicy1)
        self.acountDetailsLabel.setMinimumSize(QSize(120, 0))

        self.horizontalLayout_2.addWidget(self.acountDetailsLabel)


        self.verticalLayout.addWidget(self.accountWidget)

        self.accountButtonWidget = QWidget(self.controllerWidget)
        self.accountButtonWidget.setObjectName(u"accountButtonWidget")
        self.accountButtonWidget.setStyleSheet(u"QPushButton {\n"
"  background-color: rgb(82, 158, 218);\n"
"  color: #fff;\n"
"  font-weight: 400;\n"
"  border-radius: 12px;\n"
"  border: 1px solid rgb(82, 158, 218);\n"
"  padding: 5px 10px;\n"
"  margin-top: 2px;\n"
"  outline: 0px;\n"
"}\n"
"QPushButton:hover {\n"
"  border: 1px solid #9ac3fe;\n"
"}\n"
"QPushButton:focus {\n"
"  border: 1px solid #9ac3fe;\n"
"}")
        self.horizontalLayout_3 = QHBoxLayout(self.accountButtonWidget)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(-1, 5, -1, 5)
        self.settingsButton = QPushButton(self.accountButtonWidget)
        self.settingsButton.setObjectName(u"settingsButton")

        self.horizontalLayout_3.addWidget(self.settingsButton)

        self.logoutButton = QPushButton(self.accountButtonWidget)
        self.logoutButton.setObjectName(u"logoutButton")

        self.horizontalLayout_3.addWidget(self.logoutButton)


        self.verticalLayout.addWidget(self.accountButtonWidget)


        self.horizontalLayout.addWidget(self.controllerWidget)

        self.tripListWidget = QWidget(mainWidget)
        self.tripListWidget.setObjectName(u"tripListWidget")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.MinimumExpanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.tripListWidget.sizePolicy().hasHeightForWidth())
        self.tripListWidget.setSizePolicy(sizePolicy2)
        self.tripListWidget.setStyleSheet(u"QWidget {\n"
"  background-color: #fff;\n"
"  border-radius: 12px;\n"
"}\n"
"QLabel {\n"
"  color: #464d55;\n"
"  font-weight: 600;\n"
"}\n"
"QLabel#tripListHeading {\n"
"  color: #0f1925;\n"
"  font-size: 30px;\n"
"  bottom-margin: 5px;\n"
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
"  outline: 0px;\n"
"}\n"
"QPushButton:hover {\n"
"  border: 3px solid #9ac3fe;\n"
"}\n"
"QPushButton:focus {\n"
"  border: 3px solid #9ac3fe;\n"
"}\n"
"\n"
"QScrollBar:vertical {\n"
"\n"
"  border-color: rgb(227, 227, 227);\n"
"  border-width: 1px;\n"
"  border-style: solid;\n"
"  border-radius: 8p"
                        "x;\n"
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
        self.verticalLayout_2 = QVBoxLayout(self.tripListWidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.tripListHeading = QLabel(self.tripListWidget)
        self.tripListHeading.setObjectName(u"tripListHeading")
        self.tripListHeading.setAlignment(Qt.AlignRight|Qt.AlignTop|Qt.AlignTrailing)

        self.verticalLayout_2.addWidget(self.tripListHeading)

        self.scrollArea = QScrollArea(self.tripListWidget)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scrollArea.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.scrollArea.setWidgetResizable(True)
        self.tripListScrollWidget = QWidget()
        self.tripListScrollWidget.setObjectName(u"tripListScrollWidget")
        self.tripListScrollWidget.setGeometry(QRect(0, 0, 547, 559))
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.tripListScrollWidget.sizePolicy().hasHeightForWidth())
        self.tripListScrollWidget.setSizePolicy(sizePolicy3)
        self.tripListScrollWidget.setStyleSheet(u"QWidget#notificationWidget{\n"
"  background-color: #fff;\n"
"  border-radius: 12px;\n"
"  border: 3px solid rgb(82, 158, 218);\n"
"}\n"
"\n"
"QLabel#notificationHeaderLabel {\n"
"  color: #0f1925;\n"
"  font-size: 24px;\n"
"  margin-bottom: 10px;\n"
"  text-align: right;\n"
"}\n"
"\n"
"QLabel#noNotificationLabel {\n"
"  font-size: 16px;\n"
"  padding: 50px 20px;\n"
"}\n"
"\n"
"QWidget#hLineSplitWidget {\n"
"  border: 0px;\n"
"  background-color: #0f1925;\n"
"}")
        self.verticalLayout_3 = QVBoxLayout(self.tripListScrollWidget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.notificationWidget = QWidget(self.tripListScrollWidget)
        self.notificationWidget.setObjectName(u"notificationWidget")
        self.verticalLayout_4 = QVBoxLayout(self.notificationWidget)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.notificationHeaderLabel = QLabel(self.notificationWidget)
        self.notificationHeaderLabel.setObjectName(u"notificationHeaderLabel")
        self.notificationHeaderLabel.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.verticalLayout_4.addWidget(self.notificationHeaderLabel)

        self.noNotificationLabel = QLabel(self.notificationWidget)
        self.noNotificationLabel.setObjectName(u"noNotificationLabel")
        self.noNotificationLabel.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.noNotificationLabel)

        self.notificationLayout = QVBoxLayout()
        self.notificationLayout.setObjectName(u"notificationLayout")

        self.verticalLayout_4.addLayout(self.notificationLayout)


        self.verticalLayout_3.addWidget(self.notificationWidget)

        self.hLineSplitWidget = QWidget(self.tripListScrollWidget)
        self.hLineSplitWidget.setObjectName(u"hLineSplitWidget")
        sizePolicy4 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.hLineSplitWidget.sizePolicy().hasHeightForWidth())
        self.hLineSplitWidget.setSizePolicy(sizePolicy4)
        self.hLineSplitWidget.setMinimumSize(QSize(0, 3))

        self.verticalLayout_3.addWidget(self.hLineSplitWidget)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(-1, 5, -1, 5)
        self.newTripButton = QPushButton(self.tripListScrollWidget)
        self.newTripButton.setObjectName(u"newTripButton")

        self.horizontalLayout_4.addWidget(self.newTripButton)


        self.verticalLayout_3.addLayout(self.horizontalLayout_4)

        self.tripListLayout = QVBoxLayout()
        self.tripListLayout.setObjectName(u"tripListLayout")

        self.verticalLayout_3.addLayout(self.tripListLayout)

        self.verticalSpacer_2 = QSpacerItem(20, 0, QSizePolicy.Minimum, QSizePolicy.MinimumExpanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_2)

        self.scrollArea.setWidget(self.tripListScrollWidget)

        self.verticalLayout_2.addWidget(self.scrollArea)


        self.horizontalLayout.addWidget(self.tripListWidget)


        self.retranslateUi(mainWidget)

        QMetaObject.connectSlotsByName(mainWidget)
    # setupUi

    def retranslateUi(self, mainWidget):
        mainWidget.setWindowTitle(QCoreApplication.translate("mainWidget", u"Form", None))
        self.currentTripButton.setText(QCoreApplication.translate("mainWidget", u"Current Trip", None))
        self.futureTripButton.setText(QCoreApplication.translate("mainWidget", u"Future Trips", None))
        self.pastTripButton.setText(QCoreApplication.translate("mainWidget", u"Past Trips", None))
        self.acountDetailsLabel.setText(QCoreApplication.translate("mainWidget", u"accountDetails", None))
        self.settingsButton.setText(QCoreApplication.translate("mainWidget", u"Settings", None))
        self.logoutButton.setText(QCoreApplication.translate("mainWidget", u"Logout", None))
        self.tripListHeading.setText(QCoreApplication.translate("mainWidget", u"titleList", None))
        self.notificationHeaderLabel.setText(QCoreApplication.translate("mainWidget", u"Alerts", None))
        self.noNotificationLabel.setText(QCoreApplication.translate("mainWidget", u"No notifications", None))
        self.newTripButton.setText(QCoreApplication.translate("mainWidget", u"New Trip", None))
    # retranslateUi

