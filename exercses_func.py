# # Конвертировать километры в мили.
# def convert(numbers):
# 	return numbers * 1.6 

# print(convert(5))


# # Конвертировать день в секунды.
# def convert1(numbers2):
# 	return numbers2 * 60 * 60

# print(convert1(24))



# Создать пароль из 8 символов с большими буквами и числами.
# pass_one = (input('Enter a pass: '))

# def validpassword(password):
# 	number = 0
# 	upper = 0
# 	for i in password:
# 		if i.isdigit():
# 			number += 1
# 		elif i.isupper():
# 			upper += 1 
# 	if number > 1 and upper > 0 and len(password) > 7:
# 		return 'True'
# 	else:
# 		return 'False'

# print(validpassword(pass_one))





def my_fact(factorial):
	f = 1
	if factorial > 0: 
		for i in range(2,factorial+1):
			f *= i
		return f	
print(my_fact(5))


