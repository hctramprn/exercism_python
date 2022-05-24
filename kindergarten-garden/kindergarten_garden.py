student_list = ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Fred',
                'Ginny', 'Harriet', 'Ileana', 'Joseph', 'Kincaid', 'Larry']

plants_dict = {'G': 'Grass', 'C': 'Clover', 'R': 'Radishes', 'V': 'Violets'}


class Garden:
    def __init__(self, diagram, students=student_list):
        self.garden = diagram.split()
        self.students = sorted(students)

    def plants(self, name):
        index = self.students.index(name) * 2
        plants_char = self.garden[0][index:index +
                                     2] + self.garden[1][index:index + 2]
        return [plants_dict[char] for char in plants_char]