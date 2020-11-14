import json 

user = 'user.json'
# choice = input('Где ты хочешь помыть машину?') == 'Зейтун'
# if choice:
# 	car_type = input('Jeep or Sedan')
# 	if car_type == 'Jeep':
# 		price = 1000	
# 	else:
# 		price = 1000

# user_result = {
# 	'choice': choice,
# 	'car_type': car_type,
# 	'price': price
# }



try:
	with open(user) as file:
		user = json.load(file)
		print(user)
except:
	with open(user, 'w') as file:
		user = json.dump(user_result, file)
