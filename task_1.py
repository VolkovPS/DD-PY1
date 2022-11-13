from pprint import pprint
start = 0  # Уход от магических чисел в списке
finish = 15
lst = [{"bin": bin(i), "dec": i, "hex": hex(i), "oct": oct(i)} for i in range(start, finish + 1)]  #Создание списка словарей
pprint(lst)
