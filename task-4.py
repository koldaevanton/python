with open("text_4.txt", "r", encoding="utf-8") as textFile:
    with open("text_4a.txt", "w", encoding="utf-8") as writeFile:
        translations = {
            "One": "Один",
            "Two": "Два",
            "Three": "Три",
            "Four": "Четыре",
        }
        lines = textFile.readlines()
        for line in lines:
            s_line = line.split()
            write_line = ""
            for word in s_line:
                write_word = word
                if word in translations:
                    write_word = translations[word]
                write_line += f"{write_word} "
            writeFile.write(f"{write_line.rstrip()}\n")
