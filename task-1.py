def my_divide(a, b):
    try:
        return a / b;
    except ZeroDivisionError:
        return None


while True:
    dividend_str = input("Enter dividend: ")
    try:
        dividend = int(dividend_str)
        break
    except ValueError:
        print("Error! Enter only a number!")

while True:
    divisor_str = input("Enter divisor: ")
    try:
        divisor = int(divisor_str)
        break
    except ValueError:
        print("Error! Enter only a number!")

result = my_divide(dividend, divisor)
if result is None:
    print("Division by zero is not allowed!")
else:
    print(f"Result: {result}")
