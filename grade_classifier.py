grade = float(input("Grade / 20:"))

if grade >= 16 and grade < 20:
    print("Very Good")
elif grade >= 14 and grade < 16:
    print("Good")
elif grade >= 12 and grade < 14 :
    print("Fairly Good")
elif grade >= 10 and grade < 12:
    print("Pass")
else:
    print("Fail")
