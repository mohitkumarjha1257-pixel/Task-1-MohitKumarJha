import json
import os

# ==========================================
# MODEL: DATA LOGIC & PERSISTENCE
# ==========================================

DATA_FILE = "tasks.json"
my_tasks = []

def load_tasks():
    """Loads tasks from the JSON file into memory when the app starts."""
    global my_tasks
    # Check if the file exists before trying to read it
    if os.path.exists(DATA_FILE):
        f = open(DATA_FILE, "r")
        my_tasks = json.load(f) # Deserialization: JSON -> Python List
        f.close()
    else:
        my_tasks = []
     
def add_task():
    """Appends a new task and immediately saves it to disk."""
    new_task = input("Enter the task description: ")
    my_tasks.append(new_task)
    
    # Ensure persistence after every modification
    
    """Saves the current state of memory into the JSON file."""
    f = open(DATA_FILE, "w")
    # Serialization: Python List -> JSON text
    # indent=4 makes the JSON file human-readable
    json.dump(my_tasks, f, indent=4)
    f.close()
        
    print(f"SUCCESS: '{new_task}' added and saved to disk.")

def get_tasks():
    """Returns the current state of the to-do list."""
    return my_tasks

# ==========================================
# VIEW & API BOUNDARY: USER INTERFACE
# ==========================================
    
def display_tasks():
    tasks = get_tasks()
    
    print("\nCURRENT TASKS:")
    if not tasks:
        print("No tasks found. Your list is empty.")
    else:
        for index, task in enumerate(tasks):
            print(f"[{index}] {task}")

def main():
    # 1. Boot up sequence: Load existing data into memory
    load_tasks()
    
    while True:
        
        print("\n--- To-Do-List ---")
        print("1. Add a Task")
        print("2. View Tasks")
        print("3. Exit")
        
        choice = input("Enter your choice (1-3): ")
        
        if choice == '1':
            add_task()
            
        elif choice == '2':
            display_tasks()
            
        elif choice == '3':
            print("Terminating process. Goodbye!")
            break
            
        else:
            print("ERROR: Invalid input. Please select 1, 2, or 3.")

# The Gatekeeper
if __name__ == "__main__":
    main()