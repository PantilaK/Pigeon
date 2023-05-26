from ComponentEditUI import *
from enum import IntEnum, Enum
from Reminder import Reminder
from datetime import date
from Tripcomponent import *

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from TripControl import TripController

class TypeString(str, Enum):
    trip = "Trip"
    travel = "Travel"
    place = "Place"
    stay = "Stay"
    eat = "Eat"
    event = "Event"

class TypeIndex(IntEnum):
    trip = 0
    travel = 1
    place = 2
    stay = 3
    eat = 4
    event = 5  

    #default placeholder
    none = -1

typeStringToIndexDict:dict[str,int] = {TypeString.trip:TypeIndex.trip,
                                        TypeString.travel:TypeIndex.travel,
                                        TypeString.place:TypeIndex.place,
                                        TypeString.stay:TypeIndex.stay,
                                        TypeString.event:TypeIndex.event,
                                        TypeString.eat:TypeIndex.eat}



class EditController:
    
    def __init__(self, model=None, typeEdit:str=TypeString.trip, canChangeType:bool = True, controller = None):
        self.view:ComponentEditUI = ComponentEditUI(self)
        self.currentShowMode:str = typeEdit
        self.canChangeType:bool = canChangeType
        self.model:"Stay" = model

        self.controller = controller

        if self.model is not None:
            t = type(self.model)

            if t == Trip:
                self.currentShowMode = TypeString.trip
                self.setTextEditTrip()
            elif t == Travel:
                self.currentShowMode = TypeString.travel
                self.setTextEditTravel()
            elif t == Place:
                self.currentShowMode = TypeString.place
                self.setTextPlaceEdit()
            elif t == Eat:
                print("Ea")
                self.currentShowMode = TypeString.eat
                self.setTextEatEdit()
            elif t == Event:
                self.currentShowMode = TypeString.event
                self.setTextEventEdit()
            elif t == Stay:
                self.currentShowMode = TypeString.stay
                self.setTextStayEdit()
            
            self.canChangeType = False


        self.subUIDict:dict[str,QWidget] = {TypeString.trip:self.view.UI.tripEditWidget,
                                            TypeString.travel:self.view.UI.travelEditWidget,
                                            TypeString.place:self.view.UI.placeEditWidget,
                                            TypeString.stay:self.view.UI.stayEditWidget,
                                            TypeString.eat:self.view.UI.eatEditWidget,
                                            TypeString.event:self.view.UI.eventEditWidget}
        self.clearErrorField()
        self.updateComboBox()
        self.toggleComboBox()
        self.updateUIType()

        self.view.exec()

    def typeChange(self):
        self.currentShowMode = self.view.UI.typeComboBox.currentText()
        
        if self.currentShowMode == TypeString.trip:
            self.reminders = []

        self.updateUIType()

    def updateComboBox(self):
        self.view.UI.typeComboBox.setCurrentIndex(typeStringToIndexDict[self.currentShowMode])

    def toggleComboBox(self):
        if self.canChangeType:
            self.view.UI.typeComboBox.setDisabled(False)
        else:
            self.view.UI.typeComboBox.setDisabled(True)

    def updateUIType(self):
        for k in self.subUIDict:
            self.subUIDict[k].setVisible(False)
        self.subUIDict[self.currentShowMode].setVisible(True)

    def clearErrorField(self):
        self.view.UI.errorLabel.setText(" ")

    def cancel(self):
        self.view.close()
        self.controller.update()

    def ok(self):
        source = self.view.getSelectedType()

        if source == TypeString.trip:
            info = self.getTripInfo()

            if self.model is None:
                self.controller.addTrip(info=info, reminders=self.reminders)
            else:
                self.controller.editTrip(info=info, reminders=self.reminders)
                self.controller.mainControl.update()

        elif source == TypeString.travel:
            info = self.getTravelInfo()

            if self.model is None:
                self.controller.addTravel(info=info)
            else:
                self.controller.editTravel(info=info)
                self.controller.mainControl.update()

        elif source == TypeString.place:
            info = self.getPlaceInfo()

            if self.model is None:
                self.controller.addPlace(info=info)
            else:
                self.controller.editPlace(info=info)
                self.controller.mainControl.update()

        elif source == TypeString.eat:
            info = self.getEatInfo()

            if self.model is None:
                self.controller.addEat(info=info)
            else:
                self.controller.editEat(info=info)
                self.controller.mainControl.update()

        elif source == TypeString.event:
            info = self.getEventInfo()

            if self.model is None:
                self.controller.addEvent(info=info)
            else:
                self.controller.editEvent(info=info)
                self.controller.mainControl.update()

        elif source == TypeString.stay:
            info = self.getStayInfo()

            if self.model is None:
                self.controller.addStay(info=info)
            else:
                self.controller.editStay(info=info)
                self.controller.mainControl.update()

        self.view.close()

    def addReminder(self):
        name = self.view.UI.tripAddReminderLineEdit.text()
        reminder= Reminder(name=name)

        self.reminders.append(reminder)
        self.view.UI.tripAddReminderLineEdit.setText("")

    def setTextEditTrip(self):
        self.view.UI.tripNameLineEdit.setText(self.model.getName())
        self.view.UI.tripFromDateTimeEdit.setDateTime(self.model.getTimeFrom())
        self.view.UI.tripToDateTimeEdit.setDateTime(self.model.getTimeTo())
        self.view.UI.tripTimeSensitiveCheckBox.setChecked(self.model.getRemind())
        self.view.UI.tripTimeSensitiveDateTimeEdit.setDateTime(self.model.getTimesensitive())
        self.view.UI.tripInfoTextEdit.setText(self.model.getInfo())

    def setTextEditTravel(self):
        self.view.UI.travelNameLineEdit.setText(self.model.getName())
        self.view.UI.travelFromDateTimeEdit.setDateTime(self.model.getTimeFrom())
        self.view.UI.travelToDateTimeEdit.setDateTime(self.model.getTimeTo())
        self.view.UI.travelTimeSensitiveCheckBox.setChecked(self.model.getRemind())
        self.view.UI.travelTimeSensitiveDateTimeEdit.setDateTime(self.model.getTimesensitive())
        self.view.UI.travelInfoTextEdit.setText(self.model.getInfo())
        self.view.UI.travelTicketCheckBox.setChecked(self.model.getTicketNeed())
        self.view.UI.travelTicketPriceLineEdit.setText(self.model.getTicketPrice())

    def setTextPlaceEdit(self):
        self.view.UI.placeNameLineEdit.setText(self.model.getName())
        self.view.UI.placeFromDateTimeEdit.setDateTime(self.model.getTimeFrom())
        self.view.UI.placeToDateTimeEdit.setDateTime(self.model.getTimeTo())
        self.view.UI.placeTimeSensitiveCheckBox.setChecked(self.model.getRemind())
        self.view.UI.placeTimeSensitiveDateTimeEdit.setDateTime(self.model.getTimesensitive())
        self.view.UI.placeInfoTextEdit.setText(self.model.getInfo())
        self.view.UI.placeOpenHoursFromTimeEdit.setDateTime(self.model.getOpenTime())
        self.view.UI.placeOpenHoursToTimeEdit.setDateTime(self.model.getCloseTime())
        self.view.UI.placeOpenHoursInfoLineEdit.setText(self.model.getOpenInfo())
        self.view.UI.checkBox_5.setChecked(self.model.getAddOpen())

    def setTextEatEdit(self):
        self.view.UI.eatNameLineEdit.setText(self.model.getName())
        self.view.UI.eatFromDateTimeEdit.setDateTime(self.model.getTimeFrom())
        self.view.UI.eatToDateTimeEdit.setDateTime(self.model.getTimeTo())
        self.view.UI.eatTimeSensitiveCheckBox.setChecked(self.model.getRemind())
        self.view.UI.eatTimeSensitiveDateTimeEdit.setDateTime(self.model.getTimesensitive())
        self.view.UI.eatInfoTextEdit.setText(self.model.getInfo())
        self.view.UI.eatReservationCheckBox.setChecked(self.model.getResevationNeed())

    def setTextEventEdit(self):
        self.view.UI.eventNameLineEdit.setText(self.model.getName())
        self.view.UI.eventFromDateTimeEdit.setDateTime(self.model.getTimeFrom())
        self.view.UI.eventToDateTimeEdit.setDateTime(self.model.getTimeTo())
        self.view.UI.eventTimeSensitiveCheckBox.setChecked(self.model.getRemind())
        self.view.UI.eventTimeSensitiveDateTimeEdit.setDateTime(self.model.getTimesensitive())
        self.view.UI.eventInfoTextEdit.setText(self.model.getInfo())
        self.view.UI.eventTypeLineEdit.setText(self.model.getType())
        self.view.UI.eventTicketCheckBox.setChecked(self.model.getTicketNeed())
        self.view.UI.eventTicketPriceLineEdit.setText(self.model.getTicketPrice())

    def setTextStayEdit(self):
        self.view.UI.stayNameLineEdit.setText(self.model.getName())
        self.view.UI.stayFromDateTimeEdit.setDateTime(self.model.getTimeFrom())
        self.view.UI.stayToDateTimeEdit.setDateTime(self.model.getTimeTo())
        self.view.UI.stayTimeSensitiveCheckBox.setChecked(self.model.getRemind())
        self.view.UI.stayTimeSensitiveDateTimeEdit.setDateTime(self.model.getTimesensitive())
        self.view.UI.tripInfoTextEdit_4.setText(self.model.getInfo())
        self.view.UI.stayPricingFlatRateCheckBox.setChecked(self.model.getFlatRateCheck())
        self.view.UI.stayPricingPricePerNightCheckBox.setChecked(self.model.getPPNCheck())
        self.view.UI.stayFlatPriceLineEdit.setText(str(self.model.getFlatRate()))
        self.view.UI.stayPricePerNightLineEdit.setText(str(self.model.getPricePerNight()))
        self.view.UI.stayNumberOfNightLabel.setText(str(self.model.getNight()))
        self.view.UI.stayTotalPriceLabel.setText(str(self.model.getTotalPrice()))
        
    # Check if str can be converted to float
    def toFloat(self, s):
        if s is None: 
            return 0

        try:
            return float(s)
        except ValueError:
            return 0

    # Find days between dates
    def daysBetweenDates(self, timeFrom:"QDateTime", timeTo:"QDateTime"):
        dayFrom = timeFrom.date()
        dayTo = timeTo.date()

        return dayFrom.daysTo(dayTo)
    # def daysBetweenDates(self, d1:"QDateTime", d2:"QDateTime"):
    #     day1 = date(year=d1.date().year(), month=d1.date().month(), day=d1.date().day())
    #     day2 = date(year=d2.date().year(), month=d2.date().month(), day=d2.date().day())

    #     d = day2 - day1
    #     return d.days

    # Trip Info
    def getTripInfo(self):
        name = self.view.UI.tripNameLineEdit.text()
        timeFrom = self.view.UI.tripFromDateTimeEdit.dateTime()
        timeTo = self.view.UI.tripToDateTimeEdit.dateTime()
        remind = self.view.UI.tripTimeSensitiveCheckBox.isChecked()
        timesensitive = self.view.UI.tripTimeSensitiveDateTimeEdit.dateTime()
        info = self.view.UI.tripInfoTextEdit.toPlainText()

        duration = self.daysBetweenDates(timeFrom, timeTo)

        tripInfo = {'name': name, 'timeFrom': timeFrom, 'timeTo': timeTo, 'remind': remind, 
                    'timesensitive': timesensitive, 'info': info, 'duration': duration}
        
        return tripInfo
    
    # Travel Info
    def getTravelInfo(self):
        name = self.view.UI.travelNameLineEdit.text()
        timeFrom = self.view.UI.travelFromDateTimeEdit.dateTime()
        timeTo = self.view.UI.travelToDateTimeEdit.dateTime()
        remind = self.view.UI.travelTimeSensitiveCheckBox.isChecked()
        timesensitive = self.view.UI.travelTimeSensitiveDateTimeEdit.dateTime()
        info = self.view.UI.travelInfoTextEdit.toPlainText()
        ticketNeed = self.view.UI.travelTicketCheckBox.isChecked()
        ticketPrice = self.view.UI.travelTicketPriceLineEdit.text()

        travelInfo = {'name': name, 'timeFrom': timeFrom, 'timeTo': timeTo, 'remind': remind,
                      'timesensitive': timesensitive, 'info': info,'ticketNeed': ticketNeed, 
                      'ticketPrice': ticketPrice}
        
        return travelInfo

    # Place Info
    def getPlaceInfo(self):
        name = self.view.UI.placeNameLineEdit.text()
        timeFrom = self.view.UI.placeFromDateTimeEdit.dateTime()
        timeTo = self.view.UI.placeToDateTimeEdit.dateTime()
        remind = self.view.UI.placeTimeSensitiveCheckBox.isChecked()
        timesensitive = self.view.UI.placeTimeSensitiveDateTimeEdit.dateTime()
        info = self.view.UI.placeInfoTextEdit.toPlainText()
        openTime = self.view.UI.placeOpenHoursFromTimeEdit.dateTime()
        closeTime = self.view.UI.placeOpenHoursToTimeEdit.dateTime()
        openInfo = self.view.UI.placeOpenHoursInfoLineEdit.text()
        addOpen = self.view.UI.checkBox_5.isChecked()

        if not addOpen:
            d = QDateTime(QDate(0,0,0), QTime(0,0,0))
            openTime = d
            closeTime = d
            openInfo = ''

        placeInfo = {'name': name, 'timeFrom': timeFrom, 'timeTo': timeTo, 'remind': remind,
                     'timesensitive': timesensitive, 'info': info, 'openTime': openTime,
                     'closeTime': closeTime, 'openInfo': openInfo, 'addOpen': addOpen}
        
        return placeInfo

    # Eat Info
    def getEatInfo(self):
        name = self.view.UI.eatNameLineEdit.text()
        timeFrom = self.view.UI.eatFromDateTimeEdit.dateTime()
        timeTo = self.view.UI.eatToDateTimeEdit.dateTime()
        remind = self.view.UI.eatTimeSensitiveCheckBox.isChecked()
        timesensitive = self.view.UI.eatTimeSensitiveDateTimeEdit.dateTime()
        info = self.view.UI.eatInfoTextEdit.toPlainText()
        reservation = self.view.UI.eatReservationCheckBox.isChecked()

        eatInfo = {'name': name, 'timeFrom': timeFrom, 'timeTo': timeTo, 'remind': remind,
                      'timesensitive': timesensitive, 'info': info, 'reservation': reservation}
        
        return eatInfo

    # Event Info
    def getEventInfo(self):
        name = self.view.UI.eventNameLineEdit.text()
        timeFrom = self.view.UI.eventFromDateTimeEdit.dateTime()
        timeTo = self.view.UI.eventToDateTimeEdit.dateTime()
        remind = self.view.UI.eventTimeSensitiveCheckBox.isChecked()
        timesensitive = self.view.UI.eventTimeSensitiveDateTimeEdit.dateTime()
        info = self.view.UI.eventInfoTextEdit.toPlainText()
        type = self.view.UI.eventTypeLineEdit.text()
        ticketNeed = self.view.UI.eventTicketCheckBox.isChecked()
        ticketPrice = self.view.UI.eventTicketPriceLineEdit.text()

        eventInfo = {'name': name, 'timeFrom': timeFrom, 'timeTo': timeTo, 'remind': remind,
                     'timesensitive': timesensitive, 'info': info, 'type': type,
                     'ticketNeed': ticketNeed, 'ticketPrice': ticketPrice}
        
        return eventInfo

    # Stay Info
    def getStayInfo(self):
        name = self.view.UI.stayNameLineEdit.text()
        timeFrom = self.view.UI.stayFromDateTimeEdit.dateTime()
        timeTo = self.view.UI.stayToDateTimeEdit.dateTime()
        remind = self.view.UI.stayTimeSensitiveCheckBox.isChecked()
        timesensitive = self.view.UI.stayTimeSensitiveDateTimeEdit.dateTime()
        info = self.view.UI.tripInfoTextEdit_4.toPlainText()
        flatRate = self.view.UI.stayFlatPriceLineEdit.text()
        pricePerNight = self.view.UI.stayPricePerNightLineEdit.text()
        flatRateChecked = self.view.UI.stayPricingFlatRateCheckBox.isChecked()
        pricePNChecked = self.view.UI.stayPricingPricePerNightCheckBox.isChecked()

        night = self.daysBetweenDates(timeFrom, timeTo)

        flatRate = self.toFloat(flatRate) if flatRateChecked else 0
        pricePerNight = self.toFloat(pricePerNight) if pricePNChecked else 0

        totalPrice = flatRate + (night * pricePerNight)

        stayInfo =  {'name': name, 'timeFrom': timeFrom, 'timeTo': timeTo, 'remind': remind,
                     'timesensitive': timesensitive, 'info': info, 'flatRate': flatRate,
                     'pricePerNight': pricePerNight, 'flatRateCheck': flatRateChecked, 'pricePerNightCheck': pricePNChecked,
                     'night': night, 'totalPrice': totalPrice}
        
        return stayInfo
    

    def setNight(self):
        night = self.getNight()
        if night < 0:
            night = ""

        self.view.UI.stayNumberOfNightLabel.setText(str(night))

    def getNight(self):
        timeFrom = self.view.UI.stayFromDateTimeEdit.dateTime()
        timeTo = self.view.UI.stayToDateTimeEdit.dateTime()

        return self.daysBetweenDates(timeFrom, timeTo)


    def setTotalPrice(self):
        flatRateChecked = self.view.UI.stayPricingFlatRateCheckBox.isChecked()
        pricePNChecked = self.view.UI.stayPricingPricePerNightCheckBox.isChecked()

        flatRate = self.toFloat(self.view.UI.stayFlatPriceLineEdit.text()) if flatRateChecked else 0
        pricePerNight = self.toFloat(self.view.UI.stayPricePerNightLineEdit.text()) if pricePNChecked else 0
        night = self.getNight()

        totalPrice = flatRate + (night * pricePerNight)

        self.view.UI.stayTotalPriceLabel.setText(str(totalPrice))