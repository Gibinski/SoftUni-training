class Task:
    comments = []
    completed = False


    def __init__(self, name: str, due_date: str):
        self.name = name
        self.due_date = due_date


    def change_name(self, new_name: str):
        if self.name == new_name:
            return self.same_data(self.name)
        
        self.name = new_name

        return self.name


    def change_due_date(self, new_date: str):
        if self.due_date == new_date:
            return self.same_data(self.due_date)
        
        self.due_date = new_date

        return self.due_date


    def add_comment(self, comment: str):
        Task.comments.append(comment)


    def edit_comment(self, comment_number: int, new_comment: str):
        try:
            Task.comments[comment_number] = new_comment
        except IndexError:
            return "Cannot find comment."

        ", ".join(Task.comments)


    def details(self):
        return f"Name: {self.name} - Due Date: {self.due_date}"


    def same_data(self, data_name: str):
        return f"{data_name} cannot be the same."


# Test Code
task = Task("Make bed", "27/05/2020")
print(task.change_name("Go to University"))
print(task.change_due_date("28.05.2020"))
task.add_comment("Don't forget laptop")
print(task.edit_comment(0, "Don't forget laptop and notebook"))

print(task.edit_comment(10, "Don't forget laptop and notebook"))
print(task.details())