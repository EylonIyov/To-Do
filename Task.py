class Task:


    def __init__(self, title, description, priority: int):
        self.title = title
        self.description = description
        self.done = False
        self.priority = priority

    def __str__(self):
        return f"""
                Task Name: {self.title}
                Description: {self.description}
                Priority: {self.priority}
                Is it done: {self.done}
                """

    def __repr__(self):
        return f"Task Name: {self.title}, Description: {self.description}, Priority: {self.priority}"

    def mark_done(self):
        self.done = True

    def set_priority(self, priority: int):
        self.priority = priority;

    def getTitle(self):
        return self.title

    def getDescription(self):
        return self.description

    def getPriority(self):
        return self.priority