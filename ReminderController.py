from Reminder import *
from ReminderUI import *
from enum import IntEnum
import transaction

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from TripControl import TripController

class ReminderController:
    class UIMode(IntEnum):
        normal = 0
        editting = 1

    def __init__(self, model=None, parentController=None, mode=0) -> None:
        self.model:"Reminder" = model
        self.parentController:"TripController" = parentController
        self.view = ReminderUI(self, self.parentController.view)

        self.operatingMode = mode
        self.updateUI()


    def updateUI(self):
        self.setReminder()
        match self.operatingMode:
            case ReminderController.UIMode.normal:
                self.view.UI.reminderEditWidget.setVisible(False)
                self.view.UI.reminderShowWidget.setVisible(True)
                return
            
            case ReminderController.UIMode.editting:
                self.view.UI.reminderShowWidget.setVisible(False)
                self.view.UI.reminderEditWidget.setVisible(True)
                return
    
    def UIedit(self):
        self.operatingMode = ReminderController.UIMode.editting
        self.updateUI()

    def delete(self):
        #delete reminder
        self.parentController.deleteReminder(self.model)

    def editFinished(self):
        #get values
        name = self.view.UI.editReminderLineEdit.text()
        isChecked = self.view.UI.editReminderCheckBox.isChecked()

        self.parentController.editReminder(name=name, isChecked=isChecked, reminder=self.model)

        #change UI back
        self.operatingMode = ReminderController.UIMode.normal
        self.updateUI()

    def showCheck(self):
        showIsChecked = self.view.UI.showReminderCheckbox.isChecked()
        editIsChecked = self.view.UI.editReminderCheckBox.isChecked()
        
        if showIsChecked != editIsChecked:
            self.model.setIsChecked(isChecked=showIsChecked)

        transaction.commit()
        self.updateUI()

    def editCheck(self):
        showIsChecked = self.view.UI.showReminderCheckbox.isChecked()
        editIsChecked = self.view.UI.editReminderCheckBox.isChecked()
        
        if showIsChecked != editIsChecked:
            self.model.setIsChecked(isChecked=editIsChecked)

        transaction.commit()
        self.updateUI()

    def setReminder(self):
        name = self.model.getName()
        isChecked = self.model.getIsChecked()

        # Set Name
        self.view.UI.showReminderLabel.setText(name)
        self.view.UI.editReminderLineEdit.setText(name)
        
        # Set IsChecked
        self.view.UI.showReminderCheckbox.setChecked(isChecked)
        self.view.UI.editReminderCheckBox.setChecked(isChecked)


            




