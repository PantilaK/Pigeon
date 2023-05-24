from abc import ABC, abstractclassmethod
from datetime import datetime, date
import persistent, persistent.list

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from PySide6.QtCore import QDateTime

class Tripcomponent(ABC):

    def __init__(self, name, timeFrom, timeTo, remind, timesensitive, info):
        self.name = name # Hotel, Train, Place name
        self.timeFrom:"QDateTime"= timeFrom
        self.timeTo:"QDateTime" = timeTo
        self.remind:bool = remind
        self.timesensitive = timesensitive # Important
        self.briefInfo = info # Brief information

    # Name
    def getName(self):
        return self.name
    
    def setName(self, name):
        self.name = name

    # Time From, To
    def getTimeFrom(self):
        return self.timeFrom
    
    def setTimeFrom(self, timeFrom):
        self.timeFrom = timeFrom

    def getTimeTo(self):
        return self.timeTo
    
    def setTimeTo(self, timeTo):
        self.timeTo = timeTo
    
    # Timesensitive remind and timesensitive
    def getRemind(self):
        return self.remind
    
    def setRemind(self, remind):
        self.remind = remind

    def getTimesensitive(self):
        return self.timesensitive
    
    def setTimesensitive(self, timesensitive):
        self.timesensitive = timesensitive

    # Info
    def getInfo(self):
        return self.briefInfo
    
    def writeInfo(self, info):
        self.briefInfo = info

class Travel(Tripcomponent, persistent.Persistent):

    def __init__(self, name, timeFrom, timeTo, remind, timesensitive, info, ticketNeed, ticketPrice):
        super().__init__(name, timeFrom, timeTo, remind, timesensitive, info)
        self.ticketNeed:bool = ticketNeed # Ticket require
        self.ticketPrice = ticketPrice # Price of the ticket

    # Ticket needed
    def getTicketNeed(self):
        return self.ticketNeed
    
    def setTicketNeed(self, ticketNeed):
        self.ticketNeed = ticketNeed

    # Ticket price
    def getTicketPrice(self):
        return self.ticketPrice
    
    def setTicketPrice(self, ticketPrice):
        self.ticketPrice = ticketPrice

class Place(Tripcomponent, persistent.Persistent):

    def __init__(self, name, timeFrom, timeTo, remind, timesensitive, info, openTime:"QDateTime", closeTime:"QDateTime", openInfo):
        super().__init__(name, timeFrom, timeTo, remind, timesensitive, info)
        self.openTime = openTime
        self.closeTime = closeTime
        self.openInfo = openInfo

    # Open time
    def getOpenTime(self):
        return self.openTime
    
    def setOpenTime(self, openTime):
        self.openTime = openTime

    # Close time
    def getCloseTime(self):
        return self.closeTime
    
    def setCloseTime(self, closeTime):
        self.closeTime = closeTime

    # Open info -> weekend, holiday period
    def getOpenInfo(self):
        return self.openInfo
    
    def setOpenInfo(self, openInfo):
        self.openInfo = openInfo

class Restaurant(Tripcomponent, persistent.Persistent):

    def __init__(self, name, timeFrom, timeTo, remind, timesensitive, info, reservationNeed):
        super().__init__(name, timeFrom, timeTo, remind, timesensitive, info)
        self.reservationNeed = reservationNeed

    # Need reservation
    def getResevationNeed(self):
        return self.reservationNeed
    
    def setReservationNeed(self, reservationNeed):
        self.reservationNeed = reservationNeed

class Event(Tripcomponent, persistent.Persistent):

    def __init__(self, name, timeFrom, timeTo, remind, timesensitive, info, type, ticketNeed, ticketPrice):
        super().__init__(name, timeFrom, timeTo, remind, timesensitive, info)
        self.type = type
        self.ticketNeed = ticketNeed
        self.ticketPrice = ticketPrice  

    # Type of event -> movie, play, show
    def getType(self):
        return self.type

    def setType(self, type):
        self.type = type

    # Ticket needed
    def getTicketNeed(self):
        return self.ticketNeed
    
    def setTicketNeed(self, ticketNeed):
        self.ticketNeed = ticketNeed

    # Ticket price
    def getTicketPrice(self):
        return self.ticketPrice
    
    def setTicketPrice(self, ticketPrice):
        self.ticketPrice = ticketPrice

class Stay(Tripcomponent, persistent.Persistent):

    def __init__(self, name, timeFrom, timeTo, remind, timesensitive, info, flatRate, pricePerNight, period, totalPrice):
        super().__init__(name, timeFrom, timeTo, remind, timesensitive, info)
        self.flatRate = flatRate
        self.pricePerNight = pricePerNight
        self.period = period
        self.totalPrice =  totalPrice

    # Flat rate
    def getFlatRate(self):
        return self.flatRate
    
    def setFlatRate(self, flatRate):
        self.flatRate = flatRate

    # Price per night
    def getPricePerNight(self):
        return self.pricePerNight
    
    def setPricePerNight(self, pricePerNight):
        self.pricePerNight = pricePerNight

    # period
    def getPeriod(self):
        return self.period
    
    def setPeriod(self, period):
        self.period = period

    # Total price
    def getTotalPrice(self):
        return self.totalPrice
    
    def setTotalPrice(self, totalPrice):
        self.totalPrice = totalPrice

class CheckIn(Stay, persistent.Persistent):

    def __init__(self, name, timeFrom, timeTo, remind, timesensitive, info, flatRate, pricePerNight, period, totalPrice):
        super().__init__(name, timeFrom, timeTo, remind, timesensitive, info, flatRate, pricePerNight, period, totalPrice)

    # Check in date and time
    def getCheckInDate(self):
        return super().getTimeFrom()
    
class CheckOut(Stay, persistent.Persistent):

    def __init__(self, name, timeFrom, timeTo, remind, timesensitive, info, flatRate, pricePerNight, period, totalPrice):
        super().__init__(name, timeFrom, timeTo, remind, timesensitive, info, flatRate, pricePerNight, period, totalPrice)

    # Check in date and time
    def getCheckOut(self):
        return super().getTimeTo()
