from MainUI import *
from TripControl import *
from enum import Enum
from MainModel import *


class ShowMode(Enum):
    currentTrip = 0
    pastTrip = 1
    futureTrip = 2

class MainController:
    def __init__(self, loginController, user):
        from LoginControl import LoginController
        self.view = MainUI(self)
        self.model = MainModel(user)
        self.loginController: LoginController = loginController
        self.goToCurrentTrip()

    def enterMainProcess(self):
        self.update()
        self.view.show()

    def transferToLogin(self):
        self.view.close()
        self.loginController.enterLoginProcess()

    def update(self):
        #update UI with model
        pass

    def goToCurrentTrip(self):
        self.currentShowMode = ShowMode.currentTrip
        self.view.setTripMode('Current Trip')
        self.update()

    def goToPastTrip(self):
        self.currentShowMode = ShowMode.pastTrip
        self.view.setTripMode('Past Trip')
        self.update()

    def goToFutureTrip(self):
        self.currentShowMode = ShowMode.futureTrip
        self.view.setTripMode('Future Trip')
        self.update()

    def addTrip(self):
        # temporary code
        newTripControl = TripController(None, self.view)
        newTripControl.createUI()
        self.view.UI.tripListLayout.addWidget(newTripControl.UI)


