with open("text_2.txt", "r", encoding="utf-8") as textFile:
    lines = textFile.readlines()
    print(f"Lines count: {len(lines)}")
    for line_number, line in enumerate(lines):
        print(f"Words in {line_number + 1} line: {len(line.split())}")
