import sys,os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from ModeConnect.DBConnect import ConnectDatabase



class LoginController:
    def __init__(self):
        
        self.db = ConnectDatabase()
        self.selectEncodePassword()
       
    

    def selectEncodePassword(self):
        
   
        self.db.connect_db()
       
        sql = f"""
            SELECT password FROM users WHERE username = %s;
            """
        try:
           
            self.db.cursor.execute(sql)
            result = self.db.cursor.fetchall()
            print(result)
            return result

        except Exception as E:
            return E

        finally:
            # Close the database connection
            self.db.con.close()
    
    