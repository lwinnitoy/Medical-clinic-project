from clinic.dao.note_dao_pickle import NoteDAOPickle

class PatientRecord:
    def __init__(self, phn, autosave=False):
        self.autosave = autosave
        self.phn = phn
        self.note_dao = NoteDAOPickle(phn, autosave)

    def add_note(self, text):
        return self.note_dao.create_note(text)
    
    def search_note(self, code):
        return self.note_dao.search_note(code)
    
    def retrieve_patient_notes(self, text):
        return self.note_dao.retrieve_notes(text)
    
    def update_note_text(self, code, text):
        return self.note_dao.update_note(code, text)
    
    def list_patient_notes(self):
        return self.note_dao.list_notes()
        
    def delete_note(self, code):
        return self.note_dao.delete_note(code)
        

