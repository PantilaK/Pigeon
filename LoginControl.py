from LoginUI import LoginUI
from LoginModel import LoginModel

import sys

class LoginController:
    def __init__(self, app) -> None:
        self.view:LoginUI = None
        self.model:LoginModel = None
        self.app = app
    
    def enterLoginProcess(self) -> None:
        self.view.show()
        self.clearErrorFields()

    def createAccount(self):
        pass

    def CAcreateAccount(self):
        message = self.model.createAccount(self.view.CAgetUsername(), self.view.CAgetPassword())
        
        self.setErrorFieldTextCA(message)

    def login(self):
        message = self.model.verifyPassword(self.view.getUsername(), self.view.getPassword())

        if type(message) == tuple:
            self.setErrorFieldText(message[1])
        else:
            # Send user information to another window
            pass

    def cancelLogin(self):
        self.view.close()

    def CAcheckPassword(self):
        password = self.view.CAgetPassword()
        confirmPassword = self.view.CAgetComfirmPassword()

        isMatched = self.model.isPasswordMatched(password, confirmPassword)

        self.setErrorFieldTextCA(isMatched[1])
        self.view.setEnabledCACreateAccountButton(isMatched[0])

    def clearErrorFields(self):
        self.clearErrorFieldCA()
        self.clearErrorField()
    
    def clearErrorFieldCA(self):
        self.view.UI.errorLabel.setText(" ")
    
    def clearErrorField(self):
        self.view.UI.CAerrorLabel.setText(" ")

    def setErrorFieldText(self, text:str):
        self.view.UI.errorLabel.setText(text)
    
    def setErrorFieldTextCA(self, text:str):
        self.view.UI.CAerrorLabel.setText(text)
    

    