# homework6
# Заполните массив элементами арифметической прогрессии. Её первый элемент,
# разность и количество элементов нужно ввести с клавиатуры. Формула для
# получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.

list1 = []
def prog(a1, n, d):
    if n <= 0:
        return "Try again"
    return a1 + (n-1) * d

a1 = int(input())
n = int(input())
d = int(input())
for i in range (1, n+1):
    list1.append(prog(a1, i, d))
print(list1)

# Определить индексы элементов массива (списка), значения которых принадлежат
# заданному диапазону (т.е. не меньше заданного минимума и не больше заданного максимума)

print("Введите диапазон:")
a = int(input())
b = int(input())
list2 =[]
def ind(list1):
    indexes = []
    for index, i in enumerate(list1):
        if i >= a and i <= b:
            indexes.append(index)
    return indexes
        
print(ind([-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]))
