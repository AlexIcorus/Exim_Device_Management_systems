import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from PyQt6.QtWidgets import QApplication, QMainWindow,QTableWidgetItem
from ModeConnect.DBConnect import ConnectDatabase


class RegisterController:
    def __init__(self):
        
        self.db = ConnectDatabase()


    def ConfirmData(self,first_name,last_name,username,password):

            sql =   f"""INSERT INTO users (first_name, last_name,username, password) 
	            VALUES ('{first_name}', '{last_name}', '{username}', '{password}');"""
            try:
                # Execute the SQL query for adding information
                self.db.cursor.execute(sql)
                self.db.con.commit()

            except Exception as E:
                # Rollback the transaction in case of an error
                self.db.con.rollback()
                return E

            finally:
                # Close the database connection
                self.db.con.close()



        