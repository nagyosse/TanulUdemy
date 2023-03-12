import streamlit as st
import functions

todos = functions.get_todos()
def add_todo():
    todo = st.session_state["new_todo"]
    todos.append(todo)
    functions.write_todos(todos)


st.title("My todo App")
st.subheader("This is my todo app")
st.write("This productivity")

for todo in todos:
    st.checkbox(todo)

st.text_input(label="", placeholder="add new todo...",
              on_change=add_todo, key='new_todo')

st.session_state