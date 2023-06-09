from TripComponentWidget import TripComponentWidget
from ComponentEditControl import EditController
from ReminderController import ReminderController
from Tripcomponent import *
import transaction
from Reminder import Reminder

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    pass

class TripController():
    def __init__(self, tripComponent=None, mainControl=None, isExpanded=False, hasReminder=True, isExtendable=True, hasBudget=False):
        self.tripComponent:"Tripcomponent" = tripComponent
        self.isExpanded:bool = isExpanded
        self.hasReminder:bool = hasReminder
        self.isExtendable:bool = isExtendable
        self.hasBudget:bool = hasBudget
        self.mainControl = mainControl

        self.budget:list[(str, float)] = list()
        self.budgetTextName = ""
        self.budgetTextPrice = ""

        self.view:TripComponentWidget = TripComponentWidget(self, self.mainControl.view)
        self.update()

    def update(self):
        # if isExpanded make the subwidget visible
        if self.isExpanded:
            self.view.UI.tripSubWidget.setVisible(True)
            self.view.UI.tripExpandButton.setText("Close")
        else:
            self.view.UI.tripSubWidget.setVisible(False)
            self.view.UI.tripExpandButton.setText("Expand")
    
        # if hasReminder make reminder widget visible
        if self.hasReminder:
            self.view.UI.tripReminderWidget.setVisible(True)
        else:
            self.view.UI.tripReminderWidget.setVisible(False)

        # if isExtendable make tripComponentControl visible and componentWidget visible
        if self.isExtendable:
            self.view.UI.tripComponentControlWidget.setVisible(True)
            self.view.UI.componentWidget.setVisible(True)
        else:
            self.view.UI.tripComponentControlWidget.setVisible(False)
            self.view.UI.componentWidget.setVisible(False)

        # if hasBudget show budgetWidget
        self.view.UI.budgetWidget.setVisible(self.hasBudget)

        self.setTitle()
        self.setDate()
        self.showInfo()
        self.showBudgetInfo()

        if type(self.tripComponent) == Trip:
            # sort components
            self.tripComponent.componentList.sort(key=lambda x: x.getTimeFrom())
            self.view.clearComponentLists()
            components: list["Tripcomponent"] = self.tripComponent.getComponents()

            for c in components:
                if type(c) == Trip:
                    componentControl = TripController(tripComponent=c, mainControl=self, hasBudget=True)
                else:
                    componentControl = TripController(tripComponent=c, mainControl=self, hasReminder=False, isExtendable=False)
                    
                self.view.addComponent(componentControl.view)

            self.view.clearReminderList()
            reminders: list["Reminder"] = self.tripComponent.getReminders()

            for r in reminders:
                reminderControl = ReminderController(parentController=self, model=r)
                self.view.UI.tripReminderLayout.addWidget(reminderControl.view)

        if self.hasBudget:
            self.showBudgetInfo()
    
    def setUI(self, widget):
        self.widget = widget

    def expand(self):
        self.isExpanded = not self.isExpanded
        self.update()

    def delete(self):
        if type(self.tripComponent) is Trip:
            self.mainControl.deleteTrip(self.tripComponent)
        else:
            self.mainControl.deleteComponent(self.tripComponent)

    def deleteTrip(self, trip:"Trip"):
        self.tripComponent.removeComponent(component=trip)
        transaction.commit()
        self.update()

    def deleteComponent(self, component):
        self.tripComponent.removeComponent(component=component)
        transaction.commit()
        self.update()

    def setTitle(self):
        t = type(self.tripComponent)
        title = ''

        if t == Trip:
            title = f'{self.tripComponent.getName()} (Trip)'
        elif t == Travel:
            title = f'{self.tripComponent.getName()} (Travel)'
        elif t == Place:
            title = f'{self.tripComponent.getName()} (Place)'
        elif t == Eat:
            title = f'{self.tripComponent.getName()} (Eat)'
        elif t == Event:
            title = f'{self.tripComponent.getName()} (Event)'
        elif t == Stay:
            title = f'{self.tripComponent.getName()} (Stay)'

        self.view.setTitle(title)

    def setDate(self):
        d = self.tripComponent.getTimeFrom().date().toString("dd MMMM yy")
        self.view.UI.tripTime.setText(d)

    def showInfo(self):
        t = type(self.tripComponent)
        detail = ''

        if t == Trip:
            detail = self.tripInfo()
        elif t == Travel:
            detail = self.travelInfo()
        elif t == Place:
            detail = self.placeInfo()
        elif t == Eat:
            detail = self.eatInfo()
        elif t == Event:
            detail = self.eventInfo()
        elif t == Stay:
            detail = self.stayInfo()

        self.view.addDetil(detail=detail)

    # Get Information
    def tripInfo(self):
        info = f'Date: {self.tripComponent.getTimeFrom().toString("dd/MM/yyyy hh:mm")} - {self.tripComponent.getTimeTo().toString("dd/MM/yyyy hh:mm")} ({self.tripComponent.getDuration()} days)\n'
        info += f'Information:'
        otherInfo = self.tripComponent.getInfo().split('\n')
        for i in otherInfo:
            info += f'\n    {i}'

        return info
    
    def travelInfo(self):
        ticket = self.tripComponent.getTicketPrice() if self.tripComponent.getTicketNeed() else "No Ticket Needed"
        info = f'Date: {self.tripComponent.getTimeFrom().toString("dd/MM/yyyy hh:mm")} - {self.tripComponent.getTimeTo().toString("dd/MM/yyyy hh:mm")}\n'
        info += f'Ticket: {ticket}\n'
        info += f'Information:'
        otherInfo = self.tripComponent.getInfo().split('\n')
        for i in otherInfo:
            info += f'\n    {i}'

        return info
    
    def placeInfo(self):
        openTime = f'{self.tripComponent.getOpenTime().toString("hh:mm")} to {self.tripComponent.getCloseTime().toString("hh:mm")}, Extra Information: {self.tripComponent.getOpenInfo()}' if self.tripComponent.getAddOpen() else 'No Data'
        info = f'Date: {self.tripComponent.getTimeFrom().toString("dd/MM/yyyy hh:mm")} - {self.tripComponent.getTimeTo().toString("dd/MM/yyyy hh:mm")}\n'
        info += f'Open: {openTime}\n'
        info += f'Information:'
        otherInfo = self.tripComponent.getInfo().split('\n')
        for i in otherInfo:
            info += f'\n    {i}'

        return info
    
    def eatInfo(self):
        reservation = "Required" if self.tripComponent.getResevationNeed() else "No Reservation Needed"
        info = f'Date: {self.tripComponent.getTimeFrom().toString("dd/MM/yyyy hh:mm")} - {self.tripComponent.getTimeTo().toString("dd/MM/yyyy hh:mm")}\n'
        info += f'Reservation: {reservation}\n'
        info += f'Information:'
        otherInfo = self.tripComponent.getInfo().split('\n')
        for i in otherInfo:
            info += f'\n    {i}'

        return info
    
    def eventInfo(self):
        ticket = self.tripComponent.getTicketPrice() if self.tripComponent.getTicketNeed() else "No Ticket Needed"
        info = f'Date: {self.tripComponent.getTimeFrom().toString("dd/MM/yyyy hh:mm")} - {self.tripComponent.getTimeTo().toString("dd/MM/yyyy hh:mm")}\n'
        info += f'Type of Event: {self.tripComponent.getType()}\n'
        info += f'Ticket: {ticket}\n'
        info += f'Information:'
        otherInfo = self.tripComponent.getInfo().split('\n')
        for i in otherInfo:
            info += f'\n    {i}'

        return info
    
    def stayInfo(self):
        info = f'Date: {self.tripComponent.getTimeFrom().toString("dd/MM/yyyy hh:mm")} - {self.tripComponent.getTimeTo().toString("dd/MM/yyyy hh:mm")} ({self.tripComponent.getNight()} nights)\n'
        info += f'Total Price: {self.tripComponent.getTotalPrice()}\n'
        info += f'Information:'
        otherInfo = self.tripComponent.getInfo().split('\n')
        for i in otherInfo:
            info += f'\n    {i}'

        return info
    
    # Edit Component - Trip, Travel, Place, Eat, Event, Stay
    def edit(self):
        EditController(controller=self, model=self.tripComponent)

    def editTrip(self, info:dict, reminders:list["Reminder"]):
        self.tripComponent.setName(info['name'])
        self.tripComponent.setTimeFrom(info['timeFrom'])
        self.tripComponent.setTimeTo(info['timeTo'])
        self.tripComponent.setRemind(info['remind'])
        self.tripComponent.setTimesensitive(info['timesensitive'])
        self.tripComponent.writeInfo(info['info'])
        self.tripComponent.setDuration(info['duration'])

        for r in reminders:
            self.tripComponent.addReminder(r)

        transaction.commit()
        self.update()

    def editTravel(self, info:dict):
        self.tripComponent.setName(info['name'])
        self.tripComponent.setTimeFrom(info['timeFrom'])
        self.tripComponent.setTimeTo(info['timeTo'])
        self.tripComponent.setRemind(info['remind'])
        self.tripComponent.setTimesensitive(info['timesensitive'])
        self.tripComponent.writeInfo(info['info'])
        self.tripComponent.setTicketNeed(info['ticketNeed'])
        self.tripComponent.setTicketPrice(info['ticketPrice'])

        transaction.commit()
        self.update()

    def editPlace(self, info:dict):
        self.tripComponent.setName(info['name'])
        self.tripComponent.setTimeFrom(info['timeFrom'])
        self.tripComponent.setTimeTo(info['timeTo'])
        self.tripComponent.setRemind(info['remind'])
        self.tripComponent.setTimesensitive(info['timesensitive'])
        self.tripComponent.writeInfo(info['info'])
        self.tripComponent.setOpenTime(info['openTime'])
        self.tripComponent.setCloseTime(info['closeTime'])
        self.tripComponent.setOpenInfo(info['openInfo'])
        self.tripComponent.setAddOpen(info['addOpen'])

        transaction.commit()
        self.update()

    def editEat(self, info:dict):
        self.tripComponent.setName(info['name'])
        self.tripComponent.setTimeFrom(info['timeFrom'])
        self.tripComponent.setTimeTo(info['timeTo'])
        self.tripComponent.setRemind(info['remind'])
        self.tripComponent.setTimesensitive(info['timesensitive'])
        self.tripComponent.writeInfo(info['info'])
        self.tripComponent.setReservationNeed(info['reservation'])

        transaction.commit()
        self.update()

    def editEvent(self, info:dict):
        self.tripComponent.setName(info['name'])
        self.tripComponent.setTimeFrom(info['timeFrom'])
        self.tripComponent.setTimeTo(info['timeTo'])
        self.tripComponent.setRemind(info['remind'])
        self.tripComponent.setTimesensitive(info['timesensitive'])
        self.tripComponent.writeInfo(info['info'])
        self.tripComponent.setType(info['type'])
        self.tripComponent.setTicketNeed(info['ticketNeed'])
        self.tripComponent.setTicketPrice(info['ticketPrice'])

        transaction.commit()
        self.update()

    def editStay(self, info:dict):
        self.tripComponent.setName(info['name'])
        self.tripComponent.setTimeFrom(info['timeFrom'])
        self.tripComponent.setTimeTo(info['timeTo'])
        self.tripComponent.setRemind(info['remind'])
        self.tripComponent.setTimesensitive(info['timesensitive'])
        self.tripComponent.writeInfo(info['info'])
        self.tripComponent.setFlatRate(info['flatRate'])
        self.tripComponent.setFlatRateCheck(info['flatRateCheck'])
        self.tripComponent.setPricePerNight(info['pricePerNight'])
        self.tripComponent.setPPNCheck(info['pricePerNightCheck'])
        self.tripComponent.setNight(info['night'])
        self.tripComponent.setTotalPrice(info['totalPrice'])

        transaction.commit()
        self.update()
    
    # Add Component - Travel, Place, Eat, Event, Stay
    def addComponent(self):
        EditController(controller=self)

    def addTrip(self, info: dict, reminders: list['Reminder']):
        trip = Trip(name=info['name'], timeFrom=info['timeFrom'], timeTo=info['timeTo'], remind=info['remind'],
                    timesensitive=info['timesensitive'], info=info['info'], duration=info['duration'])
        
        for r in reminders:
            trip.addReminder(r)
        
        self.tripComponent.addComponent(component=trip)
        self.tripComponent.componentList.sort(key=lambda x: x.getTimeFrom())
        transaction.commit()
        self.update()

    def addTravel(self, info:dict):
        travel = Travel(name=info['name'], timeFrom=info['timeFrom'], timeTo=info['timeTo'], remind=info['remind'],
                        timesensitive=info['timesensitive'], info=info['info'], ticketNeed=info['ticketNeed'], ticketPrice=info['ticketPrice'])
        
        self.tripComponent.addComponent(component=travel)
        self.tripComponent.componentList.sort(key=lambda x: x.getTimeFrom())
        transaction.commit()
        self.update()

    def addPlace(self, info:dict):
        place = Place(name=info['name'], timeFrom=info['timeFrom'], timeTo=info['timeTo'], remind=info['remind'],
                      timesensitive=info['timesensitive'], info=info['info'], openTime=info['openTime'], closeTime=info['closeTime'], 
                      openInfo=info['openInfo'], addOpen=info['addOpen']) 
        
        self.tripComponent.addComponent(component=place)
        self.tripComponent.componentList.sort(key=lambda x: x.getTimeFrom())
        transaction.commit()
        self.update()

    def addEat(self, info):
        eat = Eat(name=info['name'], timeFrom=info['timeFrom'], timeTo=info['timeTo'], remind=info['remind'],
                  timesensitive=info['timesensitive'], info=info['info'], reservationNeed=info['reservation'])
        
        self.tripComponent.addComponent(component=eat)
        self.tripComponent.componentList.sort(key=lambda x: x.getTimeFrom())
        transaction.commit()
        self.update()

    def addEvent(self, info):
        event = Event(name=info['name'], timeFrom=info['timeFrom'], timeTo=info['timeTo'], remind=info['remind'],
                      timesensitive=info['timesensitive'], info=info['info'], type=info['type'], ticketNeed=info['ticketNeed'], ticketPrice=info['ticketPrice'])
        
        self.tripComponent.addComponent(component=event)
        self.tripComponent.componentList.sort(key=lambda x: x.getTimeFrom())
        transaction.commit()
        self.update()

    def addStay(self, info:dict):
        stay = Stay(name=info['name'], timeFrom=info['timeFrom'], timeTo=info['timeTo'], remind=info['remind'],
                      timesensitive=info['timesensitive'], info=info['info'], flatRate=info['flatRate'], pricePerNight=info['pricePerNight'], night=info['night'],
                      flatRateCheck=info['flatRateCheck'], pricePerNightCheck=info['pricePerNightCheck'], totalPrice=info['totalPrice'])
        
        self.tripComponent.addComponent(component=stay)
        self.tripComponent.componentList.sort(key=lambda x: x.getTimeFrom())
        transaction.commit()
        self.update()

    def addReminder(self):
        name = self.view.UI.tripReminderLineEdit.text()
        reminder = Reminder(name=name)
        self.tripComponent.addReminder(reminder=reminder)
        self.view.UI.tripReminderLineEdit.setText('')

        transaction.commit()
        self.update()

    def addReminderNoUpdate(self, name):
        reminder = Reminder(name=name)
        self.tripComponent.addReminder(reminder=reminder)

        transaction.commit()

    def editReminder(self, name, isChecked, reminder:"Reminder"):
        reminder.setName(name=name)
        reminder.setIsChecked(isChecked=isChecked)
        
        transaction.commit()
        self.update()

    def deleteReminder(self, reminder:"Reminder"):
        self.tripComponent.removeReminder(reminder)

        transaction.commit()
        self.update()

    def showBudgetInfo(self):
        #propagate up
        if isinstance(self.mainControl, TripController):
            self.mainControl.showBudgetInfo()
        if not self.hasBudget:
            return
        
        # clear old budget list
        self.budgetTextName = ""
        self.budgetTextPrice = ""

        # get all the budget
        if isinstance(self.tripComponent, Trip):
            components = self.tripComponent.getComponents()
            for i in range(len(components)):
                self.appendBudgetText(components[i], 0)
        
        self.view.UI.budgetNameListLabel.setText(self.budgetTextName)
        self.view.UI.budgetPriceListLabel.setText(self.budgetTextPrice)
        self.view.UI.budgetTotalBudgetLabel.setText(str(self.tripComponent.getBudget()))


    def appendBudgetText(self, component, level:int=0):
        if isinstance(component, Trip):
            self.budgetTextName += ("    " * level) + component.getName() + "\n"
            self.budgetTextPrice += "\n"
            for c in component.getComponents():
                self.appendBudgetText(c, level+1)
            self.budgetTextName += "\n"
            self.budgetTextPrice += "\n"
        else:
            # not a trip
            budget = component.getBudget()
            if budget == 0:
                return
            #budget not zero
            self.budgetTextName += ("    " * level) + component.getName() + "\n"
            self.budgetTextPrice += str(budget) + "\n"
