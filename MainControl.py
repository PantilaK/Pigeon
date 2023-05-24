from MainUI import *
from TripControl import *
from settingController import SettingController
from enum import Enum
from MainModel import *

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from LoginControl import LoginController
    from TripControl import TripController


class ShowMode(Enum):
    currentTrip = 0
    pastTrip = 1
    futureTrip = 2

class MainController:
    def __init__(self, loginController):
        self.view = MainUI(controller=self)
        self.model = MainModel(controller=self)
        self.loginController: "LoginController" = loginController
        self.goToCurrentTrip()

    def enterMainProcess(self):
        self.update()
        self.view.show()

    def transferToLogin(self):
        self.view.close()
        self.loginController.enterLoginProcess()

    def update(self):
        #update UI with model
        self.view.clearTripList()
        trips: list[TripController] = self.model.getTrips(tripMode=self.currentShowMode)
        
        for trip in trips:
            self.view.addTrip(trip.view)
        

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

    def newTrip(self):
        EditController(canChangeType=False, controller=self) 

    # Add Component
    def addTrip(self, tripInfo):
        self.model.addTrip(tripInfo=tripInfo)
        self.update()

    # Call Setting
    def settings(self):
        #go to settings
        SettingController(self)

    def changeUsername(self, username, newUsername):
        self.loginController.changeUsername(username=username, newUsername=newUsername)