def analyze(grades):
    grade_list = []
    count = 0
    for grade in grades.split(','):
        new_grade = float(grade.strip())
        grade_list.append(new_grade)
    for grade in grade_list:
        if grade >= 85:
            count += 1
    return count

string = input("Enter the grades separated by ,: \n")
print(analyze(string))