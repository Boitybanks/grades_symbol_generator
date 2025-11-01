import unittest
from letter import letter_grade

class TestLetterGrade(unittest.TestCase):

    def test_grade_A(self):
        self.assertEqual(letter_grade(85), "A")
        print("You got an A")

    def test_grade_B(self):
        self.assertEqual(letter_grade(75), "B")
        print("You got a B")

    def test_grade_C(self):
        self.assertEqual(letter_grade(65), "C")
        print("You got a C")

    def test_grade_D(self):
        self.assertEqual(letter_grade(55), "D")
        print("You got a D")

    def test_grade_F(self):
        self.assertEqual(letter_grade(45), "F")
        print("You got an F")


if __name__ == '__main__':
    unittest.main()
       

