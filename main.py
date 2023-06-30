from classes import Student, Lecturer, Reviewer
from classes import middle_rate_lc, middle_rate_st
from classes import students_list, lectors_list

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
