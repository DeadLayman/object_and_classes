students_list = []
lectors_list = []


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
            return round(sum(rate) / len(rate), 2)
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
            return round(sum(rate) / len(rate), 2)
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


student1 = Student('First', 'Student', 'some male')
student1.courses_in_progress.append('Python')
student1.finished_courses.append('JS')

student2 = Student('Second', 'Student', 'some male')
student2.courses_in_progress.append('Python')

lector1 = Lecturer('First', 'Lector')
lector1.courses_attached.append('Python')
lector2 = Lecturer('Second', 'Lector')
lector2.courses_attached.append('Python')

reviewer = Reviewer('Some', 'Reviewer')
reviewer.courses_attached.append('Python')

reviewer.rate_hw(student1, 'Python', 8)
reviewer.rate_hw(student1, 'Python', 8)
reviewer.rate_hw(student2, 'Python', 9)
reviewer.rate_hw(student2, 'Python', 9)

student1.rate_lector(lector1, 'Python', 8)
student1.rate_lector(lector1, 'Python', 8)

student2.rate_lector(lector2, 'Python', 9)
student2.rate_lector(lector2, 'Python', 9)

print(student1)
print()
print(reviewer)
print()
print(lector1)
print()
print(lector2)
print()
print(student1 < student2)
print(lector1 == lector2)
