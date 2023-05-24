from typing import Optional
import PySide6.QtCore
from settingUI_ui import *
from PySide6.QtWidgets import QDialog
import globals


class settingUI(QDialog):
    def __init__(self, controller, parentUI = None, windowType = Qt.WindowType.Dialog):
        super().__init__(parentUI, windowType)
        self.controller = controller
        self.UI = Ui_Form()
        self.UI.setupUi(self)

        self.UI.changeUsernameButton.clicked.connect(self.changeUsernameButtonClicked)
        self.UI.changePasswordButton.clicked.connect(self.changePasswordButtonClicked)

    
    def changeUsernameButtonClicked(self):
        self.controller.changeUsername()

    def changePasswordButtonClicked(self):
        self.controller.changePassword()

    def setUsername(self):
        username = globals.currentUser.username
        self.UI.usernameHeaderLabel.setText(username)

    def getNewUsername(self):
        return self.UI.usernameLineEdit.text()
                 