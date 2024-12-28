from clinic.patient_record import PatientRecord

class Patient:
    def __init__(self, phn, name, birth_date, phone, email, address, autosave=False):
        self.phn = phn
        self.name = name
        self.birth_date = birth_date
        self.phone = phone
        self.email = email
        self.address = address
        self.autosave = autosave
        self.patient_record = PatientRecord(self.phn, self.autosave) # creates a new PatientRecord object

    def __eq__(self, other):
        return (self.phn == other.phn and 
                self.name == other.name and 
                self.birth_date == other.birth_date and
                self.phone == other.phone and 
                self.email == other.email and 
                self.address == other.address) # check if all the attributes are the same

    def __str__(self):
        return f"Patient({self.phn})"