
def run():
    students = {'Héctor': 2, 'Bodo': 1, 'Alejandra': 2}
    added_students = []
    grade = 2
    name = 'Héctor'

    if name not in students.keys():
        students[name] = grade
        added_students.append(True)
    else:
        added_students.append(False)
    
    x = [name[1] for name in sorted([(students[student], student) for student in students])]
    print(x)




    #print([student[1] for student in sorted(students)])
    #print([student_name for ])

    # name = 'Hector'
    # grade = 2

    # if name not in students:
    #     students.append((name, grade))
    #     added_students.append(True)
    # else:
    #     added_students.append(False)
    
    # print(students)
    # print(added_students)


if __name__ == '__main__':
    run()
