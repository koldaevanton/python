with open("text_1.txt", "w", encoding="utf-8") as textFile:
    while True:
        next_str = input("Enter next string (leave empty to quit): ")
        if not next_str:
            break
        textFile.write(f"{next_str}\n")
