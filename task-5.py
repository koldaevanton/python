revenue = int(input("Enter company revenue: "))

expenses = int(input("Enter company expenses: "))

if expenses > revenue:
    print("Your company is unprofitable!")
else:
    print("Your company is profitable!")
    profit = revenue - expenses
    profitability = profit / revenue
    print(f"Profitability: {profitability:.2f}")
    employees = int(input("Enter number of employees: "))
    profit_for_employee = profit / employees
    print(f"Profit for one employee: {profit_for_employee:.2f}")
