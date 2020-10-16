# fruits = ['banana','apple','cherry'] # Вывод списка (list)
# print(fruits)


# numbers = [34,56,-456,7.56,-2.34]
# print(numbers[1]) # Вывод по индексу из списка(list)

# print(numbers[-1]) # Вывод с конца списка(list)


# fruits = ['banana','apple','cherry'] # Заменит в списке по индексу.
# fruits[1] = 'kiwi'
# print(fruits) 


# fruits = ['banana','apple','cherry'] # Подсчитает кол-во
# print(len(fruits))



# # append - метод,добавляющий в конец списка.

# fruits = ['banana','apple','cherry']
# fruits.append('orange') 
# fruits.append('lemon')
# print(len(fruits))


# # insert - добавляет в конкретно выбранное место.

# fruits = ['banana','apple','cherry']
# fruits.insert(1,'orange')
# print(fruits)

# #  remove - удаляет из списка. 
# fruits.remove('apple')
# print(fruits)


## pop - забирает аргумент и хранит его.

# fruits = ['banana','apple','cherry']
# fruits.pop()
# print(fruits)

# Удаление по индксу

# fruits = ['banana','apple','cherry']
# del fruits[2]
# # del fruits
# print(fruits)


# Добавление списка в список с конца(list)
# fruits = ['banana','apple','cherry']
# numbers = [34,56,-456,7.56,-2.34]
# fruits.extend(numbers)
# print(fruits)

# Сортирует с меньшего числа по большее исп. перебор.
numbers = [34,56,-456,7.36,-2.34]

numbers.sort()
num = numbers[::-1] # Переворачивает с большого по маленькое.
print(num)

numbers.reverse() # Переворачивает в обратную сторону.
print(numbers)


