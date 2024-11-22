

student_scores={
    "Harry":85,
    "Ron":99,
    "tears":89,
    "Draco":72,
    "Nevile":45
}
student_grades={}
#
# for student in student_scores:
#     score=student_scores[student]
#     if score>90:
#         student_grades[student]="Outstanding"
#     elif score>81:
#         student_grades[student]="Exceeds Exception"
#     elif 71 < score<80:
#         student_grades[student]="Acceptable"
#     else:
#         student_grades[student]="Fail"

for i in student_scores:
    get_it=student_scores[i]
    if get_it >90:
        student_grades[i]="outstanding"
    elif get_it >81:
        student_grades[i]="Exceeds Exception"
    elif get_it >71 :
        student_grades[i]="Acceptable"
    else:
        student_grades[i]="Fail"
print(student_grades)

