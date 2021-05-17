import json

with open("text_7.txt", "r", encoding="utf-8") as textFile:
    lines = textFile.readlines()
    firm_info = []
    firm_profits = {}
    average_profit = {}
    profitable_companies_count = 0
    profit_sum = 0
    for line in lines:
        s_line = line.split()
        firm_name = s_line[0]
        firm_status = s_line[1]
        firm_income = int(s_line[2])
        firm_costs = int(s_line[3])
        firm_profit = firm_income - firm_costs
        if firm_profit > 0:
            profitable_companies_count += 1
            profit_sum += firm_profit
        firm_profits[firm_name] = firm_profit

    average_profit["average_profit"] = profit_sum / profitable_companies_count
    firm_info.append(firm_profits)
    firm_info.append(average_profit)

    with open("text_7.json", "w", encoding="utf-8") as jsonFile:
        json.dump(firm_info, jsonFile, ensure_ascii=False, indent=4)




