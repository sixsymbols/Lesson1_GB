profit = float(input("Выручка"))
costs = float(input("Издержки"))
if profit > costs:
    print(f"Прибыльная. Рентабельность выручки составила {profit / costs:.2f}")
    workers = int(input("Введите количество сотрудников "))
    print(f"прибыль в расчете на одного сторудника сотавила {profit / workers:.2f}")
elif profit == costs:
    print("Работает в ноль")
else:
    print("Работает в убыток")