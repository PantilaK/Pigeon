from abc import ABC, abstractclassmethod
from datetime import datetime, date
import persistent, persistent.list

class Tripcomponent(ABC):

    def __init__(self):
        self.name = '' # Hotel, Train, Place name
        self.timesensitive = False # Important
        self.time = datetime.now() # Date and time of the event
        self.briefInfo = '' # Brief information

    # Name
    def getName(self):
        return self.name
    
    def setName(self, name):
        self.name = name
    
    # Timesensitive
    def getTimesensitive(self):
        return self.timesensitive
    
    def setTimesensitive(self, timesensitive):
        self.timesensitive = timesensitive

    # Time
    def getTime(self):
        return self.time
    
    def setTime(self, time):
        self.time = time

    # Info
    def getInfo(self):
        return self.briefInfo
    
    def writeInfo(self, info):
        self.briefInfo = info

class Travel(Tripcomponent, persistent.Persistent):

    def __init__(self):
        super().__init__()
        self.requireTicket = False # Ticket require
        self.ticket = 0 # Price of the ticket

    # Ticket price
    def getTicket(self):
        return self.ticket
    
    def setTicket(self, ticket):
        self.ticket = ticket

    # Is ticket required
    def isTicketRequired(self):
        return self.requireTicket
    
    def requireTicket(self, require):
        self.requireTicket = require

class Place(Tripcomponent, persistent.Persistent):

    def __init__(self):
        super().__init__()
        self.requireTicket = False # Ticket require
        self.ticket = 0 # Price of the ticket
        self.open = ''
        self.close = ''

    # Ticket price
    def getTicket(self):
        return self.ticket
    
    def setTicket(self, ticket):
        self.ticket = ticket

    # Is ticket required
    def isTicketRequired(self):
        return self.requireTicket
    
    def setRequireTicket(self, require):
        self.requireTicket = require

    # Opening time
    def openingTime(self):
        return self.open
    
    def setOpeningTime(self, open):
        self.open = open

    # Closing time
    def closingTime(self):
        return self.close
    
    def setClosingTime(self, close):
        self.close = close

class Restaurant(Tripcomponent, persistent.Persistent):

    def __init__(self):
        super().__init__()
        self.travel = Travel()

    # Is reservation required
    def isReservationRequire(self):
        return super().getTimesensitive()
    
    def requireReservation(self, require):
        super().setTimesensitive(require)

    # Reservation time
    def getReservationTime(self):
        return super().getTime()

    def setReservationTime(self, time):
        super().setTime(time)

class Event(Tripcomponent, persistent.Persistent):

    def __init__(self):
        super().__init__()
        self.requireTicket = False # Ticket require
        self.ticket = 0 # Price of the ticket
        self.place = Place() # Place where that event haves
        self.eventType = '' # Type of the event (Movies, Shows, Fairs, etc.)    

    # Ticket price
    def getTicket(self):
        return self.ticket
    
    def setTicket(self, ticket):
        self.ticket = ticket

    # Is ticket required
    def isTicketRequired(self):
        return self.requireTicket
    
    def setRequireTicket(self, require):
        self.requireTicket = require

    # Type of event
    def getTypeOfEvent(self):
        return self.eventType

    def setTypeOfEvent(self, eventType):
        self.eventType = eventType

class Stay(Tripcomponent, persistent.Persistent):

    def __init__(self):
        super().__init__()
        self.accommodationType = '' # Type of the accommodation (Hotel, Hostel, Apartment, etc.)
        self.period = 0 # 2 or ... nights
        self.price = 0 # Price for a whole period

    # Type of the accommodation
    def getAccommodationType(self):
        return self.accommodationType
    
    def setAccommodationType(self, type):
        self.accommodationType = type

    # Duration
    def getDuration(self):
        return self.period
    
    def setDuration(self, period):
        self.periof = period

class CheckInOut(Stay, persistent.Persistent):

    def __init__(self):
        super().__init__()
        self.checkInOutDateTime = datetime.now()

    # Check in or check out period
    def getCheckInOutPeriod(self):
        return self.checkInDateTime
    
    def setCheckInOutPeriod(self, time):
        self.checkInDateTime = time
