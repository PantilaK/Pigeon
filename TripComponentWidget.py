from ui_tripComponent import *

class TripComponentWidget(QWidget):
    def __init__(self, tripController, parent=None):
        super().__init__(parent)
        self.controller  = tripController
        self.widget = Ui_tripWidget()
        self.widget.setupUi(self)
        
        self.widget.tripExpandButton.clicked.connect(self.expandButtonClicked)
        self.widget.tripEditButton.clicked.connect(self.editButtonClicked)
        self.widget.tripDeleteButton.clicked.connect(self.deleteButtonClicked)
        self.widget.addComponentButton.clicked.connect(self.addComponentButtonClicked)

    def expandButtonClicked(self):
        self.controller.expand()

    def editButtonClicked(self):
        self.controller.edit()

    def deleteButtonClicked(self):
        self.controller.delete()

    def addComponentButtonClicked(self):
        self.controller.addComponent()

    



        