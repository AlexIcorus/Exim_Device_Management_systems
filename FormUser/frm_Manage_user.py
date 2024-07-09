import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from PyQt6.QtWidgets import QApplication, QMainWindow,QTableWidgetItem
from FormUser.frm_users_ui import Ui_frm_users
from FormUser.frm_Controller_User import UserController

class ManageUser(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_frm_users()
        self.ui.setupUi(self)
        self.setCentralWidget(self.ui.frame_3)
        self.usercontroller = UserController()

        self.result_table = self.ui.tb_show
        
        self.data = self.usercontroller.selectData()

        # self.show_data()

    # def show_data(self, data, additional_columns=None):
    #     if not data:
    #         self.result_table.setRowCount(0)
    #         return

    #     # Determine the number of columns
    #     if isinstance(data[0], dict):
    #         columns = list(data[0].keys())
    #     else:
    #         columns = ["user_Id", "first_Name", "last_Name", "address", "phone", "fax", "email", "gender", "username", "password", "emp_id"]
    #         if additional_columns:
    #             columns.extend(additional_columns)

    #     self.result_table.setRowCount(0)
    #     self.result_table.setRowCount(len(data))
    #     self.result_table.setColumnCount(len(columns))

    #     for row, entry in enumerate(data):
    #         if isinstance(entry, dict):
    #             values = [entry.get(col) for col in columns]
    #         else:
    #             values = entry

    #         for col, value in enumerate(values):
    #             cell_item = QTableWidgetItem(str(value))
    #             self.result_table.setItem(row, col, cell_item)

    #     self.result_table.setColumnHidden(0, True)
            
    
    # def show_data(self):
    #     print(self.data)
        
    #     if result:
    #         self.result_table.setRowCount(0)
    #         self.result_table.setRowCount(len(result))

    #         for row, info in enumerate(result):
    #             info_list = [
    #                 info["user_Id"],
    #                 info["first_Name"],
    #                 info["last_Name"],
    #                 info["address"],
    #                 info["phone"],
    #                 info["fax"],
    #                 info["email"],
    #                 info["gender"],
    #                 info["username"],
    #                 info["password"]
    #             ]

    #             for column, item in enumerate(info_list):
    #                 cell_item = QTableWidgetItem(str(item))
    #                 self.result_table.setItem(row, column, cell_item)

    #     else:
    #         self.result_table.setRowCount(0)
    #         return


    # def submit_user_data(self):
    #     # Use the collected user data
    #     user_data = self.collect_user_data()
    #     print('Submitting User Data:', user_data)
        
    #     result = self.user_controller.insertData(user_data["first_name"], user_data["surname"])
    #     if result:
    #         print("Error:", result)
    #     else:
    #         print("User data submitted successfully")

    # # Additional methods to update, delete, and fetch data
    # def update_user_data(self, user_id):
    #     user_data = self.collect_user_data()
    #     result = self.user_controller.updateData(user_id, user_data["first_name"], user_data["surname"])
    #     if result:
    #         print("Error:", result)
    #     else:
    #         print("User data updated successfully")

    # def delete_user_data(self, user_id):
    #     result = self.user_controller.deleteData(user_id)
    #     if result:
    #         print("Error:", result)
    #     else:
    #         print("User data deleted successfully")

    # def fetch_user_data(self):
    #     result = self.user_controller.selectData()
    #     if isinstance(result, Exception):
    #         print("Error:", result)
    #     else:
    #         self.populate_table(result)

    # def populate_table(self, data):
    #     self.ui.tb_show.setRowCount(0)
    #     for row_data in data:
    #         row_number = self.ui.tb_show.rowCount()
    #         self.ui.tb_show.insertRow(row_number)
    #         for column_number, cell_data in enumerate(row_data):
    #             self.ui.tb_show.setItem(row_number, column_number, QTableWidgetItem(str(cell_data)))


# Application entry point
if __name__ == '__main__':
    app = QApplication(sys.argv)

    main_window = ManageUser()
    main_window.show()

    sys.exit(app.exec())
