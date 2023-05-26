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

        self.UI.tripAddReminderButton.clicked.connect(self.addReminderButtonClicked)

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
    