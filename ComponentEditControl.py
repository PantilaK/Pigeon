from ComponentEditUI import *
from ComponentEditModel import *
from enum import IntEnum, Enum

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from Trip import Trip

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
        self.model:ComponentEditModel = ComponentEditModel(self) #replace this with model constructor
        self.currentShowMode:str = typeEdit
        self.canChangeType:bool = canChangeType

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
        self.model.ok(source, self.controller)

        self.view.close()

    # Trip Info
    def getTripName(self):
        return self.view.getTripName()
    
    def getTripStartDate(self):
        return self.view.getTripStartDate()
    
    def getTripEndDate(self):
        return self.view.getTripEndDate()
    
