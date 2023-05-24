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

    # Get title
    def getTitle(self):
        if self.controller.trip != None:
            return f"{self.controller.trip.getTripName()} (Trip)"
        
        typeC = type(self.controller.component)
        if typeC == Travel:
            return f"{self.controller.component.getName()} (Travel)"
        if typeC == Place:
            return f"{self.controller.component.getName()} (Place)"
        if typeC == Restaurant:
            return f"{self.controller.component.getName()} (Eat)"
        if typeC == Event:
            return f"{self.controller.component.getName()} (Event)"
        if typeC == CheckIn:
            return f"{self.controller.component.getName()} (Check In)"
        if typeC == CheckOut:
            return f"{self.controller.component.getName()} (Check Out)"

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
    
    # Show Information
    def showInfo(self):
        if self.controller.trip != None:
            return self.showTripDetail(self.controller.trip)
        
        typeC = type(self.controller.component)
        if typeC == Travel:
            return self.showTravelDetail(self.controller.component)
        if typeC == Place:
            return self.showPlaceDetail(self.controller.component)
        if typeC == Restaurant:
            return self.showEatDetail(self.controller.component)
        if typeC == Event:
            return self.showEventDetail(self.controller.component)
        if typeC == CheckIn:
            return self.showCheckInDetail(self.controller.component)
        if typeC == CheckOut:
            return self.showCheckOutDetail(self.controller.component)

    def showTripDetail(self, trip:"Trip"):
        start = trip.getStartDate().toString("dd-MM-yyyy hh:mm")
        end = trip.getEndDate().toString("dd-MM-yyyy hh:mm")

        detail = f'''
        Period: {start} - {end}
        Info: {trip.getInfo()}
        '''
        
        return detail
    
    def showTravelDetail(self, travel:"Travel"):
        start = travel.getTimeFrom().toString("dd-MM-yyyy hh:mm")
        end = travel.getTimeTo().toString("dd-MM-yyyy hh:mm")

        ticketRequired = travel.getTicketPrice() if travel.getTicketNeed() else "No Ticket Needed"

        detail = f'''
        Period: {start} - {end}
        Ticket: {ticketRequired}
        Info: {travel.getInfo()}
        '''
        return detail

    def showPlaceDetail(self, place:"Place"):
        start = place.getTimeFrom().toString("dd-MM-yyyy hh:mm")
        end = place.getTimeTo().toString("dd-MM-yyyy hh:mm")

        openT = place.getOpenTime().toString("hh:mm")
        closeT = place.getCloseTime().toString("hh:mm")

        detail = f'''
        Period: {start} - {end}
        Open: {openT} to {closeT}
        Open Info: {place.getOpenInfo()}
        Info: {place.getInfo()}
        '''
        return detail

    def showEatDetail(self, eat:"Restaurant"):
        start = eat.getTimeFrom().toString("dd-MM-yyyy hh:mm")
        end = eat.getTimeTo().toString("dd-MM-yyyy hh:mm")

        reservation = "Required" if eat.getResevationNeed else "No Reservation Needed"

        detail = f'''
        Period: {start} - {end}
        Reservation: {reservation}
        Info: {eat.getInfo()}
        '''
        return detail

    def showEventDetail(self, event:"Event"):
        start = event.getTimeFrom().toString("dd-MM-yyyy hh:mm")
        end = event.getTimeTo().toString("dd-MM-yyyy hh:mm")

        ticketRequired = event.getTicketPrice() if event.getTicketNeed() else "No Ticket Needed"

        detail = f'''
        Period: {start} - {end}
        Type of Event: {event.getType()}
        Ticket: {ticketRequired}
        Info: {event.getInfo()}
        '''
        return detail

    def showCheckInDetail(self, checkIn:"CheckIn"):
        time = checkIn.getCheckInDate().toString("dd-MM-yyyy hh:mm")

        detail = f'''
        Check In: {time}
        Night: {checkIn.getPeriod()}
        Total Price: {checkIn.getTotalPrice()}
        Info: {checkIn.getInfo()}
        '''
        return detail

    def showCheckOutDetail(self, checkOut:"CheckOut"):
        time = checkOut.getCheckOut().toString("dd-MM-yyyy hh:mm")

        detail = f'''
        Check Out: {time}
        Night: {checkOut.getPeriod()}
        Total Price: {checkOut.getTotalPrice}
        Info: {checkOut.getInfo()}
        '''
        return detail