from abc import ABC, abstractclassmethod
import persistent, persistent.list
from Reminder import Reminder

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from PySide6.QtCore import QDateTime


class Trip(persistent.Persistent):

    def __init__(self, tripName: str, startTime: "QDateTime", endTime: "QDateTime", reminder=None, timesensitive=None, info=None):
        self.duration = 0 # StartDate - EndDate
        self.startDate: "QDateTime" = startTime # Date when the trip start
        self.endDate: "QDateTime" = endTime # Date when the trip end
        self.tripName = tripName
        self.tripcomponents = persistent.list.PersistentList()
        self.reminder = Reminder()
        self.timesensitiveEvent = persistent.list.PersistentList()
        self.info = None

    # Duration
    def getDuration(self):
        return self.duration

    # Start Date
    def getStartDate(self):
        return self.startDate
    
    def setStartDate(self, startDate):
        self.startDate = startDate

    # End Date
    def getEndDate(self):
        return self.endDate
    
    def setEndDate(self, endDate):
        self.endDate = endDate

    # Trip Name
    def getTripName(self):
        return self.tripName
    
    def setTripName(self, tripName):
        self.tripName = tripName

    # Trip Components
    def addTripcomponent(self, component):
        self.tripcomponents.append(component)

    def removeTripComponent(self, component):
        self.tripcomponents.remove(component)

    # Time Sensitive Event
    def addEvent(self, event):
        self.timesensitiveEvent.append(event)

    def removeEvent(self, event):
        self.timesensitiveEvent.append(event)


    
