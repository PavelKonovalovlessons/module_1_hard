grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}

students_l = list(students)
students_l.sort()

avg_grades = list(map(lambda student_grades:
        sum(student_grades) / len(student_grades),grades))



students_avg_grade = dict(zip(students_l, avg_grades))
print(students_avg_grade)