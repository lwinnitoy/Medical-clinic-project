import sys
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QGridLayout, QVBoxLayout, QHBoxLayout
from PyQt6.QtWidgets import QPushButton, QWidget, QLabel, QLineEdit, QMessageBox, QToolBar, QListWidget, QPlainTextEdit
from PyQt6.QtGui import QAction

class ChoosePatientGUI(QWidget):
    #This class is used to choose the patient before starting the appointment.
    #Needs to have the main menu open at the same time so the user can see the phn of the patient
    #will error if the phn is not in the system

    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        self.setWindowTitle("Choose Patient")

        #minimum size of the window
        self.setMinimumSize(900, 600)
        main_layout = QVBoxLayout()
        self.setLayout(main_layout)
        

        #parent box to restrict the size of the content
        box = QWidget()

        layout = QGridLayout()
        main_layout.addWidget(box, alignment=Qt.AlignmentFlag.AlignCenter)
        box.setLayout(layout)
        box.setFixedSize(300, 100)

        self.add_back_button = QPushButton("Back")
        self.add_back_button.clicked.connect(self.add_back_button_clicked)
        layout.addWidget(self.add_back_button, 1, 0)
        

        label_phn = QLabel("Enter PHN: ")
        self.phn = QLineEdit()

        layout.addWidget(label_phn, 0, 0)
        layout.addWidget(self.phn, 0, 1)

        self.choose_button = QPushButton("Select")
        layout.addWidget(self.choose_button, 1, 1)
        self.choose_button.clicked.connect(self.choose_button_clicked)

        
    def choose_button_clicked(self):
        try:
            #sets the current patient
            phn = self.phn.text()

            if self.controller.set_current_patient(phn):
                from clinic.gui.appointment_gui import AppointmentGUI
                self.appointment_gui = AppointmentGUI(self.controller)
                self.appointment_gui.show()
                self.close()
                
        except Exception as e:
            print(str(e))
            QMessageBox.warning(self, "Phn not found", "Phn %s not found" % self.phn.text())
            self.phn.setText("")
            self.phn.setFocus()

        
    def add_back_button_clicked(self):
        from clinic.gui.clinic_actual_gui import ClinicActualGUI
        self.clinic_actual_gui = ClinicActualGUI(self.controller)
        self.clinic_actual_gui.show()
        self.close()

class AppointmentGUI(QWidget):

    def __init__(self, controller):
        super().__init__()
        # Continue here with your code!
        self.controller = controller
        self.setWindowTitle("Appointment")

        #minimum size of the window
        self.setMinimumSize(900, 600)

        main_layout = QVBoxLayout()
        main_layout.setContentsMargins(10, 0, 10, 10)
        self.setLayout(main_layout)

        #toolbar
        toolbar = QToolBar("My main toolbar")
        main_layout.addWidget(toolbar, alignment=Qt.AlignmentFlag.AlignTop)
        toolbar.setFixedWidth(900)

        #adding actions
        view_notes_action = QAction("View", self)
        toolbar.addAction(view_notes_action)
        view_notes_action.triggered.connect(self.view_note)

        create_window_action = QAction("Create", self)
        toolbar.addAction(create_window_action)
        create_window_action.triggered.connect(self.create_note)



        #Find notes widget - core widget displayed when view window is selected
        self.find_notes = QWidget()
        find_notes_layout = QVBoxLayout(self.find_notes)
        main_layout.addWidget(self.find_notes)
        find_notes_layout.setContentsMargins(0, 0, 0, 0)
        find_notes_layout.setAlignment(Qt.AlignmentFlag.AlignLeft)
        find_notes_layout.setAlignment(Qt.AlignmentFlag.AlignTop)

        #search bar - add to search box layout
        self.search_bar = QLineEdit()
        find_notes_layout.addWidget(self.search_bar)
        self.search_bar.setPlaceholderText("Start typing to search notes")
        self.search_bar.textChanged.connect(self.search_text_changed)
        

        #list widget - add to main layout
        list_box = QWidget()
        list_layout = QHBoxLayout(list_box)
        find_notes_layout.addWidget(list_box)
        list_layout.setAlignment(Qt.AlignmentFlag.AlignTop)
        list_layout.setContentsMargins(0, 0, 0, 0)

        #list notes window
        #arranges everything in list notes widget in a vertical layout
        self.list_widget = QListWidget()
        list_layout.addWidget(self.list_widget)
        self.list_widget.setFixedWidth(250)


        #note display for updating and deleting notes - add to list_layout
        note_display = QWidget()
        note_display_layout = QVBoxLayout(note_display)
        note_display_layout.setContentsMargins(0, 0, 0, 0)
        list_layout.addWidget(note_display)

        #plain text edit for note
        self.current_note_text = QPlainTextEdit()
        self.list_widget.currentItemChanged.connect(self.note_selected)
        note_display_layout.addWidget(self.current_note_text)

        #button box for update and delete buttons - add to note display layout
        updel_box = QWidget()
        updel_layout = QHBoxLayout(updel_box)
        note_display_layout.addWidget(updel_box)
        updel_layout.setContentsMargins(10, 0, 10, 0)

        #update button - add to button layout
        update_button = QPushButton("Update")
        update_button.clicked.connect(self.update_button_clicked)
        updel_layout.addWidget(update_button)

        #delete button - add to button layout
        delete_button = QPushButton("Delete")
        delete_button.clicked.connect(self.delete_button_clicked)
        updel_layout.addWidget(delete_button)








        #create note parent layout - add to main layout
        self.create_box = QWidget()
        create_box_layout = QVBoxLayout(self.create_box)
        main_layout.addWidget(self.create_box)
        self.create_box.hide()

        #plain text edit - add to create box layout
        self.note_text = QPlainTextEdit()
        create_box_layout.addWidget(self.note_text)
        self.note_text.setPlaceholderText("Enter note here")
        create_box_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        #parent box for clear and create buttons - add to create box layout
        button_box = QWidget()
        button_layout = QHBoxLayout(button_box)
        create_box_layout.addWidget(button_box)

        #create button - add to button layout
        create_button = QPushButton("Create")
        create_button.clicked.connect(self.create_button_clicked)
        button_layout.addWidget(create_button)

        #clear button - add to button layout
        clear_button = QPushButton("Clear")
        clear_button.clicked.connect(self.clear_button_clicked)
        button_layout.addWidget(clear_button)



        #back button
        add_back_button = QPushButton("End Appointment")
        add_back_button.clicked.connect(self.add_back_button_clicked)
        main_layout.addWidget(add_back_button, alignment=Qt.AlignmentFlag.AlignLeft)


        #to reload the list of notes everytime the view button is clicked
        self.view_note()    


    def add_back_button_clicked(self):
        try:
            from clinic.gui.clinic_actual_gui import ClinicActualGUI
            self.controller.unset_current_patient()
            self.clinic_actual_gui = ClinicActualGUI(self.controller)
            self.clinic_actual_gui.show()
            self.close()
        except Exception as e:
            print(str(e))

    def view_note(self):
        #function for when someone clicks the view button for notes
        self.create_box.hide()
        self.find_notes.show()

        #clears the list widget before repopulating the data
        self.list_widget.clear()

        note_list = self.controller.list_notes()

        for note in note_list:
            self.list_widget.addItem("%i: %s - %s" % (note.code, note.text, str(note.timestamp)[:10]))
        
    
    def create_note(self):
        #function for when someone clicks the create button for notes
        self.find_notes.hide()
        self.create_box.show()

    def search_text_changed(self):
        #function for when someone clicks the search button for notes
        search_text = self.search_bar.text()

        notes = self.controller.retrieve_notes(search_text)

        self.list_widget.clear()
        for note in notes:
            self.list_widget.addItem("%i: %s - %s" % (note.code, note.text, str(note.timestamp)[:10]))

    def list_all_notes(self):
        notes = self.controller.get_all_notes()
        for note in notes:
            print(note)
    
    def create_button_clicked(self):
        #function for when someone clicks the create button for notes
        note = self.note_text.toPlainText()

        #creates the note using controller
        try:
            self.controller.create_note(note)
            self.note_text.clear()
        except Exception as e:
            print(str(e))
            QMessageBox.warning(self, "Error", "Error creating note")

    def clear_button_clicked(self):
        #function for when someone clicks the clear button for notes
        self.note_text.clear()
    
    def note_selected(self):
        #function for when someone selects a note from the list
        self.current_note_text.clear()

        #case where no note is selected
        if self.list_widget.currentItem() is None:
            return
        
        #gets the note code from the list widget (first character)
        note_code = self.list_widget.currentItem().text()[0]

        try:
            note_code = int(note_code)
            note = self.controller.search_note(note_code)
            self.current_note_text.setPlainText(note.text)
        except Exception as e:
            print(str(e))
            QMessageBox.warning(self, "Error", "Error searching for note")
            self.current_note_text.setPlainText("Error searching for note")

    def update_button_clicked(self):
        #function for when someone clicks the update button for notes
        #gets the note code from the list widget (first character)
        note_code = self.list_widget.currentItem().text()[0]

        try:
            note_code = int(note_code)
            note_text = self.current_note_text.toPlainText()
            self.controller.update_note(note_code, note_text)
        except Exception as e:
            print(str(e))
            QMessageBox.warning(self, "Error", "Error updating note")
        
        #refreshes the list of notes
        self.view_note()

        #clears the current note text
        self.list_widget.setCurrentItem(None)
    
    def delete_button_clicked(self):
        #function for when someone clicks the delete button for notes
        #gets the note code from the list widget (first character)

        #starting by giving the user a warning message

        button = QMessageBox.critical(
            self,
            "Warning!",
            "This will permanently delete the note. Are you sure you want to continue?",
            buttons = QMessageBox.StandardButton.Yes,
            defaultButton=QMessageBox.StandardButton.No,
        )

        if button == QMessageBox.StandardButton.No:
            return
        
        #deletes the note
        note_code = self.list_widget.currentItem().text()[0]

        try:
            note_code = int(note_code)
            self.controller.delete_note(note_code)
        except Exception as e:
            print(str(e))
            QMessageBox.warning(self, "Error", "Error deleting note")

        #refreshes the list of notes
        self.view_note()

def main():
    app = QApplication(sys.argv)
    window = AppointmentGUI()
    window.show()
    app.exec()

if __name__ == '__main__':
    main()
