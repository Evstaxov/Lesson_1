while True:
    days = 1
    start_km = int(input("Стартовый результат: "))
    last_km = int(input("Финальный результат: "))
    if start_km <= 0 or last_km < 0:
        print("Результат должен быть больше нуля")
    else:
        while start_km < last_km:
            start_km += start_km * 0.1
            days += 1
            print(f"Спортсмен добьётся результата за {days} дней")
            break
