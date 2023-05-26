from abc import ABC, abstractclassmethod
from datetime import datetime, date
import persistent, persistent.list

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from PySide6.QtCore import QDateTime
    from Reminder import Reminder

class Tripcomponent(ABC):

    def __init__(self, name, timeFrom, timeTo, remind, timesensitive, info):
        self.__name = name # Hotel, Train, Place name
        self.__timeFrom:"QDateTime"= timeFrom
        self.__timeTo:"QDateTime" = timeTo
        self.__remind:bool = remind
        self.__timesensitive = timesensitive # Important
        self.__notification = False
        self.__briefInfo = info # Brief information

    # Name
    def getName(self):
        return self.__name
    
    def setName(self, name):
        self.__name = name

    # Time From, To
    def getTimeFrom(self):
        return self.__timeFrom
    
    def setTimeFrom(self, timeFrom):
        self.__timeFrom = timeFrom

    def getTimeTo(self):
        return self.__timeTo
    
    def setTimeTo(self, timeTo):
        self.__timeTo = timeTo
    
    # Timesensitive remind and timesensitive
    def getRemind(self):
        return self.__remind
    
    def setRemind(self, remind):
        self.__remind = remind

    def getTimesensitive(self):
        return self.__timesensitive
    
    def setTimesensitive(self, timesensitive):
        self.__timesensitive = timesensitive

    # Info
    def getInfo(self):
        return self.__briefInfo
    
    def writeInfo(self, info):
        self.__briefInfo = info

    # Notification - False, True
    def getNotification(self):
        return self.__notification
    
    def setNotification(self, noti):
        self.__notification = noti

class Trip(Tripcomponent, persistent.Persistent):
    
    def __init__(self, name, timeFrom, timeTo, remind, timesensitive, info, duration):
        super().__init__(name, timeFrom, timeTo, remind, timesensitive, info)
        self.__duration = duration
        self.__reminder: list["Reminder"] = persistent.list.PersistentList()
        self.componentList = persistent.list.PersistentList()

    # Duration
    def getDuration(self):
        return self.__duration
    
    def setDuration(self, duration):
        self.__duration = duration

    # Component List
    def getComponents(self):
        return self.componentList
    
    def addComponent(self, component):
        self.componentList.append(component)

    def removeComponent(self, component):
        self.componentList.remove(component)

    # Reminder List
    def getReminders(self):
        return self.__reminder
    
    def addReminder(self, reminder:"Reminder"):
        self.__reminder.append(reminder)

    def removeReminder(self, reminder):
        self.__reminder.remove(reminder)


class Travel(Tripcomponent, persistent.Persistent):

    def __init__(self, name, timeFrom, timeTo, remind, timesensitive, info, ticketNeed, ticketPrice):
        super().__init__(name, timeFrom, timeTo, remind, timesensitive, info)
        self.__ticketNeed:bool = ticketNeed # Ticket require
        self.__ticketPrice = ticketPrice # Price of the ticket

    # Ticket needed
    def getTicketNeed(self):
        return self.__ticketNeed
    
    def setTicketNeed(self, ticketNeed):
        self.__ticketNeed = ticketNeed

    # Ticket price
    def getTicketPrice(self):
        return self.__ticketPrice
    
    def setTicketPrice(self, ticketPrice):
        self.__ticketPrice = ticketPrice

class Place(Tripcomponent, persistent.Persistent):

    def __init__(self, name, timeFrom, timeTo, remind, timesensitive, info, openTime:"QDateTime", closeTime:"QDateTime", openInfo):
        super().__init__(name, timeFrom, timeTo, remind, timesensitive, info)
        self.__openTime = openTime
        self.__closeTime = closeTime
        self.__openInfo = openInfo

    # Open time
    def getOpenTime(self):
        return self.__openTime
    
    def setOpenTime(self, openTime):
        self.__openTime = openTime

    # Close time
    def getCloseTime(self):
        return self.__closeTime
    
    def setCloseTime(self, closeTime):
        self.__closeTime = closeTime

    # Open info -> weekend, holiday period
    def getOpenInfo(self):
        return self.__openInfo
    
    def setOpenInfo(self, openInfo):
        self.__openInfo = openInfo

class Eat(Tripcomponent, persistent.Persistent):

    def __init__(self, name, timeFrom, timeTo, remind, timesensitive, info, reservationNeed):
        super().__init__(name, timeFrom, timeTo, remind, timesensitive, info)
        self.__reservationNeed = reservationNeed

    # Need reservation
    def getResevationNeed(self):
        return self.__reservationNeed
    
    def setReservationNeed(self, reservationNeed):
        self.__reservationNeed = reservationNeed

class Event(Tripcomponent, persistent.Persistent):

    def __init__(self, name, timeFrom, timeTo, remind, timesensitive, info, type, ticketNeed, ticketPrice):
        super().__init__(name, timeFrom, timeTo, remind, timesensitive, info)
        self.__type = type
        self.__ticketNeed = ticketNeed
        self.__ticketPrice = ticketPrice  

    # Type of event -> movie, play, show
    def getType(self):
        return self.__type

    def setType(self, type):
        self.__type = type

    # Ticket needed
    def getTicketNeed(self):
        return self.__ticketNeed
    
    def setTicketNeed(self, ticketNeed):
        self.__ticketNeed = ticketNeed

    # Ticket price
    def getTicketPrice(self):
        return self.__ticketPrice
    
    def setTicketPrice(self, ticketPrice):
        self.__ticketPrice = ticketPrice

class Stay(Tripcomponent, persistent.Persistent):

    def __init__(self, name, timeFrom, timeTo, remind, timesensitive, info, flatRate, flatRateCheck, pricePerNight, pricePerNightCheck, night, totalPrice):
        super().__init__(name, timeFrom, timeTo, remind, timesensitive, info)
        self.__flatRate = flatRate
        self.__flatRateCheck = flatRateCheck
        self.__pricePerNightCheck = pricePerNightCheck
        self.__pricePerNight = pricePerNight
        self.__night = night
        self.__totalPrice =  totalPrice

    # Flat rate
    def getFlatRate(self):
        return self.__flatRate
    
    def setFlatRate(self, flatRate):
        self.__flatRate = flatRate

    # Flat rate checked
    def getFlatRateCheck(self):
        return self.__flatRateCheck
    
    def setFlatRateCheck(self, flatRateCheck):
        self.__flatRateCheck = flatRateCheck

    # Price per night
    def getPricePerNight(self):
        return self.__pricePerNight
    
    def setPricePerNight(self, pricePerNight):
        self.__pricePerNight = pricePerNight

    # Price per night check
    def getPPNCheck(self):
        return self.__pricePerNightCheck
    
    def setPPNCheck(self, pPN):
        self.__pricePerNightCheck = pPN

    # Night
    def getNight(self):
        return self.__night
    
    def setNight(self, night):
        self.__night = night

    # Total price
    def getTotalPrice(self):
        return self.__totalPrice
    
    def setTotalPrice(self, totalPrice):
        self.__totalPrice = totalPrice

# class CheckIn(Stay, persistent.Persistent):

#     def __init__(self, name, timeFrom, timeTo, remind, timesensitive, info, flatRate, flatRateCheck, pricePerNight, pricePerNightCheck, night, totalPrice):
#         super().__init__(name, timeFrom, timeTo, remind, timesensitive, info, flatRate, flatRateCheck, pricePerNight, pricePerNightCheck, night, totalPrice)

#     # Check in date and time
#     def getCheckInDate(self):
#         return super().getTimeFrom()
    
# class CheckOut(Stay, persistent.Persistent):

#     # timeFrom = timeTo = Checkout date
#     def __init__(self, name, timeFrom, timeTo, remind, timesensitive, info, flatRate, flatRateCheck, pricePerNight, pricePerNightCheck, night, totalPrice):
#         super().__init__(name, timeTo, timeTo, remind, timesensitive, info, flatRate, flatRateCheck, pricePerNight, pricePerNightCheck, night, totalPrice)
#         self.__checkInDate = timeFrom

#     # Check out date and time
#     def getCheckOut(self):
#         return super().getTimeTo()
    
#     # Check in date:
#     def getCheckInDate(self):
#         return self.__checkInDate
    
#     def setCheckInDate(self, checkInDate):
#         self.__checkInDate = checkInDate
