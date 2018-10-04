studentencijfers = [ [95, 92, 86],[66, 75, 54],[89, 72, 100],[34, 0, 0] ]

def gemiddelde_per_student(studentencijfers):
    cijferLijsten = []
    for student in studentencijfers:
        avarage = sum(student) / len(student)
        cijferLijsten.append(avarage)
    return cijferLijsten

def gemiddelde_van_alle_studenten(studentencijfers):
    accumalator = 0
    grades = 0
    for student in studentencijfers:
        for cijfer in student:
            accumalator += cijfer
            grades += 1
    avarageGrade = accumalator/grades

    return avarageGrade

print(gemiddelde_per_student(studentencijfers))
print(gemiddelde_van_alle_studenten(studentencijfers))