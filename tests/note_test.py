from unittest import TestCase, main
from clinic.note import *

class NoteTest(TestCase):

    def test_eq(self):
        note1 = Note(1, 'note1')
        note1a = Note(1, 'note1')
        note3 = Note(3, 'note3')
        self.assertEqual(note1, note1a)
        self.assertNotEqual(note1, note3)

    def test_str(self):
        note1 = Note(1, 'note1')
        note1a = Note(1, 'note1')
        self.assertEqual(str(note1), str(note1a), "Note strings are not equal")

if __name__ == '__main__':
    main()
