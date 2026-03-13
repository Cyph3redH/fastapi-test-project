class Student:
    def __init__(self, name, age, group):
        self.name = name
        self.age = age
        self.group = group
        self.grades = []
    def add_grade(self, grade):
        if 1 <= grade <= 100:
            self.grades.append(grade)
            return f"Оценка {grade} добавлена"
        return "Не верная оценка"
    def average(self):
        if self.grades:
            return sum(self.grades) / len(self.grades)
        return 0
    def info(self):
        return f"{self.name} ({self.age} лет), группа {self.group}, средний балл: {self.average():.2f}"

students = [
    Student("Лина", 20, "CS-101"),
    Student("Влад", 22, "CS-102")
]

students[0].add_grade(85)
students[0].add_grade(90)
students[1].add_grade(92)
students[1].add_grade(88)

for student in students:
    print(student.info())
print()