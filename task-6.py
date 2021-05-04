goods = []

current_good = 0
while True:
    name = input("Введине название: ")
    price = int(input("Введите цену: "))
    count = int(input("Введите количество: "))
    unit = input("Введите единицы измерения: ")

    goods.append((current_good, {"название": name, "цена": price, "количество": count, "ед": unit}))

    current_good += 1
    next_good = input("Добавить товар? (y/n): ")

    if next_good == "n":
        break

analytics = {"название": [], "цена": [], "количество": [], "ед": []}

for good in goods:
    analytics.get("название").append(good[1].get("название"))
    analytics.get("цена").append(good[1].get("цена"))
    analytics.get("количество").append(good[1].get("количество"))
    analytics.get("ед").append(good[1].get("ед"))

print(analytics)
