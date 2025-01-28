def get_todos():
    with open('report.txt', 'r') as file:
        todos = file.readlines()
        return todos
def write_todos(todolst, Filepath='report.txt'):
    with open(Filepath, 'w') as file:
        file.writelines(todolst)