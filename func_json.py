import json 

def result(n):
	c = []
	global result
	for i in range(1,n):
		if i % 3 == 0 or i % 5 == 0:
			c.append(i)
	
	result = sum(c)
	return sum(c)
n = int(input('Num: '))
c = result(n)





file_name = "sum.txt"

with open(file_name, 'w') as fl:
	json.dump(result, fl)

with open(file_name) as f:
	print(json.load(f))	