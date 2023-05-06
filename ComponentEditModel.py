from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from User import User
    from MainModel import MainModel
    from MainControl import MainController
    from ComponentEditControl import EditController

class ComponentEditModel:

    def __init__(self, editController: "EditController"):
        self.editController = editController

    def ok(self, source, mainController: "MainController"=None):
        if source == "Trip":
            tripName = self.editController.getTripName()
            mainController.addTrip(tripName)
        else:
            print("Bye")
