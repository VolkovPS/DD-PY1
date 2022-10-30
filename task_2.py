def get_count_char(str_):
    dict_ = {}
    DEFAULT_COUNT = 0
    for letters in str_.lower():
        if letters.isalpha:
            dict_[letters] = dict_.get(letters, DEFAULT_COUNT) + 1
    return dict_
...  # TODO посчитать количество каждой буквы в строке в аргументе str_

def percent (dict_):
    dict_percent = {}
    sum_dict = sum(dict_.values())
    for letters in dict_:
        dict_percent[letters] = round((dict_.get(letters)/sum_dict),2)
    return dict_percent


main_str = """
    Данное предложение будет разбиваться на отдельные слова. 
    В качестве разделителя для встроенного метода split будет выбран символ пробела. На выходе мы получим список отдельных слов. 
    Далее нужно отсортировать слова в алфавитном порядке, а после сортировки склеить их с помощью метода строк join. Приступим!!!!
"""

print(get_count_char(main_str))

