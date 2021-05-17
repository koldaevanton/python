with open("text_6.txt", "r", encoding="utf-8") as textFile:
    lines = textFile.readlines()
    my_dict = {}
    for line in lines:
        s_line = line.split(":")
        name = s_line[0]
        hours = [int(i) for s in s_line[1].split() for i in s.split("(") if i.isdigit()]
        my_dict[name] = sum(hours)

    print(my_dict)
