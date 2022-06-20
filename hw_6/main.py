class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_hw(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def _average_grade_(self):
        count_grades = 0
        sum_grades = 0
        for list_ in self.grades.values():
            count_grades += len(list_)
            for grade in list_:
                sum_grades += grade
        result = sum_grades/count_grades
        return result

    def __str__(self):
        name_ = f"Имя: {self.name}"
        surname_ = f"Фамилия: {self.surname}"
        average_grade_hw = f"Средняя оценка за домашние задания: {round(self._average_grade_(), 1)}"
        courses_in_progress_ = f"Курсы в процессе изучения: {', '.join(self.courses_in_progress)}"
        finished_courses_ = f"Завершенные курсы: {', '.join(self.finished_courses)}"
        result = f"\n{name_}\n{surname_}\n{average_grade_hw}\n{courses_in_progress_}\n{finished_courses_}"
        return result
        
class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

class Lecturer(Mentor):
    grades = {}

    def _average_grade_(self):
        count_grades = 0
        sum_grades = 0
        for list_ in self.grades.values():
            count_grades += len(list_)
            for grade in list_:
                sum_grades += grade
        result = sum_grades/count_grades
        return result

    def __str__(self):
        name_ = f"Имя: {self.name}"
        surname_ = f"Фамилия: {self.surname}"
        average_grade = f"Средняя оценка за домашние задания: {round(self._average_grade_(), 1)}"
        result = f"\n{name_}\n{surname_}\n{average_grade}"
        return result

class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        name_ = f"Имя: {self.name}"
        surname_ = f"Фамилия: {self.surname}"
        result = f"\n{name_}\n{surname_}"
        return result
 

some_lecturer = Lecturer('Some', 'Buddy')
some_lecturer.courses_attached += ['Python']

some_student = Student('Ruoy', 'Eman', 'your_gender')
some_student.courses_in_progress += ['Python', 'Git']
some_student.finished_courses += ['Введение в программирование']
some_student.rate_hw(some_lecturer, 'Python', 4)
some_student.rate_hw(some_lecturer, 'Python', 8)

some_reviewer = Reviewer('Some', 'Buddy')
some_reviewer.courses_attached += ['Python']
some_reviewer.rate_hw(some_student, 'Python', 10)
some_reviewer.rate_hw(some_student, 'Python', 5)


print(some_student)
print(some_lecturer)
print(some_reviewer)