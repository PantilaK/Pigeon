import persistent

class Reminder(persistent.Persistent):
    
    def __init__(self, name):
        self.__name = name
        self.__isChecked = False

    # Name
    def getName(self):
        return self.__name
    
    def setName(self, name):
        self.__name = name

    # Is Checked
    def getIsChecked(self):
        return self.__isChecked
    
    def setIsChecked(self, isChecked):
        self.__isChecked = isChecked