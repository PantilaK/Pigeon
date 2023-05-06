from Trip import Trip
from TripControl import TripController
import transaction

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from User import User
    from MainControl import MainController
    from MainControl import ShowMode

class MainModel:
    
    def __init__(self, controller, user):
        self.controller: MainController = controller
        self.user: "User" = user

    # Current Trip
    def addCurrentTrip(self, trip: "Trip"):
        self.user.addCurrentTrip(trip)

    # Past Trip
    def addPastTrip(self, trip: "Trip"):
        self.user.addPastTrip(trip)

    # Future Trip
    def addPastTrip(self, trip: "Trip"):
        self.user.addFutureTrip(trip)

    def addTrip(self, tripMode: "ShowMode", tripName, mainUI):
        trip = Trip(tripName)
        if tripMode == tripMode.currentTrip:
            self.user.addCurrentTrip(trip) # เวลาหาให้หาจากชื่อ trp.tripName
        elif tripMode == tripMode.pastTrip:
            self.user.addPastTrip(trip) # เวลาหาให้หาจากชื่อ trp.tripName
        else:
            self.user.addFutureTrip(trip) # เวลาหาให้หาจากชื่อ trp.tripName
        
        newTrip = TripController(None, trip, mainUI)
        newTrip.createUI()
        newTrip.setTripName(newTrip.trip.getTripName())
        
        transaction.commit()
        return newTrip

    def getTrips(self, tripMode: "ShowMode", mainUI ):
        trips = []
        
        if tripMode == tripMode.currentTrip:
            for trip in self.user.currentTrips:
                tripControl = TripController(None, trip, mainUI)
                tripControl.createUI()
                tripControl.setTripName(tripControl.trip.getTripName())
                trips.append(tripControl)
        elif tripMode == tripMode.pastTrip:
            for trip in self.user.pastTrips:
                tripControl = TripController(None, trip, mainUI)
                tripControl.createUI()
                tripControl.setTripName(tripControl.trip.getTripName())
                trips.append(tripControl)
        else:
            for trip in self.user.futureTrips:
                tripControl = TripController(None, trip, mainUI)
                tripControl.createUI()
                tripControl.setTripName(tripControl.trip.getTripName())
                trips.append(tripControl)

        return trips

    def getUsername(self):
        return self.user.getUsername()