from abc import ABC, abstractclassmethod
from datetime import datetime, date
import persistent, persistent.list

class User(persistent.Persistent):
    
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.name = ''
        self.trips = persistent.list.PersistentList()

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

    # Trips
    def addTrip(self, trip):
        self.trips.append(trip)

    def removeTrip(self, trip):
        self.trips.remove(trip)
