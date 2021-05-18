class Stationery:
    title: str

    def __init__(self, title):
        self.title = title

    def draw(self):
        print("Запуск отрисовки.")


class Pen(Stationery):
    def __init__(self):
        self.title = "ручка"

    def draw(self):
        print(f"Запуск отрисовки с помощью '{self.title}' синим цветом.")


class Pencil(Stationery):
    def __init__(self):
        self.title = "карандаш"

    def draw(self):
        print(f"Запуск отрисовки с помощью '{self.title}' серым цветом.")


class Handle(Stationery):
    def __init__(self):
        self.title = "маркер"

    def draw(self):
        print(f"Запуск отрисовки с помощью '{self.title}' красным цветом.")


pen = Pen()
pen.draw()

pencil = Pencil()
pencil.draw()

handle = Handle()
handle.draw()