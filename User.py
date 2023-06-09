from abc import ABC, abstractclassmethod
from datetime import datetime, date
import persistent, persistent.list

class User(persistent.Persistent):
    
    def __init__(self, username, password):
        self.__username = username
        self.__password = password
        self.trips = persistent.list.PersistentList()
        self.__notifications = persistent.list.PersistentList()

    # Username
    def getUsername(self):
        return self.__username
    
    def setUsername(self, username):
        self.__username = username

    # Password
    def getPassword(self):
        return self.__password
    
    def setPassword(self, password):
        self.__password = password

    # Trips
    def getTrips(self):
        return self.trips

    def addTrip(self, trip):
        self.trips.append(trip)

    def removeTrip(self, trip):
        self.trips.remove(trip)

    # Notification
    def getNotifications(self):
        return self.__notifications
    
    def addNotification(self, notification):
        self.__notifications.append(notification)

    def removeNotification(self, notification):
        self.__notifications.remove(notification)
