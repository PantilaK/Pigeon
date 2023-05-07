from ui_mainForm import *

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from MainControl import MainController


class MainUI(QWidget):
    def __init__(self, controller, parent=None) -> None:
        super().__init__(parent, Qt.WindowType.Window)
        self.controller: "MainController" = controller
        self.UI = Ui_mainWidget()
        self.UI.setupUi(self)

        self.UI.currentTripButton.clicked.connect(self.currentTripButtonPressed)
        self.UI.pastTripButton.clicked.connect(self.pastTripButtonPressed)
        self.UI.futureTripButton.clicked.connect(self.futureTripButtonPressed)
        self.UI.newTripButton.clicked.connect(self.newTripButtonPressed)
        self.UI.logoutButton.clicked.connect(self.logoutButtonPressed)

    def setTripMode(self, mode):
        self.UI.tripListHeading.setText(mode)

    def addTrip(self, newTripUI):
        self.UI.tripListLayout.addWidget(newTripUI)

    def clearTripList(self):
        for i in reversed(range(self.UI.tripListLayout.count())):
            self.UI.tripListLayout.itemAt(i).widget().setParent(None)

    def currentTripButtonPressed(self):
        self.controller.goToCurrentTrip()
    
    def pastTripButtonPressed(self):
        self.controller.goToPastTrip()

    def futureTripButtonPressed(self):
        self.controller.goToFutureTrip()

    def newTripButtonPressed(self):
        self.controller.newTrip()

    def newTripOKButtonPressed(self):
        self.controller.addTrip()

    def logoutButtonPressed(self):
        self.controller.transferToLogin()