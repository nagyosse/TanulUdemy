
while True:
    user_action = input("Mit szeretnél hozzáadni(add) vagy megnézni(show) kilépés(exit):, Szerkesztés(edit):  ")
    user_action = user_action.strip()
    match user_action:
        case 'add':
            todo = input("Enter a todo: ") + "\n"

            with open('todos.txt', 'r') as file:
                todos = file.readlines()

            # file = open('todos.txt', 'r')
            # todos = file.readlines()
            # file.close()

            todos.append(todo)

            with open('todos.txt', 'w') as file:
                file.writelines(todos)

            # file = open('todos.txt', 'w')
            # file.writelines(todos)
            # file.close()

        case 'show':

            with open('todos.txt', 'r') as file:
                todos = file.readlines()
            # file = open('todos.txt', 'r')
            # todos = file.readlines()
            # file.close()
            # new_tods = [item.strip('\n') for item in todos]

            for index, item in enumerate(todos):
                item = item.strip('\n')
                row = f"{index +1}-{item}"
                print(row)
        case 'edit':
            number = int(input("Number of the todo to edit: "))
            number = number -1

            with open('todos.txt', 'r') as file:
                todos = file.readlines()

            new_todo = input("Enter new todo: ")
            todos[number] = new_todo + '\n'

            with open('todos.txt', 'w') as file:
                file.writelines(todos)

        case 'complete':
            number = int(input("Number of the todo to complete: "))

            with open('todos.txt', 'r') as file:
                todos = file.readlines()
            index = number - 1
            todo_to_remove = todos[index]
            todos.pop(index)

            with open('todos.txt', 'w') as file:
                file.writelines(todos)

            message = f"Todo {todo_to_remove} was removed from the list."
            print(message)
        case 'exit':
            break

print("Hello")