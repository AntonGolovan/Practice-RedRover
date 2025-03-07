def addition_numbers(num_1, num_2):
    print(f"{num_1} + {num_2} = {num_1 + num_2}")

def subtraction_numbers(num_1, num_2):
    print(f"{num_1} - {num_2} = {num_1 - num_2}")

def multiplication_numbers(num_1, num_2):
    print(f"{num_1} * {num_2} = {num_1 * num_2}")

def division_numbers(num_1, num_2):
    print(f"{num_1} / {num_2} = {num_1 / num_2}")



while True:
    try:
        operations = ["+", "-", "*", "/"]
        numbers_1 = float(input("Введите первое число: "))
        while True:
            operation = input("Введите какую операцию хотите выполнить: ")
            if operation in operations:
                break
            else:
                print("Некорректный ввод! Попробуйте ввести операцию: \"+\", \"-\", \"*\", \"/\"")
        numbers_2 = float(input("Введите второе число: "))

        match operation:
            case "+":
                addition_numbers(numbers_1, numbers_2)
            case "-":
                subtraction_numbers(numbers_1, numbers_2)
            case "*":
                multiplication_numbers(numbers_1, numbers_2)
            case "/":
                division_numbers(numbers_1, numbers_2)
    except ZeroDivisionError:
        print("Вы не можете разделить на 0!")
    except ValueError:
        print("Некорректный ввод! Невозможно преобразовать строку в число. Попробуйте ввести число!")