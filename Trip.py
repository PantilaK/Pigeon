from abc import ABC, abstractclassmethod
import persistent, persistent.list
from Reminder import Reminder

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from PySide6.QtCore import QDateTime


class Trip(persistent.Persistent):

    def __init__(self, tripName: str, startTime: "QDateTime", endTime: "QDateTime", reminder:Reminder, remind, timesensitive, info):
        self.duration = 0 # StartDate - EndDate
        self.startDate: "QDateTime" = startTime # Date when the trip start
        self.endDate: "QDateTime" = endTime # Date when the trip end
        self.tripName = tripName
        self.tripcomponents = persistent.list.PersistentList()
        self.reminder = reminder
        self.remind = remind
        self.timesensitive:QDateTime = timesensitive
        self.info = info

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

    # Timesensitive: remind:bool and timesensitive:QDateTiem
    def getRemind(self):
        return self.remind
    
    def setRemind(self, remind):
        self.remind = remind

    def getTimesensitive(self):
        return self.timesensitive
    

    def setTimesensitive(self, timesensitive):
        self.timesensitive = timesensitive


    
