import psycopg2
import hashlib
import math

class LoginModel:

    def __init__(self):
        self.conn = psycopg2.connect(
            host = 'localhost',
            dbname = 'Pigeon',
            user = 'postgres',
            password = '132547',
            port = '5432'
            )
        
        self.cur = self.conn.cursor()

    def isPasswordMatch(self, password1:str, passowrd2:str):
        """
        Check if passwords are matched.

        This function check whether two passwords are matched or not.

        Parameters
        ----------
        password1 : str
            First password to check.
        password2 : str
            Second password to check.

        Returns
        -------
        bool
            password1 = password2.
        """
        
        if (password1 == passowrd2):
            return True
        
        return False

    
    def getPassword(self, username:str):
        """
        Get password of the given username from database.

        This function get password that stores in the database
        using the given username.

        Parameters
        ----------
        username : str
            Username to find password.

        Returns
        -------
            Password of the given username.
        """

        self.cur.execute(f'''select "password" from "userPassword"
        where "username" = '{username}' ''')
        userPassword = self.cur.fetchone()[0]
        
        return userPassword

    def storingPassword(self, username:str, password:str):
        """
        Add username and password into database table.

        This function receive username and password then convert password into 
        hash before add it into the database table.

        Parameters
        ----------
        username : str
            Username to add.
        password : str
            Password to add.
        """

        hash = hashlib.sha256(password.encode()).hexdigest()

        self.cur.execute(f'''insert into "userPassword"(username, password)
        values('{username}', '{hash}')''')
        self.conn.commit()

    def usernameExists(self, username:str):
        """
        Check if username exists.

        This function check if the given username is already
        exists in the database table or not.

        Parameters
        ----------
        username : str
            username to check if it is existed,
        
        Returns
        -------
        bool
            username is existed.
        """

        self.cur.execute(f'''select "username" from "userPassword"
        where "username" = '{username}' ''')

        if self.cur.fetchone() == None:
            return False
        
        return True
    
    def createAccount(self, username:str, password:str):
        """
        Check username availability.

        This function check whether there is the same username in the 
        database table or not. If not it will create an account for
        the user.

        Parameters
        ----------
        username : str
            username to check and create an account.
        password : str
            password for an account.
        """

        if not self.usernameExists(username):
            self.storingPassword(username, password)
            return True
        

    def verifyPassword(self, username:str, password:str):
        """
        Verify password.

        This function check input password matchs with password that is
        in database or not.

        Parameters
        ----------
        username : str
            username that is used to verify.
        password : str
            input password to be checked.
    
        Returns
        -------
        bool
            True or False.
        """
        hash = hashlib.sha256(password.encode()).hexdigest()

        if hash == self.getPassword(username):
            return True
        else:
            return False

# o = LoginDriver()
# math.sqrt()
# o.isPasswordMatch()
# o.createAccount()

# o = LoginModel()
# o.createAccount("jiji","koko")
# o.verifyPassword('jiji', 'kok')
