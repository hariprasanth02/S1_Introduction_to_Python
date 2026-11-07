weight = int(input("Enter the weight (Kg): "))
height = float(input("Enter the height (m): "))

bmi = weight/height ** 2

if bmi >= 30:
    print(f"{bmi:.1f} (Obese)" )

elif bmi >=25 and bmi < 30:
    print(f"{bmi:.1f} (Overweight)")

elif bmi >=18.5 and bmi < 25:
    print(f"{bmi:.1f} (Normal)")

elif bmi < 18.5:
    print(f"{bmi:.1f} (Underweight)")

else:
    print("Unknown Value")

