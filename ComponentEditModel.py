from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from User import User
    from MainModel import MainModel
    from ComponentEditControl import EditController
    from PySide6.QtCore import QDateTime

class ComponentEditModel:

    def __init__(self, editController: "EditController"):
        self.editController = editController

    def ok(self, source, controller = None):
        from MainControl import MainController
        if source == "Trip":
            tripName = self.editController.getTripName()
            startDateTime = self.editController.getTripStartDate()
            endDateTime = self.editController.getTripEndDate()
            if type(controller) == MainController:
                controller.addTrip(tripName=tripName, startDate=startDateTime, endDate=endDateTime)
            else: # for editing
                controller.editTripInfo(tripName=tripName, startDate=startDateTime, endDate=endDateTime)
                
        else:
            print("Bye")

