from LoginControl import *
from LoginUI import *
import ZODB
import ZODB.FileStorage
import sys


if __name__ == '__main__':
    storage = ZODB.FileStorage.FileStorage('data.fs')
    db = ZODB.DB(storage)
    connection = db.open()
    root = connection.root()
    if 'username' not in root:
        root['username'] = {}
    else:
        print(root['username'])

    app = QApplication(sys.argv)
    
    loginControl = LoginController(app)
    loginControl.view = LoginUI(loginControl)
    loginControl.model = LoginModel(root)
    loginControl.enterLoginProcess()
    sys.exit(app.exec())