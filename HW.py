class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_l(self, lector, course, grade):
        if isinstance(lector, Lector) and course in lector.courses_attached and course in self.courses_in_progress:
            if course in lector.grades:
                lector.grades[course] += [grade]
            else:
                lector.grades[course] = [grade]
        else:
            return 'Ошибка'

    def mean_grade(self):
        sum_grades = 0
        count_grades = 0
        for grades_of_course in self.grades.values():
            sum_grades += sum(grades_of_course)
            count_grades += len(grades_of_course)

        return sum_grades / count_grades

    def __str__(self):
        return (f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.mean_grade()}\n'
                f'Курсы в процессе изучения: {', '.join(self.courses_in_progress)}\n'
                f'Завершенные курсы: {', '.join(self.finished_courses)}')

    def __gt__(self, other):
        return self.mean_grade() > other.mean_grade()

    def __eq__(self, other):
        return self.mean_grade() == other.mean_grade()


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lector(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def mean_grade(self):
        sum_grades = 0
        count_grades = 0
        for grades_of_course in self.grades.values():
            sum_grades += sum(grades_of_course)
            count_grades += len(grades_of_course)

        return sum_grades / count_grades

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.mean_grade()}'

    def __gt__(self, other):
        return self.mean_grade() > other.mean_grade()

    def __eq__(self, other):
        return self.mean_grade() == other.mean_grade()


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
        return f'Имя:{self.name}\nФамилия:{self.surname}'


best_student = Student('Ruoy', 'Eman', 'man')
best_student.finished_courses += ['C+']
best_student.courses_in_progress += ['Python']
best_student.grades = {'C+': [10, 10, 10, 10]}

bad_student = Student('John', 'Smit', 'man')
bad_student.finished_courses += []
bad_student.courses_in_progress += ['C+', 'Python']

woman_lector = Lector('Sara', 'Parker')
woman_lector.courses_attached += ['Python']

man_lector = Lector('Brad', 'Pitt')
man_lector.courses_attached += ['C+']


hot_reviewer = Reviewer('Jenifer', 'Lopez')
hot_reviewer.courses_attached += ['Python']

cool_reviewer = Reviewer('Chak', 'Norris')
cool_reviewer.courses_attached += ['C+']

print(hot_reviewer)
print(cool_reviewer)

hot_reviewer.rate_hw(best_student, 'Python', 10)
hot_reviewer.rate_hw(best_student, 'Python', 10)
hot_reviewer.rate_hw(best_student, 'Python', 9)
hot_reviewer.rate_hw(best_student, 'Python', 10)

hot_reviewer.rate_hw(bad_student, 'Python', 4)
cool_reviewer.rate_hw(bad_student, 'C+', 5)
hot_reviewer.rate_hw(bad_student, 'Python', 3)
cool_reviewer.rate_hw(bad_student, 'C+', 2)
hot_reviewer.rate_hw(bad_student, 'Python', 3)
cool_reviewer.rate_hw(bad_student, 'C+', 4)
hot_reviewer.rate_hw(bad_student, 'Python', 2)
cool_reviewer.rate_hw(bad_student, 'C+', 2)

best_student.mean_grade()
bad_student.mean_grade()

print(best_student)
print(bad_student)

print(best_student > bad_student)

best_student.rate_l(woman_lector, 'Python', 10)
best_student.rate_l(woman_lector, 'Python', 9)
best_student.rate_l(woman_lector, 'Python', 10)

bad_student.rate_l(woman_lector, 'Python', 1)
bad_student.rate_l(woman_lector, 'Python', 2)
bad_student.rate_l(woman_lector, 'Python', 1)
bad_student.rate_l(woman_lector, 'Python', 2)

bad_student.rate_l(man_lector, 'C+', 2)
bad_student.rate_l(man_lector, 'C+', 1)
bad_student.rate_l(man_lector, 'C+', 6)
bad_student.rate_l(man_lector, 'C+', 1)

woman_lector.mean_grade()
man_lector.mean_grade()

print(woman_lector)
print(man_lector)

print(man_lector < woman_lector)


def mean_grade_students(list_students, course):
    sum_grades = 0
    count_grades = 0
    for student in list_students:
        sum_grades += sum(student.grades[course])
        count_grades += len(student.grades[course])
    return sum_grades / count_grades


def mean_grade_lectors(list_lectors, course):
    sum_grades = 0
    count_grades = 0
    for lector in list_lectors:
        sum_grades += sum(lector.grades[course])
        count_grades += len(lector.grades[course])
    return sum_grades / count_grades
