import to_do_module as todo

to_do_list = []

file_path = "E:\Files\Programming\python\Learn Python\To_Do_list\_todo_save.csv"

while True:
    todo.to_do_menu()
    u_choice = int(input("Enter the number corresponding to your choice:"))
    if u_choice == 1:
        in_complete = ""
        todo.add_task(to_do_list,in_complete)
    
    elif u_choice == 2:
        todo.view_task(to_do_list)
    
    elif u_choice == 3:
        status = "Complete"
        todo.mark_status_task(to_do_list,status)

    elif u_choice == 4:
        status = "in-Complete"
        todo.mark_status_task(to_do_list,status)

    elif u_choice == 5:
        todo.task_remove(to_do_list)

    elif u_choice == 6:
        todo.edit_task(to_do_list)
    
    elif u_choice == 7:
        todo.save_todo(to_do_list,file_path)
        print("Save Successful!")

    elif u_choice == 8:
        print("-------------------------------------\nHave a Nice Day\n-------------------------------------\n")
        break
