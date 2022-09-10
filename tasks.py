from tempfile import NamedTemporaryFile
import csv
import os
import sys

DONE = " V"

def list(stdout=sys.stdout, filename="tasks.csv"):
    """
    List the current known tasks.
    """
    with open("tasks.csv", newline= '') as tasks_file:
        reader = csv.reader(tasks_file)
        
        for i in reader:
            if len(i) == 2:
                name, completed = i
                if not completed == 'False':
                    stdout.write(f"{name}{DONE}\n")
                else:
                    stdout.write(f"{name}\n")


def create(name, filename="tasks.csv"):
    """
    Create a new task.
    """

    with open("tasks.csv", "a") as tasks_file:
        writer = csv.writer(tasks_file)
        writer.writerow([name, False])



def complete(complete=False, stdout=sys.stdout,filename='tasks.csv'):
    """
    Mark an existing task as completed.
    """
    with (
        open("tasks.csv") as tasks_file,
        NamedTemporaryFile("w", delete=False, newline='') as new,
    ):
        reader = csv.reader(tasks_file)
        print("Current tasks:")
        
            
        for i in enumerate(reader,1):
            if len(i) == 3 :
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

    try:
        os.remove("tasks.csv")  
        os.rename(new.name, "tasks.csv")        
    except:
        os.rename(new.name, "tasks.csv")


operations = dict(create=create, complete=complete, list=list)


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