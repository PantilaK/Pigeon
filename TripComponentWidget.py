from tripComponent_ui import *

class TripComponentWidget(QWidget):
    def __init__(self, tripController, parentUI=None):
        super().__init__(parentUI)
        self.controller  = tripController
        self.UI = Ui_tripWidget()
        self.UI.setupUi(self)
        
        self.UI.tripExpandButton.clicked.connect(self.expandButtonClicked)
        self.UI.tripEditButton.clicked.connect(self.editButtonClicked)
        self.UI.tripDeleteButton.clicked.connect(self.deleteButtonClicked)
        self.UI.addComponentButton.clicked.connect(self.addComponentButtonClicked)
        self.UI.tripReminderAddButton.clicked.connect(self.tripReminderAddButtonClicked)
        self.UI.tripReminderLineEdit.returnPressed.connect(self.tripReminderLineEditReturn)

    def addComponent(self, component):
        self.UI.componentLayout.addWidget(component)

    def clearComponentLists(self):
        for i in reversed(range(self.UI.componentLayout.count())):
            self.UI.componentLayout.itemAt(i).widget().setParent(None)

    def expandButtonClicked(self):
        self.controller.expand()

    def editButtonClicked(self):
        self.controller.edit()

    def deleteButtonClicked(self):
        self.controller.delete()

    def addComponentButtonClicked(self):
        self.controller.addComponent()

    def tripReminderAddButtonClicked(self):
        self.controller.addReminder()

    def tripReminderLineEditReturn(self):
        self.controller.addReminder()
    
    # Add detail
    def addDetil(self, detail):
        self.UI.label.setText(detail)

    def setTitle(self, title):
        self.UI.tripTitle.setText(title)
