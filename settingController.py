from settingUI import settingUI
import globals

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from MainControl import MainController

class SettingController:
    def __init__(self, mainController):
        self.mainController: "MainController" = mainController
        self.view:settingUI = settingUI(self, self.mainController.view)

        self.usernameErrorMessage = " "
        self.passwordErrorMessage = " "
        self.updateUI()

        self.view.exec()


    def updateUI(self):
        self.view.UI.passwordErrorLabel.setText(self.passwordErrorMessage)
        self.view.UI.usernameErrorLabel.setText(self.usernameErrorMessage)
        self.view.setUsername()

    def changeUsername(self):
        # change username button is clicked from UI
        username = globals.currentUser.username
        newUsername = self.view.getNewUsername()
        self.mainController.changeUsername(username=username, newUsername=newUsername)
        self.view.setUsername()

    def changePassword(self):
        # change password button is clicked from UI
        pass
