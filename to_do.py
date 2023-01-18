tasks = []

def add_task(task):
    tasks.append(task)
    print("Task added:", task)

def complete_task(task):
    tasks.remove(task)
    print("Task completed:", task)

def list_tasks():
    print("Tasks:")
    for task in tasks:
        print(task)

add_task("Buy groceries")
add_task("Do laundry")
add_task("Pay bills")
list_tasks()
complete_task("Do laundry")
list_tasks()