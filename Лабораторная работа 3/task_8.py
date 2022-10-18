money_capital = 10000
salary = 5000
spend = 6000
increase = 0.05

month = 0
total_money = money_capital  # общее количесвто денег на начало расчета до вычета затрат
while total_money > spend:
    total_money = total_money + salary - spend  # после вычета затрат
    spend = spend * (1 + increase)  # пересчет затрат
    month = month + 1  # подсчет количества месяцев
print(month)
