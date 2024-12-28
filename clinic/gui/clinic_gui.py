import sys
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QGridLayout
from PyQt6.QtWidgets import QPushButton, QWidget, QLineEdit, QDialog, QDialogButtonBox, QLabel, QMessageBox
from clinic.controller import Controller
from clinic.gui.clinic_actual_gui import ClinicActualGUI

class ClinicGUI(QWidget):

    def __init__(self):
        super().__init__()
        # Continue here with your code!
        self.controller = Controller(True)
        self.setWindowTitle("Clinic Login")
        self.resize(600, 400)

        # sub window
        self.clinicActual_gui = ClinicActualGUI(self.controller)

        # layout initialization
        layout = QGridLayout()

        # login page
        add_login_button = QPushButton("Login")
        add_login_button.setFixedSize(450, 25)
        add_login_button.clicked.connect(self.add_login_button_clicked)

        add_quit_button = QPushButton("Quit")
        add_quit_button.setFixedSize(450, 25)
        add_quit_button.clicked.connect(self.close)

        self.username_input = QLineEdit()
        self.username_input.setFixedSize(450, 25)
        self.username_input.setPlaceholderText("Username")

        self.password_input = QLineEdit()
        self.password_input.setFixedSize(450, 25)
        self.password_input.setPlaceholderText("Password")
        self.password_input.setEchoMode(QLineEdit.EchoMode.Password)

        layout.addWidget(self.username_input, 0, 0)
        layout.addWidget(self.password_input, 1, 0)
        layout.addWidget(add_login_button, 2, 0, alignment=Qt.AlignmentFlag.AlignRight)
        layout.addWidget(add_quit_button, 3, 0, alignment=Qt.AlignmentFlag.AlignRight)

        layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.setRowStretch(0, 1)
        self.setLayout(layout)

    def add_login_button_clicked(self):
        username = self.username_input.text().strip()
        password = self.password_input.text().strip()

        try:
            if self.controller.login(username, password):
                self.controller.logged_in_user = username
                self.clinicActual_gui = ClinicActualGUI(self.controller)
                self.clinicActual_gui.show()
                self.hide()
        except Exception as e:
            button = QMessageBox.critical(
                self,
                "invalid login",
                "incorrect username or password",
                buttons=QMessageBox.StandardButton.Discard
            )

def main():
    app = QApplication(sys.argv)
    window = ClinicGUI()
    window.show()
    app.exec()

if __name__ == '__main__':
    main()