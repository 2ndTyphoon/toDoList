def add_task(file_path):
    with open(file_path, "a") as file:
        file.write(input(f'\n' "#Какую задачу добавить?: ") + "\n")
        print(f"#Задача добавлена")
    check_tasks(file_path)


def remove_task(file_path):
    #check_tasks(file_path)

    with open(file_path, "r") as file:
        lines = file.readlines()

    print(len(lines))

    if len(lines) == 0:
        print(f"Пока что тут пусто..." '\n'
              f"Давайте что-нибудь добавим!")
    else:
        remove_line = int(input(f"#Какую задачу удалить?: "))
        if remove_line < 1 or remove_line > len(lines) + 1:
            print(f"#Неверная задача для удаления, попробуйте ещё раз")
        return

        del lines[remove_line - 1]

        with open(file_path, "w") as file:
            file.writelines(lines)

        print(f"#Задача удалена")

        check_tasks(file_path)


def check_tasks(file_path):
    with open(file_path, "r") as file:
        lines = file.readlines()

        if not lines:
            print(f"Пока что тут пусто..." '\n'
              f"Давайте что-нибудь добавим!")
        else:
            with open(file_path, "r") as file:
                whatToDo = file.read()
            print(f'\n' "#Актуальный список задач:")
            print(f"{whatToDo}")


file_path = "tasks.txt"

print(f"#Для перехода к задачи, введите её номер" '\n'
      f"#1. Проверить список дел" '\n'
      f"#2. Добавить новую задачу" '\n'
      f"#3. Удалить существующую задачу" '\n'
      f"#4. Выход" '\n')

user_input = ""

while user_input != 4:
    user_input = int(input("#Что будем делать?: "))
    if user_input == 1:
        check_tasks(file_path)
    elif user_input == 2:
        add_task(file_path)
    elif user_input == 3:
        remove_task(file_path)