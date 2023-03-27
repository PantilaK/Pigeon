from ui_LoginUI import *
import sys


class LoginUI(QWidget):
    def __init__(self, controller) -> None:
        super().__init__(None)
        self.controller = controller
        self.UI = Ui_Form()
        self.UI.setupUi(self)
        self.UI.createAccountWidget.setVisible(False)
        self.resize(500, 600)

        self.UI.cancelButton.clicked.connect(self.cancelButtonClicked)
        self.UI.loginButton.clicked.connect(self.loginButtonClicked)
        self.UI.createAccountButton.clicked.connect(self.createAccountButtonClicked)

    def getUsername(self) -> str:
        return self.UI.usernameLineEdit.text()
    
    def getPassword(self) -> str:
        return self.UI.passwordLineEdit.text()
    
    def CAgetUsername(self) -> str:
        return self.UI.CAusernameLineEdit.text()
    
    def CAgetPassword(self) -> str:
        return self.UI.CApasswordLineEdit.text()
    
    def CAgetComfirmPassword(self) -> str:
        return self.UI.CAconfirmPasswordLineEdit.text()
    
    def cancelButtonClicked(self) -> None:
        self.controller.cancelLogin()

    def loginButtonClicked(self) -> None:
        self.controller.login()

    def createAccountButtonClicked(self) -> None:
        self.controller.createAccount()
    

