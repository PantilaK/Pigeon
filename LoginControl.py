from LoginUI import LoginUI
from LoginModel import LoginModel

import globals
import sys
from MainControl import MainController

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
        username = self.view.CAgetUsername()
        password = self.view.CAgetPassword()
        message = self.model.createAccount(username, password)
        
        self.setErrorFieldTextCA(message)

    def login(self):
        username = self.view.getUsername()
        password = self.view.getPassword()
        message = self.model.verifyPassword(username, password)

        if type(message) == tuple:
            self.setErrorFieldText(message[1])
        else:
            # Send user information to another window
            self.setErrorFieldText("go to main")
            # temporary login function
            self.view.close()
            globals.currentUser = self.model.getUser(username)
            self.transferToMain()

    def transferToMain(self):
        # temporary main startup
        mainControl = MainController(self)
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
    

    