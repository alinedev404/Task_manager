from termcolor import colored
import os
import time

user_choice = ""

with open("tasks.txt", "a"):
    pass
with open("tasks_complete.txt", "a"):
    pass

def show_task(file_name):
    count = 1
    with open(file_name, "r") as file:
        while True:
            task = file.readline()
            if task == "":
                break
            print(f"{count} . {task}", end = "")
            count += 1
def delete_item(file_name, task_number):
    with open(file_name, "r") as file:
        tasks = file.readlines()
        delete_task = tasks.pop(int(task_number) - 1)
    with open(file_name, "w") as file:
        for task in tasks:
            file.write(task)
    return delete_task
def ux (sub1, sub2, sub3, t):
    while True:
        if t == 1:
            user_choice = input(f"{sub1} . Return to menu\n{sub2} . Exit\nEnter: ")

            if user_choice in (sub1, sub2):
                break
            else:
                os.system("cls")
                print(colored("Invalid Input", "red"))
                time.sleep(1)
        elif t == 2:
            user_choice = input(f"{sub1} . Return to menu\n{sub2} . Exit\n{sub3} . Clear\nEnter: ")

            if user_choice in (sub1, sub2, sub3):
                if user_choice == "3":
                    while True:
                        r = input("Do you want to clear all complete task\n1 . Yes\n2 . No\nEnter: ")
                        if r in ("1", "2"):
                            if r == "1":
                                with open("tasks_complete.txt", "w") as file:
                                    file.write("")
                                user_choice = "1"
                            elif r == "2":
                                break
                            break
                        else:
                            os.system("cls")
                            print(colored("Invalid Input", "red"))
                            time.sleep(1)
                break
            else:
                os.system("cls")
                print(colored("Invalid Input", "red"))
                time.sleep(1)
    return user_choice
def sub_title(sub):
    os.system("cls")
    print(f"======================== << {sub} >> ========================")
def count_tasks(file_name):
    count = 0
    with open(file_name, "r") as file:
        for task in file:
            count += 1
    return count
def confirm_action(action_type, task_number):
    while True:
        user_choice = input("\nAre you sure ???\n1 . Yes\n2 . No\n3 . Exit\nEnter: ")
        is_number = user_choice.isdigit()
        if is_number == True and user_choice == "1":
            if action_type == 1:
                delete_task = delete_item("tasks.txt", task_number)
                with open("tasks_complete.txt", "a") as file:
                    file.write(delete_task)
                    os.system("cls")
                    print(colored("Task complete\n", "green"))
                    time.sleep(1)
                    break
            elif action_type == 2:
                delete_item("tasks.txt", task_number)
                os.system("cls")
                print(colored("Task deleted\n", "red"))
                time.sleep(1)
                break
        elif is_number == True and user_choice in ("2", "3"):
            break
        else:
            os.system("cls")
            print(colored("Invalid Input", "red"))
            time.sleep(1)
    return user_choice
def task_action(title, action, confirm_type):
    user_choice = ""
    while True:
        if user_choice in ("1", "3"):
            break
        sub_title(f" {title} ")
        show_task("tasks.txt")
        print()
        count = count_tasks("tasks.txt")
        task_number = input(f"Which task do you want to {action}: ")
        is_number = task_number.isdigit()

        if is_number == True and 1 <= int(task_number)  <= count:
            user_choice = confirm_action(confirm_type, task_number)
            break
        else:
            os.system("cls")
            print(colored("Invalid input", "red"))
            time.sleep(1)

while True:
    if user_choice in ("2", "3"):
        break
    while True:
        os.system("cls")
        choice = input("======================== << TASK   MANAGER >> ========================\n1 . Add Task\n2 . My Tasks\n3 . Mark as Done\n4 . Delete Task\n5 . Completed Tasks\n6 . Exit\n\nEnter: ")

        if choice in ("1", "2", "3", "4", "5", "6"):
            break
        else:
            os.system("cls")
            print(colored("Invalid Input", "red"))
            time.sleep(1)

    if choice == "1":
        sub_title("ADD  TASK")
        while True:
            task_text = input("Enter Task: ")
            if task_text.strip() == "":
                os.system("cls")
                print(colored("Invalid Input", "red"))
                time.sleep(1)
            else:
                with open("tasks.txt", "a") as file:
                    file.write(f"{task_text}\n")
                os.system("cls")
                print(colored("Task added\n", "green"))
                time.sleep(1)
                break
    elif choice == "2":
        sub_title(" MY TASK ")
        show_task("tasks.txt")
        print()
        user_choice = ux("1", "2", "3", 1)
    elif choice == "3":
        task_action("MARK AS DONE", "complete", 1)
    elif choice == "4":
        task_action("DELETE TASK", "delete", 2)
    elif choice == "5":
        sub_title(" COMPLETED TASK ")
        with open("tasks_complete.txt", "a") as file:
            file.write("")
        show_task("tasks_complete.txt")
        print()
        user_choice = ux("1", "2", "3", 2)
    elif choice == "6":
        break