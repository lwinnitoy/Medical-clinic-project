from clinic.dao.patient_dao import PatientDAO
from clinic.dao.patient_encoder import PatientEncoder
from clinic.dao.patient_decoder import PatientDecoder
import json

class PatientDAOJSON(PatientDAO):
    
    def __init__(self, autosave=False):
        self.autosave = autosave
        self.patients = {}

        #loads the patients from the file
        if self.autosave:
            self.patients = self.load_patients()
        
    #searches for the patient with the given phn, returns None if not found
    def search_patient(self, key):
        return self.patients.get(key, None)
    
    #adds the new patient to the patients dictionary
    def create_patient(self, patient):
        self.patients[patient.phn] = patient

        #saves the patients to the file if autosave is enabled
        if self.autosave:
            self.save_patients()
        return patient
    
    #returns a list of patients that contain the the given name (search_string)
    def retrieve_patients(self, search_string):
        return [patient for patient in self.patients.values() if search_string in patient.name]
    
    #updates the patient with the given key to a new version of the patient
    def update_patient(self, key, patient):

        #gets the original patient to be updated
        old_p = self.patients.get(key, None)
        if old_p.phn != patient.phn:
            self.patients.pop(old_p.phn)
            old_p.phn = patient.phn
            self.patients[old_p.phn] = old_p

        #updates the patient's information
        old_p.name = patient.name
        old_p.birth_date = patient.birth_date
        old_p.phone = patient.phone
        old_p.email = patient.email
        old_p.address = patient.address

        #saves the patients to the file if autosave is enabled
        if self.autosave:
            self.save_patients()

        return True
    
    #deletes the patient with the given key
    def delete_patient(self, key):
        if self.patients.pop(key, None) is None:
            return False
        else:
            #saves the patients to the file if autosave is enabled
            if self.autosave:
                self.save_patients()
            return True

    #returns a list of all the patients
    def list_patients(self):
        return list(self.patients.values())
    

    #saves the patients to the file using json format
    def save_patients(self):
        with open('clinic/patients.json', 'w') as f:
            json.dump(list(self.patients.values()), f, cls=PatientEncoder)
    
    #loads the patients from the file using json format
    def load_patients(self):
        try:
            with open('clinic/patients.json', 'r') as f:
                file_content = f.read()
                # print("File content before loading:", file_content)
                patient_list = json.loads(file_content, cls=PatientDecoder)
                # print("Loaded patient list:", patient_list)
                return {patient.phn: patient for patient in patient_list}
        except FileNotFoundError:
            # print("File not found.")
            return {}
        except json.JSONDecodeError:
            # print("ERROR: cannot decode the file")
            return {}
