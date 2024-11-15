from clinic.patient import Patient

class Controller:
    def __init__(self):
        self.users = {'user': 'clinic2024'}
        self.logged_in_user = None
        self.patients = []
        self.current_patient = None

    def login(self, username, password):
        if username in self.users and self.users[username] == password:
            self.logged_in_user = username # set the logged_in_user to the username
            return True
        return False

    def is_logged(self):
        return self.logged_in_user is not None # return self.logged_in_user if it is not equal to None

    def logout(self):
        self.logged_in_user = None

    def create_patient(self, phn, name, birthdate, phone, email, address):
        if not self.is_logged():
            return None
        if any(p.phn == phn for p in self.patients): # check if the patient is already in the list
            return None
        new_patient = Patient(phn, name, birthdate, phone, email, address)
        self.patients.append(new_patient)
        return new_patient
    
    def search_patient(self, phn):
        if not self.is_logged():
            return None
        patients = [p for p in self.patients if p.phn == phn]
        return patients[0] if patients else None # return the patient if the patient is in the patients list
    
    def retrieve_patients(self, name):
        if not self.is_logged():
            return None
        return [p for p in self.patients if name in p.name] # return the patient if their name is in the patients list
    
    def update_patient(self, old_phn, new_phn, name, birthdate, phone, email, address):
        if not self.is_logged():
            return False
        patient = self.search_patient(old_phn)
        if patient is None:
            return False
        patient.phn = new_phn
        patient.name = name
        patient.birthdate = birthdate
        patient.phone = phone
        patient.email = email
        patient.address = address
        return True
    
    def delete_patient(self, phn):
        if not self.is_logged():
            return False
        patient = self.search_patient(phn)
        if patient:
            self.patients.remove(patient)
            return True
        return False
    
    def list_patients(self):
        if not self.is_logged():
            return None
        return self.patients
    
    def get_current_patient(self):
        if not self.is_logged():
            return None
        return self.current_patient
    
    def set_current_patient(self, phn):
        if not self.is_logged():
            return False
        patient = self.search_patient(phn)
        if patient:
            self.current_patient = patient
            return True
    

    #creates a notes for the current patient with the given text
    def create_note(self, text):
        if not self.is_logged():
            return None
        if self.current_patient is None:
            return None
        return self.current_patient.patient_record.add_note(text)
    
    #returns the note with the given code
    #calls function (search_note()) in patient_record.py
    def search_note(self, code):
        if not self.is_logged():
            return None
        if self.current_patient is None:
            return None
        return self.current_patient.patient_record.search_note(code)
    
    # retrives notes with the given text
    # does not check if empty since it should return an empty list if no notes are found
    def retrieve_notes(self, text):
        if not self.is_logged():
            return None
        if self.current_patient is None:
            return None
        return self.current_patient.patient_record.retrieve_patient_notes(text)
    
    # updates the note with the given code
    #   returns none if not logged in, no current patient, no patient record,
    #   or no note with the given code
    def update_note(self, code, text):
        if not self.is_logged():
            return None
        if self.current_patient is None:
            return None
        return self.current_patient.patient_record.update_note_text(code, text)
    
    # lists all the notes for the current patient
    def list_notes(self):
        if not self.is_logged():
            return None
        if self.current_patient is None:
            return None
        return self.current_patient.patient_record.list_patient_notes()
    
    # deletes the note with the given code
    def delete_note(self, code):
        if not self.is_logged():
            return None
        if self.current_patient is None:
            return None
        return self.current_patient.patient_record.delete_note(code)