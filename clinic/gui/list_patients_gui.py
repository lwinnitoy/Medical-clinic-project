import sys
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QGridLayout
from PyQt6.QtWidgets import QPushButton, QWidget, QLabel, QTableWidget, QTableWidgetItem


class ListPatientsGUI(QWidget):

    def __init__(self, controller):
        super().__init__()
        # Continue here with your code!
        self.controller = controller
        self.setWindowTitle("List Patients")

        layout = QGridLayout()

        # patients = self.controller.list_patients()
        # print(f"2: {patients}")

        self.patients_table = QTableWidget()
        self.patients_table.setColumnCount(3)
        self.patients_table.setHorizontalHeaderLabels(["PHN", "Name", "Birth Date"])
        self.populate_table()
        layout.addWidget(self.patients_table, 0, 0)

        add_close_button = QPushButton("Close")
        add_close_button.clicked.connect(self.add_close_button_clicked)
        layout.addWidget(add_close_button, 4, 0, alignment=Qt.AlignmentFlag.AlignLeft)
        
        # layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.setRowStretch(0, 1)
        layout.setRowStretch(4, 1)
        self.setLayout(layout)


    def populate_table(self):
        # fetch patient from controller
        patients = self.controller.list_patients()
        self.patients_table.setRowCount(len(patients))
        
        # populate table
        for row, patient in enumerate(patients):
            # print(f"Patient {row}: PHN={patient.phn}, Name={patient.name}, Birth Date={patient.birth_date}")

            phn_item = QTableWidgetItem(str(patient.phn))
            phn_item.setFlags(Qt.ItemFlag.ItemIsSelectable | Qt.ItemFlag.ItemIsEnabled)
            self.patients_table.setItem(row, 0, phn_item)

            name_item = QTableWidgetItem(patient.name)
            name_item.setFlags(Qt.ItemFlag.ItemIsSelectable | Qt.ItemFlag.ItemIsEnabled)
            self.patients_table.setItem(row, 1, name_item)

            birth_date_item = QTableWidgetItem(patient.birth_date)
            birth_date_item.setFlags(Qt.ItemFlag.ItemIsSelectable | Qt.ItemFlag.ItemIsEnabled)
            self.patients_table.setItem(row, 2, birth_date_item)

        self.patients_table.resizeColumnsToContents()
        self.patients_table.resizeRowsToContents()

        # sort table by PHN
        self.patients_table.setSortingEnabled(True)
        self.patients_table.sortItems(0, Qt.SortOrder.AscendingOrder)

    def add_close_button_clicked(self):
        self.close()
            

def main():
    app = QApplication(sys.argv)
    window = ListPatientsGUI()
    window.show()
    app.exec()

if __name__ == '__main__':
    main()
