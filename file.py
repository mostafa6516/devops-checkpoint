import builtins
open = builtins.open  # Ensures we use the correct open function

FILE_NAME = "text.txt"

def show_data():
    try:
        with open(FILE_NAME, "r") as f:
            print("\n--- Current Data in File ---")
            print(f.read())
            print("----------------------------")
    except FileNotFoundError:
        print("\n[!] File not found. Add some data first!")

def add_data():
    new_text = input("Enter the text you want to add: ")
    with open(FILE_NAME, "a") as f:
        f.write(new_text + "\n")
    print("Successfully added!")

def clear_data():
    confirm = input("Are you sure you want to delete ALL data? (yes/no): ")
    if confirm.lower() == "yes":
        with open(FILE_NAME, "w") as f:
            f.write("") # This clears the file
        print("File cleared!")

# --- MAIN MENU LOOP ---
while True:
    print("\n=== SIMPLE FILE MENU ===")
    print("1. Show Data")
    print("2. Add Data")
    print("3. Clear All Data")
    print("4. Exit")
    
    choice = input("Choose an option (1-4): ")
    
    if choice == "1":
        show_data()
    elif choice == "2":
        add_data()
    elif choice == "3":
        clear_data()
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid choice, please try again.")
