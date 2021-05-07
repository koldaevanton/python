def my_func(x, y):
    """Raises real positive base number into integer negative power

    :param x: real positive base
    :param y: integer negative power
    :return: A number representing the given real positive base taken to the power of the given
    integer negative exponent.
    """
    if x <= 0:
        print("Error! x is not positive!")
        return
    if y >= 0:
        print("Error! y is not negative!")
        return
    if not isinstance(y, int):
        print("Error! y is not integer!")
        return

    divisor = 1
    for i in range(abs(y)):
        divisor *= x

    return 1 / divisor


print(help(my_func))
x_str = input("Enter real positive base: ")

try:
    x_float = float(x_str)
except ValueError:
    print("Error! Use only real positive number as base!")
    exit()

if x_float <= 0:
    print("Error! Use only real positive number as base!")
    exit()

y_str = input("Enter integer negative power: ")

try:
    y_int = int(y_str)
except ValueError:
    print("Error! Use only negative integer number as power!")
    exit()

if y_int >= 0:
    print("Error! Use only negative integer number as power!")
    exit()

print(my_func(x_float, y_int))
