from json import JSONEncoder
from clinic.patient import Patient

#the following encoder class is modified version of lab 9 code
class PatientEncoder(JSONEncoder):
  def default(self, obj):
    if isinstance(obj, Patient):
      return {
        "__type__": "Patient", 
        "phn": obj.phn, 
        "name": obj.name, 
        "birthdate": obj.birth_date, 
        "phone": obj.phone, 
        "email": obj.email, 
        "address": obj.address, 
        "autosave": obj.autosave
      }
    return super().default(obj)