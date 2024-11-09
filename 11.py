class Teacher:
    def __init__(self, name, subject):
        self.name = name
        self.subject = subject
        self.students = []

    def add_student(self, student):
        if student not in self.students:
            self.students.append(student)
            student.set_teacher(self)
            print(f"Учитель {self.name} добавил ученика {student.name}")

    def give_assignment(self, assignment):
        for student in self.students:
            student.receive_assignment(assignment)
        print(f"Учитель {self.name} дал задание по предмету {self.subject}: {assignment}")

class Student:
    def __init__(self, name):
        self.name = name
        self.assignments = []
        self.teacher = None

    def set_teacher(self, teacher):
        self.teacher = teacher
        print(f"Ученик {self.name} теперь учится у учителя {teacher.name}")

    def receive_assignment(self, assignment):
        self.assignments.append(assignment)
        print(f"Ученик {self.name} получил задание: {assignment}")

    def complete_assignment(self):
        if self.assignments:
            completed = self.assignments.pop(0)
            print(f"Ученик {self.name} выполнил задание: {completed}")
        else:
            print(f"У ученика {self.name} нет заданий для выполнения")

teacher = Teacher(name="Пареха", subject="Математика")
student1 = Student(name="Сашок")
student2 = Student(name="Давидушка")

teacher.add_student(student1)
teacher.add_student(student2)

teacher.give_assignment("Решить уравнение")

student1.complete_assignment()
student2.complete_assignment()
