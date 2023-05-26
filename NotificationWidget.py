from notification_ui import *

class NotificationWidget(QWidget):
    def __init__(self, controller=None, parentUI=None):
        super().__init__(parentUI)
        self.controller = controller
        self.UI = Ui_notificationUI()
        self.UI.setupUi(self)

        self.UI.dismissButton.clicked.connect(self.dismissButtonClicked)

    def dismissButtonClicked(self):
        self.controller.dismiss()

    
