def int_func(input_string):
    words = input_string.split()
    output = ""
    for word in words:
        allowed_word = True
        for symbol in word:
            ord_symbol = ord(symbol)
            if ord_symbol < 97 or ord_symbol > 122:
                allowed_word = False
                break

        if allowed_word:
            output += f"{word.title()} "

    return output.rstrip()


print(int_func("nice авп ъghj jапро hjjпаро вапрghgh cool"))
