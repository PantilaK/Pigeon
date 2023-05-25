from typing import Optional
import PySide6.QtCore
import PySide6.QtWidgets
from ReminderWidget_ui import *

class ReminderUI(QWidget):
    def __init__(self, control, parent=None):
        super().__init__(parent)
        self.controller = control
        self.UI = Ui_Form()
        self.UI.setupUi(self)

        self.UI.showEditButton.clicked.connect(self.editButtonClicked)
        self.UI.showDeleteButton.clicked.connect(self.deleteButtonClicked)
        self.UI.editReminderLineEdit.editingFinished.connect(self.reminderEditFinished)
        self.UI.editOKButton.clicked.connect(self.editOKButtonClicked)
        self.UI.editDeleteButton.clicked.connect(self.deleteButtonClicked)
        self.UI.showReminderCheckbox.stateChanged.connect(self.showCheck)

    def editButtonClicked(self):
        self.controller.UIedit()

    def deleteButtonClicked(self):
        self.controller.delete()

    def reminderEditFinished(self):
        self.controller.editFinished()

    def editOKButtonClicked(self):
        self.controller.editFinished()

    def showCheck(self):
        self.controller.showCheck()


