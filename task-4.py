number = int(input("Enter positive decimal: "))

max_digit = 0
number_left = number

while number_left > 0:
    last_digit = number_left % 10
    number_left = number_left // 10

    if last_digit > max_digit:
        max_digit = last_digit

print(max_digit)
