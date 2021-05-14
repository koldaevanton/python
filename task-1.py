from sys import argv

script_name, working_time, price_per_hour, bonus = argv

salary = int(working_time) * int(price_per_hour) + int(bonus)

print(salary)
