from typing import TYPE_CHECKING
import globals

if TYPE_CHECKING:
    from User import User
    from MainModel import MainModel
    from ComponentEditControl import EditController
    from PySide6.QtCore import QDateTime
    from TripControl import TripController

class ComponentEditModel:

    def __init__(self, editController: "EditController"):
        self.editController = editController

    def ok(self, source, controller = None):
        from MainControl import MainController

        if source == "Trip":
            tripInfo = self.editController.getTripInfo()

            if type(controller) == MainController:
                controller.addTrip(tripInfo=tripInfo)
            else: # for editing
                # controller.editTripInfo(tripName=tripName, startDate=startDateTime, endDate=endDateTime)
                pass

        elif source == "Travel":
            print("Travel")
            travelInfo = self.editController.getTravelInfo()
            controller.addTravel(travelInfo=travelInfo, trip=controller.trip)
        
        elif source == "Place":
            print("Place")
            placeInfo = self.editController.getPlaceInfo()
            controller.addPlace(placeInfo=placeInfo, trip=controller.trip)

        elif source == "Eat":
            print("Eat")
            eatInfo = self.editController.getEatInfo()
            controller.addEat(eatInfo=eatInfo, trip=controller.trip)
        
        elif source == "Event":
            print("Event")
            eventInfo = self.editController.getEventInfo()
            controller.addEvent(eventInfo=eventInfo, trip=controller.trip)

        elif source == "Stay":
            print("Stay")
            stayInfo = self.editController.getStayInfo()
            stayInfo['period'] = 0
            stayInfo['totalPrice'] = 0
            controller.addCheckIn(stayInfo=stayInfo, trip=controller.trip)

            checkoutDate = stayInfo['timeTo']
            stayInfo['timeFrom'] = checkoutDate
            controller.addCheckOut(stayInfo=stayInfo, trip=controller.trip)
        else:
            print("Bye")

        globals.mainController.update()

