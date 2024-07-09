import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from PyQt6.QtWidgets import QApplication, QMainWindow, QTableWidgetItem
from FormEmployees.frm_Employees_ui import Ui_frm_employee
from FormEmployees.frm_Controller_Employees import EmployeeController


class ManageEmployee(QMainWindow):
    def __init__(self):
       
        super().__init__()
        self.ui = Ui_frm_employee()
        self.ui.setupUi(self)
        # self.setCentralWidget(self.ui.frame_Main)

        # Initialize controller and database connection
        # self.controller = EmployeeController()
        # self.db = ConnectDatabase()

        # Connect buttons to methods
        # self.ui.btn_insert.clicked.connect(self.insertData)
        # self.ui.btn_edit.clicked.connect(self.updateData)
        # self.ui.btn_delete.clicked.connect(self.deleteData)
        # self.ui.btn_search.clicked.connect(self.searchData)
        # Load initial data
        # self.show_data_in_table()
        # self.initUi()

    def initUi(self):
        print('Hello every one My name is alex')
        
        # self.first_name = self.ui.txt_name
        # self.last_name = self.ui.txt_surname
        # self.emp_code = self.ui.txt_emp_code
        # self.phone = self.ui.txt_phone
        # self.address = self.ui.txt_address
        # self.email = self.ui.txt_email
        # self.male = self.ui.rb_Male
        # self.female = self.ui.rb_Female

        # self.tb_show = self.ui.tb_show

        # self.role = self.ui.cmb_role
        # self.position = self.ui.cmb_position
        # self.company = self.ui.cmb_company
        # self.department = self.ui.cmb_department
        # # # Initialize other UI elements similarly
        # self.btn_insert = self.ui.btn_insert
        # self.btn_edit = self.ui.btn_edit
        # self.btn_delete = self.ui.btn_delete
        # self.btn_search = self.ui.btn_search
        # self.controller = EmployeeController


    def show_data_in_table(self):
        print('ok, Hello World')
        return
        data = self.controller.selectData()
        self.ui.tb_show.clear()

        
        self.ui.tb_show.setRowCount(len(data))
        self.ui.tb_show.setColumnCount(len(data[0])) 

        
        for row_num, (uid, uname, ulast, address, phone, email, gender, role, position, department, company) in enumerate(data):
            self.ui.tb_show.setItem(row_num, 0, QTableWidgetItem(str(uid)))
            self.ui.tb_show.setItem(row_num, 1, QTableWidgetItem(uname))
            self.ui.tb_show.setItem(row_num, 2, QTableWidgetItem(ulast))
            self.ui.tb_show.setItem(row_num, 3, QTableWidgetItem(address))
            self.ui.tb_show.setItem(row_num, 4, QTableWidgetItem(phone))
            self.ui.tb_show.setItem(row_num, 5, QTableWidgetItem(email))
            self.ui.tb_show.setItem(row_num, 6, QTableWidgetItem(gender))
            self.ui.tb_show.setItem(row_num, 7, QTableWidgetItem(role))
            self.ui.tb_show.setItem(row_num, 8, QTableWidgetItem(position))
            self.ui.tb_show.setItem(row_num, 9, QTableWidgetItem(department))
            self.ui.tb_show.setItem(row_num, 10, QTableWidgetItem(company))


