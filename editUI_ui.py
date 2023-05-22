# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'editUI.ui'
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
from PySide6.QtWidgets import (QAbstractSpinBox, QApplication, QCheckBox, QComboBox,
    QDateTimeEdit, QGridLayout, QHBoxLayout, QLabel,
    QLayout, QLineEdit, QPushButton, QScrollArea,
    QSizePolicy, QSpacerItem, QTextEdit, QTimeEdit,
    QVBoxLayout, QWidget)
import dropdownArrow_rc

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.setWindowModality(Qt.NonModal)
        Form.resize(669, 550)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
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
"QLabel#errorLabel {\n"
"  color: #e6583c;\n"
"  font-weight: 6"
                        "00;\n"
"  font-size: 10px;\n"
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
"  background-color: #464d55;\n"
"  color: #fff;\n"
"  font-weight: 600;\n"
"  border-radius: 12px;\n"
"  border: 1px solid #464d55;\n"
"  padding: 5px 15px;\n"
"  outline: 0px;\n"
"}\n"
"QPushButton:hover {\n"
"  border: 1px solid #767e89;\n"
"}\n"
"QPushButton:focus {\n"
"  border: 1px solid #767e89;\n"
"}\n"
"QCheckBox {\n"
"  color: #464d55;\n"
"  font-weight: 600;\n"
"}\n"
"QDateTimeEdit{\n"
"  color: #464d55;\n"
"  font-weight: 600;\n"
"  border-ra"
                        "dius: 8px;\n"
"  border: 1px solid #e0e4e7;\n"
"  padding: 5px 15px;}\n"
"QDateTimeEdit::on{\n"
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
"  border-color: rgb(227, 227, 227);"
                        "\n"
"  border-width: 1px;\n"
"  border-style: solid;\n"
"  border-radius: 8px;\n"
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
        self.verticalLayout_3 = QVBoxLayout(self.widget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.typeControlLayout = QHBoxLayout()
        self.typeControlLayout.setObjectName(u"typeControlLayout")
        self.typeControlLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")

        self.typeControlLayout.addWidget(self.label)

        self.typeComboBox = QComboBox(self.widget)
        self.typeComboBox.addItem("")
        self.typeComboBox.addItem("")
        self.typeComboBox.addItem("")
        self.typeComboBox.addItem("")
        self.typeComboBox.addItem("")
        self.typeComboBox.addItem("")
        self.typeComboBox.setObjectName(u"typeComboBox")
        sizePolicy.setHeightForWidth(self.typeComboBox.sizePolicy().hasHeightForWidth())
        self.typeComboBox.setSizePolicy(sizePolicy)
        self.typeComboBox.setMinimumSize(QSize(200, 0))
        self.typeComboBox.setEditable(False)

        self.typeControlLayout.addWidget(self.typeComboBox)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.typeControlLayout.addItem(self.horizontalSpacer)


        self.verticalLayout_3.addLayout(self.typeControlLayout)

        self.editWidget = QWidget(self.widget)
        self.editWidget.setObjectName(u"editWidget")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.editWidget.sizePolicy().hasHeightForWidth())
        self.editWidget.setSizePolicy(sizePolicy1)
        self.editWidget.setStyleSheet(u"QWidget#editWidget{\n"
"border: 2px solid #464d55;\n"
"border-radius: 12px;}")
        self.horizontalLayout_2 = QHBoxLayout(self.editWidget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.scrollArea = QScrollArea(self.editWidget)
        self.scrollArea.setObjectName(u"scrollArea")
        sizePolicy2 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.scrollArea.sizePolicy().hasHeightForWidth())
        self.scrollArea.setSizePolicy(sizePolicy2)
        self.scrollArea.setMinimumSize(QSize(0, 200))
        self.scrollArea.setStyleSheet(u"QWidget#scrollArea{\n"
"border: 0px;\n"
"}")
        self.scrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContent = QWidget()
        self.scrollAreaWidgetContent.setObjectName(u"scrollAreaWidgetContent")
        self.scrollAreaWidgetContent.setGeometry(QRect(0, 0, 589, 2264))
        self.verticalLayout_4 = QVBoxLayout(self.scrollAreaWidgetContent)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.tripEditWidget = QWidget(self.scrollAreaWidgetContent)
        self.tripEditWidget.setObjectName(u"tripEditWidget")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.tripEditWidget.sizePolicy().hasHeightForWidth())
        self.tripEditWidget.setSizePolicy(sizePolicy3)
        self.gridLayout = QGridLayout(self.tripEditWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.tripNameLineEdit = QLineEdit(self.tripEditWidget)
        self.tripNameLineEdit.setObjectName(u"tripNameLineEdit")

        self.gridLayout.addWidget(self.tripNameLineEdit, 0, 1, 1, 1)

        self.tripInfoTextEdit = QTextEdit(self.tripEditWidget)
        self.tripInfoTextEdit.setObjectName(u"tripInfoTextEdit")
        sizePolicy4 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.tripInfoTextEdit.sizePolicy().hasHeightForWidth())
        self.tripInfoTextEdit.setSizePolicy(sizePolicy4)
        self.tripInfoTextEdit.setMinimumSize(QSize(0, 50))

        self.gridLayout.addWidget(self.tripInfoTextEdit, 4, 1, 1, 1)

        self.tripReminderWidget = QWidget(self.tripEditWidget)
        self.tripReminderWidget.setObjectName(u"tripReminderWidget")
        self.verticalLayout_5 = QVBoxLayout(self.tripReminderWidget)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(-1, -1, -1, 12)
        self.tripReminderLayout = QVBoxLayout()
        self.tripReminderLayout.setObjectName(u"tripReminderLayout")

        self.verticalLayout_5.addLayout(self.tripReminderLayout)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(-1, -1, -1, 0)
        self.tripAddReminderLineEdit = QLineEdit(self.tripReminderWidget)
        self.tripAddReminderLineEdit.setObjectName(u"tripAddReminderLineEdit")

        self.horizontalLayout.addWidget(self.tripAddReminderLineEdit)

        self.tripAddReminderButton = QPushButton(self.tripReminderWidget)
        self.tripAddReminderButton.setObjectName(u"tripAddReminderButton")
        sizePolicy5 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.tripAddReminderButton.sizePolicy().hasHeightForWidth())
        self.tripAddReminderButton.setSizePolicy(sizePolicy5)

        self.horizontalLayout.addWidget(self.tripAddReminderButton)


        self.verticalLayout_5.addLayout(self.horizontalLayout)


        self.gridLayout.addWidget(self.tripReminderWidget, 2, 1, 1, 1)

        self.label_7 = QLabel(self.tripEditWidget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_7, 3, 0, 1, 1)

        self.label_8 = QLabel(self.tripEditWidget)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_8, 4, 0, 1, 1)

        self.label_6 = QLabel(self.tripEditWidget)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout.addWidget(self.label_6, 2, 0, 1, 1)

        self.label_3 = QLabel(self.tripEditWidget)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 1)

        self.label_2 = QLabel(self.tripEditWidget)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_4 = QLabel(self.tripEditWidget)
        self.label_4.setObjectName(u"label_4")
        sizePolicy3.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy3)

        self.horizontalLayout_3.addWidget(self.label_4)

        self.tripFromDateTimeEdit = QDateTimeEdit(self.tripEditWidget)
        self.tripFromDateTimeEdit.setObjectName(u"tripFromDateTimeEdit")
        sizePolicy6 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.tripFromDateTimeEdit.sizePolicy().hasHeightForWidth())
        self.tripFromDateTimeEdit.setSizePolicy(sizePolicy6)
        self.tripFromDateTimeEdit.setCalendarPopup(True)

        self.horizontalLayout_3.addWidget(self.tripFromDateTimeEdit)

        self.label_5 = QLabel(self.tripEditWidget)
        self.label_5.setObjectName(u"label_5")
        sizePolicy5.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy5)

        self.horizontalLayout_3.addWidget(self.label_5)

        self.tripToDateTimeEdit = QDateTimeEdit(self.tripEditWidget)
        self.tripToDateTimeEdit.setObjectName(u"tripToDateTimeEdit")
        sizePolicy6.setHeightForWidth(self.tripToDateTimeEdit.sizePolicy().hasHeightForWidth())
        self.tripToDateTimeEdit.setSizePolicy(sizePolicy6)
        self.tripToDateTimeEdit.setCalendarPopup(True)

        self.horizontalLayout_3.addWidget(self.tripToDateTimeEdit)


        self.gridLayout.addLayout(self.horizontalLayout_3, 1, 1, 1, 1)

        self.widget_4 = QWidget(self.tripEditWidget)
        self.widget_4.setObjectName(u"widget_4")
        self.verticalLayout_6 = QVBoxLayout(self.widget_4)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.tripTimeSensitiveCheckBox = QCheckBox(self.widget_4)
        self.tripTimeSensitiveCheckBox.setObjectName(u"tripTimeSensitiveCheckBox")

        self.verticalLayout_6.addWidget(self.tripTimeSensitiveCheckBox)

        self.tripTimeSensitiveDateTimeEdit = QDateTimeEdit(self.widget_4)
        self.tripTimeSensitiveDateTimeEdit.setObjectName(u"tripTimeSensitiveDateTimeEdit")
        self.tripTimeSensitiveDateTimeEdit.setCalendarPopup(True)

        self.verticalLayout_6.addWidget(self.tripTimeSensitiveDateTimeEdit)


        self.gridLayout.addWidget(self.widget_4, 3, 1, 1, 1)


        self.verticalLayout_4.addWidget(self.tripEditWidget)

        self.travelEditWidget = QWidget(self.scrollAreaWidgetContent)
        self.travelEditWidget.setObjectName(u"travelEditWidget")
        self.gridLayout_2 = QGridLayout(self.travelEditWidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.travelInfoTextEdit = QTextEdit(self.travelEditWidget)
        self.travelInfoTextEdit.setObjectName(u"travelInfoTextEdit")
        sizePolicy4.setHeightForWidth(self.travelInfoTextEdit.sizePolicy().hasHeightForWidth())
        self.travelInfoTextEdit.setSizePolicy(sizePolicy4)
        self.travelInfoTextEdit.setMinimumSize(QSize(0, 50))

        self.gridLayout_2.addWidget(self.travelInfoTextEdit, 5, 2, 1, 2)

        self.label_9 = QLabel(self.travelEditWidget)
        self.label_9.setObjectName(u"label_9")

        self.gridLayout_2.addWidget(self.label_9, 0, 0, 1, 2)

        self.widget_5 = QWidget(self.travelEditWidget)
        self.widget_5.setObjectName(u"widget_5")
        self.verticalLayout_7 = QVBoxLayout(self.widget_5)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.travelTimeSensitiveCheckBox = QCheckBox(self.widget_5)
        self.travelTimeSensitiveCheckBox.setObjectName(u"travelTimeSensitiveCheckBox")

        self.verticalLayout_7.addWidget(self.travelTimeSensitiveCheckBox)

        self.travelTimeSensitiveDateTimeEdit = QDateTimeEdit(self.widget_5)
        self.travelTimeSensitiveDateTimeEdit.setObjectName(u"travelTimeSensitiveDateTimeEdit")
        self.travelTimeSensitiveDateTimeEdit.setCalendarPopup(True)

        self.verticalLayout_7.addWidget(self.travelTimeSensitiveDateTimeEdit)


        self.gridLayout_2.addWidget(self.widget_5, 4, 2, 1, 2)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_10 = QLabel(self.travelEditWidget)
        self.label_10.setObjectName(u"label_10")
        sizePolicy3.setHeightForWidth(self.label_10.sizePolicy().hasHeightForWidth())
        self.label_10.setSizePolicy(sizePolicy3)

        self.horizontalLayout_4.addWidget(self.label_10)

        self.travelFromDateTimeEdit = QDateTimeEdit(self.travelEditWidget)
        self.travelFromDateTimeEdit.setObjectName(u"travelFromDateTimeEdit")
        sizePolicy6.setHeightForWidth(self.travelFromDateTimeEdit.sizePolicy().hasHeightForWidth())
        self.travelFromDateTimeEdit.setSizePolicy(sizePolicy6)
        self.travelFromDateTimeEdit.setCalendarPopup(True)

        self.horizontalLayout_4.addWidget(self.travelFromDateTimeEdit)

        self.label_11 = QLabel(self.travelEditWidget)
        self.label_11.setObjectName(u"label_11")
        sizePolicy5.setHeightForWidth(self.label_11.sizePolicy().hasHeightForWidth())
        self.label_11.setSizePolicy(sizePolicy5)

        self.horizontalLayout_4.addWidget(self.label_11)

        self.travelToDateTimeEdit = QDateTimeEdit(self.travelEditWidget)
        self.travelToDateTimeEdit.setObjectName(u"travelToDateTimeEdit")
        sizePolicy6.setHeightForWidth(self.travelToDateTimeEdit.sizePolicy().hasHeightForWidth())
        self.travelToDateTimeEdit.setSizePolicy(sizePolicy6)
        self.travelToDateTimeEdit.setCalendarPopup(True)

        self.horizontalLayout_4.addWidget(self.travelToDateTimeEdit)


        self.gridLayout_2.addLayout(self.horizontalLayout_4, 1, 2, 1, 2)

        self.label_13 = QLabel(self.travelEditWidget)
        self.label_13.setObjectName(u"label_13")

        self.gridLayout_2.addWidget(self.label_13, 2, 0, 1, 1)

        self.travelTicketWidget = QWidget(self.travelEditWidget)
        self.travelTicketWidget.setObjectName(u"travelTicketWidget")
        self.gridLayout_3 = QGridLayout(self.travelTicketWidget)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.label_14 = QLabel(self.travelTicketWidget)
        self.label_14.setObjectName(u"label_14")

        self.gridLayout_3.addWidget(self.label_14, 0, 0, 1, 1)

        self.travelTicketPriceLineEdit = QLineEdit(self.travelTicketWidget)
        self.travelTicketPriceLineEdit.setObjectName(u"travelTicketPriceLineEdit")

        self.gridLayout_3.addWidget(self.travelTicketPriceLineEdit, 0, 1, 1, 1)


        self.gridLayout_2.addWidget(self.travelTicketWidget, 3, 2, 1, 2)

        self.label_15 = QLabel(self.travelEditWidget)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_2.addWidget(self.label_15, 4, 0, 1, 1)

        self.label_16 = QLabel(self.travelEditWidget)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_2.addWidget(self.label_16, 5, 0, 1, 1)

        self.label_12 = QLabel(self.travelEditWidget)
        self.label_12.setObjectName(u"label_12")

        self.gridLayout_2.addWidget(self.label_12, 1, 0, 1, 1)

        self.travelNameLineEdit = QLineEdit(self.travelEditWidget)
        self.travelNameLineEdit.setObjectName(u"travelNameLineEdit")

        self.gridLayout_2.addWidget(self.travelNameLineEdit, 0, 2, 1, 2)

        self.travelTicketCheckBox = QCheckBox(self.travelEditWidget)
        self.travelTicketCheckBox.setObjectName(u"travelTicketCheckBox")

        self.gridLayout_2.addWidget(self.travelTicketCheckBox, 2, 2, 1, 2)


        self.verticalLayout_4.addWidget(self.travelEditWidget)

        self.placeEditWidget = QWidget(self.scrollAreaWidgetContent)
        self.placeEditWidget.setObjectName(u"placeEditWidget")
        self.gridLayout_4 = QGridLayout(self.placeEditWidget)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.label_17 = QLabel(self.placeEditWidget)
        self.label_17.setObjectName(u"label_17")

        self.gridLayout_4.addWidget(self.label_17, 0, 1, 1, 1)

        self.placeNameLineEdit = QLineEdit(self.placeEditWidget)
        self.placeNameLineEdit.setObjectName(u"placeNameLineEdit")

        self.gridLayout_4.addWidget(self.placeNameLineEdit, 0, 3, 1, 1)

        self.label_25 = QLabel(self.placeEditWidget)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_4.addWidget(self.label_25, 7, 1, 1, 1)

        self.checkBox_5 = QCheckBox(self.placeEditWidget)
        self.checkBox_5.setObjectName(u"checkBox_5")

        self.gridLayout_4.addWidget(self.checkBox_5, 3, 3, 1, 1)

        self.placeOpenHoursWidget = QWidget(self.placeEditWidget)
        self.placeOpenHoursWidget.setObjectName(u"placeOpenHoursWidget")
        self.verticalLayout_9 = QVBoxLayout(self.placeOpenHoursWidget)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.horizontalWidget_5 = QWidget(self.placeOpenHoursWidget)
        self.horizontalWidget_5.setObjectName(u"horizontalWidget_5")
        self.horizontalLayout_5 = QHBoxLayout(self.horizontalWidget_5)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_19 = QLabel(self.horizontalWidget_5)
        self.label_19.setObjectName(u"label_19")
        sizePolicy3.setHeightForWidth(self.label_19.sizePolicy().hasHeightForWidth())
        self.label_19.setSizePolicy(sizePolicy3)

        self.horizontalLayout_5.addWidget(self.label_19)

        self.placeOpenHoursFromTimeEdit = QTimeEdit(self.horizontalWidget_5)
        self.placeOpenHoursFromTimeEdit.setObjectName(u"placeOpenHoursFromTimeEdit")
        self.placeOpenHoursFromTimeEdit.setButtonSymbols(QAbstractSpinBox.NoButtons)

        self.horizontalLayout_5.addWidget(self.placeOpenHoursFromTimeEdit)

        self.label_20 = QLabel(self.horizontalWidget_5)
        self.label_20.setObjectName(u"label_20")
        sizePolicy5.setHeightForWidth(self.label_20.sizePolicy().hasHeightForWidth())
        self.label_20.setSizePolicy(sizePolicy5)

        self.horizontalLayout_5.addWidget(self.label_20)

        self.placeOpenHoursToTimeEdit = QTimeEdit(self.horizontalWidget_5)
        self.placeOpenHoursToTimeEdit.setObjectName(u"placeOpenHoursToTimeEdit")
        self.placeOpenHoursToTimeEdit.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.placeOpenHoursToTimeEdit.setCalendarPopup(False)

        self.horizontalLayout_5.addWidget(self.placeOpenHoursToTimeEdit)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_2)


        self.verticalLayout_9.addWidget(self.horizontalWidget_5)

        self.placeOpenHoursInfoLineEdit = QLineEdit(self.placeOpenHoursWidget)
        self.placeOpenHoursInfoLineEdit.setObjectName(u"placeOpenHoursInfoLineEdit")

        self.verticalLayout_9.addWidget(self.placeOpenHoursInfoLineEdit)


        self.gridLayout_4.addWidget(self.placeOpenHoursWidget, 4, 3, 1, 1)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_22 = QLabel(self.placeEditWidget)
        self.label_22.setObjectName(u"label_22")
        sizePolicy3.setHeightForWidth(self.label_22.sizePolicy().hasHeightForWidth())
        self.label_22.setSizePolicy(sizePolicy3)

        self.horizontalLayout_6.addWidget(self.label_22)

        self.placeFromDateTimeEdit = QDateTimeEdit(self.placeEditWidget)
        self.placeFromDateTimeEdit.setObjectName(u"placeFromDateTimeEdit")
        sizePolicy6.setHeightForWidth(self.placeFromDateTimeEdit.sizePolicy().hasHeightForWidth())
        self.placeFromDateTimeEdit.setSizePolicy(sizePolicy6)
        self.placeFromDateTimeEdit.setCalendarPopup(True)

        self.horizontalLayout_6.addWidget(self.placeFromDateTimeEdit)

        self.label_23 = QLabel(self.placeEditWidget)
        self.label_23.setObjectName(u"label_23")
        sizePolicy5.setHeightForWidth(self.label_23.sizePolicy().hasHeightForWidth())
        self.label_23.setSizePolicy(sizePolicy5)

        self.horizontalLayout_6.addWidget(self.label_23)

        self.placeToDateTimeEdit = QDateTimeEdit(self.placeEditWidget)
        self.placeToDateTimeEdit.setObjectName(u"placeToDateTimeEdit")
        sizePolicy6.setHeightForWidth(self.placeToDateTimeEdit.sizePolicy().hasHeightForWidth())
        self.placeToDateTimeEdit.setSizePolicy(sizePolicy6)
        self.placeToDateTimeEdit.setCalendarPopup(True)

        self.horizontalLayout_6.addWidget(self.placeToDateTimeEdit)


        self.gridLayout_4.addLayout(self.horizontalLayout_6, 1, 3, 1, 1)

        self.label_24 = QLabel(self.placeEditWidget)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_4.addWidget(self.label_24, 6, 1, 1, 1)

        self.label_21 = QLabel(self.placeEditWidget)
        self.label_21.setObjectName(u"label_21")

        self.gridLayout_4.addWidget(self.label_21, 1, 1, 1, 1)

        self.placeTimeSensitiveWidget = QWidget(self.placeEditWidget)
        self.placeTimeSensitiveWidget.setObjectName(u"placeTimeSensitiveWidget")
        self.verticalLayout_8 = QVBoxLayout(self.placeTimeSensitiveWidget)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.placeTimeSensitiveCheckBox = QCheckBox(self.placeTimeSensitiveWidget)
        self.placeTimeSensitiveCheckBox.setObjectName(u"placeTimeSensitiveCheckBox")

        self.verticalLayout_8.addWidget(self.placeTimeSensitiveCheckBox)

        self.placeTimeSensitiveDateTimeEdit = QDateTimeEdit(self.placeTimeSensitiveWidget)
        self.placeTimeSensitiveDateTimeEdit.setObjectName(u"placeTimeSensitiveDateTimeEdit")
        self.placeTimeSensitiveDateTimeEdit.setCalendarPopup(True)

        self.verticalLayout_8.addWidget(self.placeTimeSensitiveDateTimeEdit)


        self.gridLayout_4.addWidget(self.placeTimeSensitiveWidget, 6, 3, 1, 1)

        self.placeInfoTextEdit = QTextEdit(self.placeEditWidget)
        self.placeInfoTextEdit.setObjectName(u"placeInfoTextEdit")
        sizePolicy4.setHeightForWidth(self.placeInfoTextEdit.sizePolicy().hasHeightForWidth())
        self.placeInfoTextEdit.setSizePolicy(sizePolicy4)
        self.placeInfoTextEdit.setMinimumSize(QSize(0, 50))

        self.gridLayout_4.addWidget(self.placeInfoTextEdit, 7, 3, 1, 1)

        self.label_18 = QLabel(self.placeEditWidget)
        self.label_18.setObjectName(u"label_18")

        self.gridLayout_4.addWidget(self.label_18, 3, 1, 1, 1)


        self.verticalLayout_4.addWidget(self.placeEditWidget)

        self.eventEditWidget = QWidget(self.scrollAreaWidgetContent)
        self.eventEditWidget.setObjectName(u"eventEditWidget")
        self.gridLayout_6 = QGridLayout(self.eventEditWidget)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.label_40 = QLabel(self.eventEditWidget)
        self.label_40.setObjectName(u"label_40")

        self.gridLayout_6.addWidget(self.label_40, 2, 0, 1, 1)

        self.eventTicketCheckBox = QCheckBox(self.eventEditWidget)
        self.eventTicketCheckBox.setObjectName(u"eventTicketCheckBox")

        self.gridLayout_6.addWidget(self.eventTicketCheckBox, 3, 2, 1, 2)

        self.label_38 = QLabel(self.eventEditWidget)
        self.label_38.setObjectName(u"label_38")
        self.label_38.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_6.addWidget(self.label_38, 5, 0, 1, 1)

        self.label_39 = QLabel(self.eventEditWidget)
        self.label_39.setObjectName(u"label_39")
        self.label_39.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_6.addWidget(self.label_39, 6, 0, 1, 1)

        self.eventTimeSensitiveWidget = QWidget(self.eventEditWidget)
        self.eventTimeSensitiveWidget.setObjectName(u"eventTimeSensitiveWidget")
        self.verticalLayout_11 = QVBoxLayout(self.eventTimeSensitiveWidget)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.eventTimeSensitiveCheckBox = QCheckBox(self.eventTimeSensitiveWidget)
        self.eventTimeSensitiveCheckBox.setObjectName(u"eventTimeSensitiveCheckBox")

        self.verticalLayout_11.addWidget(self.eventTimeSensitiveCheckBox)

        self.eventTimeSensitiveDateTimeEdit = QDateTimeEdit(self.eventTimeSensitiveWidget)
        self.eventTimeSensitiveDateTimeEdit.setObjectName(u"eventTimeSensitiveDateTimeEdit")
        self.eventTimeSensitiveDateTimeEdit.setCalendarPopup(True)

        self.verticalLayout_11.addWidget(self.eventTimeSensitiveDateTimeEdit)


        self.gridLayout_6.addWidget(self.eventTimeSensitiveWidget, 5, 2, 1, 2)

        self.label_36 = QLabel(self.eventEditWidget)
        self.label_36.setObjectName(u"label_36")

        self.gridLayout_6.addWidget(self.label_36, 3, 0, 1, 1)

        self.eventTicketWidget = QWidget(self.eventEditWidget)
        self.eventTicketWidget.setObjectName(u"eventTicketWidget")
        self.gridLayout_7 = QGridLayout(self.eventTicketWidget)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.label_37 = QLabel(self.eventTicketWidget)
        self.label_37.setObjectName(u"label_37")

        self.gridLayout_7.addWidget(self.label_37, 0, 0, 1, 1)

        self.eventTicketPriceLineEdit = QLineEdit(self.eventTicketWidget)
        self.eventTicketPriceLineEdit.setObjectName(u"eventTicketPriceLineEdit")

        self.gridLayout_7.addWidget(self.eventTicketPriceLineEdit, 0, 1, 1, 1)


        self.gridLayout_6.addWidget(self.eventTicketWidget, 4, 2, 1, 2)

        self.eventNameLineEdit = QLineEdit(self.eventEditWidget)
        self.eventNameLineEdit.setObjectName(u"eventNameLineEdit")

        self.gridLayout_6.addWidget(self.eventNameLineEdit, 0, 2, 1, 2)

        self.label_33 = QLabel(self.eventEditWidget)
        self.label_33.setObjectName(u"label_33")

        self.gridLayout_6.addWidget(self.label_33, 0, 0, 1, 2)

        self.eventInfoTextEdit = QTextEdit(self.eventEditWidget)
        self.eventInfoTextEdit.setObjectName(u"eventInfoTextEdit")
        sizePolicy4.setHeightForWidth(self.eventInfoTextEdit.sizePolicy().hasHeightForWidth())
        self.eventInfoTextEdit.setSizePolicy(sizePolicy4)
        self.eventInfoTextEdit.setMinimumSize(QSize(0, 50))

        self.gridLayout_6.addWidget(self.eventInfoTextEdit, 6, 2, 1, 2)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label_34 = QLabel(self.eventEditWidget)
        self.label_34.setObjectName(u"label_34")
        sizePolicy3.setHeightForWidth(self.label_34.sizePolicy().hasHeightForWidth())
        self.label_34.setSizePolicy(sizePolicy3)

        self.horizontalLayout_8.addWidget(self.label_34)

        self.eventFromDateTimeEdit = QDateTimeEdit(self.eventEditWidget)
        self.eventFromDateTimeEdit.setObjectName(u"eventFromDateTimeEdit")
        sizePolicy6.setHeightForWidth(self.eventFromDateTimeEdit.sizePolicy().hasHeightForWidth())
        self.eventFromDateTimeEdit.setSizePolicy(sizePolicy6)
        self.eventFromDateTimeEdit.setCalendarPopup(True)

        self.horizontalLayout_8.addWidget(self.eventFromDateTimeEdit)

        self.label_35 = QLabel(self.eventEditWidget)
        self.label_35.setObjectName(u"label_35")
        sizePolicy5.setHeightForWidth(self.label_35.sizePolicy().hasHeightForWidth())
        self.label_35.setSizePolicy(sizePolicy5)

        self.horizontalLayout_8.addWidget(self.label_35)

        self.eventToDateTimeEdit = QDateTimeEdit(self.eventEditWidget)
        self.eventToDateTimeEdit.setObjectName(u"eventToDateTimeEdit")
        sizePolicy6.setHeightForWidth(self.eventToDateTimeEdit.sizePolicy().hasHeightForWidth())
        self.eventToDateTimeEdit.setSizePolicy(sizePolicy6)
        self.eventToDateTimeEdit.setCalendarPopup(True)

        self.horizontalLayout_8.addWidget(self.eventToDateTimeEdit)


        self.gridLayout_6.addLayout(self.horizontalLayout_8, 2, 2, 1, 2)

        self.label_41 = QLabel(self.eventEditWidget)
        self.label_41.setObjectName(u"label_41")

        self.gridLayout_6.addWidget(self.label_41, 1, 0, 1, 1)

        self.eventTypeLineEdit = QLineEdit(self.eventEditWidget)
        self.eventTypeLineEdit.setObjectName(u"eventTypeLineEdit")

        self.gridLayout_6.addWidget(self.eventTypeLineEdit, 1, 2, 1, 1)


        self.verticalLayout_4.addWidget(self.eventEditWidget)

        self.eatEditWidget = QWidget(self.scrollAreaWidgetContent)
        self.eatEditWidget.setObjectName(u"eatEditWidget")
        self.gridLayout_8 = QGridLayout(self.eatEditWidget)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.label_42 = QLabel(self.eatEditWidget)
        self.label_42.setObjectName(u"label_42")
        sizePolicy3.setHeightForWidth(self.label_42.sizePolicy().hasHeightForWidth())
        self.label_42.setSizePolicy(sizePolicy3)

        self.horizontalLayout_9.addWidget(self.label_42)

        self.eatFromDateTimeEdit = QDateTimeEdit(self.eatEditWidget)
        self.eatFromDateTimeEdit.setObjectName(u"eatFromDateTimeEdit")
        sizePolicy6.setHeightForWidth(self.eatFromDateTimeEdit.sizePolicy().hasHeightForWidth())
        self.eatFromDateTimeEdit.setSizePolicy(sizePolicy6)
        self.eatFromDateTimeEdit.setCalendarPopup(True)

        self.horizontalLayout_9.addWidget(self.eatFromDateTimeEdit)

        self.label_43 = QLabel(self.eatEditWidget)
        self.label_43.setObjectName(u"label_43")
        sizePolicy5.setHeightForWidth(self.label_43.sizePolicy().hasHeightForWidth())
        self.label_43.setSizePolicy(sizePolicy5)

        self.horizontalLayout_9.addWidget(self.label_43)

        self.eatToDateTimeEdit = QDateTimeEdit(self.eatEditWidget)
        self.eatToDateTimeEdit.setObjectName(u"eatToDateTimeEdit")
        sizePolicy6.setHeightForWidth(self.eatToDateTimeEdit.sizePolicy().hasHeightForWidth())
        self.eatToDateTimeEdit.setSizePolicy(sizePolicy6)
        self.eatToDateTimeEdit.setCalendarPopup(True)

        self.horizontalLayout_9.addWidget(self.eatToDateTimeEdit)


        self.gridLayout_8.addLayout(self.horizontalLayout_9, 2, 1, 1, 1)

        self.label_44 = QLabel(self.eatEditWidget)
        self.label_44.setObjectName(u"label_44")
        self.label_44.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_8.addWidget(self.label_44, 4, 0, 1, 1)

        self.eatTimeSensitiveWidget = QWidget(self.eatEditWidget)
        self.eatTimeSensitiveWidget.setObjectName(u"eatTimeSensitiveWidget")
        self.verticalLayout_12 = QVBoxLayout(self.eatTimeSensitiveWidget)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.eatTimeSensitiveCheckBox = QCheckBox(self.eatTimeSensitiveWidget)
        self.eatTimeSensitiveCheckBox.setObjectName(u"eatTimeSensitiveCheckBox")

        self.verticalLayout_12.addWidget(self.eatTimeSensitiveCheckBox)

        self.eatTimeSensitiveDateTimeEdit = QDateTimeEdit(self.eatTimeSensitiveWidget)
        self.eatTimeSensitiveDateTimeEdit.setObjectName(u"eatTimeSensitiveDateTimeEdit")
        self.eatTimeSensitiveDateTimeEdit.setCalendarPopup(True)

        self.verticalLayout_12.addWidget(self.eatTimeSensitiveDateTimeEdit)


        self.gridLayout_8.addWidget(self.eatTimeSensitiveWidget, 4, 1, 1, 1)

        self.label_45 = QLabel(self.eatEditWidget)
        self.label_45.setObjectName(u"label_45")

        self.gridLayout_8.addWidget(self.label_45, 2, 0, 1, 1)

        self.label_46 = QLabel(self.eatEditWidget)
        self.label_46.setObjectName(u"label_46")
        self.label_46.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_8.addWidget(self.label_46, 6, 0, 1, 1)

        self.eatInfoTextEdit = QTextEdit(self.eatEditWidget)
        self.eatInfoTextEdit.setObjectName(u"eatInfoTextEdit")
        sizePolicy4.setHeightForWidth(self.eatInfoTextEdit.sizePolicy().hasHeightForWidth())
        self.eatInfoTextEdit.setSizePolicy(sizePolicy4)
        self.eatInfoTextEdit.setMinimumSize(QSize(0, 50))

        self.gridLayout_8.addWidget(self.eatInfoTextEdit, 6, 1, 1, 1)

        self.eatNameLineEdit = QLineEdit(self.eatEditWidget)
        self.eatNameLineEdit.setObjectName(u"eatNameLineEdit")

        self.gridLayout_8.addWidget(self.eatNameLineEdit, 1, 1, 1, 1)

        self.label_47 = QLabel(self.eatEditWidget)
        self.label_47.setObjectName(u"label_47")

        self.gridLayout_8.addWidget(self.label_47, 1, 0, 1, 1)

        self.label_48 = QLabel(self.eatEditWidget)
        self.label_48.setObjectName(u"label_48")

        self.gridLayout_8.addWidget(self.label_48, 3, 0, 1, 1)

        self.eatReservationCheckBox = QCheckBox(self.eatEditWidget)
        self.eatReservationCheckBox.setObjectName(u"eatReservationCheckBox")

        self.gridLayout_8.addWidget(self.eatReservationCheckBox, 3, 1, 1, 1)


        self.verticalLayout_4.addWidget(self.eatEditWidget)

        self.stayEditWidget = QWidget(self.scrollAreaWidgetContent)
        self.stayEditWidget.setObjectName(u"stayEditWidget")
        self.gridLayout_5 = QGridLayout(self.stayEditWidget)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_28 = QLabel(self.stayEditWidget)
        self.label_28.setObjectName(u"label_28")
        sizePolicy3.setHeightForWidth(self.label_28.sizePolicy().hasHeightForWidth())
        self.label_28.setSizePolicy(sizePolicy3)

        self.horizontalLayout_7.addWidget(self.label_28)

        self.stayFromDateTimeEdit = QDateTimeEdit(self.stayEditWidget)
        self.stayFromDateTimeEdit.setObjectName(u"stayFromDateTimeEdit")
        sizePolicy6.setHeightForWidth(self.stayFromDateTimeEdit.sizePolicy().hasHeightForWidth())
        self.stayFromDateTimeEdit.setSizePolicy(sizePolicy6)
        self.stayFromDateTimeEdit.setCalendarPopup(True)

        self.horizontalLayout_7.addWidget(self.stayFromDateTimeEdit)

        self.label_29 = QLabel(self.stayEditWidget)
        self.label_29.setObjectName(u"label_29")
        sizePolicy5.setHeightForWidth(self.label_29.sizePolicy().hasHeightForWidth())
        self.label_29.setSizePolicy(sizePolicy5)

        self.horizontalLayout_7.addWidget(self.label_29)

        self.stayToDateTimeEdit = QDateTimeEdit(self.stayEditWidget)
        self.stayToDateTimeEdit.setObjectName(u"stayToDateTimeEdit")
        sizePolicy6.setHeightForWidth(self.stayToDateTimeEdit.sizePolicy().hasHeightForWidth())
        self.stayToDateTimeEdit.setSizePolicy(sizePolicy6)
        self.stayToDateTimeEdit.setCalendarPopup(True)

        self.horizontalLayout_7.addWidget(self.stayToDateTimeEdit)


        self.gridLayout_5.addLayout(self.horizontalLayout_7, 2, 1, 1, 1)

        self.stayNameLineEdit = QLineEdit(self.stayEditWidget)
        self.stayNameLineEdit.setObjectName(u"stayNameLineEdit")

        self.gridLayout_5.addWidget(self.stayNameLineEdit, 1, 1, 1, 1)

        self.label_31 = QLabel(self.stayEditWidget)
        self.label_31.setObjectName(u"label_31")
        self.label_31.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_5.addWidget(self.label_31, 6, 0, 1, 1)

        self.label_30 = QLabel(self.stayEditWidget)
        self.label_30.setObjectName(u"label_30")

        self.gridLayout_5.addWidget(self.label_30, 4, 0, 1, 1)

        self.stayTimeSensitiveWidget = QWidget(self.stayEditWidget)
        self.stayTimeSensitiveWidget.setObjectName(u"stayTimeSensitiveWidget")
        self.verticalLayout_10 = QVBoxLayout(self.stayTimeSensitiveWidget)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.stayTimeSensitiveCheckBox = QCheckBox(self.stayTimeSensitiveWidget)
        self.stayTimeSensitiveCheckBox.setObjectName(u"stayTimeSensitiveCheckBox")

        self.verticalLayout_10.addWidget(self.stayTimeSensitiveCheckBox)

        self.stayTimeSensitiveDateTimeEdit = QDateTimeEdit(self.stayTimeSensitiveWidget)
        self.stayTimeSensitiveDateTimeEdit.setObjectName(u"stayTimeSensitiveDateTimeEdit")
        self.stayTimeSensitiveDateTimeEdit.setCalendarPopup(True)

        self.verticalLayout_10.addWidget(self.stayTimeSensitiveDateTimeEdit)


        self.gridLayout_5.addWidget(self.stayTimeSensitiveWidget, 6, 1, 1, 1)

        self.label_26 = QLabel(self.stayEditWidget)
        self.label_26.setObjectName(u"label_26")

        self.gridLayout_5.addWidget(self.label_26, 1, 0, 1, 1)

        self.label_27 = QLabel(self.stayEditWidget)
        self.label_27.setObjectName(u"label_27")

        self.gridLayout_5.addWidget(self.label_27, 2, 0, 1, 1)

        self.label_32 = QLabel(self.stayEditWidget)
        self.label_32.setObjectName(u"label_32")
        self.label_32.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_5.addWidget(self.label_32, 8, 0, 1, 1)

        self.tripInfoTextEdit_4 = QTextEdit(self.stayEditWidget)
        self.tripInfoTextEdit_4.setObjectName(u"tripInfoTextEdit_4")
        sizePolicy4.setHeightForWidth(self.tripInfoTextEdit_4.sizePolicy().hasHeightForWidth())
        self.tripInfoTextEdit_4.setSizePolicy(sizePolicy4)
        self.tripInfoTextEdit_4.setMinimumSize(QSize(0, 50))

        self.gridLayout_5.addWidget(self.tripInfoTextEdit_4, 8, 1, 1, 1)

        self.stayPricingWidget = QWidget(self.stayEditWidget)
        self.stayPricingWidget.setObjectName(u"stayPricingWidget")
        self.verticalLayout_13 = QVBoxLayout(self.stayPricingWidget)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.stayPricingFlatRateCheckBox = QCheckBox(self.stayPricingWidget)
        self.stayPricingFlatRateCheckBox.setObjectName(u"stayPricingFlatRateCheckBox")

        self.verticalLayout_13.addWidget(self.stayPricingFlatRateCheckBox)

        self.stayPricingPricePerNightCheckBox = QCheckBox(self.stayPricingWidget)
        self.stayPricingPricePerNightCheckBox.setObjectName(u"stayPricingPricePerNightCheckBox")

        self.verticalLayout_13.addWidget(self.stayPricingPricePerNightCheckBox)

        self.widget_11 = QWidget(self.stayPricingWidget)
        self.widget_11.setObjectName(u"widget_11")
        self.gridLayout_9 = QGridLayout(self.widget_11)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.label_49 = QLabel(self.widget_11)
        self.label_49.setObjectName(u"label_49")

        self.gridLayout_9.addWidget(self.label_49, 0, 0, 1, 1)

        self.stayFlatPriceLineEdit = QLineEdit(self.widget_11)
        self.stayFlatPriceLineEdit.setObjectName(u"stayFlatPriceLineEdit")

        self.gridLayout_9.addWidget(self.stayFlatPriceLineEdit, 0, 1, 1, 1)


        self.verticalLayout_13.addWidget(self.widget_11)

        self.stayPricingPricePerNightWidget = QWidget(self.stayPricingWidget)
        self.stayPricingPricePerNightWidget.setObjectName(u"stayPricingPricePerNightWidget")
        self.gridLayout_10 = QGridLayout(self.stayPricingPricePerNightWidget)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.stayPricePerNightLineEdit = QLineEdit(self.stayPricingPricePerNightWidget)
        self.stayPricePerNightLineEdit.setObjectName(u"stayPricePerNightLineEdit")

        self.gridLayout_10.addWidget(self.stayPricePerNightLineEdit, 0, 1, 1, 1)

        self.label_50 = QLabel(self.stayPricingPricePerNightWidget)
        self.label_50.setObjectName(u"label_50")

        self.gridLayout_10.addWidget(self.label_50, 0, 0, 1, 1)

        self.label_51 = QLabel(self.stayPricingPricePerNightWidget)
        self.label_51.setObjectName(u"label_51")

        self.gridLayout_10.addWidget(self.label_51, 1, 0, 1, 1)

        self.stayNumberOfNightLabel = QLabel(self.stayPricingPricePerNightWidget)
        self.stayNumberOfNightLabel.setObjectName(u"stayNumberOfNightLabel")
        self.stayNumberOfNightLabel.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_10.addWidget(self.stayNumberOfNightLabel, 1, 1, 1, 1)


        self.verticalLayout_13.addWidget(self.stayPricingPricePerNightWidget)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_11.addItem(self.horizontalSpacer_3)

        self.label_53 = QLabel(self.stayPricingWidget)
        self.label_53.setObjectName(u"label_53")

        self.horizontalLayout_11.addWidget(self.label_53)

        self.stayTotalPriceLabel = QLabel(self.stayPricingWidget)
        self.stayTotalPriceLabel.setObjectName(u"stayTotalPriceLabel")

        self.horizontalLayout_11.addWidget(self.stayTotalPriceLabel)


        self.verticalLayout_13.addLayout(self.horizontalLayout_11)


        self.gridLayout_5.addWidget(self.stayPricingWidget, 4, 1, 1, 1)


        self.verticalLayout_4.addWidget(self.stayEditWidget)

        self.scrollArea.setWidget(self.scrollAreaWidgetContent)

        self.horizontalLayout_2.addWidget(self.scrollArea)


        self.verticalLayout_3.addWidget(self.editWidget)

        self.okCancelLayout = QHBoxLayout()
        self.okCancelLayout.setObjectName(u"okCancelLayout")
        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.okCancelLayout.addItem(self.horizontalSpacer_4)

        self.okButton = QPushButton(self.widget)
        self.okButton.setObjectName(u"okButton")

        self.okCancelLayout.addWidget(self.okButton)

        self.cancelButton = QPushButton(self.widget)
        self.cancelButton.setObjectName(u"cancelButton")

        self.okCancelLayout.addWidget(self.cancelButton)


        self.verticalLayout_3.addLayout(self.okCancelLayout)

        self.errorLabel = QLabel(self.widget)
        self.errorLabel.setObjectName(u"errorLabel")
        self.errorLabel.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.verticalLayout_3.addWidget(self.errorLabel)


        self.verticalLayout.addWidget(self.widget)


        self.retranslateUi(Form)

        self.typeComboBox.setCurrentIndex(-1)


        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText(QCoreApplication.translate("Form", u"Type:", None))
        self.typeComboBox.setItemText(0, QCoreApplication.translate("Form", u"Trip", None))
        self.typeComboBox.setItemText(1, QCoreApplication.translate("Form", u"Travel", None))
        self.typeComboBox.setItemText(2, QCoreApplication.translate("Form", u"Place", None))
        self.typeComboBox.setItemText(3, QCoreApplication.translate("Form", u"Stay", None))
        self.typeComboBox.setItemText(4, QCoreApplication.translate("Form", u"Eat", None))
        self.typeComboBox.setItemText(5, QCoreApplication.translate("Form", u"Event", None))

        self.typeComboBox.setCurrentText("")
        self.typeComboBox.setPlaceholderText(QCoreApplication.translate("Form", u"Select component type", None))
        self.tripNameLineEdit.setText("")
        self.tripNameLineEdit.setPlaceholderText(QCoreApplication.translate("Form", u"Insert Trip Name", None))
        self.tripInfoTextEdit.setPlaceholderText(QCoreApplication.translate("Form", u"Insert general information here", None))
        self.tripAddReminderLineEdit.setPlaceholderText(QCoreApplication.translate("Form", u"Insert new reminders", None))
        self.tripAddReminderButton.setText(QCoreApplication.translate("Form", u"Add", None))
        self.label_7.setText(QCoreApplication.translate("Form", u"Time Sensitive:", None))
        self.label_8.setText(QCoreApplication.translate("Form", u"Information:", None))
        self.label_6.setText(QCoreApplication.translate("Form", u"Reminders:", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"Time:", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"Trip Name:", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"from ", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"to", None))
        self.tripTimeSensitiveCheckBox.setText(QCoreApplication.translate("Form", u"Remind me", None))
        self.travelInfoTextEdit.setPlaceholderText(QCoreApplication.translate("Form", u"Insert general information here", None))
        self.label_9.setText(QCoreApplication.translate("Form", u"Travel Name:", None))
        self.travelTimeSensitiveCheckBox.setText(QCoreApplication.translate("Form", u"Remind me", None))
        self.label_10.setText(QCoreApplication.translate("Form", u"from ", None))
        self.label_11.setText(QCoreApplication.translate("Form", u"to", None))
        self.label_13.setText(QCoreApplication.translate("Form", u"Ticket:", None))
        self.label_14.setText(QCoreApplication.translate("Form", u"Price:", None))
        self.travelTicketPriceLineEdit.setPlaceholderText(QCoreApplication.translate("Form", u"Insert price of the ticket", None))
        self.label_15.setText(QCoreApplication.translate("Form", u"Time Sensitive:", None))
        self.label_16.setText(QCoreApplication.translate("Form", u"Information:", None))
        self.label_12.setText(QCoreApplication.translate("Form", u"Time:", None))
        self.travelNameLineEdit.setPlaceholderText(QCoreApplication.translate("Form", u"Insert Travel Name", None))
        self.travelTicketCheckBox.setText(QCoreApplication.translate("Form", u"Tickets needed", None))
        self.label_17.setText(QCoreApplication.translate("Form", u"Place Name:", None))
        self.placeNameLineEdit.setPlaceholderText(QCoreApplication.translate("Form", u"Insert Place Name", None))
        self.label_25.setText(QCoreApplication.translate("Form", u"Information:", None))
        self.checkBox_5.setText(QCoreApplication.translate("Form", u"Add open hours", None))
        self.label_19.setText(QCoreApplication.translate("Form", u"from ", None))
        self.label_20.setText(QCoreApplication.translate("Form", u"to", None))
        self.placeOpenHoursInfoLineEdit.setPlaceholderText(QCoreApplication.translate("Form", u"Add additional information here (eg. \"Weekdays only\")", None))
        self.label_22.setText(QCoreApplication.translate("Form", u"from ", None))
        self.label_23.setText(QCoreApplication.translate("Form", u"to", None))
        self.label_24.setText(QCoreApplication.translate("Form", u"Time Sensitive:", None))
        self.label_21.setText(QCoreApplication.translate("Form", u"Time:", None))
        self.placeTimeSensitiveCheckBox.setText(QCoreApplication.translate("Form", u"Remind me", None))
        self.placeInfoTextEdit.setPlaceholderText(QCoreApplication.translate("Form", u"Insert general information here", None))
        self.label_18.setText(QCoreApplication.translate("Form", u"Open Hours:", None))
        self.label_40.setText(QCoreApplication.translate("Form", u"Time:", None))
        self.eventTicketCheckBox.setText(QCoreApplication.translate("Form", u"Tickets needed", None))
        self.label_38.setText(QCoreApplication.translate("Form", u"Time Sensitive:", None))
        self.label_39.setText(QCoreApplication.translate("Form", u"Information:", None))
        self.eventTimeSensitiveCheckBox.setText(QCoreApplication.translate("Form", u"Remind me", None))
        self.label_36.setText(QCoreApplication.translate("Form", u"Ticket:", None))
        self.label_37.setText(QCoreApplication.translate("Form", u"Price:", None))
        self.eventTicketPriceLineEdit.setPlaceholderText(QCoreApplication.translate("Form", u"Insert price of the ticket", None))
        self.eventNameLineEdit.setPlaceholderText(QCoreApplication.translate("Form", u"Insert Event Name", None))
        self.label_33.setText(QCoreApplication.translate("Form", u"Event Name:", None))
        self.eventInfoTextEdit.setPlaceholderText(QCoreApplication.translate("Form", u"Insert general information here", None))
        self.label_34.setText(QCoreApplication.translate("Form", u"from ", None))
        self.label_35.setText(QCoreApplication.translate("Form", u"to", None))
        self.label_41.setText(QCoreApplication.translate("Form", u"Type:", None))
        self.eventTypeLineEdit.setPlaceholderText(QCoreApplication.translate("Form", u"Insert event type (eg. Movies, Play, Show, etc.)", None))
        self.label_42.setText(QCoreApplication.translate("Form", u"from ", None))
        self.label_43.setText(QCoreApplication.translate("Form", u"to", None))
        self.label_44.setText(QCoreApplication.translate("Form", u"Time Sensitive:", None))
        self.eatTimeSensitiveCheckBox.setText(QCoreApplication.translate("Form", u"Remind me", None))
        self.label_45.setText(QCoreApplication.translate("Form", u"Time:", None))
        self.label_46.setText(QCoreApplication.translate("Form", u"Information:", None))
        self.eatInfoTextEdit.setPlaceholderText(QCoreApplication.translate("Form", u"Insert general information here", None))
        self.eatNameLineEdit.setText("")
        self.eatNameLineEdit.setPlaceholderText(QCoreApplication.translate("Form", u"Insert Restaurant Name", None))
        self.label_47.setText(QCoreApplication.translate("Form", u"Restaurant:", None))
        self.label_48.setText(QCoreApplication.translate("Form", u"Reservation:", None))
        self.eatReservationCheckBox.setText(QCoreApplication.translate("Form", u"Need reservation", None))
        self.label_28.setText(QCoreApplication.translate("Form", u"from ", None))
        self.label_29.setText(QCoreApplication.translate("Form", u"to", None))
        self.stayNameLineEdit.setText("")
        self.stayNameLineEdit.setPlaceholderText(QCoreApplication.translate("Form", u"Insert Accommodation Name", None))
        self.label_31.setText(QCoreApplication.translate("Form", u"Time Sensitive:", None))
        self.label_30.setText(QCoreApplication.translate("Form", u"Pricings:", None))
        self.stayTimeSensitiveCheckBox.setText(QCoreApplication.translate("Form", u"Remind me", None))
        self.label_26.setText(QCoreApplication.translate("Form", u"Accommodation:", None))
        self.label_27.setText(QCoreApplication.translate("Form", u"Time:", None))
        self.label_32.setText(QCoreApplication.translate("Form", u"Information:", None))
        self.tripInfoTextEdit_4.setPlaceholderText(QCoreApplication.translate("Form", u"Insert general information here", None))
        self.stayPricingFlatRateCheckBox.setText(QCoreApplication.translate("Form", u"Flat Rate", None))
        self.stayPricingPricePerNightCheckBox.setText(QCoreApplication.translate("Form", u"Price per night", None))
        self.label_49.setText(QCoreApplication.translate("Form", u"Flat Price:", None))
        self.label_50.setText(QCoreApplication.translate("Form", u"Price per night:", None))
        self.label_51.setText(QCoreApplication.translate("Form", u"Number of night(s):", None))
        self.stayNumberOfNightLabel.setText(QCoreApplication.translate("Form", u"#ofNights", None))
        self.label_53.setText(QCoreApplication.translate("Form", u"Total Price:", None))
        self.stayTotalPriceLabel.setText(QCoreApplication.translate("Form", u"#totalprice", None))
        self.okButton.setText(QCoreApplication.translate("Form", u"OK", None))
        self.cancelButton.setText(QCoreApplication.translate("Form", u"Cancel", None))
        self.errorLabel.setText(QCoreApplication.translate("Form", u"error", None))
    # retranslateUi

