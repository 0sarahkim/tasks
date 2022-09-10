from tempfile import TemporaryFile
import os
import tasks


# Tasks are always marked complete (showing a green check mark) -- fix that so that they are not complete when created, and only marked complete once the `complete` routine is run

#Notice that the task IDs start at 0. Fix this so they start at 1, which is a bit more user friendly.

#Show an error if someone tries to `complete` a task which is already completed, or filter it out entirely from the list of completable tasks

"""
1.Create 2 tasks, and list them (they should not be complete when created)
"""
def test_create_and_list():
    tasks.create("Laundry", filename="tests.csv")
    tasks.create("Dishes", filename="tests.csv")
    
    with TemporaryFile("w+") as stdout:
        tasks.list(stdout=stdout, filename="tests.csv")
        stdout.seek(0)
        contents = stdout.readlines()
    os.remove("tasks.csv")
    assert contents == ["Laundry\n", "Dishes\n"]

"""
2. Show an error if someone tries to `complete` a task which is already completed, or filter it out entirely from the list of completable tasks
"""    

def test_complete():
    tasks.create("Laundry", filename="tests.csv")
    
    with TemporaryFile("w+") as stdout:
        tasks.complete(stdout=stdout, filename="tests.csv")
        stdout.seek(0)
        contents = stdout.readlines()
    os.remove("tasks.csv")
    assert contents == ["Current tasks:\n","1 Laundry False\n"]
    