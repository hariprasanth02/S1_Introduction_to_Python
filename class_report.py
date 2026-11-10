names = ["Ana","Ben","Chloe","Dan"]
grades = [14.5,8.0,17.0,11.5]
total = 0
for number, (name,grade) in enumerate( zip(names,grades),start=1):
    if grade >= 10:
        status = "PASS"
    else:
        status = "FAIL"

    print(f"{number}. {name}: {grade} {status}")
    total += grade

average = total/len(grades)

print(f"Average:{average:.2f}")

