from TripControl import TripController
import transaction
import globals
from datetime import datetime
from Reminder import Reminder

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from PySide6.QtCore import QDateTime
    from User import User
    from MainControl import MainController
    from MainControl import ShowMode

class MainModel:
    
    def __init__(self, controller):
        self.controller: MainController = controller

    def addTrip(self, tripInfo:dict):
        trip = Trip(tripInfo['name'], tripInfo['timeFrom'], tripInfo['timeTo'], Reminder(),
                    tripInfo['remind'], tripInfo['timesensitive'], tripInfo['info'])
        globals.currentUser.addTrip(trip) # เวลาหาให้หาจากชื่อ trp.tripName
        
        transaction.commit()

    def getTrips(self, tripMode: "ShowMode"):
        trips = []

        trip: Trip
        for trip in globals.currentUser.trips:
            sDate = trip.startDate
            eDate = trip.endDate

            if self.before(sDate) and self.before(eDate):
                if tripMode == tripMode.pastTrip:
                    tripControl = TripController(trip=trip, mainControl=self.controller)
                    trips.append(tripControl)
            elif self.before(sDate):
                if tripMode == tripMode.currentTrip:
                    tripControl = TripController(trip=trip, mainControl=self.controller)
                    trips.append(tripControl)
            elif tripMode == tripMode.futureTrip:
                tripControl = TripController(trip=trip, mainControl=self.controller)
                trips.append(tripControl)

        return trips
    
    # if before(startDate) -> True = past
    # elif before(endDate) -> True = current
    # else = future
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
