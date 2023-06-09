from editUI_ui import *
from PySide6.QtWidgets import QDialog
from PySide6 import QtCore

class ComponentEditUI(QDialog):
    def __init__(self, controller, parent=None) -> None:
        super().__init__(parent,Qt.WindowType.Dialog)
        self.controller = controller
        self.UI = Ui_Form()
        self.UI.setupUi(self)

        self.UI.tripFromDateTimeEdit.setDateTime(QtCore.QDateTime.currentDateTime())
        self.UI.tripToDateTimeEdit.setDateTime(QtCore.QDateTime.currentDateTime())
        self.UI.tripTimeSensitiveDateTimeEdit.setDateTime(QtCore.QDateTime.currentDateTime())

        self.UI.travelFromDateTimeEdit.setDateTime(QtCore.QDateTime.currentDateTime())
        self.UI.travelToDateTimeEdit.setDateTime(QtCore.QDateTime.currentDateTime())
        self.UI.travelTimeSensitiveDateTimeEdit.setDateTime(QtCore.QDateTime.currentDateTime())

        self.UI.placeFromDateTimeEdit.setDateTime(QtCore.QDateTime.currentDateTime())
        self.UI.placeToDateTimeEdit.setDateTime(QtCore.QDateTime.currentDateTime())
        self.UI.placeTimeSensitiveDateTimeEdit.setDateTime(QtCore.QDateTime.currentDateTime())

        self.UI.eventFromDateTimeEdit.setDateTime(QtCore.QDateTime.currentDateTime())
        self.UI.eventToDateTimeEdit.setDateTime(QtCore.QDateTime.currentDateTime())
        self.UI.eventTimeSensitiveDateTimeEdit.setDateTime(QtCore.QDateTime.currentDateTime())

        self.UI.eatFromDateTimeEdit.setDateTime(QtCore.QDateTime.currentDateTime())
        self.UI.eatToDateTimeEdit.setDateTime(QtCore.QDateTime.currentDateTime())
        self.UI.eatTimeSensitiveDateTimeEdit.setDateTime(QtCore.QDateTime.currentDateTime())

        self.UI.stayFromDateTimeEdit.setDateTime(QtCore.QDateTime.currentDateTime())
        self.UI.stayToDateTimeEdit.setDateTime(QtCore.QDateTime.currentDateTime())
        self.UI.stayTimeSensitiveDateTimeEdit.setDateTime(QtCore.QDateTime.currentDateTime())

        self.UI.typeComboBox.currentTextChanged.connect(self.typeComboBoxChanged)
        self.UI.okButton.clicked.connect(self.okButtonClicked)
        self.UI.cancelButton.clicked.connect(self.cancelButtonClicked)

        self.UI.stayNumberOfNightLabel.setText('')
        self.UI.stayFromDateTimeEdit.dateChanged.connect(self.setNight)
        self.UI.stayToDateTimeEdit.dateChanged.connect(self.setNight)

        self.UI.stayTotalPriceLabel.setText('0')
        self.UI.stayPricingFlatRateCheckBox.stateChanged.connect(self.setTotalPrice)
        self.UI.stayFlatPriceLineEdit.textChanged.connect(self.setTotalPrice)
        self.UI.stayPricingPricePerNightCheckBox.stateChanged.connect(self.setTotalPrice)
        self.UI.stayPricePerNightLineEdit.textChanged.connect(self.setTotalPrice)

        self.UI.placeOpenHoursFromTimeEdit.timeChanged.connect(self.placeOpenHoursFromChanged)

        self.UI.tripFromDateTimeEdit.dateTimeChanged.connect(self.tripFromDateChanged)
        self.UI.travelFromDateTimeEdit.dateTimeChanged.connect(self.travelFromDateChanged)
        self.UI.placeFromDateTimeEdit.dateTimeChanged.connect(self.placeFromDateChanged)
        self.UI.eventFromDateTimeEdit.dateTimeChanged.connect(self.eventFromDateChanged)
        self.UI.eatFromDateTimeEdit.dateTimeChanged.connect(self.eatFromDateChanged)
        self.UI.stayFromDateTimeEdit.dateTimeChanged.connect(self.stayFromDateChanged)

        self.UI.tripAddReminderButton.clicked.connect(self.addReminderButtonClicked)

        # hiding widgets
        self.UI.stayPricingFlatRateWidget.setVisible(False)
        self.UI.stayPricingPricePerNightWidget.setVisible(False)
        self.UI.placeOpenHoursWidget.setVisible(False)
        self.UI.eventTicketWidget.setVisible(False)
        self.UI.travelTicketWidget.setVisible(False)

    def typeComboBoxChanged(self):
        self.controller.typeChange()

    def okButtonClicked(self):
        self.controller.ok()
    
    def getSelectedType(self):
        return self.UI.typeComboBox.currentText()
    
    def cancelButtonClicked(self):
        self.controller.cancel()

    def addReminderButtonClicked(self):
        self.controller.addReminder()

    def setNight(self):
        self.controller.setNight()

    def setTotalPrice(self):
        self.controller.setTotalPrice()

    def tripFromDateChanged(self):
        self.controller.tripSetMinimumFinish()

    def travelFromDateChanged(self):
        self.controller.travelSetMinimumFinish()

    def placeFromDateChanged(self):
        self.controller.placeSetMinimumFinish()

    def eventFromDateChanged(self):
        self.controller.eventSetMinimumFinish()

    def eatFromDateChanged(self):
        self.controller.eatSetMinimumFinish()

    def stayFromDateChanged(self):
        self.controller.staySetMinimumFinish()
    
    def placeOpenHoursFromChanged(self):
        self.controller.placeSetMinimumOpenHoursTo()