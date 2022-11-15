import random
import string
def get_random_password(p = 8) -> str:  #По умолчанию будет выводится восьмизначный пароль
    list_pass = ''.join(random.sample(string.ascii_uppercase + string.ascii_lowercase
                                      + string.digits, p))  #Объединение пароля для удобства копирования без запятых
    return list_pass

print(get_random_password())  #В качестве перменной можно задать длину пароля
