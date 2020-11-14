import json

file_name = "test.txt"

name = ["ani",'John','Bob']
number = [1,2,3]

name_dict = {}
x =  -1
for i in name:
	x += 1
	name_dict[number[x]] = i


result = name_dict

with open(file_name, 'w') as f:
	json.dump(name_dict,f)

# f = open(file_name)
# print(f.read())


json_data = json.load(f)
print(json_data)