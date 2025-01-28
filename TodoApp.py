from Fcntodo import get_todos, write_todos

while True:
    userAction = input('Type add, show, edit, complete or exit: ')
    userAction = userAction.strip()

    if userAction.startswith('add'):
        gloTodos = get_todos()
        todo = (userAction[4:])
        gloTodos.append(todo +'\n')

        write_todos(gloTodos)

    elif userAction.startswith('show'):
        gloTodos = get_todos()
        for index, item in enumerate(gloTodos):
            row = f"{index + 1}-{item}"
            print(row.strip('\n'))

    elif userAction.startswith('edit'):
        gloTodos = get_todos()

        number = int(userAction[5:])
        number = number -1
        new_todo = input('enter a new todo:')
        gloTodos[number] = new_todo

        write_todos(gloTodos)
    elif userAction.startswith('complete'):
        gloTodos = get_todos()

        number = int(input("Number of todo to complete: "))
        gloTodos.pop(number -1)

        write_todos(gloTodos)
    else:
        break

