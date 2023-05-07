from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from User import User
    from MainModel import MainModel
    from ComponentEditControl import EditController

class ComponentEditModel:

    def __init__(self, editController: "EditController"):
        self.editController = editController

    def ok(self, source, controller = None):
        from MainControl import MainController
        if source == "Trip":
            tripName = self.editController.getTripName()
            if type(controller) == MainController:
                controller.addTrip(tripName)
            else:
                # for trip in self.user.
                print(controller)
                
        else:
            print("Bye")
