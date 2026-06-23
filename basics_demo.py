
from os import open


#reading files
import builtins
open = builtins.open
test_file = open("text.txt", "r")
print(test_file.read())




def welcome_user(name):
    """Function to greet the user."""
    return f"Hello {name}! Welcome to your first Python project."

def main():
    user_name = input("Enter your name: ")
    print(welcome_user(user_name))
    
    tasks = ["Learn Python", "Build a project", "Celebrate"]
    
    print("\nHere are your current goals:")


    for index, task in enumerate(tasks, 1):
        print(f"{index}. {task}")
    
    new_task = input("\nAdd a new goal: ")
    tasks.append(new_task)
    
    print("\nUpdated goal list:")
    for task in tasks:
        print(f"- {task}")
        
    val1 = 10
    val2 = 5
    print(f"\nQuick Math: {val1} + {val2} = {val1 + val2}")

if __name__ == "__main__":
    main()

name = "mostafa"
age = 30
price = 19.99

print(f"name is {name}\nage is {age}\nprice is {price}")


grades = [90, 80, 70, 60, 50]

after_append_grades = []

for gra in grades:
    bounes =gra +1
    after_append_grades.append(bounes)

print ("grades : ", grades)
print ("after_append_grades : ", after_append_grades)





def get_discount(price):
    return price * 0.5

user_input = input("Enter the price: ")

discounted_price = get_discount(float(user_input))

print(f"The price after 50% discount is: {discounted_price}")













test_file .close()