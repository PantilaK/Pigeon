from NotificationWidget import NotificationWidget

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from MainControl import MainController
    from Reminder import Notification

class NotificationController:
    def __init__(self, model=None, parentController = None):
        self.model:Notification = model
        self.parentController:MainController = parentController

        self.view = NotificationWidget(self, self.parentController.view)

        self.updateUI()

    def updateUI(self):
        self.setNoti()

    def dismiss(self):
        #delete notification
        self.parentController.deleteNoti(self.model)

    def setNoti(self):
        name = self.model.getName()
        self.view.UI.notificationLabel.setText(name)
