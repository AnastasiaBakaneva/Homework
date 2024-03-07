total_cost = 0  # Общая стоимость билетов
count_ticket = int(input("Введите количество билетов к покупке:"))
for i in range(1, count_ticket + 1):
    age = int(input("Введите возраст для каждого билета:"))
    if age < 18:
        total_cost += 0
    elif 18 <= age < 25:
        total_cost += 990
    elif age >= 25:
        total_cost += 1390
if count_ticket > 3:
    discount = total_cost / 100 * 10
    cost_disc = total_cost - discount  # Стоимость билетов со скидкой
    print("Скидка =", discount)
    print("Общая стоимость со скидкой=", total_cost, "-", discount, "=", cost_disc)
else:
    print("Общая стоимость =", total_cost)
