from itertools import count, cycle

my_num = int(input("Enter number to count from this to 20: "))

iter1 = count(my_num)

my_squares = []

for i in iter1:
    if i > 20:
        break
    print(i)
    my_squares.append(i**2)

iter2 = cycle(my_squares)

sum = 0

for i in iter2:
    print(i)
    sum += i
    if sum > 100000:
        break

print(f"Sum: {sum}")
