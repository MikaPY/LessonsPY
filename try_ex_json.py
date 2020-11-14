import json

f_n = 'try,ex,json.txt'
try:
	with open(f_n) as file:
		user = json.load(file)
		print('Hello',user)
except:
	username = input('What is your name? ')
	with open(f_n, 'w')as file:
		user = json.dump(username, file)
		# print('Hello',user)