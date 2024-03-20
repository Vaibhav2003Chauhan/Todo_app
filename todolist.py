import tabulate
tasks_list=[]  # empty list for the task

# each task is stored in form of dictonaryand that dictonary is stored in the form of list

'''task={

    "id":"total_task",
    "description":"string of varible length",
    "status":"pending,Completed"
}'''

total_task=1 # initially the first task to be considered 

print("***********************************************************")
print("           Welcome to the Todo List using Python           ")
print("************************************************************")
print()

print("Please !! Press 1 to add a new task")
print("Please !! Press 2 to delete a task")
print("Please !! Press 3 to change status of task")
print("Please !! Press 4 to display all tasks")

print()

user_input=input("Please Enter a Choice or press E for exit of program: ").strip()

# print(user_input)

while user_input !="e" :
    
    if user_input=="1":
        #Adding of the task need to be done in this phase
        current_task={
            "id":total_task,
            "desc":"",
            "status":"Pending"
        }
        task_description=input("Enter the task description: ")
        total_task=total_task+1
        current_task["desc"]=task_description
        tasks_list.append(current_task)

        # print(tasks_list)
        print()
        print("Task Added sucessfully ")
        print()
    elif user_input=="2":
        # Deletion of task logic 
        task_id=int(input("Enter the Task id to be Deleted: ").strip())
        founded=False
        for task in tasks_list:
            if task["id"]==task_id:
                tasks_list.remove(task)
                founded=True
                break
        print()

        if not founded:
            print(f"Task with id {task_id} not found") 
        else:
            print("Task deleted successfully")

            print()      

    elif user_input=="3":
        #updating Status of the program
        task_id=int(input("Enter id of task to mark as complete : ").strip())

        task_index=-1

        # Search task wth task_id in tasks list
        for index,task in enumerate(tasks_list):

            if task["id"]==task_id:
                task_index=index
                break

        print()

        if task_index == -1:
            print(f"Task with id {task_id} not found") 
        else:
            tasks_list[task_index]["status"]="completed"

            print("Task updated successfully")

        print()
    elif user_input=="4":
        # printing the whole dictonary
        # for task in tasks_list:
        #     for key,value in task.items():
        #         print(f'{key} : {value}')
        
    
        if len(tasks_list) == 0:
            print("The list is empty please enter up task")
            print()
        else:
            
            header = tasks_list[0].keys()
            rows =  [x.values() for x in tasks_list]
            print(tabulate.tabulate(rows, header,tablefmt='grid'))
            print()
           
    elif user_input=="E":
        # exitimng Program 
        break
       

    user_input=input("Please Enter a Choice or press E for exit of program: ").strip()