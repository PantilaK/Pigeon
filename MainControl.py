from MainUI import *
from settingController import SettingController
from enum import Enum
from TripControl import TripController
import transaction
from ComponentEditControl import EditController
from Tripcomponent import *
from Reminder import Reminder

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from LoginControl import LoginController
    from TripControl import TripController
    from User import User


class ShowMode(Enum):
    currentTrip = 0
    pastTrip = 1
    futureTrip = 2

class MainController:
    def __init__(self, loginController, user):
        self.view = MainUI(controller=self)
        self.model:"User" = user
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
        trips: list["Trip"] = self.getTrips()
        print( trips, "KOOKO")

        for trip in trips:
            # trip.setTitle()
            # trip.showInfo()
            tripControl = TripController(tripComponent=trip, mainControl=self)
            self.view.addTrip(tripControl.view)
        

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

    def addTrip(self, info: dict):
        trip = Trip(name=info['name'], timeFrom=info['timeFrom'], timeTo=info['timeTo'], remind=info['remind'],
                    timesensitive=info['timesensitive'], info=info['info'], duration=info['duration'])
        
        self.model.addTrip(trip=trip)
        transaction.commit()
        self.update()

    def deleteTrip(self, trip:"Trip"):
        self.model.removeTrip(trip=trip)
        transaction.commit()
        self.update()

    def getTrips(self):
        trips = []

        trip: Trip
        for trip in self.model.getTrips():
            sDate = trip.getTimeFrom()
            eDate = trip.getTimeTo()

            if self.before(sDate) and self.before(eDate):
                if self.currentShowMode == ShowMode.pastTrip:
                    trips.append(trip)
            elif self.before(sDate):
                if self.currentShowMode == ShowMode.currentTrip:
                    trips.append(trip)
            elif self.currentShowMode == ShowMode.futureTrip:
                trips.append(trip)

        return trips
    
    def before(self, d: "QDateTime"):
        today = datetime.today()
        dTime = d.time()
        dDate = d.date()

        if dDate.year() == today.year and dDate.month() == today.month and dDate.day() == today.day:
            if dTime.hour() > today.hour: return False
            if dTime.minute() > today.minute: return False

        if dDate.year() > today.year: return False
        if dDate.year() < today.year: return True
        
        if dDate.month() > today.month: return False
        if dDate.month() < today.month: return True
        
        if dDate.day() > today.day: return False

        return True

    # Call Setting
    def settings(self):
        #go to settings
        SettingController(mainController=self)
