from abc import ABC, abstractclassmethod
from datetime import datetime, date
import persistent, persistent.list

class User(persistent.Persistent):
    
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.name = ''
        self.pastTrips = persistent.list.PersistentList()
        self.currentTrips = persistent.list.PersistentList()
        self.futureTrips = persistent.list.PersistentList()

    # Username
    def getUsername(self):
        return self.username
    
    def setUsername(self, username):
        self.username = username

    # Password
    def getPassword(self):
        return self.password
    
    def setPassword(self, password):
        self.password = password

    # Name
    def getName(self):
        return self.name
    
    def setName(self, name):
        self.name = name

    # Past Trips
    def addPastTrip(self, trip):
        self.pastTrips.append(trip)

    def removePastTrip(self, trip):
        self.pastTrips.remove(trip)

    # Current Trips
    def addCurrentTrip(self, trip):
        self.currentTrips.append(trip)

    def removeCurrentTrip(self, trip):
        self.currentTrips.remove(trip)

    # Future Trips
    def addFutureTrip(self, trip):
        self.futureTrips.append(trip)

    def removeFutureTrip(self, trip):
        self.futureTrips.remove(trip)
