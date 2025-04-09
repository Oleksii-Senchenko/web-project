# Створіть функцію divide, яка приймає два числа a та b і повертає результат ділення a на b.
# Додайте декоратор @check_division_error до цієї функції.
from division_error import check_division_error



@check_division_error
def divide(a,b):
    return a / b

result = divide(10,2)
anti_result = divide(10,2)

print(result)
print(anti_result)