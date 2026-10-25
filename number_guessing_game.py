import random

secret =random.randint(1,100)

attempts = 0
while attempts < 7:
    guess = int(input("Your Guess:"))
    attempts+=1
    if guess > secret:
        print("Too High")
    elif guess < secret:
        print("Too Low")
    else:
        print(f"Bravo! Found in {attempts} attempts")
        break
else:
    print(f"Lost,The secret number was:{secret}")


