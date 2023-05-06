from MainUI import *
from TripControl import *
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
    def __init__(self, loginController, user):
        self.view = MainUI(self)
        self.model = MainModel(self, user)
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
        trips: list[TripController] = self.model.getTrips(self.currentShowMode, self.view)
        
        for trip in trips:
            self.view.addTrip(trip.UI)
        

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

    def addTrip(self, tripName):
        # temporary code
        newTrip = self.model.addTrip(self.currentShowMode, tripName, self.view)
        self.view.addTrip(newTrip.UI)
        # self.view.UI.tripListLayout.addWidget(newTripControl.UI)


