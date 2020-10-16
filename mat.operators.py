# # # % деление по модулю.

# # # x = 7 
# # # y = 5 
# # # result = x % y
# # # print(result)

# # # x = 13 
# # # y = 5 
# # # result = x % y 
# # # print(result)


# # # x = -25
# # # y = 5 
# # # result = x % y 
# # # print(result)


# # # x = 5 
# # # y = 25 
# # # result = x % y 
# # # print(result)


# # # // целочисленное деление
# # x = 10 
# # y = 3 
# # result = x // y 
# # print(result)


# # x = 125 
# # y = 7 
# # result = x // y 
# # print(result)

# # x = -25
# # y = 4 
# # res = x // y 
# # print(res)


# # x = 2 
# # y = 5 
# # res = x // y 
# # print(res)


# # # ** возведение в степень 

# # x = 5 
# # y = 3 
# # res = x ** y 
# # print(res)


# # x = 15 
# # y = 6 
# # res = x ** y 
# # print(res)


# # x = 5 
# # y = 15 
# # res = x ** y 
# # print(result)


# # # ** 0.5 (корень)

# # x = 4  
# # res = x ** 0.5 
# # print(res)

# # # Example
# # balance = 100 
# # paychek = 150 
# # newsbalance = balance + paychek
# # print(newsbalance)

# # # Example 2 
# # balance = 0
# # # newsbalance = balance + 150 
# # balance += 150 
# # balance += 50 
# # balance -= 25
# # print(balance)


# # #ATM

# # balance = 0 
# # hello = "\n\tЗдраствуйте"

# # print(hello)

# # terminal = input("\n\tХотите пополнить баланс ?")

# # print(terminal)

# # cash = int(input("\n\tВведите сумму: "))

# # balance += cash 
# # print('\n\tВаш баланс:',balance,"$")



# x = 5 
# y = 7 
# print(x <= y) # True 

# x = 10
# y = 2 
# print(x <= y) # False 


# x = 5 
# y = 7 
# print(x == y) # равно !

# x = 4 
# y = 2 
# print(x != y) # не равно ! 


# balance = 1000
# newbalance = 10000
# print(balance >= newbalance)
# print(balance <= newbalance)


# classone = int(input("Введите кол-во учеников "))
# max_people = 16 
# result = classone > 16
# print(result)
# old_or_even = classone % 2 
# print(old_or_even == 1)


# # classone -= 1
# first_class = classone / 2 
# second_class = first_class - 1 #(+1)
# print(first_class, second_class)



procent = int(input("После скольки процентов выключить ? "))
time = int(input("В какое время вы просыпайтесь ?"))
procent = time - 1 
day_one = int(input("Enter num"))
day_two = int(input("Enter num"))
day_three = int(input("Enter num"))
res = (day_one + day_two + day_three) / 3 
print(res)
print(res == time,"100%")