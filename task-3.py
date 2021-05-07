def sum_of_max_two(x1, x2, x3):
    list_of_args = [x1, x2, x3]
    min_element = min(list_of_args)
    return sum(list_of_args) - min_element


print(sum_of_max_two(5,7,10))
