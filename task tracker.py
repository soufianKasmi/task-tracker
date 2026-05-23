hello=""""
1-add task 
2-update_task
3-delete_task
5-list_tasks
7-quit
the choice:   
"""
tasks=[]
def add_task(task_id):

    task_name=input("enter the task name:  ")
    "not done"
    task={
        "task name":task_name,
        "status":"todo 📋",
        "id":task_id 
    }
    tasks.append(task)
    print(f"task id {task_id}, added!")
def update_task(which_task,status):
    for i in range(len(tasks)):
        if tasks[i]['id']==which_task:
            tasks[i]['status']="in progress ⚒️" if status=='1' else "done ✅"
            print(f'task {which_task} updated!✔️')
            return
    print("task not found")
def delete_task(tasks,which_task):
    for i in range(len(tasks)):
        if tasks[i]['id']==which_task:
            tasks.remove(tasks[i])
            print(f'task {which_task} deleted!')
            return
    print("task not found")
def list_tasks(tasks):
    if not tasks: 
        print("no tasks yet! 📭")
        return
    for task in tasks:
        print(f"[{task['id']}]  {task['task name']} : {task['status']}")
def get_in(prompt):
    while True: 
        try : 
            return int(input(prompt))
        except ValueError:
            print("invalid number , please enter a valid number !")







task_id=0
while True : 
    inp = input(hello)
    if inp=='1':
        task_id+=1
        add_task(task_id)
    elif inp=='2':
        which_task=get_in("enter the task ID :")
        status=input("1-in progress⚒️ \n2-done ✅")
        if (1<=which_task<=task_id) and (status in ("1","2")):
            update_task(which_task,status)
        else: 
            print('invalid input , please enter the right id or status')
    elif inp=='3':
        which_task=get_in("the id : ")
        delete_task(tasks,which_task)
    elif inp=='5':
        list_tasks(tasks)
    elif inp=='7':
        break
    else : 
        print("invalid choice , please enter a number between 1 and 6 ")
    




