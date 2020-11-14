import json 

f_n = 'Hi JS.json'


p_1 = {
	'name': 'Aram',
	'age': 18,
	'height': 188,
	'awards':['master',3,2,1]
}


p_2 = {
	'name': 'Anri',
	'age': 14,
	'height': 178,
	'awards':[3,2,1]
}


m_p = [p_1,p_2]
with open(f_n, 'w') as file:
	json.dump(m_p, file)


file = open(f_n) # Чтение по умолчанию.
json_data = json.load(file)
for data in json_data:
	# print(data)
	print('\nPlayer name is', data['name'])
	print('Player age is', data['age'])
	print('Player height is', data ['height'])
	print('Player awards is', data['awards'])