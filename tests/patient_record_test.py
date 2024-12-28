from unittest import TestCase, main
from clinic.patient_record import *
from clinic.note import *

class PatientRecordTest(TestCase):

    def setUp(self):
        self.note1a = Note(1, 'note1')
        self.note2a = Note(2, 'note2')
    
    def test_add_note(self):
        record = PatientRecord()
        note1 = record.add_note('note1')
        note2 = record.add_note('note2')

        self.assertEqual(note1.code, 1)
        self.assertEqual(note2.code, 2)
        self.assertEqual(note1.text, 'note1')
        self.assertEqual(note2.text, 'note2')

    def test_search_note(self):
        record = PatientRecord()
        note1 = record.add_note('note1')
        note2 = record.add_note('note2')

        self.assertEqual(note1, record.search_note(1))
        self.assertEqual(note2, record.search_note(2))
        self.assertIsNone(record.search_note(3))

    def test_retrieve_patient_notes(self):
        record = PatientRecord()
        record.add_note('note1')
        record.add_note('note2')
        record.add_note('another note1')

        notes = record.retrieve_patient_notes('note1')
        self.assertEqual(len(notes), 2)
        self.assertEqual(notes[0].text, 'note1')
        self.assertEqual(notes[1].text, 'another note1')

    def test_update_note_text(self):
        record = PatientRecord()
        record.add_note('note1')
        record.add_note('note2')

        self.assertTrue(record.update_note_text(1, 'updated note1'))
        self.assertEqual(record.search_note(1).text, 'updated note1')
        self.assertFalse(record.update_note_text(3, 'non-existent note'))

    def test_list_patient_notes(self):
        record = PatientRecord()
        note1 = record.add_note('note1')
        note2 = record.add_note('note2')

        notes = record.list_patient_notes()
        self.assertEqual(notes[0], note2)
        self.assertEqual(notes[1], note1)

    def test_delete_note(self):
        record = PatientRecord()
        record.add_note('note1')
        record.add_note('note2')

        self.assertTrue(record.delete_note(1))
        self.assertFalse(record.delete_note(1))
        self.assertTrue(record.delete_note(2))
        self.assertFalse(record.delete_note(2))


if __name__ == '__main__':
    main()