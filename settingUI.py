from typing import Optional
import PySide6.QtCore
from settingUI_ui import *
from PySide6.QtWidgets import QDialog

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from settingController import SettingController


class settingUI(QDialog):
    def __init__(self, controller, parentUI = None, windowType = Qt.WindowType.Dialog):
        super().__init__(parentUI, windowType)
        self.controller: "SettingController" = controller
        self.UI = Ui_Form()
        self.UI.setupUi(self)

        self.UI.changeUsernameButton.clicked.connect(self.changeUsernameButtonClicked)
        self.UI.changePasswordButton.clicked.connect(self.changePasswordButtonClicked)
        self.UI.enterNewPasswordLineEdit.textChanged.connect(self.passwordLineEditChange)
        self.UI.reEnterNewPasswordLineEdit.textChanged.connect(self.passwordLineEditChange)
        self.UI.doneButton.clicked.connect(self.doneButtonClicked)

    
    def changeUsernameButtonClicked(self):
        self.controller.changeUsername()

    def changePasswordButtonClicked(self):
        self.controller.changePassword()

    def setUsername(self, username):
        self.UI.usernameHeaderLabel.setText(username)

    def getNewUsername(self):
        return self.UI.usernameLineEdit.text()
    
    def getNewPassword(self):
        return self.UI.enterNewPasswordLineEdit.text()
    
    def getNewPasswordConfirm(self):
        return self.UI.reEnterNewPasswordLineEdit.text()
    
    def getPassword(self):
        return self.UI.enterPreviousPasswordLineEdit.text()
    
    def passwordLineEditChange(self):
        self.controller.checkPassword()

    def setEnableChangePasswordButton(self, enable):
        self.UI.changePasswordButton.setEnabled(enable)

    def doneButtonClicked(self):
        self.controller.done()
                 