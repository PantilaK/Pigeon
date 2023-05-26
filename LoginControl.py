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
        self.clearErrorFields()

    def CAcreateAccount(self):
        username = self.view.CAgetUsername()
        password = self.view.CAgetPassword()
        create = self.model.createAccount(username, password)
        message = create[1]
        
        self.setErrorFieldTextCA(message)

        if create[0]:
            self.view.close()
            self.view.UI.createAccountWidget.setVisible(False)
            self.view.UI.loginWidget.setVisible(True)
            self.transferToMain(username=username)

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

        isMatched = self.isPasswordMatched(password, confirmPassword)

        self.setErrorFieldTextCA(isMatched[1])
        self.view.setEnabledCACreateAccountButton(isMatched[0])

    def clearErrorFields(self):
        self.clearErrorFieldCA()
        self.clearErrorField()
        self.view.UI.usernameLineEdit.setText('')
        self.view.UI.passwordLineEdit.setText('')
        self.view.UI.CAusernameLineEdit.setText('')
        self.view.UI.CApasswordLineEdit.setText('')
        self.view.UI.CAconfirmPasswordLineEdit.setText('')
    
    def clearErrorFieldCA(self):
        self.view.UI.errorLabel.setText(" ")
    
    def clearErrorField(self):
        self.view.UI.CAerrorLabel.setText(" ")

    def setErrorFieldText(self, text:str):
        self.view.UI.errorLabel.setText(text)
    
    def setErrorFieldTextCA(self, text:str):
        self.view.UI.CAerrorLabel.setText(text)

    def isPasswordMatched(self, password1:str, passowrd2:str):
        if (password1 == passowrd2) and (password1 != "" or password1 != " "):
            return (True, "")
        
        return (False, "Passwords do not match")


    