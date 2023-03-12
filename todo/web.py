import streamlit as st
import functions

todos = functions.get_todos()
st.title("My todo App")
st.subheader("This is my todo app")
st.write("This productivity")

for todo in todos:
    st.checkbox(todo)

st.text_input(label="", placeholder="add new todo...")
