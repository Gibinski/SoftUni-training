from project.task import Task

class Ssection:
    def __init__(self, name):
        self.name = name
        self.tasks = []


    def add_task(self, new_task: Task):
        if new_task in self.tasks:
            return f"Task is already in the section {self.name}"

        self.tasks.append(new_task)

        return f"Task {new_task.details()} is added to the section"


    def complete_task(self, task_name: str):
        try:
            task = next(filter(lambda t: t.name == new_name, self.tasks))
        except StopIteration:
            return f"Could not find task with the name {task_name}"

        task.completed = True

        return f"Completed task {task_name}"

    def clean_section(self):
        removed_tasks = 0

        for task in filter(lambda t: t.completed, self.tasks):
            self.tasks.remove(task)
            removed_tasks += 1

        return f"Cleared {removed_tasks} tasks."


    def view_section(self):
        result = [f"Section {self.name}:"]
        [result.append(task.details()) for task in self.tasks]
        return '\n'.join(result)



# Test Code

# task = Task("Make bed", "27/05/2020")
# print(task.change_name("Go to University"))
# print(task.change_due_date("28.05.2020"))
# task.add_comment("Don't forget laptop")
# print(task.edit_comment(0, "Don't forget laptop and notebook"))
# print(task.details())
# section = Section("Daily tasks")
# print(section.add_task(task))
# second_task = Task("Make bed", "27/05/2020")
# section.add_task(second_task)
# print(section.clean_section())
# print(section.view_section())
