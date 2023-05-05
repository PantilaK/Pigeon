from TripComponentWidget import TripComponentWidget
from ComponentEditControl import EditController

class TripController():
    def __init__(self, tripComponent, mainUI=None):
        self.tripComponent = tripComponent
        self.isExpanded:bool = False
        self.hasReminder:bool = False
        self.isExtendable:bool = True
        self.UI:TripComponentWidget = None
        self.mainUI = mainUI

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
        pass

    def delete(self):
        pass

    def addComponent(self):
        #temporary run code
        EditController()
        
        #temporary add component code
        newComponentControl = TripController(self)
        newComponentControl.createUI()
        self.UI.widget.componentLayout.addWidget(newComponentControl.UI)

