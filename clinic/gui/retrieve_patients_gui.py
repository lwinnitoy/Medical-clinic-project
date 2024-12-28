import sys
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QGridLayout
from PyQt6.QtWidgets import QPushButton, QWidget, QLabel, QTableWidget, QTableWidgetItem, QLineEdit, QDialog, QDialogButtonBox, QMessageBox


class RetrievePatientsGUI(QWidget):

    def __init__(self, controller):
        super().__init__()
        # Continue here with your code!
        self.controller = controller
        self.setWindowTitle("Retrieve Patient(s)")

        layout = QGridLayout()

        self.phn_input = QLineEdit()
        self.phn_input.setFixedSize(175, 25)
        self.phn_input.setPlaceholderText("Name")
        layout.addWidget(self.phn_input, 0, 0)

        self.patients_table = QTableWidget()
        self.patients_table.setColumnCount(6)
        self.patients_table.setHorizontalHeaderLabels(["PHN", "Name", "Birth Date", "Phone", "Email", "Address"])
        
        layout.addWidget(self.patients_table, 1, 0)

        add_retrieve_button = QPushButton("Retrieve")
        add_retrieve_button.clicked.connect(self.add_retrieve_button_clicked)
        layout.addWidget(add_retrieve_button, 0, 0, alignment=Qt.AlignmentFlag.AlignRight)

        add_close_button = QPushButton("Close")
        add_close_button.clicked.connect(self.add_close_button_clicked)
        layout.addWidget(add_close_button, 2, 0, alignment=Qt.AlignmentFlag.AlignLeft)
        
        # layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.setRowStretch(0, 1)
        layout.setRowStretch(4, 1)
        self.setLayout(layout)

    def add_retrieve_button_clicked(self):
        self.patients_table.clearContents()
        name = self.phn_input.text().strip()
        print(f"DEBUG: Retrieving patient with Name={name}")
        patients = self.controller.retrieve_patients(name)
        print(f"DEBUG: Found patients: {patients}")
        if patients:
            self.patients_table.setRowCount(len(patients))
            for row, patient in enumerate(patients):
                phn_item = QTableWidgetItem(str(patient.phn))
                phn_item.setFlags(Qt.ItemFlag.ItemIsSelectable | Qt.ItemFlag.ItemIsEnabled)
                self.patients_table.setItem(row, 0, phn_item)

                name_item = QTableWidgetItem(patient.name)
                name_item.setFlags(Qt.ItemFlag.ItemIsSelectable | Qt.ItemFlag.ItemIsEnabled)
                self.patients_table.setItem(row, 1, name_item)

                birth_date_item = QTableWidgetItem(patient.birth_date)
                birth_date_item.setFlags(Qt.ItemFlag.ItemIsSelectable | Qt.ItemFlag.ItemIsEnabled)
                self.patients_table.setItem(row, 2, birth_date_item)

                phone_item = QTableWidgetItem(patient.phone)
                phone_item.setFlags(Qt.ItemFlag.ItemIsSelectable | Qt.ItemFlag.ItemIsEnabled)
                self.patients_table.setItem(row, 3, phone_item)

                email_item = QTableWidgetItem(patient.email)
                email_item.setFlags(Qt.ItemFlag.ItemIsSelectable | Qt.ItemFlag.ItemIsEnabled)
                self.patients_table.setItem(row, 4, email_item)

                address_item = QTableWidgetItem(patient.address)
                address_item.setFlags(Qt.ItemFlag.ItemIsSelectable | Qt.ItemFlag.ItemIsEnabled)
                self.patients_table.setItem(row, 5, address_item)

            self.patients_table.resizeColumnsToContents()
            self.patients_table.resizeRowsToContents()

    def add_close_button_clicked(self):
            self.close()
            

def main():
    app = QApplication(sys.argv)
    window = RetrievePatientsGUI()
    window.show()
    app.exec()

if __name__ == '__main__':
    main()
