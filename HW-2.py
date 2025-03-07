from typing import Callable, Literal

print('''
1)написати функцію на замикання котра буде в собі зберігати список справ, вам потрібно реалізувати два методи:
- перший записує в список нову справу
- другий повертає всі записи

def notes():
    notes_list = []

    def inner(action, note=None):
        nonlocal notes_list

        def add_note(note: str):
            notes_list.append(note)

        def get_notes():
            return notes_list

        if action == "add":
            add_note(note)
        elif action == "get":
            return get_notes()

    return inner

inner = notes()

inner("add", "Buy milk")
inner("add", "Buy bread")

print(inner("get"))



inner = notes()
inner.add_note("Buy milk")
inner.add_note("Buy bread")
print(inner.get_notes())

''')


def notes():
    notes_list = []

    def inner(action, note=None):
        nonlocal notes_list

        def add_note(note: str):
            notes_list.append(note)

        def get_notes():
            return notes_list

        if action == "add":
            add_note(note)
        elif action == "get":
            return get_notes()

    return inner


inner = notes()

inner("add", "Buy milk")
inner("add", "Buy bread")

print(inner("get"))

print('''
2) протипізувати перше завдання

def notes() -> Callable[[str, str | None], list[str] | None]:
    notes_list = []

    def inner(action: Literal["add", "get"], note: str | None = None) -> list[str] | None:
        nonlocal notes_list

        def add_note(note: str)-> None:
            notes_list.append(note)

        def get_notes()-> list[str]:
            return notes_list

        if action == "add":
            add_note(note)
        elif action == "get":
            return get_notes()

    return inner


inner = notes()

inner("add", "Buy milk")
inner("add", "Buy bread")

print(inner("get"))

''')


def notes() -> Callable[[str, str | None], list[str] | None]:
    notes_list = []

    def inner(action: Literal["add", "get"], note: str | None = None) -> list[
                                                                             str] | None:
        nonlocal notes_list

        def add_note(note: str) -> None:
            notes_list.append(note)

        def get_notes() -> list[str]:
            return notes_list

        if action == "add":
            add_note(note)
        elif action == "get":
            return get_notes()

    return inner


inner = notes()

inner("add", "Buy milk")
inner("add", "Buy bread")

print(inner("get"))

print('''
3) створити функцію котра буде повертати сумму розрядів числа у вигляді строки (також використовуемо типізацію)

Приклад:

expanded_form(12) # return '10 + 2'
expanded_form(42) # return '40 + 2'
expanded_form(70304) # return '70000 + 300 + 4'

def expanded_numbers(n: int) -> str:
    l = len(str(n))
    res_lst = [
        val + "0" * (l - i - 1)
        if i != l - 1
           and val != "0"
        else (val if l-i-1 == 0 else "")
        for (i, val)
        in enumerate(list(str(n)))
    ]
    print(" + ".join([i for i in res_lst if i != ""]))


expanded_numbers(12) # return '10 + 2'
expanded_numbers(42) # return '40 + 2'
expanded_numbers(70304) # return '70000 + 300 + 4'
''')


def expanded_numbers(n: int) -> str:
    l = len(str(n))
    res_lst = [
        val + "0" * (l - i - 1)
        if i != l - 1
           and val != "0"
        else (val if l - i - 1 == 0 else "")
        for (i, val)
        in enumerate(list(str(n)))
    ]
    print(" + ".join([i for i in res_lst if i != ""]))


expanded_numbers(12)  # return '10 + 2'
expanded_numbers(42)  # return '40 + 2'
expanded_numbers(70304)  # return '70000 + 300 + 4'

print('''
4) створити декоратор котрий буде підраховувати скільки разів була запущена функція 
продекорована цим декоратором, та буде виводити це значення після виконання функцій
''')

def counter(func: Callable) -> Callable:
    counter = 0
    def wrapper(*args, **kwargs) -> Callable:
        nonlocal counter
        counter += 1
        func(*args, **kwargs)
        print(f"Function {func.__name__} was called {counter} times")

    return wrapper

@counter
def fnc():
    print("Hello")

fnc()
fnc()
fnc()
fnc()