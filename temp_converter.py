temp = float(input("Enter temperature: "))

unit = input("Convert to C/F : ")

if unit == "C":
    farenheit = (temp * 9/5) + 32
    print(f"Temperature in farenheit is : {farenheit:.2f}")
elif unit == "F":
    celcius = (temp-32)*5/9
    print(f"Temperature in celcius is : {celcius:.2f}")

else:
    print(("Unknown temperature"))