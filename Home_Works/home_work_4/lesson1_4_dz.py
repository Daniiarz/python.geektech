todos = []


while True:
    action = input("Выберите действие: Y) Добавить задачу V) Показать задачи C) Отметить выполненные ")
    if action == "Y":
        todo = input("Задача: ")
        deadline = input("Дэдлайн: ")
        data = input("Добавлено: ")
        completed = False
        todos.append([todo, deadline, data, completed])   #список в списке
        print("Задача добавлена!")
    elif action == "V":
        print()
        if len(todos) == 0:
            print("Нет задач!")
        print("Задача       Дэдлайн       Дата добавления       Выполненные")
        for pos, i in enumerate(todos):    # позиция, нумерация
            print(pos, i[0], i[1], i[2], i[3])
        print()
    elif action == "С":
        index = int(input("Отметить задачу "))
        todos[index][3] = True  # по индексу
        print(todos)
    else:
        print("Выберете правильный вариант!\n")








