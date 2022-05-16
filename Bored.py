# Free time task picker
# Created by Nick Lueth, 5/16/2022
import random


# This function returns a value from a random index in a provided list
def choose(my_list):
    return my_list[random.randint(0, len(my_list)-1)]


# This function pulls in information from a file and turns the data into a list
def read_in(file_name):
    f = open(file_name, "r")
    items = f.read().split("\n")
    return items


# This is the main method
if __name__ == '__main__':
    # Category of tasks
    myTasks = ["Read", "Study", "Project"]
    # Things to do for each task
    books = read_in("Books.txt")
    certs = read_in("Study.txt")
    projects = read_in("Projects.txt")
    # Choose a task
    task = choose(myTasks)
    # Formulate a response based on what task they are assigned
    if task == "Read":
        print(f"I think you should read {choose(books)}.")
    elif task == "Study":
        print(f"I think you should study for the {choose(certs)} certificate.")
    else:
        print(f"I think you should work on your {choose(projects)}.")
