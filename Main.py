from LoginControl import *
from LoginUI import *
from PasswordManager import *


if __name__ == '__main__':
    app = QApplication(sys.argv)
    loginControl = LoginController(None, None)
    loginControl.view = LoginUI(loginControl)
    loginControl.model = PasswordManager()
    loginControl.startLoginProcess()
    sys.exit(app.exec())