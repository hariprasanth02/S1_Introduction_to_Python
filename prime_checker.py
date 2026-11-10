num = int(input("Enter a number: "))

if num < 1:
    print("Not a prime number")

else:
    for num in range(2,num+1):
        is_prime = True
    
        for i in range(2,num):
            if num % i == 0:
                is_prime = False
                break


        if is_prime:
            print(f"{num} is a Prime number")
        else:
            print(f" {num} Not a prime number")
