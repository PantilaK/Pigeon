from ui_LoginUI import *
import sys


class LoginUI(QWidget):
    def __init__(self) -> None:
        super().__init__(None)
        self.UI = Ui_Form()
        self.UI.setupUi(self)
        self.UI.createAccountWidget.setVisible(False)
        self.resize(500, 600)

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
    

if __name__ == '__main__':
    app = QApplication(sys.argv)
    testLogin = LoginUI()
    testLogin.show()
    sys.exit(app.exec())

