import random

def get_unique_list_numbers(left_boarder, right_boarder, amount) -> list[int]:
    list_ran = random.sample(range(left_boarder, right_boarder + 1), amount)  #Переменные добавлены, чтобы уйти от магических числа
    return list_ran

list_unique_numbers = get_unique_list_numbers(-10, 10, 15)
print(list_unique_numbers)
print(len(list_unique_numbers) == len(set(list_unique_numbers)))
