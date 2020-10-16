# #Set похоже на list. Не может содержать дубликаты. Не имеет индексов и выдает рандомно.
# #Fronzeset  похоже на tuple.


# # set1 = {12,23,'11','Hello'}
# # for x in set1:
# # 	print(x)
# # 	# print(set1)


# thisset = {'apple','banana','cherry'}

# print('banana'in thisset) # Проверяем есть ли данное лсово.


# # add - добавление одного аргумнета.
# # update - добавление несокльких аргунетов.
# # remove - удаление аргумента.

# set1 = {1,6,7,'Q'}
# set2 = {1,2,4,'hi'}
# set3  = {1,3,5,'hello'}

# set1.add(123)
# print(set1)

# set2.clear()
# print(set2)

# new = set3.copy()
# print(new)


# print(set1.difference(set2,set3)) #  разница. 

# set1.discard(1) # удаляет элемент. 
# print(set1)

# set1.pop() # Возвращает какой либо аргумент.
# print(set1)


# set1.update(set2)
# print(set1)



# my_list = [1,1,2,3,4,7,8,9] # удалить разницу.
# # my_set = set[my_list]
# # print(list(my_set))


# my_lst = [] # удалить разницу 
# for i in my_list:
# 	if i not in my_lst:
# 		my_lst.append(i)
# print(my_lst)


# a = set('hello')
# print(a)


# my_txt = input('Create')
# print(my_txt[:2]+my_txt[-2:])


# word = input('Please mention a word :')

# char = word[0]
# word = word.replace(char,'$')

# word = char + word[1:]
# print(word)



str1 = 'abc'
str2 = 'xyz'
print(str2[:2] +str1[-1]+' '+str1[:2]+str2[-1])


if len(word) > 2:
	if word[-1:] == 'ing':
		word += 'ly'
	else:
		word += 'ing'
		print(word)
