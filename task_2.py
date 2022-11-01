def get_count_char(str_):
    dict1 = {}
    for letters in str_.lower():
        if letters.isalpha():
            dict1[letters] = dict1.get(letters, 0) + 1
    return dict1

def percent(dict):
    dict_percents = {}
    sum_dict = sum(dict.values())
    for letters in dict:
        dict_percents[letters] = round((dict.get(letters, 0) / sum_dict * 100), 3)
    return dict_percents

main_str = """
    Данное предложение будет разбиваться на отдельные слова. 
    В качестве разделителя для встроенного метода split будет выбран символ пробела. На выходе мы получим список отдельных слов. 
    Далее нужно отсортировать слова в алфавитном порядке, а после сортировки склеить их с помощью метода строк join. Приступим!!!!
"""

print(get_count_char(main_str))
dict_percent = get_count_char(main_str)
print(percent(dict_percent))
