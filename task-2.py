my_list = []

while True:
    element = input("Enter a number (type 'q' to quit): ")
    if element == "q":
        break;
    my_list.append(element)

current_element_number = 0
while current_element_number + 1 < len(my_list):
    element1 = my_list.pop(current_element_number)
    element2 = my_list.pop(current_element_number)

    my_list.insert(current_element_number, element2)
    my_list.insert(current_element_number + 1, element1)

    current_element_number += 2

print(my_list)
