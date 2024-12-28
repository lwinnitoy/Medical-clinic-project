import sys
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QGridLayout
from PyQt6.QtWidgets import QPushButton, QWidget, QLabel, QLineEdit


class RemovePatientGUI(QWidget):

    def __init__(self, controller):
        super().__init__()
        # Continue here with your code!
        self.controller = controller
        self.setWindowTitle("Delete Patient")

        layout = QGridLayout()

        self.phn_input = QLineEdit()
        self.phn_input.setFixedSize(450, 25)
        self.phn_input.setPlaceholderText("Personal Health Number")
        layout.addWidget(self.phn_input, 0, 0)

        # add_back_button = QPushButton("Back")
        # add_back_button.clicked.connect(self.add_back_button_clicked)
        # layout.addWidget(add_back_button, 6, 0, alignment=Qt.AlignmentFlag.AlignLeft)

        add_remove_button = QPushButton("Delete")
        add_remove_button.clicked.connect(self.add_remove_button_clicked)
        layout.addWidget(add_remove_button, 6, 0, alignment=Qt.AlignmentFlag.AlignLeft)
        
        # layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        # layout.setRowStretch(0, 1)
        # layout.setRowStretch(4, 1)
        self.setLayout(layout)

    # self, phn, name, birthdate, phone, email, address
    def add_remove_button_clicked(self):
        phn = self.phn_input.text().strip()

        try:
            print(f"DEBUG: Deleting patient with PHN={phn}")
            self.controller.delete_patient(phn)
            self.close()
        except Exception as e:
            print("could not delete patient")
            

def main():
    app = QApplication(sys.argv)
    window = RemovePatientGUI()
    window.show()
    app.exec()

if __name__ == '__main__':
    main()
