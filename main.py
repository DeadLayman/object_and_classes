class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

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

    def _average_rate_student(self):
        rate = []
        if len(self.grades) != 0:
            for grade in self.grades.values():
                rate.extend(grade)
            return '%.1f' % (sum(rate) / len(rate))
        else:
            return rate

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname} ' \
               f'\nСредняя оценка за домашние задания: {self._average_rate_student()}' \
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

    def _average_rate_lector(self):
        rate = []
        if len(self.lector_grades) != 0:
            for grade in self.lector_grades.values():
                rate.extend(grade)
            return '%.1f' % (sum(rate) / len(rate))
        else:
            return rate

    def __str__(self):
        return f'Имя: {self.name} \nФамилия: {self.surname} \nСредняя оценка за лекции: {self._average_rate_lector()}'


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
