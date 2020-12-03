
from functools import reduce


# Вывести сумму чисел (целые и не целые) длинна числа(7) внимание на запятую и правила сложения
# continue
# вывести словарь отсортированый по ключам
# вывести список чисел которые повторяется и вывести в формате ключ(число) значение(кол-во повторений)
# c = [2, 3, 4, 1, 0, 2, 4, 5, 7, 8, 9, 6, 2, 3, 5, 6, 7, 9, 0, 4, 9]
# # list comprehension
# repeat = []
# for i in c:
#     if c.count(i) > 1:
#         repeat.append(i)
# print(sorted(repeat))
#
# amount_item = []
# for i in repeat:
#     tup_item = (i, repeat.count(i))
#     if tup_item not in amount_item:
#         amount_item.append(tup_item)
# print(sorted(amount_item))

# def dict_ser(z):
#     value = []
#     for i in c:
#         if z == i:
#             value.append(z)
#             amount = len(value)
#             act_dict = {z: amount}
#     return act_dict
# print(dict_ser(9))


# a = {"d1": 1, "d3": "d_value", "d2": True, "d4": 123}
# new_dict = {}
#
#
# c = [2, 3, 4, 1, 0, 2, 4, 5, 7, 8, 9, 6, 2, 3, 5, 6, 7]
# !!!!!!!!!!!!!!!!!!!!!!!!!!
# def sum_big(x):
#     list_num = []
#     str_x = str(x)
#     sep_num = str_x.strip('.')
#     for i in sep_num:
#         if i != '.':
#             list_num.append(int(i))
#     return sum(list_num)
# print(sum_big(2.2563545))
# #with countinue

#=========================================================================================================
# Вивести відсортований список та видалити дублікати елементів
# зробити в одну стрічку
# a = [9, 6, 1, 2, 8, 4, 5, 6, 7, 3, 3, 8, 9, 10, 6]
# print(set(a))
#
# # Вивести список елементів, які повторюються
# # Не використовуючи тип даних 'set'
# a_1 = [9, 6, 1, 2, 8, 4, 5, 6, 7, 3, 3, 8, 9, 10, 6]
# s = [i for i in a_1 if a_1.count(i) > 1]
# print(s)
#
# # Вивести відсортований список елементів без їх дублікатів
# # Без використання 'set'
c = [9, 6, 1, 12, 123, 2, 2, 8, 4, 5, 6, 7, 3, 3, 8, 67, 43, 9, 10, 6]
#
# sl = []
# for i in c:
#     if i not in sl:
#         sl.append(i)
# print(sl)

# x_list = []
# def sum_numb(x):
#     for i in range(round(x)):
#         if i is enumerate():
#             x_list.append(i)
#     return sum(x_list)
# print(sum_numb(23.2564))


# x = 14
# for val in range(x):
#     if val == 3:
#         pass
# else:
#     print('L')
# def some_f():
#     for i in range(5):
#         if i == 2:
#             print(i)
#             return
#     else:
#         print('Some Text')
# print(some_f())

def test(a, b, c, *args, **kwargs):
    print(type(a))
    print(type(args))
    print(type(kwargs))
    print(b)
    print(c)
l = lambda a, b, c, *args, **kwargs: print((a, b, c))
l(*c, test1='pass', test='failed', test3='skipped', test4=None, test5=True)
# test(*c, test1='pass', test='failed', test3='skipped', test4=None, test5=True)
s = [_ for _ in range(10)]


def fun(a):
    a = ...
print(s)

# Lambda example:
#
# It’s a short expression from def and can be used for some non bigest actions.
#
# lambda arg1, arg2, ….: expression
#
# L = lambda a, b=2, *c, **d: [a, b, c, d]
#
# L(1, 2, 3, 4, x=1, y=2) => [1, 2, (2, 4), (‘y’ : 2, ‘x’ : 1)]
#
# print(list(filter((lambda x: x%2 == 0), range(5))))
#
# result: [0, 2, 4]

a = [1, 2, 3, 4, 5]

def f_test(x):

       return x*2

c = map(f_test, a)
print(list(c))

data = [2, 3, 4, 5, 6, 7]

test_f = lambda x, y: x*y

print(reduce(test_f, data))