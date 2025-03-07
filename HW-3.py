import abc
from abc import abstractmethod

print('''
Створити клас Rectangle:
-він має приймати дві сторони x,y
-описати поведінку на арифметични методи:
  + сумма площин двох екземплярів ксласу
  - різниця площин двох екземплярів ксласу
  == площин на рівність
  != площин на не рівність
  >, < меньше більше
  при виклику метода len() підраховувати сумму сторін

  ###############################################################################
''')


class Rectangle:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y
        self.area = x * y

    def __add__(self, other: "Rectangle"):
        return self.area + other.area

    def __sub__(self, other: "Rectangle"):
        return self.area - other.area

    def __eq__(self, other: "Rectangle"):
        return self.area == other.area

    def __ne__(self, other: "Rectangle"):
        return self.area != other.area

    def __gt__(self, other: "Rectangle"):
        return self.area > other.area

    def __lt__(self, other: "Rectangle"):
        return self.area < other.area

    def __len__(self):
        return (self.x + self.y) * 2


rect1 = Rectangle(3, 4)
rect2 = Rectangle(2, 5)

print('''
rect1 = Rectangle(3, 4)
rect2 = Rectangle(2, 5)
''')

print("sum", rect1 + rect2)
print("sub", rect1 - rect2)
print("eq", rect1 == rect2)
print("ne", rect1 != rect2)
print("gt", rect1 > rect2)
print("lt", rect1 < rect2)
print("len", len(rect1))

print('''
створити класс Human (name, age)

class Human:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
###############################################################################
''')


class Human:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age


print('''
створити два класси Prince и Cinderella які наслідуються від Human:
у попелюшки мае бути ім'я, вік, розмір нонги
у принца має бути ім'я, вік, та розмір знайденого черевичка, а також метод котрий буде приймати список попелюшок, та шукати ту саму

в класі попелюшки має бути count який буде зберігати кількість створених екземплярів классу
також має бути метод классу який буде виводити це значення
 
 
 class Cinderella(Human):
    def __init__(self, name: str, age: int, size: int):
        super().__init__(name, age)
        self.size = size

    def __str__(self):
        return f"{self.name} {self.age} {self.size}"

    def __repr__(self):
        return self.__str__()


class Prince(Human):
    def __init__(self, name: str, age: int, size: int):
        super().__init__(name, age)
        self.size = size

    def __str__(self):
        return f"{self.name} {self.age} {self.size}"

    def __repr__(self):
        return self.__str__()

    def find_cinderella(self, cinderellas: list[Cinderella]):
        for cinderella in cinderellas:
            if cinderella.size == self.size:
                return cinderella


sinderellas = [
    Cinderella("Sinderella-1", 100, 39),
    Cinderella("Sinderella-2", 26, 43),
    Cinderella("Sinderella-3", 38, 38),
    Cinderella("Sinderella-4", 18, 35), ]

prince = Prince("Prince-1", 18, 35)

print(prince.find_cinderella(sinderellas))

''')


class Cinderella(Human):
    def __init__(self, name: str, age: int, size: int):
        super().__init__(name, age)
        self.size = size

    def __str__(self):
        return f"{self.name} {self.age} {self.size}"

    def __repr__(self):
        return self.__str__()


class Prince(Human):
    def __init__(self, name: str, age: int, size: int):
        super().__init__(name, age)
        self.size = size

    def __str__(self):
        return f"{self.name} {self.age} {self.size}"

    def __repr__(self):
        return self.__str__()

    def find_cinderella(self, cinderellas: list[Cinderella]):
        for cinderella in cinderellas:
            if cinderella.size == self.size:
                return cinderella


sinderellas = [
    Cinderella("Sinderella-1", 100, 39),
    Cinderella("Sinderella-2", 26, 43),
    Cinderella("Sinderella-3", 38, 38),
    Cinderella("Sinderella-4", 18, 35), ]

prince = Prince("Prince-1", 18, 35)

print(prince.find_cinderella(sinderellas))


print('''
1) Створити абстрактний клас Printable який буде описувати абстрактний метод print()
2) Створити класи Book та Magazine в кожного в конструкторі змінна name, та який наслідуются від класу Printable
3) Створити клас Main в якому буде:
- змінна класу printable_list яка буде зберігати книжки та журнали
- метод add за допомогою якого можна додавати екземпляри класів в список і робити перевірку чи то що передають є класом Book або Magazine инакше ігрнорувати додавання
- метод show_all_magazines який буде виводити всі журнали викликаючи метод print абстрактного классу
- метод show_all_books який буде виводити всі книги викликаючи метод print абстрактного классу

Приклад:

Main.add(Magazine('Magazine1'))
    Main.add(Book('Book1'))
    Main.add(Magazine('Magazine3'))
    Main.add(Magazine('Magazine2'))
    Main.add(Book('Book2'))

    Main.show_all_magazines()
    print('-' * 40)
    Main.show_all_books()
    

для перевірки ксассів використовуємо метод isinstance, приклад:


user = User('Max', 15)
shape = Shape()

isinstance(max, User) -> True
isinstance(shape, User) -> False


class Printable(abc.ABC):
    @abstractmethod
    def print(self):
        pass


class Book(Printable):
    def __init__(self, name: str):
        self.name = name

    def print(self):
        print(self.name)


class Magazine(Printable):
    def __init__(self, name: str):
        self.name = name

    def print(self):
        print(self.name)


class Main:
    printable_list = []

    @classmethod
    def add(cls, printable: Printable):
        if isinstance(printable, Book) or isinstance(printable, Magazine):
            cls.printable_list.append(printable)

    @classmethod
    def show_all_magazines(cls):
        for printable in cls.printable_list:
            if isinstance(printable, Magazine):
                printable.print()

    @classmethod
    def show_all_books(cls):
        for printable in cls.printable_list:
            if isinstance(printable, Book):
                printable.print()

Main.add(Magazine('Magazine1'))
Main.add(Book('Book1'))
Main.add(Magazine('Magazine3'))
Main.add(Magazine('Magazine2'))
Main.add(Book('Book2'))

Main.show_all_magazines()
print('-' * 40)
Main.show_all_books()
''')


class Printable(abc.ABC):
    @abstractmethod
    def print(self):
        pass


class Book(Printable):
    def __init__(self, name: str):
        self.name = name

    def print(self):
        print(self.name)


class Magazine(Printable):
    def __init__(self, name: str):
        self.name = name

    def print(self):
        print(self.name)


class Main:
    printable_list = []

    @classmethod
    def add(cls, printable: Printable):
        if isinstance(printable, Book) or isinstance(printable, Magazine):
            cls.printable_list.append(printable)

    @classmethod
    def show_all_magazines(cls):
        for printable in cls.printable_list:
            if isinstance(printable, Magazine):
                printable.print()

    @classmethod
    def show_all_books(cls):
        for printable in cls.printable_list:
            if isinstance(printable, Book):
                printable.print()

Main.add(Magazine('Magazine1'))
Main.add(Book('Book1'))
Main.add(Magazine('Magazine3'))
Main.add(Magazine('Magazine2'))
Main.add(Book('Book2'))

Main.show_all_magazines()
print('-' * 40)
Main.show_all_books()