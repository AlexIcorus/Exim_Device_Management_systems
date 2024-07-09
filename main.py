
import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QPushButton, QWidget, QMdiArea
from FormLogin.frm_manage_login import ManageLogin


# Application entry point
if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = ManageLogin()
    window.show()

    sys.exit(app.exec())
