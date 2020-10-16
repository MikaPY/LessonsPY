
# year = int(input('Please input '))
# if (year % 4 == 0 or year % 100 == 0) and year % 400 != 0:
# 	print('ok')
# else:
# 	print('no')


# import random 

# x = 'abcdefgh'

# r = random.choice(x)
# print(r)



bot = int(input('Enter a num: '))
user = int(input('Enter a num: '))
if bot > user:
	print('Цифры бота больше, чем у юзера: ')
elif bot == user:
	print('Цифра бота юольше, либо равно число юзеру: ')	
else:
	print('Цифра юзера больше,чем у бота: ')


# man_1 = int(input('Enter a num: '))
# man_2 = int(input('Enter a num: '))
# man_3 = int(input('Enter a num: '))
# man_4 = int(input('Enter a num: '))
# if num_1 > num_2 and num_3 and num_4:
# 	print('Больше, чем остальные: ')
# elif num_2 > num_3 and num_4:
# 	print('Больше, чем остальное, но меньше, чем 1 ый: ')
# elif num_3 > num_4:
# 	print('Больше, чем последний, но меньше, чем 1х два ')
# else: 
# 	print('Они ровны')
	

# age_1 = int(input('first1'))
# age_2 = int(input('first2'))
# age_3 = int(input('first3'))
# age_4 = int(input('first4'))
# result = age_1 > age_2 and age_1 > age > age_3 and age_1 > age_4


# x = 1234
# dirst_number = x // 1000
# second_number  = x % 1000
# second_result =  second_number // 1000
# third_number = second_number % 100
# third_result = third_number // 10
# fourth_number = third_number % 10

# print(first_number)
# print(second_number)
# print(third_number)
# print(fourth_number)


# result = ''
# result += str(fourth_number) + str(third_number) + str(third_number) + str(second_number)
# print(int(result))




# age = int(input('Your age ?: '))
# sex = input('Your sex ?: M / F ') 
# marital = input('You are married ? Y / N') 
# if sex == 'F' and marital == 'Y'
# elif sex == 'F' or sex == 'M' and 40 < age < 60:
# 	print('You well work only urban areas: ')
# elif sex == 'M' and age > 20 and age  < 40:
# 	print('He can work anywhere')
# else:
# 	print('ERROR')



import random as r 

choice = 'RPS'
man = input('Please enter a R(Rock), P(Paper), S(Scisors)')

pc = r.choice(choice)
if man == 'R' and pc == 'S' or man == 'P' and pc == 'R' or man == 'S' and pc == 'P':
	print(man,pc, 'Win man :) ')
elif man == 'S' and pc == 'R' or man == 'R' and pc == 'P' or man == 'P' and pc == 'S':
	print(man,pc, 'Win pc :) ')	
else:
	print('Not a won')





