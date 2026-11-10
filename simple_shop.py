items = []
while True:
    choice = input("1. Add 2.Remove 3.Show 0 Quit: ")
    if choice == "1":
        item_name = input("Enter item name : ").strip().lower()
        if item_name not in items:
            items.append(item_name)
        else:
            print("Item already exists")

    elif choice == "2":
        item_name = input("Enter item name you want to remove : ").strip().lower()
        if item_name in items:
            items.remove(item_name) 
        else:
            print("Not in the list")

    elif choice == "3":
        for i, item in enumerate(sorted(items),start = 1):
            print(f"{i}. {item}")

    elif choice == "0":
        print("Good Bye")
        break

    else:
        print("Invalid Choice")
