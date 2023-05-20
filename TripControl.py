from TripComponentWidget import TripComponentWidget
from ComponentEditControl import EditController
import globals
from TripModel import TripModel

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from Trip import Trip
    from User import User

class TripController():
    def __init__(self,  trip: "Trip", tripComponent=None, mainUI=None):
        self.tripComponent = tripComponent
        self.isExpanded:bool = False
        self.hasReminder:bool = False
        self.isExtendable:bool = True
        self.UI:TripComponentWidget = None
        self.trip = trip
        self.mainUI = mainUI
        self.model = TripModel(tripController=self)

    def createUI(self):
        self.UI = TripComponentWidget(self, self.mainUI)
        self.update()

    def update(self):
        # if isExpanded make the subwidget visible
        if self.isExpanded:
            self.UI.widget.tripSubWidget.setVisible(True)
            self.UI.widget.tripExpandButton.setText("Close")
        else:
            self.UI.widget.tripSubWidget.setVisible(False)
            self.UI.widget.tripExpandButton.setText("Expand")
    
        # if hasReminder make reminder widget visible
        if self.hasReminder:
            self.UI.widget.tripReminderWidget.setVisible(True)
        else:
            self.UI.widget.tripReminderWidget.setVisible(False)

        # if isExtendable make tripComponentControl visible and componentWidget visible
        if self.isExtendable:
            self.UI.widget.tripComponentControlWidget.setVisible(True)
            self.UI.widget.componentWidget.setVisible(True)
        else:
            self.UI.widget.tripComponentControlWidget.setVisible(False)
            self.UI.widget.componentWidget.setVisible(False)
    
    def setUI(self, widget):
        self.widget = widget

    def expand(self):
        self.isExpanded = not self.isExpanded
        self.update()

    def edit(self):
        EditController(controller=self, typeEdit="Trip",canChangeType=None)

    def editTripInfo(self, tripName, startDate, endDate):
        self.model.editTripInfo(tripName=tripName, startDate=startDate, endDate=endDate)

    def delete(self):
        pass

    def setTripName(self, tripName):
        self.UI.widget.tripTitle.setText(tripName)

    def setTripTime(self, startTime):
        self.UI.widget.tripTime.setText(startTime)

    def addComponent(self):
        #temporary run code
        EditController()
        pass
        
        #temporary add component code
        # newComponentControl = TripController(self, None)
        # newComponentControl.createUI()
        # self.UI.widget.componentLayout.addWidget(newComponentControl.UI)

