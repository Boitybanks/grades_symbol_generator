# Write a function called letter_grade(mark:int) -> str that returns a letter a student got:
# ○ A = 80–100
# ○ B = 70–79
# ○ C = 60–69
# ○ D = 50–59
# ○ F = below 50
# Write unit tests to test if the function returns the expected.
# the file structure of the program must be
# letter.py
# test_letter.py

def letter_grade(mark):
    """_Function returns a specific letter according to the grades of a student_

    Args:
        mark (_integer_): _The Mark range of a the students_

    Returns:
        _Str_: _A letter associated with the marks_
    """
    mark = int(mark)
    if mark >= 80:
        return "A"
    if mark >= 70:
        return "B"
    if mark >= 60:
        return "C"
    if mark >= 50:
        return "D"
    else:
        return "F"
#marks = input("Enter your marks: ")
print(letter_grade(85))

