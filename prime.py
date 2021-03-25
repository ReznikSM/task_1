while True:
    try:
        a = int (input("Введите число: "))
    except ValueError:
        print("Неверный формат")
        continue
    else:
        break
if a < 2:
    print("Число ни простое и ни сложное")
    quit()
n=0
for i in range(2, a // 2+1):
    if (a % i == 0):
        n = n+1
if (n <= 0):
    print("Число простое")
else:
    print("Число сложное")