from typing import TYPE_CHECKING
import globals
import transaction

if TYPE_CHECKING:
    from TripControl import TripController
    from Trip import Trip

class TripModel:

    def __init__(self, tripController: "TripController"):
        self.controller = tripController

    def editTripInfo(self, tripName, startDate, endDate):
        if tripName != "":
            self.controller.trip.tripName = tripName

    def deleteTrip(self, trip: "Trip"):
        globals.currentUser.removeTrip(trip)
        globals.mainController.update()

        transaction.commit()
        