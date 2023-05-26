import hashlib
from User import User
import transaction

class LoginModel:

    def __init__(self, root):
        self.root = root

    
    def getPassword(self, username:str):
        if username in self.root['username']:
            return self.root['username'][username].getPassword()


    def storingPassword(self, username:str, password:str):
        hash = hashlib.sha256(password.encode()).hexdigest()

        tmp = self.root['username']
        tmp[username] = User(username, hash)
        self.root['username'] = tmp

        transaction.commit()

    def createAccount(self, username:str, password:str):
        ruser = username.strip()
        username = ruser

        if username == "" or password == "":
            return (False, "Invalid username or password")
        
        if username in self.root['username']:
            return (False, "Username already exists")
        
        self.storingPassword(username, password)
        return (True, "Account Succesfully Created")

    def verifyPassword(self, username:str, password:str):
        # Check if username exists
        ruser = username.strip()
        username = ruser
        if username not in self.root['username']:
            return (False, "Username does not exists")
        
        # temp = self.root['username']
        # user:User = temp[username]
        # print(user.currentTrips[2].getTripName(), user.currentTrips[4].getTripName())
        # temp = self.root['username']
        # user:User = temp[username]
        # t1 = Trip("Trip 3")
        # t2 = Trip("Trip 4")
        # user.addCurrentTrip(t1)
        # user.addCurrentTrip(t2)
        # transaction.commit()
        
        hash = hashlib.sha256(password.encode()).hexdigest()

        if hash == self.getPassword(username):
            return True
        else:
            return (False, "Incorrect password")
        
    def getUser(self, username: str):
        ruser = username.strip()
        username = ruser
        tmp = self.root['username']
        user = tmp[username]
        return user
    
    def changeUsername(self, newUsername: str, username: str):
        newUsername = newUsername

        if newUsername == "":
            return "Invalid username"
        
        if newUsername in self.root['username']:
            return "Username already exists"
        
        self.storingNewUsername(username=username, newUsername=newUsername)
        return "Username Change Sucessfully"
    
    def storingNewUsername(self, username, newUsername):
        tmp = self.root['username']

        user:User = tmp[username]
        del tmp[username]
        user.setUsername(username=newUsername)

        tmp[newUsername] = user
        self.root['username'] = tmp

        transaction.commit()

    def changePassword(self, username, password:str):
        if password == "":
            return "Invalid password"
        
        hash = hashlib.sha256(password.encode()).hexdigest()

        tmp = self.root['username']

        user:User = tmp[username]
        user.setPassword(hash)

        tmp[username] = user
        self.root['username'] = tmp

        transaction.commit()
        return "Password Changed Sucessfully"



        
    

