student_score = {
    "harry": 81,
    "ron":78,
    "sanika":68,
    "pranita":97,
    "yogita":98
}
student_gread={}
for i in student_score:
    score =student_score[i]
    if score > 90:
        student_gread[i]="Outstanding"
    if score > 80:
        student_gread[i] = "Exceeds the expectation"
    if score > 70:
        student_gread[i] = "Acceptable"
    else:
        student_gread[i] = "Failed"
print(student_gread)