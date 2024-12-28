import json
from clinic.patient import Patient

#the following decoder class is modified version of lab 9 code
class PatientDecoder(json.JSONDecoder):
    def __init__(self, *args, **kwargs):
        super().__init__(object_hook=self.object_hook, *args, **kwargs)

    def object_hook(self, dct):
        if '__type__' in dct and dct['__type__'] == 'Patient':
            return Patient(dct['phn'], dct['name'], dct['birthdate'], dct['phone'], dct['email'], dct['address'], dct['autosave'])
        return dct
    