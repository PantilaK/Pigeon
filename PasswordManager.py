import psycopg2
import hashlib

class PasswordManager:

    def __init__(self):
        self.conn = psycopg2.connect(
            host = 'localhost',
            dbname = 'Pigeon',
            user = 'postgres',
            password = '132547',
            port = '5432'
            )
        
        self.usernamePassword = {}
        
        self.cur = self.conn.cursor()

        self.getUsernamePassword()
    
    # Get username and password from database
    def getUsernamePassword(self):
        self.cur.execute('''select * from "userPassword"''')
        userPassword = self.cur.fetchall()

        for username in userPassword:
            self.usernamePassword[username[0]] = username[1]

    # username (str)
    # password (str)
    # Storing username and hash password into the database tabel and hashMap
    def storingPassword(self, username:str, password:str):
        hash = hashlib.sha256(password.encode()).hexdigest()
        print(hash)
        self.usernamePassword[username] = hash

        self.cur.execute('''insert into "userPassword"(username, password)
        values('{}', '{}')'''.format(username, hash))
        self.conn.commit()

    # username (str)
    # password (str)
    # Check if username is available or not
    # Call storingPassword function to store username password into database
    # and hashMap
    def createAccount(self, username:str, password:str):
        if username not in self.usernamePassword:
            self.storingPassword(username, password)

    def verifyPassword(self, username:str, password:str):
        hash = hashlib.sha256(password.encode()).hexdigest()

        if hash == self.usernamePassword.get(username):
            print("correct")
            print()
            return True
        else:
            print(hash)
            print(self.usernamePassword.get(username))

if __name__ == "__main__":
    o = PasswordManager()
    # o.storingPassword("hicodsv", "hohoho")
    o.verifyPassword("hicodsv", "hohoho" )
    o.getUsernamePassword()