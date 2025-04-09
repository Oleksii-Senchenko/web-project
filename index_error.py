# Створіть декоратор @check_index_error, який перевіряє, чи виходить
# індекс за межі списку при доступі до елементу. Якщо при виклику функції сталася помилка індексації,
# декоратор повинен вивести повідомлення про помилку та завершити виконання програми.


def check_index_error(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except IndexError:
            print("Error: Index Error...")
            return None
    return wrapper


@check_index_error
def get_element_by_index(my_list, index):
    return my_list[index]


print(get_element_by_index([1, 2, 3], 5))
