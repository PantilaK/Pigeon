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

    app = QApplication(sys.argv)
    loginControl = LoginController(LoginModel(root))
    sys.exit(app.exec())