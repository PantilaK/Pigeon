from typing import TYPE_CHECKING
import globals

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
            tripInfo = self.editController.getTripInfo()
            if type(controller) == MainController:
                controller.addTrip(tripInfo=tripInfo)
            else: # for editing
                # controller.editTripInfo(tripName=tripName, startDate=startDateTime, endDate=endDateTime)
                pass
                
        else:
            print("Bye")

        globals.mainController.update()

