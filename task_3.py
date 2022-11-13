import random

def get_unique_list_numbers(a, b, p) -> list[int]:
    list_ran = random.sample(range(a, b + 1), p)  #Переменные добавлены, чтобы уйти от магических числа
    return list_ran

list_unique_numbers = get_unique_list_numbers(-10, 10, 15)
print(list_unique_numbers)
print(len(list_unique_numbers) == len(set(list_unique_numbers)))
