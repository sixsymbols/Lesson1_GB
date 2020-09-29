a = int(input("Первый день пробежки в км"))
b = int(input("Общий результат пробежки в км "))
result_d = 1
result_km = a
while result_km < b:
        a = a + 0.1 * a
        result_d += 1
        result_km = result_km + a
print(f"Вы достигнете столько км на %.d день" % result_d)