"""

Pupil Records
Players can recruit wizard pupils into their armies. Depending on the pupil's marks, they gain different in-game abilities.

Assignment
Complete the Student class.

Constructor
The constructor should set the name parameter to the name instance variable.
It should also initialize a private data member called __courses to an empty dictionary.
calculate_letter_grade method
It should take a score as a parameter.

If score is 90 or above the function should return "A"
If score is between 80 and 89 (inclusive) the function should return "B"
If score is between 70 and 79 (inclusive) the function should return "C"
If score is between 60 and 69 (inclusive) the function should return "D"
Otherwise, the function should return "F"
add_course method
It should take a course_name and score as parameters.

It should calculate_letter_grade based on the score.
It should set the course_name as a key in the courses dictionary and the calculated letter grade as the corresponding value.
get_courses method
It should return the private __courses dictionary.

"""

class Student:
    def __init__(self, name):
        self.name = name
        self.__courses = {}

    def calculate_letter_grade(self, score):
        if (score >= 90):
            return "A"
        elif (score >= 80 and score <= 89):
            return "B"
        elif  (score >= 70 and score <= 79):
            return "C"
        elif (score >= 60 and score <= 69):
            return "D"
        else:
            return "F"

    def add_course(self, course_name, score):
        grade = self.calculate_letter_grade(score)
        self.__courses[course_name] = grade

    def get_courses(self):
        return self.__courses

