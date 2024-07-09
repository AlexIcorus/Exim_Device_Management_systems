import sys,os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from ModeConnect.DBConnect import ConnectDatabase



class UserController:
    def __init__(self):
        
        self.db = ConnectDatabase()
        
       
    

    def selectData(self):
    # Connect to the database
        self.db.connect_db()
 
        sql = f"""
            SELECT * FROM users """

        try:
            # Execute the SQL query for searching information
            self.db.cursor.execute(sql)
            result = self.db.cursor.fetchall()
            print(result)
            return result

        except Exception as E:
            return E

        finally:
            # Close the database connection
            self.db.con.close()
    
    def insertData(self, first_name, last_name):
        self.db.connect_db()
        sql = "INSERT INTO employee (first_name, last_name) VALUES (?, ?);"
        try:
            self.db.cursor.execute(sql, (first_name, last_name))
            self.db.con.commit()

        except Exception as E:
            return E
        
        finally:
            self.db.con.close()
    
    def updateData(self, id, first_name, last_name):
        self.db.connect_db()
        sql = "UPDATE employee SET first_name = ?, last_name = ? WHERE id = ?;"
        try:
            self.db.cursor.execute(sql, (first_name, last_name, id))
            self.db.con.commit()

        except Exception as E:
            return E
        
        finally:
            self.db.con.close()
    
    def deleteData(self, id):
        self.db.connect_db()
        sql = "DELETE FROM employee WHERE id = ?;"
        try:
            self.db.cursor.execute(sql, (id,))
            self.db.con.commit()

        except Exception as E:
            return E
        
        finally:
            self.db.con.close()

    