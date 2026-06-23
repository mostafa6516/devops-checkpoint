FILE_NAME = "text.txt"

while True:
    print("\n1. Show data")
    print("2. Add data")
    print("3. Clear data")
    print("4. Exit")
    choice = input("Choose (1-4): ")

    if choice == "1":
        try:
            f = open(FILE_NAME, "r")
            print(f.read())
            f.close()
        except FileNotFoundError:
            print("File not found. Add some data first!")

    elif choice == "2":
        text = input("Enter text: ")
        f = open(FILE_NAME, "a")
        f.write(text + "\n")
        f.close()
        print("Added!")

    elif choice == "3":
        confirm = input("Are you sure you want to clear the file? (yes/no): ")
        if confirm.upper() == "yes":
            f = open(FILE_NAME, "w")
            f.close()
            print("File cleared!")
        else:
            print("File not cleared!")
            
    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid choice.")