class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        students_list.append(self)

    def rate_lector(self, lector, course, grade):
        if grade > 10:
            print('Оценка должна быть по 10-бальной шкале')
        if isinstance(lector, Lecturer) and course in lector.courses_attached and course in self.courses_in_progress:
            if course in lector.lector_grades:
                lector.lector_grades[course] += [grade]
            else:
                lector.lector_grades[course] = [grade]
        else:
            return 'Ошибка'

    def _average_of_student(self):
        rate = []
        if len(self.grades) != 0:
            for grade in self.grades.values():
                rate.extend(grade)
            return round(sum(rate) / len(rate), 1)
        else:
            return 'Оценок нет'

    def __lt__(self, other):
        if isinstance(other, Student):
            return self._average_of_student() < other._average_of_student()
        return f'{other.name} не является студентом'

    def __eq__(self, other):
        if isinstance(other, Student):
            return self._average_of_student() == other._average_of_student()
        return f'{other.name} не является студентом'

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname} ' \
               f'\nСредняя оценка за домашние задания: {self._average_of_student()}' \
               f'\nКурсы в процессе изучения: {", ".join(self.courses_in_progress)} ' \
               f'\nЗавершенные курсы: {", ".join(self.finished_courses)}'


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.lector_grades = {}
        lectors_list.append(self)

    def _average_of_lector(self):
        rate = []
        if len(self.lector_grades) != 0:
            for grade in self.lector_grades.values():
                rate.extend(grade)
            return round(sum(rate) / len(rate), 1)
        else:
            return 'Оценок нет'

    def __gt__(self, other):
        if isinstance(other, Lecturer):
            return self._average_of_lector() > other._average_of_lector()
        return f'{other.name} не является лектором'

    def __eq__(self, other):
        if isinstance(other, Lecturer):
            return self._average_of_lector() == other._average_of_lector()
        return f'{other.name} не является лектором'

    def __str__(self):
        return f'Имя: {self.name} \nФамилия: {self.surname} \nСредняя оценка за лекции: {self._average_of_lector()}'


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
        return f'Имя: {self.name}\nФамилия: {self.surname}'


students_list = []
lectors_list = []


def middle_rate_st(student_list, course):
    rate_st = []
    for student in student_list:
        if isinstance(student, Student):
            if course in student.grades:
                rate_st += student.grades.get(course)
            else:
                continue
    print(f'Средняя оценка студентов по курсу {course} - {round(sum(rate_st) / len(rate_st), 1)}')


def middle_rate_lc(lector_list, course):
    rate_lc = []
    for lector in lector_list:
        if isinstance(lector, Lecturer):
            if course in lector.lector_grades:
                rate_lc += lector.lector_grades.get(course)
            else:
                continue
    print(f'Средняя оценка лекторов за курс {course} - {round(sum(rate_lc) / len(rate_lc), 1)}')


student1 = Student('First', 'Student', 'some male')
student1.courses_in_progress.append('Python')
student1.courses_in_progress.append('JS')
student1.finished_courses.append('C++')

student2 = Student('Second', 'Student', 'some male')
student2.courses_in_progress.append('Python')

lector1 = Lecturer('First', 'Lector')
lector1.courses_attached.append('Python')
lector2 = Lecturer('Second', 'Lector')
lector2.courses_attached.append('Python')
lector2.courses_attached.append('JS')

reviewer = Reviewer('Some', 'Reviewer')
reviewer.courses_attached.append('Python')
reviewer.courses_attached.append('JS')

reviewer.rate_hw(student1, 'Python', 8)
reviewer.rate_hw(student1, 'Python', 8)
reviewer.rate_hw(student1, 'JS', 8)
reviewer.rate_hw(student1, 'JS', 10)

reviewer.rate_hw(student2, 'Python', 9)
reviewer.rate_hw(student2, 'Python', 9)

student1.rate_lector(lector1, 'Python', 7)
student1.rate_lector(lector1, 'Python', 8)
student1.rate_lector(lector2, 'JS', 10)
student1.rate_lector(lector2, 'JS', 10)

student2.rate_lector(lector2, 'Python', 9)
student2.rate_lector(lector2, 'Python', 9)

print(student1)
print()
print(student2)
print()
print(reviewer)
print()
print(lector1)
print()
print(lector2)
print()
print(student1 < student2)
print(lector1 == lector2)
print()
middle_rate_st(students_list, 'Python')
middle_rate_st(students_list, 'JS')
middle_rate_lc(lectors_list, 'Python')
middle_rate_lc(lectors_list, 'JS')
