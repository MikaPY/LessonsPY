file_name = 'name.txt'
# with open("name.txt",'w') as f:
# 	f.write('hi my frind\nwhat are you doing?')


with open(file_name) as file:
	for i in file:
		for c in i:
			print(c)


c = open(file_name)
print(c.read())
c.close()

print(file.readlines())