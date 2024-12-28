import sys
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QVBoxLayout
from PyQt6.QtWidgets import QPushButton, QWidget, QLabel


class ClinicActualGUI(QMainWindow):

    def __init__(self, controller):
        super().__init__()
        # Continue here with your code!
        self.controller = controller
        self.setWindowTitle("Clinic")

        self.create_patient_gui = None
        self.search_patient_gui = None
        self.retrieve_patients_gui = None
        self.update_patient_gui = None
        self.remove_patient_gui = None
        self.list_patients_gui = None

        # print(f"DEBUG: Logged user: {self.controller.logged_in_user}")

        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.setSpacing(20)
        layout.setContentsMargins(100, 100, 100, 100)

        menu_label = QLabel("Clinic Menu")
        menu_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        menu_label.setStyleSheet("font-size: 20px; font-weight: bold;")
        layout.addWidget(menu_label)

        add_patient_button = QPushButton("Add new patient")
        add_patient_button.clicked.connect(self.add_patient_button_clicked)
        layout.addWidget(add_patient_button)

        add_search_patient_button = QPushButton("Search Patient (by PHN)")
        add_search_patient_button.clicked.connect(self.add_search_patient_button_clicked)
        layout.addWidget(add_search_patient_button)

        add_retrieve_patient_button = QPushButton("Retrieve Patients (by Name)")
        add_retrieve_patient_button.clicked.connect(self.add_retrieve_patient_button_clicked)
        layout.addWidget(add_retrieve_patient_button)

        add_update_patient_button = QPushButton("Update Existing Patient")
        add_update_patient_button.clicked.connect(self.add_update_patient_button_clicked)
        layout.addWidget(add_update_patient_button)

        add_remove_patient_button = QPushButton("Remove Patient")
        add_remove_patient_button.clicked.connect(self.add_remove_patient_button_clicked)
        layout.addWidget(add_remove_patient_button)

        add_list_patients_button = QPushButton("List Patients")
        add_list_patients_button.clicked.connect(self.add_list_patients_button_clicked)
        layout.addWidget(add_list_patients_button)

        start_appointment_button = QPushButton("Start Appointment with Patient")
        start_appointment_button.clicked.connect(self.start_appointment_button_clicked)
        layout.addWidget(start_appointment_button)

        add_logout_button = QPushButton("Logout")
        add_logout_button.clicked.connect(self.add_logout_button_clicked)
        layout.addWidget(add_logout_button)

        logged_in_user_label = QLabel(f"Logged in as: {self.controller.logged_in_user}")
        logged_in_user_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(logged_in_user_label)
        
        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

    def add_patient_button_clicked(self):
        from clinic.gui.create_patient_gui import CreatePatientGUI
        self.create_patient_gui = CreatePatientGUI(self.controller)
        self.create_patient_gui.show()

    def add_search_patient_button_clicked(self):
        from clinic.gui.search_patient_gui import SearchPatientGUI
        self.search_patient_gui = SearchPatientGUI(self.controller)
        self.search_patient_gui.show()

    def add_retrieve_patient_button_clicked(self):
        from clinic.gui.retrieve_patients_gui import RetrievePatientsGUI
        self.retrieve_patients_gui = RetrievePatientsGUI(self.controller)
        self.retrieve_patients_gui.show()

    def add_update_patient_button_clicked(self):
        from clinic.gui.update_existing_patient_gui import UpdatePatientGUI
        self.update_patient_gui = UpdatePatientGUI(self.controller)
        self.update_patient_gui.show()

    def add_remove_patient_button_clicked(self):
        from clinic.gui.remove_patient_gui import RemovePatientGUI
        self.remove_patient_gui = RemovePatientGUI(self.controller)
        self.remove_patient_gui.show()

    def add_list_patients_button_clicked(self):
        from clinic.gui.list_patients_gui import ListPatientsGUI
        self.list_patients_gui = ListPatientsGUI(self.controller)
        self.list_patients_gui.show()

    def start_appointment_button_clicked(self):
        from clinic.gui.appointment_gui import ChoosePatientGUI
        self.appointment_gui = ChoosePatientGUI(self.controller)
        self.appointment_gui.show()
        self.close()

    def add_logout_button_clicked(self):
        from clinic.gui.clinic_gui import ClinicGUI
        try:
            self.controller.logout()
            self.clinic_gui = ClinicGUI()
            self.clinic_gui.controller.logged_in_user = None
            self.clinic_gui.show()
            self.close()
        except Exception as e:
            print(str(e))

    def set_logged_in_user(self, username):
        self.controller.logged_in_user = username
        self.logged_in_user_label.setText(f"Logged in as: {username}")

    def closeEvent(self, event):
        if self.create_patient_gui:
            self.create_patient_gui.close()
        if self.search_patient_gui:
            self.search_patient_gui.close()
        if self.retrieve_patients_gui:
            self.retrieve_patients_gui.close()
        if self.update_patient_gui:
            self.update_patient_gui.close()
        if self.remove_patient_gui:
            self.remove_patient_gui.close()
        if self.list_patients_gui:
            self.list_patients_gui.close()
        event.accept()

def main():
    app = QApplication(sys.argv)
    window = ClinicActualGUI()
    window.show()
    app.exec()

if __name__ == '__main__':
    main()
