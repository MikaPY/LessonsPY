# theList = ['Gu',9,9.1,True,(1,2,3,4,5)]
# print(theList)


# theNotebooks = ('Lenovo','Macbook','HP','Acer')
# if 'Macbook' in theNotebooks:
# 	print('Yes')


# thePass = input('Enter your pass: ')
# theChars = ('!','@','#','$','%','&','**')
# pointNums = 0
# pointChars = 0
# for i in thePass:
# 	if i.isdigit():
# 		pointNums += 1 


# for i in pointNums:
# 	if i.isdigit():
# 		pointChars += 1
	

# if len(thePass) > 8 and pointChars > 1 and pointNums > 1:
# 	print('Your pass strong: ')
# else:
# 	print('Your pass is not strong: ')



# theLink = 'https://www.youtube.com/watch?v=RRW2aUSw5vU'
# x = theLink.index('=')
# print(x)
# point = 0
# for i in theLink:
# 	point += 1
# 	if i == '=':
# 		break

# print(theLink[point:])



# if pol == pol[::-1]:
# 	print('Open')





theInt = input('Enter a num: ').split()
result = []

for i in theInt:

	if int(i) % 2 == 0:
		result.append(i)

print(result)



# my_str = "ergwfreg123egtert45gg10"
# my_list = []

# for i in my_str:
# 	if my_str.isdigit():
		