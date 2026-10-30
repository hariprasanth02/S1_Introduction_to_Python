contacts = {}

while True:
    choice = input ("1: Add, 2: Search, 3: List, 0: Quit :" )
    if choice == "1":
        name = input("Enter name of the person:")
        phone_number = input("Enter phone number of person:")
        if name not in contacts:
            contacts[name] = []
            contacts[name].append(phone_number)

    elif choice == "2":
        name = input("Name:")
        print(contacts.get(name,"Not Found"))
        
    elif choice == "3":
        for name in sorted(contacts):
            print(f"{name}: {','.join(contacts[name])}")
    elif choice == "0":
        print("Hey, You are out of Contacts")
        break
    else:
        print("Invalid Choice")

