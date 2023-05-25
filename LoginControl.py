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

    def enterLoginProcess(self):
        self.view.show()
        self.clearErrorField()
        
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
            self.view.close()
            # globals.currentUser = self.model.getUser(username)
            self.transferToMain(username=username)

    def transferToMain(self, username):
        # temporary main startup
        mainControl = MainController(self, user=self.model.getUser(username=username))
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


    