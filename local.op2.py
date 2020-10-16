# Logical Operators - Логические Операторы. 

# Operator 'and' -  Оператор 'and'


# Returns True if both statements are true
# Возвращает Да, если оба параметра верны.

x = 4 
result = x < 5 and x < 10 # Output: True , Выводит: Да.
print(result)


# Returns False if both statements are false
# Возвращает Нет, если оба параметра не верны

x = 6 
result = x < 5 and x > 10 # Ouput: False, Выводит: Нет.
print(result)


# Operator 'or' - Оператор 'or'


# Returns True if one of the statements are True
# Возвращает Да, если одно из параметров верно

x = 4 
result = x < 5 or x > 10 # Ouput: True, Выводит Да
print(result)


# Returns False if two of the statements are False
# Возвращает Нет, если оба параметра не верны

x = 4 
result = x > 5 or x > 10 # Ouput: False, Выводит False
print(result)


# Operator 'not' - Оператор 'not'

# Reverse the result,returns False if the result is True 
# Обратный результат, возвращает Нет, если результат Да

x = 4 
result = not(x < 5 or x < 10) # Output: False, Вывод Нет
print(result)


# Boolean operators


# Operator 'and'

# False and False = False 
# True and True = True 
# True and False = False 


# Operator 'or'

# False or False = False 
# True and True = True 
# False or False = False 

# Operator 'not'
# not True = False 
# not False = True 


# Python Identity operators
# Индификационные операторы в Пайтон

# Operator 'is'

# Returns True if both variables are the same object
# Возвращает Да, если обе переменные явл. одним и тем же объектом


# Returns true if both variables are not the same object
# Возвращает, Да, если обе переменные не явл. одним и тем же объектом.

