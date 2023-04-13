from LoginUI import LoginUI

class LoginController:
    def __init__(self) -> None:
        self.view = None
        self.model = None
    
    def enterLoginProcess(self) -> None:
        self.view.show()

    def createAccount(self):
        pass

    def login(self):
        pass

    def cancelLogin(self):
        pass

    def checkPassword(self):
        pass

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

    

    