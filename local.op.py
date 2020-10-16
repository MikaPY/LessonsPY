x = 4 # Переменная равная 5.  
res = x < 5 and x < 10 # Оба должны быть верными. True.
print(res)


x = 6  # Возвратит False, т.к. другой не верен. 
res x < 5 and x < 10 


x = 4 
res = x < 5 or x > 10 # Вернет True, т.к. первый x верен.


x = 4 
res = not(x < 5 or x < 10) # Вернет False, т.к. исп. пренудительное not. 
print(res)


x = 6 
y = 6 
print(x is y)


name = "Mika"
name_2 = "mika"
print(name is name_2)


name_3 = "Mika"
name_4 = 'mika'
print(name_3 is not name_4)
print(id(name))
print(id(name_2))



about_me = 'I am Mikael Saribekyan i have Covid19,sorry my friend i cannot Covid19'
word = 'Covid19'
name = 'Mikael'
result = word in about_me 
print(result)
result = word not in about_me
print(result)
result = word  in about_me and name in about_me
print(result)


name_and_last_name = 'Mikael saribekyan 1995 Мой год рождения'
name = 'Mikael'
date = '1454'
rand = 'Year'
res = name in name_and_last_name or date in name_and_last_name or rand in name_and_last_name 

print(res)


per = 'Сарибекян Микаэль в 2003 г. украл шоколадку из супермаркета'
per_2 = 'шоколадку'
per_3 = 'украл'
per_4 = 'Бандит'
res = per_2 in per and per_3 in per or (per_4 in per )
print(res)


item_banana = input('Have you banana in refrigerator ? ') == 'y'
item_light = input("Do you have a light ? ") == 'y'
res = item_banana and not item_light, 'Достать банан '
print(res)


# item_light = input('Have you banana in refrigerator ? ') == 'y'
item_banana = input('Do you have a light ? ') == 'y'
buy = input('Принести банан или нет ? ') == 'y'
# res = item_banana and not  item_light 
res_2 = not item_banana and buy 
print(res_2)


item_faucet = input('У тебя сломан кран ? ') == 'нет'
item_water = input('У тебя есть вода ? ') == 'да'
result = not item_faucet and  item_water

print(result,'Тогда дай стакан воды :)')


item_car = input('Твоя машина свободна ? ') == 'да'
item_oil = input('Есть ли у тебя бензин ? ') == 'да'
result = item_car and item_oil 

print(result,'Тогда поедем покатаемся :) ')