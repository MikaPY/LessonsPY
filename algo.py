# # recursion()

# # def recursion():
# # 	print('Hello world')
# # 	recursion()
# # recursion()



# # Find factorial:
# def factorial(x):
# 	if x == 0:
# 		return 1 
# 	elif x == 1:
# 		return 1 
# 	else:
# 		print(x)
# 		return x *factorial(x-1)

# print(factorial(5))



# Find fibonacci:
def fibonacci(x):
	if x == 1:
		return 0
	elif x == 2:
		return 1 
	else:
		print(x)
		return fibonacci(x-1) + fibonacci(x-2)

print(fibonacci(10))



# Lineary search:
# Bineary search:

# Buble sort:

# old_list = [10,75,43,15,25,-4,27]

# def buble_sort(my_list):
# 	last_item = len(my_list) - 1

# 	for i in range(0,last_item):
# 		for j in range(0,last_item -i):
# 			if my_list[j] > my_list[j+1]:
# 				my_list[j], my_list[j+1] = my_list[j+1],my_list[j]
# 			print(my_list)
# 	return my_list

# print('Old list',old_list)
# new_list = buble_sort(old_list).copy()
# print('New list',new_list)


a = 1
b = 11
c = 29

if a > b > c:
	a,b,c = c,b,a
	print(a,b,c)

elif a>c>b:
	a,b,c=b,c,a
	print(a,b,c)

elif b > a > c:
	a,b,c=c,a,b
	print(a,b,c)

elif b>c>a:
	a,b,c=a,c,b
	print(a,b,c)


elif c>b>a:
	a,b,c=a,b,c
	print(a,b,c)

elif c>a>b:
	a,b,c=b,a,c
	print(a,b,c)

else:
	print(a,b,c)




theList= [5, 78, 45, 12, 56, 991,]
num = 11

def thePack(lst, target):
	