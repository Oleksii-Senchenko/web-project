# Створіть декоратор @check_division_error, який перевіряє, чи немає ділення на нуль в функціях.
# Якщо при виклику функції сталася помилка ділення на нуль, декоратор повинен вивести повідомлення про
# помилку та завершити виконання програми.

def check_division_error(func):
    def wrapper(a,b):
        try:
            return func(a, b)
        except ZeroDivisionError:
            print("Error: Division Error...")
            return None
    return wrapper


@check_division_error
def division(a,b):
    return round(a/b,1)


result = division(10,3)
anti_result = division(10,0)

print(result)
print(anti_result)
