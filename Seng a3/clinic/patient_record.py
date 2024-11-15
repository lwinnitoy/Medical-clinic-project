from clinic.note import Note

class PatientRecord:

    def __init__(self):
        self.autocounter = 0
        self.record = {}

    def add_note(self, text):
        self.autocounter += 1
        self.record[self.autocounter] = Note(self.autocounter, text)
        return self.record[self.autocounter]
    
    def search_note(self, code):
        return self.record.get(code, None)
    
    def retrieve_patient_notes(self, text):
        return [note for note in self.record.values() if text in note.text]
    
    def update_note_text(self, code, text):
        note = self.search_note(code)
        if note:
            note.text = text
            return True
        return False
    
    def list_patient_notes(self):
        lst = list(self.record.values())
        lst.reverse()
        return lst
        
    def delete_note(self, code):
        return False if self.record.pop(code, None) is None else True
        

