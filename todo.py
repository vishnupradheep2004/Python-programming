import sys
import os

def display_todos():
    if os.path.exists('todos.txt'):
        with open('todos.txt', 'r') as file:
            todos = file.readlines()
            for i, todo in enumerate(todos, 1):
                print(f"{i}. {todo.strip()}")
    else:
        print("No todos found.")

def add_todo(todo):
    with open('todos.txt', 'a') as file:
        file.write(f"{todo}\n")
        print(f"Added todo: {todo}")

def delete_todo(todo_number):
    try:
        todo_number = int(todo_number)
        with open('todos.txt', 'r') as file:
            todos = file.readlines()
        with open('todos.txt', 'w') as file:
            for i, todo in enumerate(todos, 1):
                if i != todo_number:
                    file.write(todo)
        print(f"Deleted todo #{todo_number}")
    except ValueError:
        print("Invalid todo number.")

def main():
    while True:
        print("\nOptions:")
        print("1. Add todo")
        print("2. Display todo")
        print("3. Delete todo")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            todo = input("Enter the todo: ")
            add_todos()
        elif choice == "2": 
            display_todo(todo)
        elif choice == "3":
            todo_number = input("Enter the todo number to delete: ")
            delete_todo(todo_number)
        elif choice == "4":
            print("Goodbye!")
            sys.exit(0)
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
