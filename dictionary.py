thisDict = {'name':'Aram','year':1994}
print(thisDict)

thisDict = {'country':'Armenia','capital':'Yerevan'}
print(thisDict)

thisDict = {'car':'BMW','color':'Black'}
print(thisDict)

result = thisDict.popitem() # вывод с конца.
print(x)


thisDict = {'name':'Aram','year':1994}
thisDict['year'] = 2014
thisDict['okay'] = 2020
print(thisDict)

thisDict = {'name':'Aram','year':1994}
print(len(thisDict)) # показывает кол-во key:vallue

thisDict = {'name':'Aram','year':1994}
for i in range(10):
	thisDict[i] = 5 
print(thisDict)

thisDict = {'name':'Aram','year':1994} # Добавление словаря в цикл 'for'
for i in thisDict:
	print(i)

new_dict = {}

my_dict = {'name':'Mika','age':1995}
for i,j in my_dict.items():
	new_dict[i] = j
print(new_dict)


new_dict = {}

my_dict = {'name':['Mika',99,True,False,0.99],'age':1995}
for i,j in my_dict.items():
	new_dict[i] = j
print(new_dict)

print(my_dict.fromkeys('3'))







my_list = []
my_summ = 0

this_Dict = {'a':1,'b':2,'c':4,'d':0}
for i in this_Dict.values(): # выбор валю
	my_list.append(i) # добавление переменной с валю.
my_list.sort()	# сортирока 
print(my_list[-1]) # вывод и сортировка с большего числа.
for i in my_list:
	my_summ += i
result = my_summ / len(my_list)
print(result)

print(sum(my_list)/len(my_list))


this_Dict = {}
this_Dict['key'] = 123
print(this_Dict)


my_list = [3, 10, 4, 12, 3]
for i in my_list:
	if i % 2 == 0:
		my_list.remove(i)
		print(my_list)