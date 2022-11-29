class Programmer:
    def __init__(self, name: str, language: str, skills: int):
        self.name = name
        self.language = language
        self.skills = skills


    def watch_course(self, course_name, language, skills_erned):
        if self.language == language:
            self.skills += skills_erned
            return f"{self.name} watched {course_name}"
        else:
            return f"{self.name} does not know {language}"


    def change_language(self, new_language, skills_needed):
        if self.skills >= skills_needed:
            if new_language != self.language:
                message = f"{self.name} switched from {self.language} to {new_language}"
                self.language = new_language
                return message
            else:
                return f"{self.name} already knows {new_language}"
        else:
            return f"{self.name} needs {skills_needed - self.skills} more skills"

        
# Test Code
programmer = Programmer("John", "Java", 50)
print(programmer.watch_course("Python Masterclass", "Python", 84))
print(programmer.change_language("Java", 30))
print(programmer.change_language("Python", 100))
print(programmer.watch_course("Java: zero to hero", "Java", 50))
print(programmer.change_language("Python", 100))
print(programmer.watch_course("Python Masterclass", "Python", 84))
