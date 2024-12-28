from clinic.dao.note_dao import NoteDAO
from clinic.note import Note
from pickle import dump, load

class NoteDAOPickle(NoteDAO):

    def __init__(self, phn, autosave=False):
        self.autosave = autosave
        self.phn = phn
        self.notes = {}
        self.counter = 0

        #load the notes if autosave is enabled
        if self.autosave:
            self.notes = self.load_notes()
            self.counter = max(self.notes.keys(), default=0)
        
    #searches for the note with the given code
    def search_note(self, code):
        return self.notes.get(code, None)
    
    #creates a note with the given text
    def create_note(self, text):
        self.counter += 1
        self.notes[self.counter] = Note(self.counter, text)

        #save the notes if autosave is enabled
        if self.autosave:
            self.save_notes()
        
        return self.notes[self.counter]
    
    #retrieves all the notes that contain the given text
    def retrieve_notes(self, text):
        return [note for note in self.notes.values() if text in note.text]
    
    #updates the note with the given code to have the given text
    def update_note(self, code, text):
        note = self.notes.get(code, None)
        if note is not None:
            note.text = text

            #save the notes if autosave is enabled
            if self.autosave:
                self.save_notes()

            return True
        return False
    
    #deletes the note with the given code
    def delete_note(self, code):
        if self.notes.pop(code, None) is None:
            return False
        
        #save the notes if autosave is enabled
        if self.autosave:
            self.save_notes()

        return True
    
    #lists all the notes
    def list_notes(self):
        lst = list(self.notes.values())
        lst.reverse()
        return lst
    

    #loads the notes from a binary file using pickle
    def load_notes(self):
        notes = {}
        try:
            #opens the file in rb mode and reads the notes
            with open(f"clinic/records/{self.phn}.dat", "rb") as file:

                #loads the notes until the end of the file
                while True:
                    try:
                        note = load(file)
                        notes[note.code] = note
                    except EOFError:
                        break
            return notes
        #if the file does not exist, return an empty dictionary
        except FileNotFoundError:
            return notes
    
    #saves the notes to a binary file using pickle
    def save_notes(self):
        #opens the file in wb mode and writes the notes
        with open(f"clinic/records/{self.phn}.dat", "wb") as file:
            for note in self.notes.values():
                dump(note, file)