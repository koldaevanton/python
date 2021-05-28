class NonInteger(Exception):
    def __init__(self, error):
        self.error = error


my_list = []

while True:
    txt = input("Введите следующее число (введите 'stop' для остановки): ")
    if txt == "stop":
        print(my_list)
        print("Конец.")
        break
    try:
        if not txt.isdigit():
            raise NonInteger("Не является числом")
    except NonInteger as err:
        print(err.error)
    else:
        my_list.append(int(txt))





