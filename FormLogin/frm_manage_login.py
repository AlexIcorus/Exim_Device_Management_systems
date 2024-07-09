import sys
import bcrypt
from PyQt6.QtWidgets import QApplication, QWidget, QMessageBox

from FormLogin.frm_login_ui import Ui_frm_Login
from ModeConnect.DBConnect import ConnectDatabase
from FormLogin.frm_Controller_Login import LoginController
from Register.frm_register_Manage import RegisterManage

class ManageLogin(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_frm_Login()
        self.ui.setupUi(self)
        self.register = self.ui.btn_register
        self.register.clicked.connect(self.OpenRegister)
        self.windows =[]
        # self.db = ConnectDatabase()
        # self.Data = LoginController()

        # self.init_ui()

    # def init_ui(self):
    #     self.user = self.ui.txt_username
    #     self.password = self.ui.txt_password
    #     self.Login = self.ui.btn_login
    #     self.Register = self.ui.btn_register

    #     self.Login.clicked.connect(self.login) 
    #     self.Register.clicked.connect(self.OpenRegister)

    def OpenRegister(self):
        registerform = RegisterManage()
        self.windows.append(registerform)
        registerform.show()
        # self.close()
       
      

    # @pyqtSlot()
    # def login(self):
        
    #     username = self.user.text()
    #     password = self.password.text()

    #     if not username or not password:
    #         QMessageBox.warning(self, "Input Error", "Please enter both username and password.")
    #         return

    #     result = self.Data.selectEncodePassword()

    #     if result:
    #         # stored_hash = result[0]
    #         # if bcrypt.checkpw(password.encode('utf-8'), stored_hash.encode('utf-8')):
    #         #     QMessageBox.information(self, "Login Success", "You have successfully logged in!")
    #         # else:
    #         #     QMessageBox.warning(self, "Login Failed", "Incorrect password.")
    #         print('Pass',result)
    #         return
    #     else:
    #         # QMessageBox.warning(self, "Login Failed", "Username not found.")
    #         print('Fail')
    #         return
