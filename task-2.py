class MyZeroDivision(Exception):
    def __init__(self, error_msg):
        print(error_msg)


divisible = int(input("Введите делимое: "))
divisor = int(input("Введите делитель: "))

try:
    if divisor == 0:
        raise MyZeroDivision("Деление на ноль невозможно")
    else:
        print(divisible/divisor)
except MyZeroDivision:
    pass
