import json
import csv
import datetime


def main_menu():
    print("Добро пожаловать в Персональный помощник!")
    print("Выберите действие:")
    print("1. Управление заметками")
    print("2. Управление задачами")
    print("3. Управление контактами")
    print("4. Управление финансовыми записями")
    print("5. Калькулятор")
    print("6. Выход")

    choice = input("Введите номер действия: ")

    if choice == '1':
        manage_notes()
    elif choice == '2':
        manage_tasks()
    elif choice == '3':
        manage_contacts()
    elif choice == '4':
        manage_finances()
    elif choice == '5':
        calculator()
    elif choice == '6':
        print("Выход из программы.")
    else:
        print("Неверный ввод, попробуйте снова.")
        main_menu()


class Note:
    def __init__(self, id, title, content, timestamp):
        self.id = id
        self.title = title
        self.content = content
        self.timestamp = timestamp

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'content': self.content,
            'timestamp': self.timestamp
        }


class Task:
    def __init__(self, id, title, description, done, priority, due_date):
        self.id = id
        self.title = title
        self.description = description
        self.done = done
        self.priority = priority
        self.due_date = due_date

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'done': self.done,
            'priority': self.priority,
            'due_date': self.due_date
        }


class Contact:
    def __init__(self, id, name, phone, email):
        self.id = id
        self.name = name
        self.phone = phone
        self.email = email

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'phone': self.phone,
            'email': self.email
        }


class FinanceRecord:
    def __init__(self, id, amount, category, date, description):
        self.id = id
        self.amount = amount
        self.category = category
        self.date = date
        self.description = description

    def to_dict(self):
        return {
            'id': self.id,
            'amount': self.amount,
            'category': self.category,
            'date': self.date,
            'description': self.description
        }


# Функции для работы с данными

def load_data(filename, cls):
    try:
        with open(filename, "r") as file:
            return [cls(**item) for item in json.load(file)]
    except FileNotFoundError:
        return []


def save_data(filename, data):
    with open(filename, "w") as file:
        json.dump([item.to_dict() for item in data], file, indent=4)


def export_to_csv(data, filename):
    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=data[0].to_dict().keys())
        writer.writeheader()
        for row in data:
            writer.writerow(row.to_dict())


def import_from_csv(filename, cls):
    data = []
    with open(filename, mode='r', newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            data.append(cls(**row))
    return data



def create_note():
    title = input("Введите заголовок заметки: ")
    content = input("Введите содержимое заметки: ")
    timestamp = datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")
    note = Note(len(load_data("notes.json", Note)) + 1, title, content, timestamp)
    notes = load_data("notes.json", Note)
    notes.append(note)
    save_data("notes.json", notes)
    print("Заметка добавлена!")


def view_notes():
    notes = load_data("notes.json", Note)
    for note in notes:
        print(f"ID: {note.id} | Заголовок: {note.title} | Дата: {note.timestamp}")


def manage_notes():
    print("Управление заметками:")
    print("1. Создать новую заметку")
    print("2. Просмотр заметок")
    print("3. Экспорт заметок в CSV")
    print("4. Вернуться в главное меню")
    choice = input("Выберите действие: ")

    if choice == '1':
        create_note()
    elif choice == '2':
        view_notes()
    elif choice == '3':
        export_to_csv(load_data("notes.json", Note), "notes.csv")
    elif choice == '4':
        main_menu()
    else:
        print("Неверный выбор, попробуйте снова.")
        manage_notes()


def create_task():
    title = input("Введите название задачи: ")
    description = input("Введите описание задачи: ")
    priority = input("Установите приоритет (Высокий, Средний, Низкий): ")
    due_date = input("Введите срок выполнения задачи (ДД-ММ-ГГГГ): ")
    task = Task(len(load_data("tasks.json", Task)) + 1, title, description, False, priority, due_date)
    tasks = load_data("tasks.json", Task)
    tasks.append(task)
    save_data("tasks.json", tasks)
    print("Задача добавлена!")


def view_tasks():
    tasks = load_data("tasks.json", Task)
    for task in tasks:
        print(
            f"ID: {task.id} | Задача: {task.title} | Статус: {'Выполнена' if task.done else 'Не выполнена'} | Приоритет: {task.priority} | Срок: {task.due_date}")


def manage_tasks():
    print("Управление задачами:")
    print("1. Создать новую задачу")
    print("2. Просмотр задач")
    print("3. Экспорт задач в CSV")
    print("4. Вернуться в главное меню")
    choice = input("Выберите действие: ")

    if choice == '1':
        create_task()
    elif choice == '2':
        view_tasks()
    elif choice == '3':
        export_to_csv(load_data("tasks.json", Task), "tasks.csv")
    elif choice == '4':
        main_menu()
    else:
        print("Неверный выбор, попробуйте снова.")
        manage_tasks()


def create_contact():
    name = input("Введите имя контакта: ")
    phone = input("Введите номер телефона: ")
    email = input("Введите email: ")
    contact = Contact(len(load_data("contacts.json", Contact)) + 1, name, phone, email)
    contacts = load_data("contacts.json", Contact)
    contacts.append(contact)
    save_data("contacts.json", contacts)
    print("Контакт добавлен!")


def view_contacts():
    contacts = load_data("contacts.json", Contact)
    for contact in contacts:
        print(f"ID: {contact.id} | Имя: {contact.name} | Телефон: {contact.phone} | Email: {contact.email}")


def manage_contacts():
    print("Управление контактами:")
    print("1. Добавить новый контакт")
    print("2. Просмотр контактов")
    print("3. Экспорт контактов в CSV")
    print("4. Вернуться в главное меню")
    choice = input("Выберите действие: ")

    if choice == '1':
        create_contact()
    elif choice == '2':
        view_contacts()
    elif choice == '3':
        export_to_csv(load_data("contacts.json", Contact), "contacts.csv")
    elif choice == '4':
        main_menu()
    else:
        print("Неверный выбор, попробуйте снова.")
        manage_contacts()



def create_finance_record():
    amount = float(input("Введите сумму операции: "))
    category = input("Введите категорию операции: ")
    date = input("Введите дату операции (ДД-ММ-ГГГГ): ")
    description = input("Введите описание операции: ")
    finance = FinanceRecord(len(load_data("finance.json", FinanceRecord)) + 1, amount, category, date, description)
    finances = load_data("finance.json", FinanceRecord)
    finances.append(finance)
    save_data("finance.json", finances)
    print("Финансовая запись добавлена!")


def view_finances():
    finances = load_data("finance.json", FinanceRecord)
    for finance in finances:
        print(
            f"ID: {finance.id} | Сумма: {finance.amount} | Категория: {finance.category} | Дата: {finance.date} | Описание: {finance.description}")


def manage_finances():
    print("Управление финансовыми записями:")
    print("1. Добавить новую финансовую запись")
    print("2. Просмотр финансовых записей")
    print("3. Экспорт финансовых записей в CSV")
    print("4. Вернуться в главное меню")
    choice = input("Выберите действие: ")

    if choice == '1':
        create_finance_record()
    elif choice == '2':
        view_finances()
    elif choice == '3':
        export_to_csv(load_data("finance.json", FinanceRecord), "finance.csv")
    elif choice == '4':
        main_menu()
    else:
        print("Неверный выбор, попробуйте снова.")
        manage_finances()



def calculator():
    while True:
        print("Калькулятор:")
        print("1. Сложение")
        print("2. Вычитание")
        print("3. Умножение")
        print("4. Деление")
        print("5. Выход")

        choice = input("Выберите операцию: ")

        if choice == '5':
            main_menu()
            break

        try:
            num1 = float(input("Введите первое число: "))
            num2 = float(input("Введите второе число: "))

            if choice == '1':
                print(f"Результат: {num1 + num2}")
            elif choice == '2':
                print(f"Результат: {num1 - num2}")
            elif choice == '3':
                print(f"Результат: {num1 * num2}")
            elif choice == '4':
                if num2 == 0:
                    print("Ошибка: деление на ноль!")
                else:
                    print(f"Результат: {num1 / num2}")
            else:
                print("Неверный выбор, попробуйте снова.")
        except ValueError:
            print("Ошибка: введите корректные числа.")


if __name__ == "__main__":
    main_menu()
