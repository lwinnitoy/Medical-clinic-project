from unittest import TestCase, main
from clinic.patient import Patient

class PatientTests(TestCase):

    def setUp(self):
        self.patient1 = Patient("1234567890", "John Doe", "1990-01-01", "555-555-5555", "john@example.com", "123 Main St")
        self.patient2 = Patient("1234567890", "John Doe", "1990-01-01", "555-555-5555", "john@example.com", "123 Main St")
        self.patient3 = Patient("0987654321", "Jane Doe", "1992-02-02", "555-555-5556", "jane@example.com", "456 Elm St")

    def test_eq(self):
        self.assertEqual(self.patient1, self.patient2)
        self.assertNotEqual(self.patient1, self.patient3)

    def test_str(self):
        self.assertEqual(str(self.patient1), "Patient(1234567890)")
        self.assertEqual(str(self.patient3), "Patient(0987654321)")


if __name__ == '__main__':
    main()
