month = int(input("Enter month number (1-12): "))

if month < 1 or month > 12:
    print("Error! Month number must be 1-12")
else:
    seasons_list = ["winter", "winter", "spring", "spring", "spring", "summer", "summer", "summer",
                    "fall", "fall", "fall", "winter"]

    print("List solution: ")
    print(seasons_list[month-1])

    seasons = {1: "winter", 2: "winter", 3: "spring", 4: "spring", 5: "spring", 6: "summer", 7: "summer", 8: "summer",
               9: "fall", 10: "fall", 11: "fall", 12: "winter"}

    print("Dict solution: ")
    print(seasons.get(month))
