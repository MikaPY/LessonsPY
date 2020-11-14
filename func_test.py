import json


def alpfh(vowel):
	count = 0
	v = ('a','u','o','i','e')
	for i in vowel:
		if i in v:
			count += 1
	return count	


vowel = input('Enter: ')

c= (alpfh(vowel))


f_l = 'vowel.txt'

with open(f_l, 'w') as fl:
	json.dump(c, fl)

with open(f_l) as fl:
	print(json.load(fl))	