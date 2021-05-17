with open("text_3.txt", "r", encoding="utf-8") as textFile:
    lines = textFile.readlines()
    print("Employees with less than 20000 salary:")
    salary_sum = 0
    employees_count = 0
    for line in lines:
        s_line = line.split()
        if len(s_line) < 2:
            continue
        name = s_line[0]
        salary = s_line[1]
        f_salary = float(salary)
        salary_sum += f_salary
        employees_count += 1
        if f_salary < 20000:
            print(name)
    print()
    print(f"Average salary: {salary_sum / employees_count:.2f}")
