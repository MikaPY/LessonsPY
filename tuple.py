# tuple - не изменяемый список хранящий различные типпы данных. 

# a = 'a',0 
# print(type(a))

# b = tuple()
# print(type(b))


# tup1 = ('physics', 'chemistr', 1997, 2000)
# print(tup1.__sizeof__())


# name = 'John'
# print(name.__sizeof__())
# name1 = 'Johnatn'
# print(name1.__sizeof__())



# thistuple = ("apple", "banana", "cherry")
# print(len(thistuple))


# # len - считает длинну объектов.
# name2 = 'John'
# print(len(name2))


# # count - проверяет количество какого-либо объектов.
# thistuple = ("apple", "banana", "cherry")
# print(thistuple.count('banana'))

# # Цикл для tuple.
# thistuple = ("apple", "banana", "banana", "cherry")
# if "apple" in thistuple:
# 	print("Yes", 'apple', 'is in the fruits tuple')


# thistuple = ("apple", "banana", "cherry", "kiwi")
# print(thistuple[1:3])


# x = (5, 10, 15, 20)


# # y = reversed(x)
# # print(tuple(y))

# print(x[::-1]) # переварачивает tuple.


# Отрицательный индекс.

# thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
# print(thistuple[-4:]), [-1]


# tuple1 = ("a", "b", "c")
# tuple2 = (1, 2, 3)

# tuple3 = tuple1 + tuple2
# print(tuple3)



# num = [10,20,30,(10,20),40]
# c = 0 
# for n in num:
# 	if isinstance(n, tuple):
# 		break
# 	c += 1
# print(c)



# names = ('Mika', 'Rub', 'Arno', 'Gag', 'Alex')
# if 'Mika' in names:
# 	print('Ok')


# import random as r 
# names = ('Mika', 'Rub', 'Arno', 'Gag', 'Alex')
# print(r.choice(names))



# tup = ('e', 'x', 'e', 'r', 'c', 'i', 's','e','s')
# mystr = ''. join(tup)
# print(mystr)