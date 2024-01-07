todo_list = []
counter = 0

while 1:
    print("Enter a todo, like add an item, remove an item:")
    if counter:
        local_counter = 1
        for task in todo_list:
            print("[" + str(local_counter) + "] " + str(task))
            local_counter += 1
    action = input()



    if action == 'add':
        task_input = input("Please enter an item to be added :")
        #task = " ".join(task_input.split(" ")[0: len(task_input)])
        todo_list.append(task_input)
        counter += 1


    if action == 'remove':
        id = input("Please enter an id to be deleted :")
        item_to_delete = todo_list[int(id)-1]

        if item_to_delete:
            todo_list.remove(item_to_delete)
            counter -= 1

