print(
    '''
    1)написати прогу яка вибирає зі введеної строки числа і виводить їх
    так як вони написані
    наприклад:
        st = 'as 23 fdfdg544 34' #введена строка
        23, 544, 34              #вивело в консолі
        
    def select_digits(st):
    return print(",".join([i for i in st if i.isdigit()]))
    
    select_digits('as 23 fdfdg544')
    '''
)


def select_digits(st):
    return print(",".join([i for i in st if i.isdigit()]))


select_digits('as 23 fdfdg544')

#################################################################################

print('''
    2)написати прогу яка вибирає зі введеної строки числа і виводить їх
    так як вони написані
    наприклад:
        st = 'as 23 fdfdg544 34' #введена строка
        23, 544, 34              #вивело в консолі
        
    def select_digits_as_it_is(st):
    return print(" ".join("".join([i if i.isdigit() else " " for i in st]).split()))
    
    select_digits_as_it_is('as 23 fdfdg544 34')
       
    ''')


def select_digits_as_it_is(st):
    return print(" ".join("".join([i if i.isdigit() else " " for i in st]).split()))


select_digits_as_it_is('as 23 fdfdg544 34')

# #################################################################################
#
print('''
    ist comprehension

1)є строка:
greeting = 'Hello, world'
записати кожний символ як окремий елемент списку і зробити його заглавним:
['H', 'E', 'L', 'L', 'O', ',', ' ', 'W', 'O', 'R', 'L', 'D']
        
    def split_to_list_and_capitalize(st):
    return print([i.upper() for i in st])
    
    split_to_list_and_capitalize('Hello, world')
    ''')


def split_to_list_and_capitalize(st):
    return print([i.upper() for i in st])


split_to_list_and_capitalize('Hello, world')

#
print('''
    2) з диапозону від 0-50 записати тільки не парні числа при цьому піднести їх до квадрату
приклад:
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289, 324, ...]
        
    def list_of_squares(lst):
    return print([i ** 2 if i != 0 else 0 for i in lst if i % 2 != 0 or i == 0])
    
    lst = range(0, 50)

    list_of_squares(lst)
    ''')


def list_of_squares(lst):
    return print([i ** 2 if i != 0 else 0 for i in lst if i % 2 != 0 or i == 0])


lst = range(0, 50)

list_of_squares(lst)

#
print(''' 
# - створити функцію яка виводить ліст
def print_list(*lst):
    return print(lst)


print_list(1, "2", 3, {"ttt": 235})

''')


def print_list(*lst):
    return print(lst)


print_list(1, "2", 3, {"ttt": 235})

print('''
# - створити функцію яка приймає три числа та виводить та повертає найбільше.
def max_of_3(*args: int | float):
    return print(max(args))


max_of_3(3, 7, 1)
 '''
      )


def max_of_3(*args: int | float):
    return print(max(args))


max_of_3(3, 7, 1)

print('''
- створити функцію яка приймає будь-яку кількість чисел, повертає найменьше, а виводить найбільше

def min_max(*args: int | float):
    print(max(args))
    return min(args)
    
min_max(3, 7, 1)
''')


def min_max(*args: int | float):
    print(max(args))
    return min(args)


min_max(3, 7, 1)

print('''
# - створити функцію яка повертає найбільше число з ліста
def max_of_list(lst: list[int | float]):
    return max(args)


max_of_list([3, 7, 1])
''')


def max_of_list(lst: list[int | float]):
    return max(lst)


print(max_of_list([3, 7, 1]))

print('''
# - створити функцію яка повертає найменьше число з ліста
def sum_of_list(*args: int | float):
    return print(sum(args))


sum_of_list(3, 7, 1)
''')


def sum_of_list(*args: int | float):
    return print(sum(args))


sum_of_list(3, 7, 1)

print('''
# - створити функцію яка приймає ліст чисел та повертає середнє арифметичне його значень.
def avg_of_list(*args: int | float):
    return print(sum(args) / len(args))

avg_of_list(3, 7, 1)
''')


def avg_of_list(*args: int | float):
    return print(sum(args) / len(args))


avg_of_list(3, 7, 1)

# ################################################################################################
# 1)Дан list:
list = [22, 3, 5, 2, 8, 2, -23, 8, 23, 5]


#   - знайти мін число
#   - видалити усі дублікати
#   - замінити кожне 4-те значення на 'X'

def list_manipulation(lst):
    print(min(list))
    print(set(list))
    print([val if (i + 1) % 4 != 0 or i == 0 else "X" for i, val in enumerate(list)])


# 2) вивести на екран пустий квадрат з "*" сторона якого вказана як агрумент функції
def square(n):
    top_bottom = "* " + (" * " * (n - 2)) + " *"
    middle = "* " + ("   " * (n - 2)) + " *"
    lst = [top_bottom if i == 0 or i == n - 1 else middle for i in range(n)]
    return print("\n".join(lst))


square(15)


# 3) вывести табличку множення за допомогою цикла while

def multiplication_table():
    for i in range(1, 11):
        print(" ".join([str(i * j).rjust(3) for j in range(1, 11)]))


def multiplication_table_while():
    i = 1
    while i <= 10:
        print(" ".join([str(i * j).rjust(3) for j in range(1, 11)]))
        i += 1


def multiplication_table_comprehension():
    [print(" ".join([str(i * j).rjust(3) for j in range(1, 11)])) for i in range(1, 11)]


# 4) переробити це завдання під меню

while True:
    print('''
        1) ліст маніпуляції
        2) вивести на екран пустий квадрат з "*" сторона якого вказана як агрумент функції
        3) вывести табличку множення за допомогою цикла while
        4) вивести табличку множення за допомогою вкладених циклів
        5) вивести табличку множення за допомогою list comprehension
        6) выйти из программы
    ''')
    val = input("Введіть номер завдання: ")
    if val == "1":
        list_manipulation([22, 3, 5, 2, 8, 2, -23, 8, 23, 5])
    elif val == "2":
        n = int(input("Введіть сторону квадрату: "))
        square(n)
    elif val == "3":
        multiplication_table_while()
    elif val == "4":
        multiplication_table()
    elif val == "5":
        multiplication_table_comprehension()
    elif val == "6":
        print("Выход из программы...")
        break
    else:
        print("Невірно введені дані")
