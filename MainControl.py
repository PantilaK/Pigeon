from MainUI import *
from settingController import SettingController
from enum import Enum
from TripControl import TripController
import transaction
from ComponentEditControl import EditController
from Tripcomponent import *
from Reminder import Reminder, Notification
from PySide6.QtCore import QTimer
from NotificationController import NotificationController
from copy import deepcopy

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from LoginControl import LoginController
    from TripControl import TripController
    from User import User


class ShowMode(Enum):
    currentTrip = 0
    pastTrip = 1
    futureTrip = 2

class MainController:

    def __init__(self, loginController, user):
        self.view = MainUI(controller=self)
        self.model:"User" = user
        self.loginController: "LoginController" = loginController
        self.goToCurrentTrip()

        self.timer = QTimer()
        self.timer.timeout.connect(self.checkNoti)
        self.timer.start(1000)


    def enterMainProcess(self):
        self.update()
        self.view.show()

    def transferToLogin(self):
        self.timer.stop()
        self.view.close()
        self.loginController.enterLoginProcess()

    def update(self):
        #sort trips
        self.model.trips.sort(key=lambda x: x.getTimeFrom())

        #update UI with model
        self.view.clearTripList()
        trips: list["Trip"] = self.getTrips()

        for trip in trips:
            tripControl = TripController(tripComponent=trip, mainControl=self)
            self.view.addTrip(tripControl.view)

        self.updateNoti()
        self.updateUsername()

    def updateNoti(self):
        self.view.clearNotificationList()
        noti: list["Notification"] = self.model.getNotifications()

        if noti:
            # if list is not empty
            self.view.UI.noNotificationLabel.setVisible(False)
        else:
            self.view.UI.noNotificationLabel.setVisible(True)

        for n in noti:
            notiControl = NotificationController(parentController=self, model=n)
            self.view.UI.notificationLayout.addWidget(notiControl.view)

    def updateUsername(self):
        username = self.model.getUsername()
        self.view.UI.acountDetailsLabel.setText(username)
        

    def goToCurrentTrip(self):
        self.currentShowMode = ShowMode.currentTrip
        self.view.setTripMode('Current Trip')
        self.update()

    def goToPastTrip(self):
        self.currentShowMode = ShowMode.pastTrip
        self.view.setTripMode('Past Trip')
        self.update()

    def goToFutureTrip(self):
        self.currentShowMode = ShowMode.futureTrip
        self.view.setTripMode('Future Trip')
        self.update()

    def newTrip(self):
        EditController(canChangeType=False, controller=self)

    def addTrip(self, info: dict, reminders: list['Reminder']):
        trip = Trip(name=info['name'], timeFrom=info['timeFrom'], timeTo=info['timeTo'], remind=info['remind'],
                    timesensitive=info['timesensitive'], info=info['info'], duration=info['duration'])
        
        for r in reminders:
            trip.addReminder(r)
        
        self.model.addTrip(trip=trip)

        transaction.commit()
        self.update()

    def deleteTrip(self, trip:"Trip"):
        self.model.removeTrip(trip=trip)
        transaction.commit()
        self.update()

    def getTrips(self):
        trips = []

        trip: Trip
        for trip in self.model.getTrips():
            sDate = trip.getTimeFrom()
            eDate = trip.getTimeTo()

            if self.before(sDate) and self.before(eDate):
                if self.currentShowMode == ShowMode.pastTrip:
                    trips.append(trip)
            elif self.before(sDate):
                if self.currentShowMode == ShowMode.currentTrip:
                    trips.append(trip)
            elif self.currentShowMode == ShowMode.futureTrip:
                trips.append(trip)

        return trips

    # Call Setting
    def settings(self):
        #go to settings
        SettingController(mainController=self)

    def checkNoti(self):
        trips: list["Trip"] = self.model.getTrips()

        for t in trips:
            if t.getRemind() and not t.getNotification() and self.beforeEqual(t.getTimesensitive()):
                t.setNotification(True)
                detail = f'Trip: {t.getName()} start on {t.getTimeFrom().toString("dd/MM/yyyy hh:mm")}'
                self.addNoti(detail=detail)

            components: list["Tripcomponent"] = t.getComponents()
            for c in components:
                if c.getRemind() and not c.getNotification() and self.beforeEqual(c.getTimesensitive()):
                    c.setNotification(True)
                    detail = ''
                        
                    if type(c) == Travel:
                        detail = f'Travel: {c.getName()} on {c.getTimeFrom().toString("dd/MM/yyyy hh:mm")}'
                    elif type(c) == Place:
                        detail = f'Place: {c.getName()} on {c.getTimeFrom().toString("dd/MM/yyyy hh:mm")}'
                    elif type(c) == Eat:
                        detail = f'Eat: {c.getName()} on {c.getTimeFrom().toString("dd/MM/yyyy hh:mm")}'
                    elif type(c) == Event:
                        detail = f'Event: {c.getName()} on {c.getTimeFrom().toString("dd/MM/yyyy hh:mm")}'
                    elif type(c) == Stay:
                        detail = f'Stay: {c.getName()} on {c.getTimeFrom().toString("dd/MM/yyyy hh:mm")}'
                    
                    self.addNoti(detail=detail)

    def addNoti(self, detail):
        noti = Notification(name=detail)
        self.model.addNotification(noti)

        transaction.commit()
        self.updateNoti()

    def deleteNoti(self, noti:"Notification"):
        self.model.removeNotification(noti)

        transaction.commit()
        self.updateNoti()

    def before(self, d1:"QDateTime"):
        t = datetime.today()
        today = datetime(year=t.year, month=t.month, day=t.day, hour=t.hour, minute=t.minute)
        d = datetime(year=d1.date().year(), month=d1.date().month(), day=d1.date().day(), hour=d1.time().hour(), minute=d1.time().minute())

        return today >= d
    
    def beforeEqual(self, d1:"QDateTime"):
        t = datetime.today()
        today = datetime(year=t.year, month=t.month, day=t.day, hour=t.hour, minute=t.minute)
        d = datetime(year=d1.date().year(), month=d1.date().month(), day=d1.date().day(), hour=d1.time().hour(), minute=d1.time().minute())

        return d <= today
