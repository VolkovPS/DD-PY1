list_numbers = [2, -93, -2, 8, -36, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]
max_index = 0
max_value = 0
for i in range(len(list_numbers)):  # проверка всего списка
    max_value = list_numbers[max_index]
    current_value = list_numbers[i]
    if current_value > max_value:
        max_value = current_value  # замена максимального значения на текущее
        max_index = i  # замена индекса
list_numbers[max_index], list_numbers[-1] = list_numbers[-1], list_numbers[max_index]  # множественное присваивание

print(list_numbers)
