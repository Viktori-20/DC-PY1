money_capital = 10000
salary = 5000
spend = 6000
increase = 0.05

month = 0
# количество месяцев, которое можно прожить
overran = salary - spend
# превышение расходов над доходами

while money_capital + overran >= 0:
    overran = salary - spend
    # превышение расходов над доходами
    money_capital += overran
    # уменьшение подушки безопасности
    spend *= (1 + increase)
    # повышение трат
    month += 1
    if money_capital <= 0:
        break
        
print(month)
