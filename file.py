import builtins
open = builtins.open  # Ensures we use the correct open function
print("[+] file.py started - CI/CD pipeline test")

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

# --- TEST CODE (Runs without requiring input) ---
def test_file_operations():
    import os
    test_filename = "test_temp.txt"
    print("\n[+] Running automated test for file operations...")
    
    # Temporary mock of FILE_NAME
    global FILE_NAME
    original_filename = FILE_NAME
    FILE_NAME = test_filename
    
    try:
        # Write test data
        with open(FILE_NAME, "w") as f:
            f.write("Line 1\nLine 2\n")
        
        # Read and check test data
        with open(FILE_NAME, "r") as f:
            content = f.read()
            
        assert content == "Line 1\nLine 2\n", f"Test failed! Expected 'Line 1\\nLine 2\\n', got {repr(content)}"
        print("[+] Automated test passed successfully!")
    finally:
        # Clean up
        if os.path.exists(test_filename):
            os.remove(test_filename)
        # Restore FILE_NAME
        FILE_NAME = original_filename

# Execute test
test_file_operations()

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
        print("argo test")

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