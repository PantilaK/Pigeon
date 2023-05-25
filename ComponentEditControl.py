from ComponentEditUI import *
from enum import IntEnum, Enum
from Reminder import Reminder
from datetime import date
from Tripcomponent import *
import transaction

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from User import User

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
    stay = 2
    eat = 3
    event = 4  

    #default placeholder
    none = -1

typeStringToIndexDict:dict[str,int] = {TypeString.trip:TypeIndex.trip,
                                        TypeString.travel:TypeIndex.travel,
                                        TypeString.place:TypeIndex.place,
                                        TypeString.stay:TypeIndex.stay,
                                        TypeString.event:TypeIndex.event}



class EditController:
    
    def __init__(self, model=None, typeEdit:str=TypeString.trip, canChangeType:bool = True, controller = None):
        self.view:ComponentEditUI = ComponentEditUI(self)
        self.currentShowMode:str = typeEdit
        self.canChangeType:bool = canChangeType
        self.model = model

        self.controller = controller

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

    def ok(self):
        source = self.view.getSelectedType()

        if source == 'Trip':
            self.addTrip()
        elif source == 'Travel':
            self.addTravel()

        transaction.commit()
        self.controller.update()

        self.view.close()

    def addTrip(self):
        info = self.view.getTripInfo()
        duration = self.daysBetweenDates(info['timeFrom'], info['timeTo'])
        trip = Trip(name=info['name'], timeFrom=info['timeFrom'], timeTo=info['timeTo'], remind=info['remind'],
                    timesensitive=info['timesensitive'], info=info['info'], duration=duration, reminder=Reminder())
        
        self.model.addTrip(trip=trip)

    def addTravel(self):
        info = self.view.getTravelInfo()
        travel = Travel(name=info['name'], timeFrom=info['timeFrom'], timeTo=info['timeTo'], remind=info['remind'],
                    timesensitive=info['timesensitive'], info=info['info'], ticketNeed=info['ticketNeed'], ticketPrice=info['ticketPrice'])
        
        self.model.addComponent(component=travel)

    # Find days between dates
    def daysBetweenDates(self, d1:"QDateTime", d2:"QDateTime"):
        day1 = date(year=d1.date().year(), month=d1.date().month(), day=d1.date().day())
        day2 = date(year=d2.date().year(), month=d2.date().month(), day=d2.date().day())

        return day2 - day1  

    # Get Info
    # def getinfo(self):
    #     return self.view.getTripInfo()
    
    # def getTravelInfo(self):
    #     return self.view.getTravelInfo()
    
    # def getPlaceInfo(self):
    #     return self.view.getPlaceInfo()
    
    # def getEatInfo(self):
    #     return self.view.getEatInfo()
    
    # def getEventInfo(self):
    #     return self.view.getEventInfo()
    
    # def getStayInfo(self):
    #     return self.view.getStayInfo()
    
