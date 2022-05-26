class School:
    def __init__(self):
        self.students = {}
        self.added_students = []

    def add_student(self, name, grade):
        if name not in self.students.keys():
            self.students[name] = grade
            self.added_students.append(True)
        else:
            self.added_students.append(False)

    def roster(self):
        return [name[1] for name in sorted([(self.students[student], student) for student in self.students])]

    def grade(self, grade_number):
        return [student
                for student in sorted(self.students) if self.students[student] == grade_number]

    def added(self):
        return self.added_students
