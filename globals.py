from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from User import User
    from MainControl import MainController

currentUser: "User" = None
mainController: "MainController" = None