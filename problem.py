celsius = int(input("Enter a num: ")) # конвертация цельсия в фарейнгейт.
fahrenheit = 32 + 1.8 * celsius

print(fahrenheit)


fahrenheit = int(input("Enter a num: ")) # конвертация фарнгейт в цельсия.
celsius  = (fahrenheit - 32) / 1.8 

print(celsius)


minutes = int(input('Enter a num: ')) # ковертация минуты в секунды. 
seconds = minutes * 60  

print(seconds)


day = int(input("Enter a num: ")) # конвертация дней в минуты и секунды.
minutes = 24 * 60 * day 

print(type(minutes), 'minutes')
second = minutes * 60 

print(type(second), 'seconds')


angle = int(input("Enter a num: ")) # проверяем два наших угла равны ли другому углу.
angle_2 = int(input("Enter a num: "))
res = angle + angle_2 == 90

print(res)


angle = int(input("Enter a num: "))  # калькуляция размера 3 ого угла. 
triangle = int(input("Enter a num: "))
size = 180
res =  size - (angle + triangle )

print(res)


num1 = int(input("Enter a num: ")) # сравнение 
res = num1 > 100

print(res)


mod = int(input("Enter a num: ")) # сравнение по модулю
res = mod % 400 == 0 # False 

print(res)


radius = int(input("Enter a num: "))
turnover = int(input("Enter a num: "))
c = radius * 2 * 3.14 
res = radius * c

print(res)







