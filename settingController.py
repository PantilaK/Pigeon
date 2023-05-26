from settingUI import settingUI
import hashlib

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from MainControl import MainController

class SettingController:
    def __init__(self, mainController):
        self.mainController: "MainController" = mainController
        self.view:settingUI = settingUI(self, self.mainController.view)

        self.usernameErrorMessage = ""
        self.passwordErrorMessage = ""
        self.updateUI()

        self.view.exec()


    def updateUI(self):
        self.view.UI.passwordErrorLabel.setText(self.passwordErrorMessage)
        self.view.UI.usernameErrorLabel.setText(self.usernameErrorMessage)

        username = self.mainController.model.getUsername()
        print(username)
        self.view.setUsername(username=username)

    def changeUsername(self):
        # change username button is clicked from UI
        username = self.mainController.model.getUsername()
        newUsername = self.view.getNewUsername().strip()

        m = self.mainController.loginController.model.changeUsername(username=username, newUsername=newUsername)
        self.usernameErrorMessage = m
        self.updateUI()

    def changePassword(self):
        # change password button is clicked from UI
        username = self.mainController.model.getUsername()
        password = self.mainController.model.getPassword()
        previousPassword = self.view.getPassword()
        newPassword = self.view.getNewPassword()
        hash = hashlib.sha256(previousPassword.encode()).hexdigest()
        print(previousPassword, password)
        
        if self.mainController.loginController.isPasswordMatched(hash, password)[0]:
            m = self.mainController.loginController.model.changePassword(username=username, password=newPassword)
            self.passwordErrorMessage = m

        self.updateUI()

    def checkPassword(self):
        password = self.view.getNewPassword()
        confirmPassword = self.view.getNewPasswordConfirm()

        r = self.mainController.loginController.isPasswordMatched(password, confirmPassword)
        isMatched = r[0]
        m = r[1]
        self.passwordErrorMessage = m

        self.view.setEnableChangePasswordButton(isMatched)

        self.updateUI()

    def done(self):
        self.view.close()
