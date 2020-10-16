temp = input('temp = ')
num = int(temp[:-1])
char = temp[:-1].upper() == 'C'

if char:
	far = (num * 9/5) + 32 
	print(far)
else:
	cel = (num - 32) * 5/9
	print(cel)




dog_year = int(input('dog year - '))

if dog_year <= 2:
	human_year = dog_year * 5.25
	print(human_year)

elif dog_year < 0:
	print('worng input')
else:
	human_year = 3.5 + dog_year * 4
	print(human_year)