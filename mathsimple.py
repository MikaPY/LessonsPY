def my_fact(factorial):
	f = 1
	if factorial > 0: 
		for i in range(2,factorial+1):
			f *= i
		return f	
# print(my_fact())

