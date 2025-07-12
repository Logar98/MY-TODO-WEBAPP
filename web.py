import streamlit as st
import functions as fs

todos=fs.reading()
def add_todo():
    todo=st.session_state["new_todo"]+"\n"
    todos.append(todo)
    fs.writing(todos)

st.title("MY TODO APP")
st.subheader("This will help you improve your productivity")
st.write("This is your list of todos")

for i,todo in enumerate(todos):
    checkbox=st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(i)
        fs.writing(todos)
        del st.session_state[todo]
        st.rerun()
    else:
        continue

st.text_input(label="", placeholder="Enter a todo...", 
              on_change=add_todo, key="new_todo")