from functools import reduce


def multiply_all(el1, el2):
    return el1 * el2


my_list = [i for i in range(100, 1001) if i % 2 == 0]
print(reduce(multiply_all, my_list))
