from TripComponentWidget import TripComponentWidget
from ComponentEditControl import EditController
from ReminderController import ReminderController
from Tripcomponent import *

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    pass

class TripController():
    def __init__(self, tripComponent=None, mainControl=None, isExpanded=False, hasReminder=True, isExtendable=True):
        self.tripComponent:"Trip" = tripComponent
        self.isExpanded:bool = isExpanded
        self.hasReminder:bool = hasReminder
        self.isExtendable:bool = isExtendable
        self.mainControl = mainControl

        self.view:TripComponentWidget = TripComponentWidget(self, self.mainControl.view)
        self.update()

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

        if type(self.tripComponent) == Trip:
            self.setTitle()
            self.view.clearComponentLists()
            components: list["Tripcomponent"] = self.tripComponent.getComponents()

            for c in components:
                # trip.setTitle()
                # trip.showInfo()
                componentControl = TripController(tripComponent=components, mainControl=self, hasReminder=False, isExtendable=False)
                self.view.addComponent(componentControl.view)
    
    def setUI(self, widget):
        self.widget = widget

    def expand(self):
        self.isExpanded = not self.isExpanded
        self.update()

    def edit(self):
        pass

    def delete(self):
        pass

    def setTitle(self):
        t = type(self.tripComponent)

        if t == Trip:
            title = f'{self.tripComponent.getName()} (Trip)'

        self.view.setTitle(title=title)

    def addComponent(self):
        #temporary run code
        EditController(controller=self, model=self.tripComponent)

        
        #temporary add component code, replace with update
        # newComponentControl = TripController(mainControl=self)
        # self.view.UI.componentLayout.addWidget(newComponentControl.view)

    def addReminder(self):
        #temporary run code
        newReminder = ReminderController(parentController=self)

        #temporary add component code, replace with update
        self.view.UI.tripReminderLayout.addWidget(newReminder.view)