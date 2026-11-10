grades = {
    "Ana": [14,16,12],
    "Ben": [9,11,81],
    "Chloe": [18,17,19]
}

best_student = None
best_average = -1

for student,scores in grades.items():
    average = sum(scores)/len(scores)
    print(f"{student:} {average:.1f}")

    if average > best_average:
        best_average = average
        best_student = student

print(f"Best: {best_student}")