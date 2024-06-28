class Logger:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(Logger, cls).__new__(cls)
            cls._instance.init(*args, **kwargs)
        return cls._instance

    def init(self, destination="screen"):
        self.destination = destination

    def log(self, message):
        if self.destination == "screen":
            print(message)
        elif self.destination == "file":
            with open("log.txt", "a") as file:
                file.write(message + "\n")

# Создаем единственный объект класса Logger
logger = Logger(destination="screen")

def main():
    # Считываем данные от пользователя
    numbers = input("Введите набор чисел через пробел: ").split()
    numbers = [int(num) for num in numbers]
    file_path = input("Введите путь к файлу для сохранения данных: ")

    # Логируем данные
    logger.log(f"Введенные числа: {numbers}")

    # Сохраняем числа в файл
    with open(file_path, "w") as file:
        for num in numbers:
            file.write(f"{num}\n")

    # Находим максимум и минимум
    maximum = max(numbers)
    minimum = min(numbers)

    # Логируем максимум и минимум
    logger.log(f"Максимум: {maximum}")
    logger.log(f"Минимум: {minimum}")

    # Сохраняем максимум и минимум в файл
    with open(file_path, "a") as file:
        file.write(f"Максимум: {maximum}\n")
        file.write(f"Минимум: {minimum}\n")

    # Отображаем числа, максимум и минимум
    print("Числа:", numbers)
    print("Максимум:", maximum)
    print("Минимум:", minimum)

if __name__ == "__main__":
    main()