from Reminder import *
from ReminderUI import *
from enum import IntEnum

class ReminderController:
    class UIMode(IntEnum):
        normal = 0
        editting = 1

    def __init__(self, model=None, parentController=None, mode=0) -> None:
        self.model = model
        self.parentController = parentController
        self.view = ReminderUI(self, self.parentController.view)

        self.operatingMode = mode
        self.updateUI()


    def updateUI(self):
        match self.operatingMode:
            case ReminderController.UIMode.normal:
                self.view.UI.reminderEditWidget.setVisible(False)
                self.view.UI.reminderShowWidget.setVisible(True)
                return
            
            case ReminderController.UIMode.editting:
                self.view.UI.reminderShowWidget.setVisible(False)
                self.view.UI.reminderEditWidget.setVisible(True)
                return
            
    def getView(self):
        return self.view
    
    def UIedit(self):
        self.operatingMode = ReminderController.UIMode.editting
        self.updateUI()

    def delete(self):
        #delete reminder
        pass

    def editFinished(self):
        #update values

        #change UI back
        self.operatingMode = ReminderController.UIMode.normal
        self.updateUI()

            




