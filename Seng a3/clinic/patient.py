from clinic.patient_record import PatientRecord

class Patient:
    def __init__(self, phn, name, birthdate, phone, email, address):
        self.phn = phn
        self.name = name
        self.birthdate = birthdate
        self.phone = phone
        self.email = email
        self.address = address
        self.patient_record = PatientRecord() # creates a new PatientRecord object

    def __eq__(self, other):
        return (self.phn == other.phn and 
                self.name == other.name and 
                self.birthdate == other.birthdate and
                self.phone == other.phone and 
                self.email == other.email and 
                self.address == other.address) # check if all the attributes are the same

    def __str__(self):
        return f"Patient({self.phn})"