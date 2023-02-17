import functions
import PySimpleGUI as sg


label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Enter todo", key="todo")
add_button = sg.Button("add")

window = sg.Window('My to-do app', layout=[[label], [input_box, add_button]])

while True:
    event, value = window.read()
    print(event)
    print(value)
    match event:
        case "add":
            todos = functions.get_todo()
            new_todo = value["todo"] + "\n"
            todos.append(new_todo)
            functions.write_todos(todos)
        case sg.WIN_CLOSED:
            break



window.close()
