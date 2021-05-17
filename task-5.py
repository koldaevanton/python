from random import randint

with open("text_5.txt", "w+", encoding="utf-8") as textFile:
    # Part 1. Generate numbers and write to file
    numbers = [str(randint(0, 100)) for i in range(20)]
    str_numbers = " ".join(numbers)
    textFile.write(str_numbers)

    # Part 2. Read file and calculate sum
    textFile.seek(0)
    sum = 0
    content = textFile.readline()
    s_content = content.split()
    for s_num in s_content:
        num = float(s_num)
        sum += num

    print(f"Sum of all numbers: {sum:.2f}")
