from LoginControl import *
from LoginUI import *
from LoginModel import *


if __name__ == '__main__':
    app = QApplication(sys.argv)
    loginControl = LoginController(app)
    loginControl.view = LoginUI(loginControl)
    loginControl.model = LoginModel()
    loginControl.enterLoginProcess()
    sys.exit(app.exec())