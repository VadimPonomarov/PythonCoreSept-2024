print('''
1) Є ось такий файл... 
ваша задача записати в новий файл тільки email'ли з доменом gmail.com 
(Хеш то що з ліва записувати не потрібно)

with open("emails.txt", "r") as f:
    emails = f.readlines()

with open("emails_gmail.txt", "w") as f:
    for email in emails:
        splt = email.split()[-1]
        if splt.find("@gmail.com") != -1:
            f.write(splt + "\n")
''')

with open("emails.txt", "r") as f:
    emails = f.readlines()

with open("emails_gmail.txt", "w") as f:
    for email in emails:
        splt = email.split()[-1]
        if splt.find("@gmail.com") != -1:
            f.write(splt + "\n")

print('''
2) Створити записну книжку покупок:
- у покупки повинна бути id, назва і ціна
- всі покупки зберігаємо в файлі
з функціоналу:
 * вивід всіх покупок
 * має бути змога додавати покупку в книгу
* має бути змога шукати по будь якому полю покупку
* має бути змога показати найдорожчу покупку
* має бути можливість видаляти покупку по id

class ShopBook:
    @staticmethod
    def all_clear():
        with open("shop_book.txt", "w") as f:
            f.write("")
    @staticmethod
    def add_item(id, name, price):
        with open("shop_book.txt", "a") as f:
            f.write(f"{id}: {name} - {price}\t")

    @staticmethod
    def get_all():
        with open("shop_book.txt", "r") as f:
            items = f.readlines()
            return items

    @staticmethod
    def get_expensive_item():
        max_price = 0
        expensive_item = None
        with open("shop_book.txt", "r") as f:
            items = f.readlines()
            for item in items:
                if item.strip():
                    price = float(item.split()[-1])
                    if price > max_price:
                        max_price = price
                        expensive_item = item
        return expensive_item

    @staticmethod
    def delete_item(id: str | int):
        id = str(id)
        with open("shop_book.txt", "r") as f:
            items = f.readlines()
        with open("shop_book.txt", "w") as f:
            for item in items:
                if item.split()[0] != id:
                    f.write(item)
        return ShopBook.get_all()

# Пример использования
ShopBook.all_clear()
ShopBook.add_item("1", "apple", "10")
ShopBook.add_item("2", "banana", "20")
ShopBook.add_item("3", "orange", "30")
ShopBook.add_item("4", "kiwi", "40")
ShopBook.add_item("5", "grape", "50")

get_all= ShopBook.get_all()
for i in get_all:
    print(i)
print("#"*100)
print(ShopBook.get_expensive_item())
print("#"*100)
all_after_delete = ShopBook.delete_item(3)
for i in all_after_delete:
    print(i)
    
''')


class ShopBook:
    @staticmethod
    def all_clear():
        with open("shop_book.txt", "w") as f:
            f.write("")
    @staticmethod
    def add_item(id, name, price):
        with open("shop_book.txt", "a") as f:
            f.write(f"{id}: {name} - {price}\t")

    @staticmethod
    def get_all():
        with open("shop_book.txt", "r") as f:
            items = f.readlines()
            return items

    @staticmethod
    def get_expensive_item():
        max_price = 0
        expensive_item = None
        with open("shop_book.txt", "r") as f:
            items = f.readlines()
            for item in items:
                if item.strip():
                    price = float(item.split()[-1])
                    if price > max_price:
                        max_price = price
                        expensive_item = item
        return expensive_item

    @staticmethod
    def delete_item(id: str | int):
        id = str(id)
        with open("shop_book.txt", "r") as f:
            items = f.readlines()
        with open("shop_book.txt", "w") as f:
            for item in items:
                if item.split()[0] != id:
                    f.write(item)
        return ShopBook.get_all()

ShopBook.all_clear()
ShopBook.add_item("1", "apple", "10")
ShopBook.add_item("2", "banana", "20")
ShopBook.add_item("3", "orange", "30")
ShopBook.add_item("4", "kiwi", "40")
ShopBook.add_item("5", "grape", "50")

get_all= ShopBook.get_all()
for i in get_all:
    print(i)
print("#"*100)
print(ShopBook.get_expensive_item())
print("#"*100)
all_after_delete = ShopBook.delete_item(3)
for i in all_after_delete:
    print(i)

print('''
(ну і меню на це все)''')

# while True:
#     print('''
#     1) Вивести всі покупки
#     2) Додати покупку
#     3) Пошук покупки
#     4) Вивести найдорожчу покупку
#     5) Видалити покупку
#     6) Вихід''')
#     val = input("Введіть номер завдання: ")
#     if val == "1":
#         get_all = ShopBook.get_all()
#         for i in get_all:
#             print(i)
#     elif val == "2":
#         id = input("Введіть id: ")
#         name = input("Введіть назву: ")
#         price = input("Введіть ціну: ")
#         ShopBook.add_item(id, name, price)
#     elif val == "3":
#         id = input("Введіть id: ")
#         print(ShopBook.delete_item(id))
#     elif val == "4":
#         print(ShopBook.get_expensive_item())
#     elif val == "5":
#         ShopBook.all_clear()
#     elif val == "6":
#         print("Выход из программы...")

print('''
Є ось такий список:
data = [
    [
        {"id": 1110, "field": {}},
        {"id": 1111, "field": {}},
        {"id": 1112, "field": {}},
        {"id": 1113, "field": {}},
        {"id": 1114, "field": {}},
        {"id": 1115, "field": {}},
    ],
    [
        {"id": 1110, "field": {}},
        {"id": 1120, "field": {}},
        {"id": 1122, "field": {}},
        {"id": 1123, "field": {}},
        {"id": 1124, "field": {}},
        {"id": 1125, "field": {}},

    ],
    [
        {"id": 1130, "field": {}},
        {"id": 1131, "field": {}},
        {"id": 1122, "field": {}},
        {"id": 1132, "field": {}},
        {"id": 1133, "field": {}},

    ]
]

потрібно брати по черзі с кожного списку id і класти в список res, якщо таке значення вже є в результуючому списку то брати наступне з того ж підсписку

з даним списком мае вийти ось такий результат:
res = [1110, 1120, 1130, 1111, 1122, .......]

def get_id(data: list):
    res = []
    while len(data) > 0:
        current = data.pop(0)
        for i, val in enumerate(current):
            if val["id"] not in res:
                res.append(val["id"])
                del current[i]
                if len(current) != 0:
                    data.append(current)
                break
    print(res)

get_id(data)
''')

data = [
    [
        {"id": 1110, "field": {}},
        {"id": 1111, "field": {}},
        {"id": 1112, "field": {}},
        {"id": 1113, "field": {}},
        {"id": 1114, "field": {}},
        {"id": 1115, "field": {}},
    ],
    [
        {"id": 1110, "field": {}},
        {"id": 1120, "field": {}},
        {"id": 1122, "field": {}},
        {"id": 1123, "field": {}},
        {"id": 1124, "field": {}},
        {"id": 1125, "field": {}},

    ],
    [
        {"id": 1130, "field": {}},
        {"id": 1131, "field": {}},
        {"id": 1122, "field": {}},
        {"id": 1132, "field": {}},
        {"id": 1133, "field": {}},

    ]
]
def get_id(data: list):
    res = []
    while len(data) > 0:
        current = data.pop(0)
        for i, val in enumerate(current):
            if val["id"] not in res:
                res.append(val["id"])
                del current[i]
                if len(current) != 0:
                    data.append(current)
                break
    print(res)

get_id(data)