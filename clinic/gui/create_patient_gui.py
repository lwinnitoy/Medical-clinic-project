import sys
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QGridLayout
from PyQt6.QtWidgets import QPushButton, QWidget, QLabel, QLineEdit


class CreatePatientGUI(QWidget):

    def __init__(self, controller):
        super().__init__()
        # Continue here with your code!
        self.controller = controller
        self.setWindowTitle("Create Patient")

        layout = QGridLayout()

        self.phn_input = QLineEdit()
        self.phn_input.setFixedSize(450, 25)
        self.phn_input.setPlaceholderText("Personal Health Number")
        layout.addWidget(self.phn_input, 0, 0)

        self.fullname_input = QLineEdit()
        self.fullname_input.setFixedSize(450, 25)
        self.fullname_input.setPlaceholderText("Full Name")
        layout.addWidget(self.fullname_input, 1, 0)

        self.birthdate_input = QLineEdit()
        self.birthdate_input.setFixedSize(450, 25)
        self.birthdate_input.setPlaceholderText("Bith Date (YYYY-MM-DD)")
        layout.addWidget(self.birthdate_input, 2, 0)

        self.phone_input = QLineEdit()
        self.phone_input.setFixedSize(450, 25)
        self.phone_input.setPlaceholderText("Phone Number")
        layout.addWidget(self.phone_input, 3, 0)

        self.email_input = QLineEdit()
        self.email_input.setFixedSize(450, 25)
        self.email_input.setPlaceholderText("Email")
        layout.addWidget(self.email_input, 4, 0)

        self.address_input = QLineEdit()
        self.address_input.setFixedSize(450, 25)
        self.address_input.setPlaceholderText("Address")
        layout.addWidget(self.address_input, 5, 0)

        # add_back_button = QPushButton("Back")
        # add_back_button.clicked.connect(self.add_back_button_clicked)
        # layout.addWidget(add_back_button, 6, 0, alignment=Qt.AlignmentFlag.AlignLeft)

        add_create_button = QPushButton("Create")
        add_create_button.clicked.connect(self.add_create_button_clicked)
        layout.addWidget(add_create_button, 6, 0, alignment=Qt.AlignmentFlag.AlignLeft)
        
        # layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        # layout.setRowStretch(0, 1)
        # layout.setRowStretch(4, 1)
        self.setLayout(layout)

    # def add_back_button_clicked(self):
    #     from clinic.gui.clinic_actual_gui import ClinicActualGUI
    #     try:
    #         self.clinic_actual_gui = ClinicActualGUI(self.controller)
    #         self.clinic_actual_gui.show()
    #         self.close()
    #     except Exception as e:
    #         print(str(e))

    # self, phn, name, birthdate, phone, email, address
    def add_create_button_clicked(self):
        phn = self.phn_input.text().strip()
        fullname = self.fullname_input.text().strip()
        birthdate = self.birthdate_input.text().strip()
        phone = self.phone_input.text().strip()
        email = self.email_input.text().strip()
        address = self.address_input.text().strip()

        try:
            self.controller.create_patient(phn, fullname, birthdate, phone, email, address)
            self.close()
        except Exception as e:
            print(str(e))
            

def main():
    app = QApplication(sys.argv)
    window = CreatePatientGUI()
    window.show()
    app.exec()

if __name__ == '__main__':
    main()
