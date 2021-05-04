input_str = input("Enter some text: ")

split_str = input_str.split()

string_number = 0
for word in split_str:
    print(f"{string_number:02d}: {word[0:10]}")
    string_number += 1
