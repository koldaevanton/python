first_result = int(input("Enter first day result (a): "))
target_result = int(input("Enter target result (b): "))

current_day = 1
current_result = first_result

while current_result < target_result:
    current_result *= 1.1
    current_day += 1

#print(f"Sportsman will achieve target result (more than {target_result} km) on {current_day} day.")
print(current_day)
