'''This module has To-Do-List funtions and elements'''

def to_do_menu():
    '''This is To-do-list main menu'''
    print("-------------------------------------\nTO-DO LIST\n-------------------------------------\n")
    print("[1] Add Task")
    print("[2] View Tasks")
    print("[3] Mark Task as Complete")
    print("[4] Mark Task as In-Complete")
    print("[5] Remove Task")
    print("[6] Edit Task")
    print("[7]Save")
    print("[8] Exit")
    print("\n-------------------------------------")

def add_task(todo_list:list,status:bool):
    '''Add tasks for do to list'''
    while True:

        print("-------------------------------------\nADD TASKS\n-------------------------------------\n")

        while True:

            get_task = input("Enter your task : ")

            todo_list.append((get_task,status))

            add_more = input("Do you like add more task(Y/N) :")

            if add_more == 'Y':
                continue
            elif add_more == 'N':
                print("Task added successfully!")
                break
        
        break

def view_task(todo_list:list):
    '''View tasks in the list'''
    while True:
        print("-------------------------------------\nView TASKS\n-------------------------------------\n")
        i = 1
        for items in todo_list:
            task = items[0]
            status = items[1]

            print("Task",i,"\t:",task, "\t|",status)

            i += 1

        print("\n-------------------------------------")

        u_input = input("Enter [b] to go back to the main menu.")

        if u_input == 'b':
            break

def mark_status_task(todo_list:list,status:str):
    while True:
        print("-------------------------------------\nMARK TASK AS",status,"\n-------------------------------------\n")

        while True:
            task_num = int(input("Enter the number to the task:"))
            task_and_status = todo_list[task_num-1]
            task = task_and_status[0]
            todo_list[task_num-1] = (task,status)
            print("Task ",task_num," marked as",status)
            
            u_input = input("Do you like continue(Y/N) :")

            if u_input == 'Y':
                continue
            elif u_input == 'N':
                break

        break

def task_remove(todo_list:list):
    while True:
        print("-------------------------------------\nRemove Task\n-------------------------------------\n")

        while True:
            task_num = int(input("Enter the number to the Remove task:"))
            task = todo_list[task_num-1]
            todo_list.remove(task)
            print("Task ",task_num,"Removed.")

            u_input = input("Do you like continue(Y/N) :")

            if u_input == 'Y':
                continue
            elif u_input == 'N':
                break

        break

def edit_task(todo_list:list):
    while True:
        print("-------------------------------------\nEdit Task\n-------------------------------------\n")

        while True:
            task_num = int(input("Enter the number to the Edit task:"))
            task = todo_list[task_num-1]
            print(task)
            edit_task = input("Enter updated task:")
            todo_list[task_num-1] = (edit_task,'')

            u_input = input("Do you like continue(Y/N) :")

            if u_input == 'Y':
                continue
            elif u_input == 'N':
                break

        break

#save todo list function
def save_todo(todolist:list):
    pass
            
            








          

        
    
