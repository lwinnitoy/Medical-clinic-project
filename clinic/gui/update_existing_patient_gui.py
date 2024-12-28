import sys
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QGridLayout
from PyQt6.QtWidgets import QPushButton, QWidget, QLabel, QLineEdit
from clinic.controller import IllegalAccessException, IllegalOperationException


class UpdatePatientGUI(QWidget):

    def __init__(self, controller):
        super().__init__()
        # Continue here with your code!
        self.controller = controller
        self.setWindowTitle("Update Patient")

        layout = QGridLayout()\
        
        self.original_phn_input = QLineEdit()
        self.original_phn_input.setFixedSize(450, 25)
        self.original_phn_input.setPlaceholderText("Original Personal Health Number")
        layout.addWidget(self.original_phn_input, 0, 0)

        self.phn_input = QLineEdit()
        self.phn_input.setFixedSize(450, 25)
        self.phn_input.setPlaceholderText("New Personal Health Number")
        layout.addWidget(self.phn_input, 1, 0)

        self.fullname_input = QLineEdit()
        self.fullname_input.setFixedSize(450, 25)
        self.fullname_input.setPlaceholderText("Full Name")
        layout.addWidget(self.fullname_input, 2, 0)

        self.birthdate_input = QLineEdit()
        self.birthdate_input.setFixedSize(450, 25)
        self.birthdate_input.setPlaceholderText("Bith Date (YYYY-MM-DD)")
        layout.addWidget(self.birthdate_input, 3, 0)

        self.phone_input = QLineEdit()
        self.phone_input.setFixedSize(450, 25)
        self.phone_input.setPlaceholderText("Phone Number")
        layout.addWidget(self.phone_input, 4, 0)

        self.email_input = QLineEdit()
        self.email_input.setFixedSize(450, 25)
        self.email_input.setPlaceholderText("Email")
        layout.addWidget(self.email_input, 5, 0)

        self.address_input = QLineEdit()
        self.address_input.setFixedSize(450, 25)
        self.address_input.setPlaceholderText("Address")
        layout.addWidget(self.address_input, 6, 0)

        add_update_button = QPushButton("Update")
        add_update_button.clicked.connect(self.add_update_button_clicked)
        layout.addWidget(add_update_button, 7, 0, alignment=Qt.AlignmentFlag.AlignLeft)

        self.setLayout(layout)

    # self, phn, name, birthdate, phone, email, address
    #update the patient data using controller
    def add_update_button_clicked(self):
        try:
            original_phn = self.original_phn_input.text().strip()
            print(f"DEBUG: Searching patient with PHN={original_phn}")
            patient = self.controller.search_patient(original_phn)
            print(f"DEBUG: Found patient: {patient}")
        
            if patient:
                phn = self.phn_input.text().strip()
                name = self.fullname_input.text().strip()
                birth_date = self.birthdate_input.text().strip()
                phone = self.phone_input.text().strip()
                email = self.email_input.text().strip()
                address = self.address_input.text().strip()

                phn = phn if phn != "" else patient.phn
                name = name if name != "" else patient.name
                birth_date = birth_date if birth_date != "" else patient.birth_date
                phone = phone if phone != "" else patient.phone
                email = email if email != "" else patient.email
                address = address if address != "" else patient.address

                self.controller.update_patient(original_phn, phn, name, birth_date, phone, email, address)
                print(f"DEBUG: Updated patient: {self.controller.search_patient(phn)}")

                new_patient = self.controller.search_patient(phn)
                print(f"DEBUG: Searching patient with PHN={phn}")
                print(f"DEBUG: Found patient: {new_patient}")
            else:
                print('ERROR CHANGING PATIENT DATA.')
                print('There is no patient registered with this PHN.')
        except IllegalAccessException:
            print('\nMUST LOGIN FIRST.')
        except IllegalOperationException:
            print('\nERROR CHANGING PATIENT DATA.')
            if self.controller.current_patient:
                if self.controller.current_patient.phn == phn:
                    print('Cannot change the current patient data. Finish appointment first.')
            else:
                print('Cannot change patient data to a new PHN that is already registered in the system.')
            

def main():
    app = QApplication(sys.argv)
    window = UpdatePatientGUI()
    window.show()
    app.exec()

if __name__ == '__main__':
    main()
