FILEPATH="todos.txt"
def reading(Filepath=FILEPATH):
    with open(Filepath, "r") as f:
            local_todos = f.readlines()
    return local_todos 

def writing(value, Filepath=FILEPATH):
       with open(Filepath, "w") as file:
         return  file.writelines(value)
