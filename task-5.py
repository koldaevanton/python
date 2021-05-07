def calculate_sum():
    total_sum = 0

    while True:
        numbers = input("Enter numbers separated with spaces (type 'q' to quit): ")
        current_sum = 0
        list_of_numbers = numbers.split()
        for number in list_of_numbers:
            if number == 'q':
                total_sum += current_sum
                print(f"Current sum: {current_sum}; Total sum: {total_sum}")
                return
            else:
                try:
                    int_number = int(number)
                except ValueError:
                    print(f"Entered value '{number}' is not an integer (or a quit symbol)!")
                    continue

                current_sum += int_number

        total_sum += current_sum
        print(f"Current sum: {current_sum}; Total sum: {total_sum}")


calculate_sum()
