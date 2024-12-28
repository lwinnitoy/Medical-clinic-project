from clinic.exception.invalid_login_exception import InvalidLoginException
from clinic.exception.duplicate_login_exception import DuplicateLoginException
from clinic.exception.invalid_logout_exception import InvalidLogoutException
from clinic.exception.illegal_access_exception import IllegalAccessException
from clinic.exception.illegal_operation_exception import IllegalOperationException
from clinic.exception.no_current_patient_exception import NoCurrentPatientException
from clinic.dao.patient_dao_json import PatientDAOJSON
from clinic.patient import Patient
import hashlib

class Controller:
    def __init__(self, autosave=False):
        #users intialized with a default user and password to pass the integration tests when sutosave is False
        self.logged_in_user = None
        self.current_patient = None
        self.autosave = autosave
        self.patient_dao = PatientDAOJSON(autosave)
        self.users = self.setup_users()
    
    def setup_users(self):
        #initiates the users from users.txt file
        users = {}
        if self.autosave:
            try:
               with open('clinic/users.txt') as fhandle:
                    for line in fhandle:
                        username, password = line.strip().split(',')
                        users[username] = password 
                    return users
            except FileNotFoundError:
                pass
        else:
            #this is the passwords if autosave is False
            return {'user': '123456', 'ali': '@G00dPassw0rd'}

    #code used from lab 9. This function is used to hash the password
    def get_password_hash(self, password):
        encoded_password = password.encode('utf-8')     
        hash_object = hashlib.sha256(encoded_password)      
        hex_dig = hash_object.hexdigest()       
        return hex_dig

    #Uses code from assignment 9. logs in the user with the given username and password
    def login(self, username, password):
        # notice that we convert the password into a password hash before

        if self.logged_in_user == username:
            raise DuplicateLoginException()
        
        if self.autosave:
            password_hash = self.get_password_hash(password)
            if self.users.get(username, None) == password_hash:
                self.logged_in_user = username
                return True
        else:
            if self.users.get(username, None) == password:
                self.logged_in_user = username
                return True
        raise InvalidLoginException()

    #returns true if a user is logged in
    def is_logged(self):
        return self.logged_in_user is not None # return self.logged_in_user if it is not equal to None

    #logs out the current user
    def logout(self):
        if not self.is_logged():
            raise InvalidLogoutException()
        self.logged_in_user = None
        return True

    #creates a patient with the given phn, name, birthdate, phone, email, and address
    def create_patient(self, phn, name, birthdate, phone, email, address):
        if not self.is_logged():
            raise IllegalAccessException()
        if self.search_patient(phn) is not None:
            raise IllegalOperationException()
        new_patient = Patient(phn, name, birthdate, phone, email, address, self.autosave)
        self.patient_dao.create_patient(new_patient)
        return new_patient
    
    #searches for the patient with the given phn
    def search_patient(self, phn):
        if not self.is_logged():
            raise IllegalAccessException()
        return self.patient_dao.search_patient(phn)
    
    # retrieves the patients with the given name
    def retrieve_patients(self, name):
        if not self.is_logged():
            raise IllegalAccessException()
        return self.patient_dao.retrieve_patients(name)
    
    def update_patient(self, old_phn, new_phn, name, birthdate, phone, email, address):
        if not self.is_logged():
            raise IllegalAccessException()
        
        updated_p = Patient(new_phn, name, birthdate, phone, email, address)
        old_p = self.search_patient(old_phn)

        #check if the patient exists
        if old_p is None:
            raise IllegalOperationException()
        
        #check if the patient is the current patient
        if old_p is self.current_patient:
            raise IllegalOperationException()
        
        #check if the new phn is already in the list and is not the same as the old phn
        if old_phn != new_phn and self.patient_dao.search_patient(new_phn) is not None:
            raise IllegalOperationException()
        
        return self.patient_dao.update_patient(old_phn, updated_p)
    
    #deletes the patient with the given phn
    def delete_patient(self, phn):
        if not self.is_logged():
            raise IllegalAccessException()
        patient = self.patient_dao.search_patient(phn)

        #check if the patient exists and that it's not the current patient
        if patient and patient is not self.current_patient:
            self.patient_dao.delete_patient(phn)
            return True
        raise IllegalOperationException()
    
    #returns the list of patients
    def list_patients(self):
        if not self.is_logged():
            raise IllegalAccessException()
        return self.patient_dao.list_patients()
    
    #returns the current patient
    def get_current_patient(self):
        if not self.is_logged():
            raise IllegalAccessException()
        return self.current_patient
    
    #sets the current patient to the patient with the given phn
    def set_current_patient(self, phn):
        if not self.is_logged():
            raise IllegalAccessException()
        patient = self.search_patient(phn)
        if patient:
            self.current_patient = patient
            return True
        raise IllegalOperationException()
    

    #unsets the current patient. Raises exception if not logged in
    def unset_current_patient(self):
        if not self.is_logged():
            raise IllegalAccessException()
        self.current_patient = None
        return True
    

    #creates a notes for the current patient with the given text
    def create_note(self, text):
        if not self.is_logged():
            raise IllegalAccessException()
        if self.current_patient is None:
            raise NoCurrentPatientException()
        return self.current_patient.patient_record.add_note(text)
    
    #returns the note with the given code
    #calls function (search_note()) in patient_record.py
    def search_note(self, code):
        if not self.is_logged():
            raise IllegalAccessException()
        if self.current_patient is None:
            raise NoCurrentPatientException()
        return self.current_patient.patient_record.search_note(code)
    
    # retrives notes with the given text
    # does not check if empty since it should return an empty list if no notes are found
    def retrieve_notes(self, text):
        if not self.is_logged():
            raise IllegalAccessException()
        if self.current_patient is None:
            raise NoCurrentPatientException
        return self.current_patient.patient_record.retrieve_patient_notes(text)
    
    # updates the note with the given code
    #   returns none if not logged in, no current patient, no patient record,
    #   or no note with the given code
    def update_note(self, code, text):
        if not self.is_logged():
            raise IllegalAccessException()
        if self.current_patient is None:
            raise NoCurrentPatientException()
        return self.current_patient.patient_record.update_note_text(code, text)
    
    # lists all the notes for the current patient
    def list_notes(self):
        if not self.is_logged():
            raise IllegalAccessException()
        if self.current_patient is None:
            raise NoCurrentPatientException()
        return self.current_patient.patient_record.list_patient_notes()
    
    # deletes the note with the given code
    def delete_note(self, code):
        if not self.is_logged():
            raise IllegalAccessException()
        if self.current_patient is None:
            raise NoCurrentPatientException()
        return self.current_patient.patient_record.delete_note(code)