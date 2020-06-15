revenue = float(input("Введите значение выручки(&)- "))
costs = float(input("Введите значение издержек(&)- "))
result = revenue - costs
if result > 0:
    print(f"Прибыль: {result}&")
    print(f"Рентабельность выручки: {result / revenue:.3f}&")
    per = int(input("Сколько сотрудников работают в вашей компании? "))
    print(f"Прибыль сотрудников составляет {result / per:.3f}&")
elif result < 0:
    print(f"Убыток вашей компании составил: {result}&")
else:
    print(f"Ваш результат равен 0")