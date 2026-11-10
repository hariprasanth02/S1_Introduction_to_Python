while True:
    grade = float(input("Enter Grade between (0-20) : "))

    if grade >= 0 and grade <= 20:
        break
    else:
        print("Invalid, Try Again")
print("Grade Saved",grade)
    
    