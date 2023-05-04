from ui_mainForm import *


class MainUI(QWidget):
    def __init__(self, controller) -> None:
        super().__init__(None)
        self.controller = controller
        self.UI = Ui_mainWidget()
        self.UI.setupUi()

        self.UI.currentTripButton.clicked.connect(self.currentTripButtonPressed)
        self.UI.pastTripButton.clicked.connect(self.pastTripButtonPressed)
        self.UI.futureTripButton.clicked.connect(self.futureTripButtonPressed)

    
    def currentTripButtonPressed(self):
        self.controller.goToCurrentTrip()

    
    def pastTripButtonPressed(self):
        self.controller.goToPastTrip()

    def futureTripButtonPressed(self):
        self.controller.goToFutureTrip()