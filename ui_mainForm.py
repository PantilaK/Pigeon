# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainForm.ui'
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
        mainWidget.resize(668, 415)
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
        self.verticalLayout.setSizeConstraint(QLayout.SetFixedSize)
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

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.accountWidget = QWidget(self.controllerWidget)
        self.accountWidget.setObjectName(u"accountWidget")
        self.horizontalLayout_2 = QHBoxLayout(self.accountWidget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.acountDetailsLabel = QLabel(self.accountWidget)
        self.acountDetailsLabel.setObjectName(u"acountDetailsLabel")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.acountDetailsLabel.sizePolicy().hasHeightForWidth())
        self.acountDetailsLabel.setSizePolicy(sizePolicy)
        self.acountDetailsLabel.setMinimumSize(QSize(120, 0))

        self.horizontalLayout_2.addWidget(self.acountDetailsLabel)


        self.verticalLayout.addWidget(self.accountWidget)


        self.horizontalLayout.addWidget(self.controllerWidget)

        self.tripListWidget = QWidget(mainWidget)
        self.tripListWidget.setObjectName(u"tripListWidget")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.MinimumExpanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.tripListWidget.sizePolicy().hasHeightForWidth())
        self.tripListWidget.setSizePolicy(sizePolicy1)
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
        self.tripListScrollWidget.setGeometry(QRect(0, 0, 446, 297))
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.tripListScrollWidget.sizePolicy().hasHeightForWidth())
        self.tripListScrollWidget.setSizePolicy(sizePolicy2)
        self.verticalLayout_3 = QVBoxLayout(self.tripListScrollWidget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
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
        self.tripListHeading.setText(QCoreApplication.translate("mainWidget", u"titleList", None))
    # retranslateUi

