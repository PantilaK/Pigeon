from NotificationWidget import NotificationWidget

class NotificationController:
    def __init__(self, model=None, parentController = None):
        self.model = model
        self.parentController = parentController

        self.view = NotificationWidget(self, self.parentController.view)

    def dismiss(self):
        #delete notification
        pass
