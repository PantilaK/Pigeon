from TripComponentWidget import TripComponentWidget
from ComponentEditControl import EditController
from ReminderController import ReminderController
import globals
from TripModel import TripModel

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from Trip import Trip
    from User import User

class TripController():
    def __init__(self,  trip: "Trip", mainControl=None, tripComponent=None, isExpanded=False, hasReminder=True, isExtendable=True, mainUI=None):
        self.tripComponent = tripComponent
        self.isExpanded:bool = isExpanded
        self.hasReminder:bool = hasReminder
        self.isExtendable:bool = isExtendable
        self.mainControl = mainControl
        self.view:TripComponentWidget = TripComponentWidget(self, self.mainControl.view)
        self.trip = trip
        self.model = TripModel(tripController=self)

    def update(self):
        # if isExpanded make the subwidget visible
        if self.isExpanded:
            self.view.UI.tripSubWidget.setVisible(True)
            self.view.UI.tripExpandButton.setText("Close")
        else:
            self.view.UI.tripSubWidget.setVisible(False)
            self.view.UI.tripExpandButton.setText("Expand")
    
        # if hasReminder make reminder widget visible
        if self.hasReminder:
            self.view.UI.tripReminderWidget.setVisible(True)
        else:
            self.view.UI.tripReminderWidget.setVisible(False)

        # if isExtendable make tripComponentControl visible and componentWidget visible
        if self.isExtendable:
            self.view.UI.tripComponentControlWidget.setVisible(True)
            self.view.UI.componentWidget.setVisible(True)
        else:
            self.view.UI.tripComponentControlWidget.setVisible(False)
            self.view.UI.componentWidget.setVisible(False)
    
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
        self.model.deleteTrip(self.trip)

    def setTripName(self, tripName):
        self.view.UI.tripTitle.setText(tripName)

    def setTripTime(self, startTime):
        self.view.UI.tripTime.setText(startTime)

    def addComponent(self):
        #temporary run code
        EditController()
        pass
        
        # main
        #temporary add component code, replace with update
        # newComponentControl = TripController(mainControl=self)
        # self.view.UI.componentLayout.addWidget(newComponentControl.view)

    def addReminder(self):
        #temporary run code
        newReminder = ReminderController(parentController=self)

        #temporary add component code, replace with update
        self.view.UI.tripReminderLayout.addWidget(newReminder.view)

        #temporary add component code
        # newComponentControl = TripController(self, None)
        # newComponentControl.createUI()
        # self.UI.widget.componentLayout.addWidget(newComponentControl.UI)

