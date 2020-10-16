# for i in range(1,12*15+1):
# 	if i % 12 == 0 and i % 15 == 0:

# 		print(i)
# 		break
		

# # Write a Python program to find the smallets number which are divisible by 12 and 15



# i = 1
# while True:
# 	if i % 12 == 0 and i % 15 == 0:
# 		print(i)
# 		break
	# i += 1


# Найти деление на 2 и и не деление на два.

# odd = 0
# even = 0

# for i in range(1,101):
# 	if i % 2 == 0:
# 		even += 1
# 	else:
# 		odd += 1

# print('odd - ', odd, 'even', even)



# Фибоначи
# x = 0
# y = 1
# while y < 40:
# 	print(y)
# 	x, y = y, x + y





# string = 'Python 3.9'
# letters = 0 
# numbers = 0 
# for i in string:
# 	if i.isalpha(): # Функция находит буквы - True
# 		letters += 1
# 	elif i.isdigit(): # Функция находит цифры - True
# 		numbers += 1
# print(letters)
# print(numbers)




# nums = 73421
# count = 0
# for i in str(nums):
# 	count += int(i)
# print(cont)


# Нахождение факториала циклом for.
# number = int(input('Entet a num: '))
# fac = 1 

# for i in range(1, number + 1):
# 	fac *= i 
# print(fac)

# Нахождение факториала циклов while.



# while True:
# 	age = int(input('Enter your age: '))
# 	if 17 < age < 21:
# 		print(age)
# 		break
# 	print('Вы ввели не то число')




import random as r
bot = 0
user = 0


user_as = input('Join game ?  ')
bot_as = r.randint(1,3)
join = user_as == 'y'
if join:
	chance = input('Enter a num: ')
	user += chance
	print(user)
else:
	bot_as



# import random as r 


Join_game = input('\n\tХочешь начать первым ? ')
if Join_game == 'Yes':
	print('\n\tВеликоплено! ')
	print('\n\tОзнакомимся с правмилами игры! ')
elif Join_game =='No':
	print('\n\tТогда начну я ! ')
	print('\n\tОзнакомимся с правмилами игры! ')
	pass


print('\nТебе и боту нужно начинать с 0 и каждый раз добавляя от 1 до 3 до рости до 21,\nкто первый доберется до 21 - тот победил ! \n\tХорошей игры. ')





	





