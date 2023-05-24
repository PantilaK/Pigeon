from settingUI import settingUI
import globals
import hashlib

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
        username = globals.currentUser.username
        password = globals.currentUser.password
        previousPassword = self.view.getPassword()
        newPassword = self.view.getNewPassword()
        hash = hashlib.sha256(previousPassword.encode()).hexdigest()
        print(previousPassword, password)
        
        if self.mainController.loginController.model.isPasswordMatched(hash, password)[0]:
            print("MMMM")
            self.mainController.loginController.model.changePassword(username=username, password=newPassword)

    def checkPassword(self):
        password = self.view.getNewPassword()
        confirmPassword = self.view.getNewPasswordConfirm()

        isMatched = self.mainController.loginController.model.isPasswordMatched(password, confirmPassword)[0]

        self.view.setEnableChangePasswordButton(isMatched)
