import mysql.connector


class ConnectDatabase:
    def __init__(self):
        self._host = "127.0.0.1"
        self._port = 3306
        self._user = "root"
        self._password = ""
        self._database = "exim_device_management_system"
        self.con = None
        self.cursor = None
    
    def connect_db(self):
        # Establish a database connection
        
        self.con = mysql.connector.connect(
            host=self._host,
            port=self._port,
            database=self._database,
            user=self._user,
            password=self._password
        )

        # Create a cursor for executing SQL queries
        self.cursor = self.con.cursor(dictionary=True)