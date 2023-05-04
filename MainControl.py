from MainUI import *
from TripControl import *
from enum import Enum


class ShowMode(Enum):
    currentTrip = 0
    pastTrip = 1
    futureTrip = 2

class MainController:
    def __init__(self):
        self.view = MainUI(self)
        self.model = None  #replace this with model constructor
        self.currentShowMode = ShowMode.currentTrip

    def enterMainProcess(self):
        self.update()
        self.view.show()

    def update(self):
        #update UI with model
        pass

    def goToCurrentTrip(self):
        self.currentShowMode = ShowMode.currentTrip
        self.update()

    def goToPastTrip(self):
        self.currentShowMode = ShowMode.pastTrip
        self.update()

    def goToFutureTrip(self):
        self.currentShowMode = ShowMode.futureTrip
        self.update()

    def addTrip(self):
        # temporary code
        newTripControl = TripController(None)
        newTripControl.createUI()
        self.view.UI.tripListLayout.addWidget(newTripControl.UI)


