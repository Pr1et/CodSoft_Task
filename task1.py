tasks = []


def addTask():
  task = input("Enter a task you want to do: ")
  tasks.append(task)
  print(f"Task '{task}' added to the list.")


def listTasks():
  if not tasks:
    print("Task not Available.")
  else:
    print("Current Tasks:")
    for index, task in enumerate(tasks):
      print(f"Task #{index}. {task}")


def deleteTask():
  listTasks()
  try:
    taskToDelete = int(input("Enter the # to delete: "))
    if taskToDelete >= 0 and taskToDelete < len(tasks):
      tasks.pop(taskToDelete)
      print(f"Task {taskToDelete} has been removed.")
    else:
      print(f"Task #{taskToDelete} was not found.")
  except:
    print("Invalid input.")

def update_task():
    listTasks()
    try:
      taskToUpdate = int(input("Enter # of task you want to update : "))
      if taskToUpdate >= 0 and taskToUpdate < len(tasks):
        new_task = input("Enter task : ")
        tasks[taskToUpdate] = new_task
        print(f"Task '{new_task}' updated")

      else:
        print("Task not found")

    except:
      print("Invalid input")

if __name__ == "__main__":
  print("Welcome to the to do list app :)")
  while True:
    print("\n")
    print("Please select one of the following options")
    print("1. Add a new task")
    print("2. Delete a task")
    print("3. List tasks")
    print("4. Update tasks")
    print("5. Quit")

    choice = input("Enter your choice: ")

    if (choice == "1"):
      addTask()
    elif (choice == "2"):
      deleteTask()
    elif (choice == "3"):
      listTasks()
    elif (choice == "4"):
      update_task()
    elif (choice == "5"):
      break
    else:
      print("Invalid input. Please try again.")

  print("Enjoy your day...")