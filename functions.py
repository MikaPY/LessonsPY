# # def my_test():
# # 	print("Hello I am a function")
# # my_test()
# # my_test()
# # my_test()



# # def my_function(fname, lname):
# # 	print(fname + " " + lname)

# # my_function('Emil', 'Sargsyan')
# # my_function('Mika', 'Saribekyan')
# # my_function('Nelly', 'Mkrtchyan')


# # def my_function(child1, child2):
# # 	print("The youngest child is " + child1)

# # my_function(child2 ="Emil", child1 = "John")


# def my_function(country):
# 	print('I am from ' + country)

# my_function('Sweden')
# # my_function('India')
# # my_function()


# def my_func1(country):
# 	pass



# def my_func2(food):
# 	for x in food:
# 		print(x)

# fruits = ["apple","banana","cherry"]

# my_func2(fruits)



# def my_func3(x):
# 	5 ** x
# res= my_func3(3)
# print(res)


# def my_func4():
# 	global x 
# 	x = 'Yo-yo'

# my_func4()
# print('Python is ' + x)



def my_func5(*args): # Хранит некоторые данные.
	print(args)
my_func5(6,7,8,9,0)	# Выдаст ввидте tuple


def my_func(**kwargs):
	print(kwargs)
my_func(name = 'Mika', age = 25)



add = lambda x,y: x + y
print(add(2,5))