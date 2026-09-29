import unittest
from studymate import Student, student_to_dict, student_from_dict


class TestStudent(unittest.TestCase):

    def setUp(self):
        self.s = Student("Sam", 3, 10)
        self.s.add_subject("Math", 65, "low")
        self.s.add_subject("Science", 85, "high")

    def test_subject(self):
        self.assertEqual(len(self.s.subjects), 2)

    def test_marks(self):
        self.s.update_marks("Math", 75)
        self.assertEqual(self.s.subjects["Math"]["marks"], 75)

    def test_wrong_marks(self):
        with self.assertRaises(ValueError):
            self.s.add_subject("History", 120, "medium")

    def test_student_data(self):
        data = student_to_dict(self.s)
        student = student_from_dict(data)

        self.assertEqual(student.name, "Sam")
        self.assertEqual(student.subjects, self.s.subjects)


if __name__ == "__main__":
    unittest.main()