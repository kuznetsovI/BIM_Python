salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
months = 10  # Количество месяцев, которое планируется протянуть без долгов
increase = 0.03  # Ежемесячный рост цен
count = 0
dolg= 0
# TODO Рассчитайте подушку безопасности, чтобы протянуть 10 месяцев без долгов
while count !=10:
    trat= spend-salary
    dolg += trat
    infl= spend* increase
    spend= spend + infl
    count += 1
print(f"Подушка безопасности, чтобы протянуть {months} месяцев без долгов:", round(dolg,2))
