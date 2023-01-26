def get_todo(filepath="todo1.txt"):
    """ Read a text file and return the list of
     to-do items.
    """
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_arg, filepath="todo1.txt"):
    """ Write the to-do items list in the text file. """
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)


while True:
    user_action = input("Type add, show, edit, complete or exit:")
    user_action = user_action.strip()

    if user_action.startswith('add'):
        todo = user_action[4:]
        # Files read in the todos variable
        # with open('todo1.txt', 'r') as file:
        # todos = file.readlines()

        todos = get_todo()
        todos.append(todo + '\n')

        # File read from the todos variables
        # with open('todo1.txt', 'w') as file:
        #    file.writelines(todos)

        write_todos(todos)

    elif user_action.startswith('show'):
        # Files read in the todos variable

        todos = get_todo()

        for index, item in enumerate(todos):
            item = item.strip('\n')
            row = f"{index + 1}-{item}"
            print(row)

    elif user_action.startswith('edit'):
        try:
            number = int(user_action[5:])
            number = number - 1

            todos = get_todo()

            new_todo = input("Enter new todo: ")
            todos[number] = new_todo + '\n'

            write_todos(todos)

        except ValueError:
            continue

    elif user_action.startswith('complete'):
        try:
            number = int(user_action[9:])

            todos = get_todo()

            index = number - 1
            todo_to_remove = todos[index].strip('\n')
            todos.pop(index)

            write_todos(todos)

            message = f"Todo {todo_to_remove} was removed from the list."
            print(message)
        except IndexError:
            print("There  is no item with that number.")
            continue

    elif user_action.startswith('exit'):
        break
    else:
        print("Command is not valid!")
print("Bye!")
