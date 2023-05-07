from Trip import Trip
from TripControl import TripController
import transaction
import CurrentUser

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from User import User
    from MainControl import MainController
    from MainControl import ShowMode

class MainModel:
    
    def __init__(self, controller):
        self.controller: MainController = controller

    # Current Trip
    def addCurrentTrip(self, trip: "Trip"):
        CurrentUser.currentUser.addCurrentTrip(trip)

    # Past Trip
    def addPastTrip(self, trip: "Trip"):
        CurrentUser.currentUser.addPastTrip(trip)

    # Future Trip
    def addPastTrip(self, trip: "Trip"):
        CurrentUser.currentUser.addFutureTrip(trip)

    def addTrip(self, tripMode: "ShowMode", tripName, mainUI):
        trip = Trip(tripName)
        if tripMode == tripMode.currentTrip:
            CurrentUser.currentUser.addCurrentTrip(trip) # เวลาหาให้หาจากชื่อ trp.tripName
        elif tripMode == tripMode.pastTrip:
            CurrentUser.currentUser.addPastTrip(trip) # เวลาหาให้หาจากชื่อ trp.tripName
        else:
            CurrentUser.currentUser.addFutureTrip(trip) # เวลาหาให้หาจากชื่อ trp.tripName
        
        newTrip = TripController(None, trip, mainUI)
        newTrip.createUI()
        newTrip.setTripName(newTrip.trip.getTripName())
        
        transaction.commit()
        return newTrip

    def getTrips(self, tripMode: "ShowMode", mainUI ):
        trips = []
        
        if tripMode == tripMode.currentTrip:
            for trip in CurrentUser.currentUser.currentTrips:
                tripControl = TripController(None, trip, mainUI)
                tripControl.createUI()
                tripControl.setTripName(tripControl.trip.getTripName())
                trips.append(tripControl)
        elif tripMode == tripMode.pastTrip:
            for trip in CurrentUser.currentUser.pastTrips:
                tripControl = TripController(None, trip, mainUI)
                tripControl.createUI()
                tripControl.setTripName(tripControl.trip.getTripName())
                trips.append(tripControl)
        else:
            for trip in CurrentUser.currentUser.futureTrips:
                tripControl = TripController(None, trip, mainUI)
                tripControl.createUI()
                tripControl.setTripName(tripControl.trip.getTripName())
                trips.append(tripControl)

        return trips
        

    def getUsername(self):
        return CurrentUser.currentUser.getUsername()