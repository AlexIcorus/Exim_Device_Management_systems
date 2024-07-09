import sys
import os
import bcrypt 
from PyQt6.QtWidgets import QApplication, QMainWindow,QTableWidgetItem,QMessageBox
from Register.ui_register_ui import Ui_MainWindow


class RegisterManage(QMainWindow):
    def __init__(self):
        super().__init__() 
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.initUi()

        self.signal_btn()

        

    def initUi(self):
        self.first_name = self.ui.txt_firstname
        self.last_name = self.ui.txt_surname
        self.username = self.ui.txt_username
        self.password = self.ui.txt_password
        self.btn_register = self.ui.btn_register
        self.btn_close = self.ui.btn_close

    def signal_btn(self):
        self.btn_close.clicked.connect(self.close_form_register())


    def close_form_register(self):
        print('Ok')
        # self.close()
    
    # def add_info(self):
    #     # Function to add student information

    #     user_info = self.get_user_info()
    #     print(user_info)
    #     return
    #     if user_info["first_name"] and user_info["last_name"]:
    #         check_result = self.check_student_id(student_id=int(user_info["student_id"]))

    #         if check_result:
    #             QMessageBox.information(self, "Warning", "Please input a new student ID",
    #                                     QMessageBox.StandardButton.Ok)
    #             # self.enable_buttons()
    #             return

    #         add_result = self.db.add_info(
    #                                       first_name=user_info["first_name"],
    #                                       last_name=user_info["last_name"],
    #                                       username=user_info["username"],
    #                                       state=user_info["password"])

    #         if add_result:
    #             QMessageBox.information(self, "Warning", f"Add fail: {add_result}, Please try again.",
    #                                     QMessageBox.StandardButton.Ok)

    #     else:
    #         QMessageBox.information(self, "Warning", "Please input student ID and first name.",
    #                                 QMessageBox.StandardButton.Ok)
            
    
    # def get_user_info(self):
    #     # Function to retrieve student information from the form
       
    #     first_name = self.first_name.text().strip()
    #     last_name = self.last_name.text().strip()
    #     username = self.username.text().strip()
    #     password = self.password.text().strip() 
      
        
    #     # converting password to array of bytes 
    #     bytes = password.encode('utf-8') 
        
    #     # generating the salt 
    #     salt = bcrypt.gensalt() 
        
    #     # Hashing the password 
    #     hash = bcrypt.hashpw(bytes, salt) 
  

    #     user_info = {
    #         "first_name": first_name,
    #         "last_name": last_name,
    #         "username": username,
    #         "password": hash
          
    #     }

    #     return user_info
    
    # def check_user_id(self, user_id):
     
    #     result = self.db.search_info(user_id=user_id)
    #     return result