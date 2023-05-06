from abc import ABC, abstractclassmethod
from datetime import datetime, date
import persistent, persistent.list

class CheckList(persistent.Persistent):
    
    def __init__(self):
        self.checked = False
        self.name = ''

    # Checked
    def getChecked(self):
        return self.checked
    
    def setChecked(self, checked):
        self.checked = checked

    # Name
    def getName(self):
        return self.name
    
    def setName(self, name):
        self.name = name

class Reservation(persistent.Persistent):

    def __init__(self):
        self.name = ''
        self.time = datetime.now()
        self.ticket = 0
        self.duration = 0

    # Name
    def getName(self):
        return self.name
    
    def setName(self, name):
        self.name = name

    # Time
    def getTime(self):
        return self.time
    
    def setTime(self, time):
        self.time = time

    # Ticket
    def getTicket(self):
        return self.ticket
    
    def setTicket(self, ticket):
        self.ticket = ticket

    # Duration
    def getDuration(self):
        return self.duration
    
    def setDuration(self, duration):
        self.duration = duration

class Reminder(persistent.Persistent):

    def __init__(self):
        self.documents = persistent.list.PersistentList()
        self.packings = persistent.list.PersistentList()
        self.reservations = persistent.list.PersistentList()

    # Documents
    def addDocument(self, document):
        self.documents.append(document)

    def getListOfDocuments(self):
        return self.documents
    
    # Packings
    def addPacking(self, packing):
        self.packings.append(packing)

    def getListOfPackings(self):
        return self.packings
    
    # Reservations
    def addReservation(self, reservation):
        self.reservations.append(reservation)