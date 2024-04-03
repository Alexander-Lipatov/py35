def math_operations():
    nums = input("Введите числа через пробел: ").split(" ")
    nums = map(int, nums)
    try:
        choice = int(input("Выберите вариант: \n"
                           "1. Сумма \n"
                           "2. Произведение \n"
                           "3. Максимальное \n"
                           "4. Минимальное \n"
                           "5. Среднее \n"))

        if choice == 1:
            res = sum(nums)
        elif choice == 2:
            res = 1
            for num in nums:
                res *= num
        elif choice == 3:
            res = max(nums)
        elif choice == 4:
            res = min(nums)
        elif choice == 5:
            res = sum(nums) / len(nums)
        else:
            raise ValueError("Введите число от 1 до 5 для выбора варианта.")

        print(res)

    except ValueError as e:
        print(e)
    except Exception:
        print("Произошла ошибка. Пожалуйста, введите корректный вариант!")


def convert_meters():
    try:
        meters = float(input("Введите количество метров: "))
        choice = int(input("Выберите вариант перевода: \n"
                           "1. Метры в мили \n"
                           "2. Метры в дюймы \n"
                           "3. Метры в ярды \n"))

        if choice == 1:
            miles = meters * 0.000621371
            print(f"{meters} метров = {miles} миль")
        elif choice == 2:
            inches = meters * 39.3701
            print(f"{meters} метров = {inches} дюймов")
        elif choice == 3:
            yards = meters * 1.09361
            print(f"{meters} метров = {yards} ярдов")
        else:
            print("Пожалуйста, введите число от 1 до 3 для выбора варианта.")

    except ValueError:
        print("Пожалуйста, введите корректное число.")
    except Exception as e:
        print("Произошла ошибка:", e)


def print_day():
    day_num = int(input("Введите номер дня недели: "))

    match day_num:
        case 1:
            print("Понедельник")
        case 2:
            print("Вторник")
        case 3:
            print("Среда")
        case 4:
            print("Четверг")
        case 5:
            print("Пятница")
        case 6:
            print("Суббота")
        case 7:
            print("Воскресенье")
        case _:
            print("Введите корректное число от 1 до 7 для выбора дня недели.")


def print_months():
    month_list = ["Январь",
                  "Февраль",
                  "Март",
                  "Апрель",
                  "Май",
                  "Июнь",
                  "Июль",
                  "Август",
                  "Сентябрь",
                  "Октябрь",
                  "Ноябрь",
                  "Декабрь",]
    month_num = int(input("Введите номер месяца: "))
    if month_num > 12 or month_num <= 0:
        print("Введите корректное число от 1 до 12 для выбора месяца.")
    else:
        print(month_list[month_num - 1])


def check_number(num):
    if num > 0:
        print("Number is positive")
    elif num < 0:
        print("Number is negative")
    else:
        print("Number is equal to zero")


def print_check_number():
    try:
        number = float(input("Введите число: "))
        check_number(number)
    except ValueError:
        print("Пожалуйста, введите корректное число.")
    except Exception as e:
        print("Произошла ошибка:", e)


def equality_check():
    numbers = input('numbers: ').strip().split(" ")
    print(numbers)
    if len(numbers) != 2:
        raise ValueError("Чисел не должно быть больше двух! Введите 2 числа!")

    if numbers[0] == numbers[1]:
        print("Введенные числа равны!")
    else:
        print(sorted(numbers))


def compare_numbers():
    try:
        num1 = float(input("Введите первое число: "))
        num2 = float(input("Введите второе число: "))

        if num1 == num2:
            print("Введенные числа равны.")
        else:
            # Сортировка чисел и вывод в порядке возрастания
            sorted_numbers = sorted([num1, num2])
            print("Введенные числа в порядке возрастания:", sorted_numbers)

    except ValueError:
        print("Пожалуйста, введите корректные числа.")
    except Exception as e:
        print("Произошла ошибка:", e)


def fizz_buzz():
    num = int(input("Введите число от 1 до 100: "))

    try:
        if num < 1 or num > 100:
            raise ValueError("Введите число от 1 до 100!")

        if num % 3 == 0 and num % 5 == 0:
            print("FizzBuzz")
        elif num % 3 == 0:
            print("Fizz")
        elif num % 5 == 0:
            print("Buzz")
        else:
            print(num)
    except Exception as e:
        print("Произошла ошибка:", e)


def degree():
    num = int(input("Введите число: "))
    degree = int(input("Введите степень возведения от 0 до 7: "))

    if degree > 7 or degree < 0:
        raise ValueError("Введите степень возведения от 0 до 7!")
    print(num ** degree)


def calc_cost_conversation():
    cost = float(input("Введите стоимость разговора одной минуты: "))
    from_operator = input("Введите оператор отправителя: ")
    to_operator = input("Введите оператор получателя: ")


def salary_manager(sales):
    salary = 200
    percentage_of_sales = 3 if sales < 500 else 5 if sales < 1000 else 8
    result_salary = salary + sales * percentage_of_sales/100
    print(f"Зарплата составляет {result_salary} рублей")
    return result_salary


def salary():
    dict_managers = {}
    
    for manager in range(1, 4):
        manager_sales = int(input(f"Введите сумму продаж менеджера "))
        name_manager = 'manager_' + str(manager)
        salary = salary_manager(manager_sales)
        dict_managers[name_manager] = salary

    for key, value in dict_managers.items():
        if value == max(dict_managers.values()):
            print(f"Менеджер с самым высокой зарплатой: {key}")
            dict_managers[key] = value + 200
            print(f"Менеджер {key} получает премию за работу 200$")

        print(f"Зарплата менеджера {key} равна {value} рублей")
    
    



        



salary()
