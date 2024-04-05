def analyze_numbers1():
    from_num = int(input("Enter a number from: "))
    to_num = int(input("Enter a number to: "))
    for i in range(from_num, to_num + 1):
        if i % 7 == 0:
            print(i, "is divisible by 7")


def analyze_numbers2():
    from_num = int(input("Enter a number from: "))
    to_num = int(input("Enter a number to: "))
    print([i for i in range(from_num, to_num + 1)])
    print([i for i in range(from_num, to_num + 1)][::-1])
    print([i for i in range(from_num, to_num + 1) if i % 7 == 0])
    print(len([i for i in range(from_num, to_num + 1) if i % 5 == 0]))


def analyze_numbers3():
    from_num = int(input("Enter a number from: "))
    to_num = int(input("Enter a number to: "))
    list_of_numbers = []
    for i in range(from_num, to_num + 1):
        if i % 7 == 0 and i % 3 == 0:
            list_of_numbers.append("FizzBuzz")
        elif i % 7 == 0:
            list_of_numbers.append("Buzz")
        elif i % 3 == 0:
            list_of_numbers.append("Fizz")
        else:
            list_of_numbers.append(i)

    print(list_of_numbers)


def analyze_numbers4():
    from_num = int(input("Enter a number from: "))
    to_num = int(input("Enter a number to: "))
    even_numbers = []
    odd_numbers = []
    nums_multiples_9 = []
    for i in range(from_num, to_num + 1):
        if i % 2 == 0:
            even_numbers.append(i)
        else:
            odd_numbers.append(i)
        if i % 9 == 0:
            nums_multiples_9.append(i)

    sum_even_numbers = sum(even_numbers)
    sum_odd_numbers = sum(odd_numbers)
    sum_nums_multiples_9 = sum(nums_multiples_9)

    print(f"Сумма четных чисел: {sum_even_numbers}")
    print(f"Сумма нечетных чисел: {sum_odd_numbers}")
    print(f"Сумма чисел кратных 9: {sum_nums_multiples_9}")

    print(f"Среднее четных: {sum_even_numbers / len(even_numbers)}")
    print(f"Среднее нечетных: {sum_odd_numbers / len(odd_numbers)}")
    print(f"Среднее чисел кратных 9: {sum_nums_multiples_9 / len(nums_multiples_9)}")


def line_symbol():
    length = int(input("Enter a number: "))
    symbol = input("Enter a symbol: ")

    for i in range(length):
        print(symbol)
