import hashlib
from User import User
import transaction

class LoginModel:

    def __init__(self, root):
        self.root = root

    def isPasswordMatched(self, password1:str, passowrd2:str):
        if (password1 == passowrd2) and (password1 != "" or password1 != " "):
            return (True, "")
        
        return (False, "Passwords do not match")

    
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
            return "Invalid username or password"
        
        if username in self.root['username']:
            return "Username already exists"
        
        self.storingPassword(username, password)
        return "Account Succesfully Created"

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

        
    

