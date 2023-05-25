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

        self.UI.typeComboBox.currentTextChanged.connect(self.typeComboBoxChanged)
        self.UI.okButton.clicked.connect(self.okButtonClicked)

    def typeComboBoxChanged(self):
        self.controller.typeChange()

    def okButtonClicked(self):
        self.controller.ok()
    
    def getSelectedType(self):
        return self.UI.typeComboBox.currentText()
    
    # Trip Info
    def getTripInfo(self):
        name = self.UI.tripNameLineEdit.text()
        timeFrom = self.UI.tripFromDateTimeEdit.dateTime()
        timeTo = self.UI.tripToDateTimeEdit.dateTime()
        remind = self.UI.tripTimeSensitiveCheckBox.isChecked()
        timesensitive = self.UI.tripTimeSensitiveDateTimeEdit.dateTime()
        info = self.UI.tripInfoTextEdit.toPlainText()

        tripInfo = {'name': name, 'timeFrom': timeFrom, 'timeTo': timeTo, 'remind': remind, 
                    'timesensitive': timesensitive, 'info': info}
        
        return tripInfo
    
    # Travel Info
    def getTravelInfo(self):
        name = self.UI.travelNameLineEdit.text()
        timeFrom = self.UI.travelFromDateTimeEdit.dateTime()
        timeTo = self.UI.travelToDateTimeEdit.dateTime()
        remind = self.UI.travelTimeSensitiveCheckBox.isChecked()
        timesensitive = self.UI.travelTimeSensitiveDateTimeEdit.dateTime()
        info = self.UI.travelInfoTextEdit.toPlainText()
        ticketNeed = self.UI.travelTicketCheckBox.isChecked()
        ticketPrice = self.UI.travelTicketPriceLineEdit.text()

        travelInfo = {'name': name, 'timeFrom': timeFrom, 'timeTo': timeTo, 'remind': remind,
                      'timesensitive': timesensitive, 'info': info,'ticketNeed': ticketNeed, 
                      'ticketPrice': ticketPrice}
        
        return travelInfo

    # Place Info
    def getPlaceInfo(self):
        name = self.UI.placeNameLineEdit.text()
        timeFrom = self.UI.placeFromDateTimeEdit.dateTime()
        timeTo = self.UI.placeToDateTimeEdit.dateTime()
        remind = self.UI.placeTimeSensitiveCheckBox.isChecked()
        timesensitive = self.UI.placeTimeSensitiveDateTimeEdit.dateTime()
        info = self.UI.placeInfoTextEdit.toPlainText()
        openTime = self.UI.placeOpenHoursFromTimeEdit.dateTime()
        closeTime = self.UI.placeOpenHoursToTimeEdit.dateTime()
        openInfo = self.UI.placeOpenHoursInfoLineEdit.text()

        placeInfo = {'name': name, 'timeFrom': timeFrom, 'timeTo': timeTo, 'remind': remind,
                     'timesensitive': timesensitive, 'info': info, 'openTime': openTime,
                     'closeTime': closeTime, 'openInfo': openInfo}
        
        return placeInfo

    # Eat Info
    def getEatInfo(self):
        name = self.UI.eatNameLineEdit.text()
        timeFrom = self.UI.eatFromDateTimeEdit.dateTime()
        timeTo = self.UI.eatToDateTimeEdit.dateTime()
        remind = self.UI.eatTimeSensitiveCheckBox.isChecked()
        timesensitive = self.UI.eatTimeSensitiveDateTimeEdit.dateTime()
        info = self.UI.eatInfoTextEdit.toPlainText()
        reservation = self.UI.eatReservationCheckBox.isChecked()

        eatInfo = {'name': name, 'timeFrom': timeFrom, 'timeTo': timeTo, 'remind': remind,
                      'timesensitive': timesensitive, 'info': info, 'reservation': reservation}
        
        return eatInfo

    # Event Info
    def getEventInfo(self):
        name = self.UI.eventNameLineEdit.text()
        timeFrom = self.UI.eventFromDateTimeEdit.dateTime()
        timeTo = self.UI.eventToDateTimeEdit.dateTime()
        remind = self.UI.eventTimeSensitiveCheckBox.isChecked()
        timesensitive = self.UI.eventTimeSensitiveDateTimeEdit.dateTime()
        info = self.UI.eventInfoTextEdit.toPlainText()
        type = self.UI.eventTypeLineEdit.text()
        ticketNeed = self.UI.eventTicketCheckBox.isChecked()
        ticketPrice = self.UI.eventTicketPriceLineEdit.text()

        eventInfo = {'name': name, 'timeFrom': timeFrom, 'timeTo': timeTo, 'remind': remind,
                     'timesensitive': timesensitive, 'info': info, 'type': type,
                     'ticketNeed': ticketNeed, 'ticketPrice': ticketPrice}
        
        return eventInfo

    # Stay Info
    def getStayInfo(self):
        name = self.UI.stayNameLineEdit.text()
        timeFrom = self.UI.stayFromDateTimeEdit.dateTime()
        timeTo = self.UI.stayToDateTimeEdit.dateTime()
        remind = self.UI.stayTimeSensitiveCheckBox.isChecked()
        timesensitive = self.UI.stayTimeSensitiveDateTimeEdit.dateTime()
        info = self.UI.tripInfoTextEdit_4.toPlainText()
        flatRate = self.UI.stayFlatPriceLineEdit.text()
        pricePerNight = self.UI.stayPricePerNightLineEdit.text()
        flatRateChecked = self.UI.stayPricingFlatRateCheckBox.isChecked()
        pricePNChecked = self.UI.stayPricingPricePerNightCheckBox.isChecked()

        stayInfo =  {'name': name, 'timeFrom': timeFrom, 'timeTo': timeTo, 'remind': remind,
                     'timesensitive': timesensitive, 'info': info, 'flatRate': flatRate,
                     'pricePerNight': pricePerNight, 'flatRateChecked': flatRateChecked, 'pricePerNightChecked': pricePNChecked}
        
        return stayInfo