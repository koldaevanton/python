from random import randint

list = []
for i in range(10):
    list.append(randint(0, 1000))

new_list = [el for el in list[1:] if el > list[list.index(el) - 1]]

print(f"Initial list:   {list}")
print(f"Processed list: {new_list}")
