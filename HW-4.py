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
(ну і меню на це все)''')


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

