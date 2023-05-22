from Trip import Trip
from TripControl import TripController
import transaction
import globals
from datetime import datetime

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from PySide6.QtCore import QDateTime
    from User import User
    from MainControl import MainController
    from MainControl import ShowMode

class MainModel:
    
    def __init__(self, controller):
        self.controller: MainController = controller

    def addTrip(self, tripName, mainUI, startDate: "QDateTime", endDate: "QDateTime"):
        trip = Trip(tripName, startTime=startDate, endTime=endDate)
        globals.currentUser.addTrip(trip) # เวลาหาให้หาจากชื่อ trp.tripName
        
        newTrip = TripController(trip=trip, mainUI=mainUI, mainController=self.controller)
        newTrip.createUI()
        newTrip.setTripName(newTrip.trip.getTripName())
        
        transaction.commit()
        return newTrip

    def getTrips(self, mainUI, tripMode: "ShowMode"):
        trips = []

        trip: Trip
        for trip in globals.currentUser.trips:
            sDate = trip.startDate
            eDate = trip.endDate

            if self.before(sDate) and self.before(eDate):
                if tripMode == tripMode.pastTrip:
                    tripControl = TripController(trip=trip, mainUI=mainUI)
                    tripControl.createUI()
                    tripControl.setTripName(trip.getTripName()+trip.getStartDate().toString("yyyy-MM-dd hh:mm"))
                    trips.append(tripControl)
            elif self.before(sDate):
                if tripMode == tripMode.currentTrip:
                    tripControl = TripController(trip=trip, mainUI=mainUI)
                    tripControl.createUI()
                    tripControl.setTripName(trip.getTripName()+trip.getStartDate().toString("yyyy-MM-dd hh:mm"))
                    trips.append(tripControl)
            elif tripMode == tripMode.futureTrip:
                tripControl = TripController(trip=trip, mainUI=mainUI)
                tripControl.createUI()
                tripControl.setTripName(trip.getTripName()+trip.getStartDate().toString("yyyy-MM-dd hh:mm"))
                trips.append(tripControl)

        return trips
    
    # if before(startDate) -> True = past
    # elif before(endDate) -> True = current
    # else = future
    def before(self, d: "QDateTime"):
        today = datetime.today()
        dTime = d.time()
        dDate = d.date()

        if dDate.year() > today.year: return False
        if dDate.month() > today.month: return False
        if dDate.day() > today.day: return False

        if dTime.hour() > today.hour: return False
        if dTime.minute() > today.minute: return False

        return True
