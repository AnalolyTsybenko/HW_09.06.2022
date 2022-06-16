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
cool_lecturer.courses_attached += ['Python', 'Git']

best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python', 'Git']
best_student.finished_courses += ['Введение в программирование']

best_student.rate_lecture(cool_lecturer, 'Python', 10)
best_student.rate_lecture(cool_lecturer, 'Python', 9)
best_student.rate_lecture(cool_lecturer, 'Python', 8)
best_student.rate_lecture(cool_lecturer, 'Git', 10)
best_student.rate_lecture(cool_lecturer, 'Git', 9)
best_student.rate_lecture(cool_lecturer, 'Git', 8)

zingy_reviewer = Reviewer('Some', 'Buddy')
zingy_reviewer.courses_attached += ['Python', 'Git']

zingy_reviewer.rate_hw(best_student, 'Python', 9)
zingy_reviewer.rate_hw(best_student, 'Python', 8)
zingy_reviewer.rate_hw(best_student, 'Python', 7)
zingy_reviewer.rate_hw(best_student, 'Git', 9)
zingy_reviewer.rate_hw(best_student, 'Git', 8)
zingy_reviewer.rate_hw(best_student, 'Git', 7)


cool_lecturer_2 = Lecturer('Some2', 'Buddy2')
cool_lecturer_2.courses_attached += ['Python', 'Git']

best_student_2 = Student('Ruoy2', 'Eman2', 'your_gender')
best_student_2.courses_in_progress += ['Python', 'Git']
best_student_2.finished_courses += ['Введение в программирование']

best_student_2.rate_lecture(cool_lecturer_2, 'Git', 6)
best_student_2.rate_lecture(cool_lecturer_2, 'Git', 5)
best_student_2.rate_lecture(cool_lecturer_2, 'Git', 4)
best_student_2.rate_lecture(cool_lecturer_2, 'Python', 5)
best_student_2.rate_lecture(cool_lecturer_2, 'Python', 4)
best_student_2.rate_lecture(cool_lecturer_2, 'Python', 3)

zingy_reviewer_2 = Reviewer('Some2', 'Buddy2')
zingy_reviewer_2.courses_attached += ['Python', 'Git']

zingy_reviewer_2.rate_hw(best_student_2, 'Git', 7)
zingy_reviewer_2.rate_hw(best_student_2, 'Git', 6)
zingy_reviewer_2.rate_hw(best_student_2, 'Git', 5)
zingy_reviewer_2.rate_hw(best_student_2, 'Python', 6)
zingy_reviewer_2.rate_hw(best_student_2, 'Python', 5)
zingy_reviewer_2.rate_hw(best_student_2, 'Python', 4)


best_student.average_student_rating(best_student.grades)
cool_lecturer.average_lecturer_rating(cool_lecturer.grades)

best_student_2.average_student_rating(best_student_2.grades)
cool_lecturer_2.average_lecturer_rating(cool_lecturer_2.grades)


students_list = [best_student, best_student_2]
lecturers_list = [cool_lecturer, cool_lecturer_2]


def average_all_students_for_course(list_students, course):
    general = []
    for val in list_students:
        general.append(sum(val.grades[course]) / len(val.grades[course]))
    return f'Средняя оценка студентов по курсу {course}: {sum(general) / len(general)}'


def average_all_lecturers_for_course(list_lecturers, course):
    general = []
    for val in list_lecturers:
        general.append(sum(val.grades[course]) / len(val.grades[course]))
    return f'Средняя оценка лекторов по курсу {course}: {sum(general) / len(general)}'


print(zingy_reviewer)
print(cool_lecturer)
print(best_student)
print()
print('У студента средний бал выше' if bool(best_student.average_value > cool_lecturer.average_value) is True
      else 'У лектора средний бал выше')
print()
print(zingy_reviewer_2)
print(cool_lecturer_2)
print(best_student_2)
print()
print('У студента2 средний бал выше' if bool(best_student_2.average_value > cool_lecturer_2.average_value) is True
      else 'У лектора2 средний бал выше')
print()
print()
print(average_all_students_for_course(students_list, 'Python'))
print(average_all_students_for_course(students_list, 'Git'))
print(average_all_lecturers_for_course(lecturers_list, 'Python'))
print(average_all_lecturers_for_course(lecturers_list, 'Git'))
