import sys
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QGridLayout
from PyQt6.QtWidgets import QPushButton, QWidget, QLabel, QTableWidget, QTableWidgetItem, QLineEdit, QDialog, QDialogButtonBox, QMessageBox


class SearchPatientGUI(QWidget):

    def __init__(self, controller):
        super().__init__()
        # Continue here with your code!
        self.controller = controller
        self.setWindowTitle("Search Patient")

        layout = QGridLayout()

        self.phn_input = QLineEdit()
        self.phn_input.setFixedSize(175, 25)
        self.phn_input.setPlaceholderText("PHN")
        layout.addWidget(self.phn_input, 0, 0)

        self.patients_table = QTableWidget()
        self.patients_table.setRowCount(6)
        self.patients_table.setColumnCount(1)
        self.patients_table.setVerticalHeaderLabels(["PHN", "Name", "Birth Date", "Phone", "Email", "Address"])
        self.patients_table.setHorizontalHeaderLabels(["Info"])
        self.patients_table.horizontalHeader().setStretchLastSection(True)
        
        layout.addWidget(self.patients_table, 1, 0)

        add_search_button = QPushButton("Search")
        add_search_button.clicked.connect(self.add_search_button_clicked)
        layout.addWidget(add_search_button, 0, 0, alignment=Qt.AlignmentFlag.AlignRight)

        add_close_button = QPushButton("Close")
        add_close_button.clicked.connect(self.add_close_button_clicked)
        layout.addWidget(add_close_button, 2, 0, alignment=Qt.AlignmentFlag.AlignLeft)
        
        # layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.setRowStretch(0, 1)
        layout.setRowStretch(4, 1)
        self.setLayout(layout)

    def add_search_button_clicked(self):
        self.patients_table.clearContents()
        phn = self.phn_input.text().strip()
        print(f"DEBUG: Searching patient with PHN={phn}")
        patient = self.controller.search_patient(phn)
        print(f"DEBUG: Found patient: {patient}")
        if patient:
            phn_item = QTableWidgetItem(str(patient.phn))
            phn_item.setFlags(Qt.ItemFlag.ItemIsSelectable | Qt.ItemFlag.ItemIsEnabled)
            self.patients_table.setItem(0, 0, phn_item)

            name_item = QTableWidgetItem(patient.name)
            name_item.setFlags(Qt.ItemFlag.ItemIsSelectable | Qt.ItemFlag.ItemIsEnabled)
            self.patients_table.setItem(1, 0, name_item)

            birth_date_item = QTableWidgetItem(patient.birth_date)
            birth_date_item.setFlags(Qt.ItemFlag.ItemIsSelectable | Qt.ItemFlag.ItemIsEnabled)
            self.patients_table.setItem(2, 0, birth_date_item)

            phone_item = QTableWidgetItem(patient.phone)
            phone_item.setFlags(Qt.ItemFlag.ItemIsSelectable | Qt.ItemFlag.ItemIsEnabled)
            self.patients_table.setItem(3, 0, phone_item)

            email_item = QTableWidgetItem(patient.email)
            email_item.setFlags(Qt.ItemFlag.ItemIsSelectable | Qt.ItemFlag.ItemIsEnabled)
            self.patients_table.setItem(4, 0, email_item)

            address_item = QTableWidgetItem(patient.address)
            address_item.setFlags(Qt.ItemFlag.ItemIsSelectable | Qt.ItemFlag.ItemIsEnabled)
            self.patients_table.setItem(5, 0, address_item)
        else:
            QMessageBox.critical(self, "Error", "Patient not found!")

    def add_close_button_clicked(self):
            self.close()
            

def main():
    app = QApplication(sys.argv)
    window = SearchPatientGUI()
    window.show()
    app.exec()

if __name__ == '__main__':
    main()
