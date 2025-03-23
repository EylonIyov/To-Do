from time import sleep

from Task import Task
import os


def add(taskList: list):
    title = input("What is the task title? \n").strip()
    Description = input("Please enter the description of the task \n").strip()
    priority = input("Please enter the priority of the task \n")
    taskList.append(Task(title, Description, priority))
    return

def removeTask(taskList: list):
    title = input("What is the task name you would like to remove? \n").strip()
    if title not in list(task.getTitle() for task in taskList):
        print("Invalid title \n")
        return
    for task in taskList:
        if task.getTitle() == title:
            print(f"The task: {task.getTitle()} has been successfuly removed \n")
            taskList.remove(task)
            return

def removeAllTasks(taskList: list):
    for task in taskList:
        taskList.remove(task)
        return

def updateTask(taskList: list):
    title = input("What is the title of the task you would like to update? \n").strip()
    if title not in list(task.getTitle() for task in taskList):
        print("Invalid title\n")
        return
    taskFields = ["title", "description", "priority"]
    updatedField = input("What is the field you would like to update? \n").strip()
    if updatedField not in taskFields:
        print("Invalid field \n")
        return
    for task in taskList:
        if task.getTitle() == title:
            changeField(task, updatedField)
            print(f"updated field {updatedField} of task {task.title} \n")
            sleep(3)
            print("Done")


def markTask(taskList: list):
    title = input("What is the title of the task you would like to mark as finished? \n")
    if title not in list(task.getTitle() for task in taskList):
        print("Invalid title \n")
        return
    for task in taskList:
        if task.getTitle() == title:
            task.mark_done()

def changeField(task, field):
    if field == "description":
        task.description = input("What is the new description of the task? \n")
    if field == "priority":
        task.priority = input("What is the new priority of the task? \n")
    if field == "title":
        task.title = input("What is the new title of the task? \n")

def viewTasks(taskList: list):
    for task in taskList:
        print(task)

def sortTasks(taskList: list):
    list.sort(key=lambda task: task.priority, reverse=True)

def exit(taskList: list):
    try:
        with open("tasks.txt", "x") as file:
            for task in taskList:
                file.write(f"{task.title}#{task.description}#{task.priority}#{task.done}\n")
            print(f"Tasks saved in {os.path} \/tasks.txt \n")
    except FileExistsError:
        with open("tasks.txt", "a") as file:
            for task in taskList:
                file.write(f"{task.title}#{task.description}#{task.priority}#{task.done}\n")
            print(f"Tasks saved in {os.path.abspath('tasks.txt')}\n")



def openFromFile(taskList: list):
    filename = input("What is the file you would like to open? \n").strip()
    try:
        with open(filename, "r") as file:
            for line in file:
                attributes_of_task = line.split("#")
                task = Task(attributes_of_task[0], attributes_of_task[1], attributes_of_task[2])
                if attributes_of_task[3] == "True":
                    task.mark_done()
                taskList.append(task)
    except FileNotFoundError:
        print("File not found\n")

def menu(taskList: list):
    while True:
        action = input("""What operation would you like to perform? \n 1. add \n 2. remove\n 3. update\n 4. mark\n 5. view\n 6. exit \n""")
        action = action.lower().strip()
        actions = ["add", "remove", "update", "mark", "view", "exit"]
        if action not in actions:
            print("Invalid action")
            sleep(2)
            continue
        else:
            if action == "add" or action == "1":
                add(taskList)
            elif action == "remove" or action == "2":
                removeTask(taskList)
            elif action == "update" or action == "3":
                updateTask(taskList)
            elif action == "mark" or action == "4":
                markTask(taskList)
            elif action == "view" or action == "5":
                viewTasks(taskList)
            elif action == "exit"or action == "6":
                exit(taskList)
                print("Goodbye")
                break

def main():
    taskList = []
    menu(taskList)

if __name__ == "__main__":
    main()
