from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from TripControl import TripController
    from User import User
    from MainModel import MainModel
    from ComponentEditControl import EditController
    from PySide6.QtCore import QDateTime

class TripModel:

    def __init__(self, tripController: "TripController"):
        self.controller = tripController

    def editTripInfo(self, tripName, startDate, endDate):
        if tripName != "":
            self.controller.trip.tripName = tripName
        