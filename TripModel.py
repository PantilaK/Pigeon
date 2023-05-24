from typing import TYPE_CHECKING
import globals
import transaction
from Tripcomponent import *

if TYPE_CHECKING:
    from TripControl import TripController
    from Trip import Trip

class TripModel:

    def __init__(self, tripController: "TripController"):
        self.controller = tripController

    def editTripInfo(self, tripName, startDate, endDate):
        if tripName != "":
            self.controller.trip.tripName = tripName

    def deleteTrip(self, trip: "Trip"):
        globals.currentUser.removeTrip(trip)
        globals.mainController.update()

        transaction.commit()

    # Add component
    # Travel
    def addTravel(self, trip:"Trip", travelInfo: dict):
        travel = Travel(travelInfo['name'], travelInfo['timeFrom'], travelInfo['timeTo'], travelInfo['remind'],
                        travelInfo['timesensitive'], travelInfo['info'], travelInfo['ticketNeed'],
                        travelInfo['ticketPrice'])
        
        trip.addTripcomponent(travel)
        
        transaction.commit()

    # Place
    def addPlace(self, trip:"Trip", placeInfo: dict):
        place = Place(placeInfo['name'], placeInfo['timeFrom'], placeInfo['timeTo'], placeInfo['remind'],
                      placeInfo['timesensitive'], placeInfo['info'], placeInfo['openTime'],
                      placeInfo['closeTime'], placeInfo['openInfo'])
        
        trip.addTripcomponent(place)

        transaction.commit()

    # Eat or Restaurant
    def addEat(self, trip:"Trip", eatInfo: dict):
        eat = Restaurant(eatInfo['name'], eatInfo['timeFrom'], eatInfo['timeTo'], eatInfo['remind'], eatInfo['timesensitive'],
                         eatInfo['info'], eatInfo['reservation'])
        
        trip.addTripcomponent(eat)
        
        transaction.commit()

    # Event
    def addEvent(self, trip:"Trip", eventInfo: dict):
        event = Event(eventInfo['name'], eventInfo['timeFrom'], eventInfo['timeTo'], eventInfo['remind'], 
                      eventInfo['timesensitive'], eventInfo['info'], eventInfo['type'], eventInfo['ticketNeed'], 
                      eventInfo['ticketPrice'])

        trip.addTripcomponent(event)

        transaction.commit()

    # Stay(CheckIn)
    def addCheckIn(self, trip:"Trip", stayInfo: dict):
        checkIn = CheckIn(stayInfo['name'], stayInfo['timeFrom'], stayInfo['timeTo'], stayInfo['remind'],
                          stayInfo['timesensitive'], stayInfo['info'], stayInfo['flatRate'], stayInfo['pricePerNight'],
                          stayInfo['period'], stayInfo['totalPrice'])
        
        trip.addTripcomponent(checkIn)

        transaction.commit()

    # Stay(CheckOut)
    def addCheckOut(self, trip:"Trip", stayInfo: dict):
        checkOut = CheckOut(stayInfo['name'], stayInfo['timeFrom'], stayInfo['timeTo'], stayInfo['remind'],
                          stayInfo['timesensitive'], stayInfo['info'], stayInfo['flatRate'], stayInfo['pricePerNight'],
                          stayInfo['period'], stayInfo['totalPrice'])
        
        trip.addTripcomponent(checkOut)

        transaction.commit()

    def getComponents(self):
        from TripControl import TripController
        components = []

        for c in self.controller.trip.tripcomponents:
            con = TripController(component=c, mainControl=self.controller)
            components.append(con)

        return components
        