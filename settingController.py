from settingUI import settingUI

class SettingController:
    def __init__(self, mainController):
        self.mainController = mainController
        self.view:settingUI = settingUI(self, self.mainController.view)

        self.usernameErrorMessage = " "
        self.passwordErrorMessage = " "
        self.updateUI()

        self.view.exec()


    def updateUI(self):
        self.view.UI.passwordErrorLabel.setText(self.passwordErrorMessage)
        self.view.UI.usernameErrorLabel.setText(self.usernameErrorMessage)

    def changeUsername(self):
        # change username button is clicked from UI
        pass

    def changePassword(self):
        # change password button is clicked from UI
        pass
