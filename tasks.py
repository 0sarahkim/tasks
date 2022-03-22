#!/usr/bin/env python3
"""
A simple task manager.

For the purposes of our exercise we store tasks in a file which we'll
call tasks.csv (a CSV file). We'll talk more later about other ways to
store state which are more robust.
"""
from tempfile import NamedTemporaryFile
import csv
import os


DONE = " V"


def list():
    """
    List the current known tasks.
    """
    with open("tasks.csv", newline= '') as tasks_file:
        reader = csv.reader(tasks_file)
        for i in reader:
            if len(i) == 2:
                name, completed = i
                if not completed == 'False':
                    print(f"{name}{DONE}")
                else:
                    print(f"{name}{''}")
    

def create(name):
    """
    Create a new task.
    """
    rows = []
    with open("tasks.csv", "r") as tasks_file:
        for row in csv.reader(tasks_file):
            if len(row) > 0:  
                rows.append(row[0])

    with open("tasks.csv", "a") as tasks_file:
        writer = csv.writer(tasks_file)
        if name not in rows:
            writer.writerow([name, False])
        else:
           print(f"{name}{' already exists in the list'}")


def complete():
    """
    Mark an existing task as completed.
    """
    with (
        open("tasks.csv") as tasks_file,
        NamedTemporaryFile("w", delete=False) as new,
    ):
        reader = csv.reader(tasks_file)
        print("Current tasks:")
        for i in enumerate(reader,1):
            if len(i) == 3:
                print(id, name, completed)

        to_complete = int(input("task ID?> "))
        writer = csv.writer(new)
        print(writer)
        tasks_file.seek(0)

        for i in enumerate(reader,1):
            if len(i[1]) == 2:
                print(i)
                id, name, completed = i[0], i[1][0], i[1][1]
                if id == to_complete:
                    writer.writerow([name, True])
                else:
                    print(writer.writerow([name, completed]))


    os.rename(new.name ,"tasks.csv")


operations = dict(
    create=create,
    complete=complete,
    list=list,
)


def main():
    print("Enter a command [create, list, complete].")
    while True:
        line = input("-> ").strip()
        if not line:
            return

        operation, *args = line.split()
                
        fn = operations.get(operation)
        fn(*args)

if __name__ == "__main__":
    main()


