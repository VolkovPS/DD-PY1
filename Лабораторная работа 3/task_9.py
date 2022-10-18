salary = 5000  # зарплата
spend = 6000  # траты
months = 10  # количество месяцев
increase = 0.03  # рост цен

need_money = 0  # количество денег, чтобы прожить 10 месяцев
sum_spend = 0

for i in range(months):  # перебор всех месяцев
    sum_spend = sum_spend + spend  # нахождение суммарных затрат
    spend = spend * (1 + increase)  # изменение ежемесячных расходов
need_money = sum_spend - salary * months  # нахождение финансовой подушки
print(round(need_money))
