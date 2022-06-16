class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.average_value = []

    def rate_lecture(self, lecturer, course, grade):
        if isinstance(lecturer,
                      Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def average_student_rating(self, students_grades):
        for val in students_grades.values():
            average_val = round(sum(val) / len(val), 1)
            self.average_value = average_val

    def __str__(self):
        return f'\nСтудент\nИмя: {self.name}\nФамилия: {self.surname}\n' \
               f'Средняя оценка за домашние задания: {self.average_value}\n' \
               f'Курсы в процессе изучения: {", ".join(self.courses_in_progress)}\n' \
               f'Завершенные курсы: {", ".join(self.finished_courses)}'

    def __lt__(self, other):
        return self.average_value < other.average


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}
        self.average_value = []

    def average_lecturer_rating(self, lecturer_grades):
        for val in lecturer_grades.values():
            sum_av = round(sum(val) / len(val), 1)
            self.average_value = sum_av

    def __str__(self):
        return f'\nЛектор\nИмя: {self.name}\nФамилия: {self.surname}\n' \
               f'Средняя оценка за лекции: {self.average_value}'

    def __lt__(self, other):
        return self.average_value < other.average_value


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student,
                      Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return f'\nПроверяющий\nИмя: {self.name}\nФамилия: {self.surname}'


cool_lecturer = Lecturer('Some', 'Buddy')
cool_lecturer.courses_attached += ['Python']

best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']
best_student.finished_courses += ['Введение в программирование']

best_student.rate_lecture(cool_lecturer, 'Python', 10)
best_student.rate_lecture(cool_lecturer, 'Python', 9)
best_student.rate_lecture(cool_lecturer, 'Python', 8)

zingy_reviewer = Reviewer('Some', 'Buddy')
zingy_reviewer.courses_attached += ['Python']

zingy_reviewer.rate_hw(best_student, 'Python', 9)
zingy_reviewer.rate_hw(best_student, 'Python', 8)
zingy_reviewer.rate_hw(best_student, 'Python', 7)

best_student.average_student_rating(best_student.grades)
cool_lecturer.average_lecturer_rating(cool_lecturer.grades)

print(zingy_reviewer)
print(cool_lecturer)
print(best_student)
print()
print('У студента средний бал выше' if bool(best_student.average_value > cool_lecturer.average_value) is True
      else 'У лектора средний бал выше')
