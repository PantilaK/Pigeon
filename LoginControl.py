from LoginUI import LoginUI
from LoginModel import LoginModel

import sys
from MainControl import MainController

class LoginController:
    def __init__(self, model=None) -> None:
        self.model:LoginModel = model
        self.view:LoginUI = LoginUI(self)
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
            self.setErrorFieldText("go to main")
            # temporary login function
            self.view.close()
            self.transferToMain()

    def transferToMain(self):
        # temporary main startup
        mainControl = MainController()
        mainControl.enterMainProcess()


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
    

    