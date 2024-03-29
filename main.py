nums = input("Enter a numbers: ").split()
res = None

try:
    choice = int(input("Выбери вариант: \n"
                       "1.Сумма \n" +
                       "2.Произведение \n" +
                       "3.Максимальное \n"
                       "4.Минимальное \n"
                       "5.Среднее \n")
                 )
    for num in nums:
        if res is None:
            res = int(num)
            continue
        elif choice == 1:
            res += int(num)
        elif choice == 2:
            res *= int(num)
        elif choice == 3:
            res = max(res, int(num))
        elif choice == 4:
            res = min(res, int(num))
        elif choice == 5:
            res += int(num)
            res = res / len(nums)
    print(res)
except Exception:
    print("Введите корректный вариант!")
