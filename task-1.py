class TrafficLight:
    __color: string
    __running: bool

    def __init__(self):
        self.__color = "red"

    def switch(self):
        colors_list = ["red", "yellow", "green", "yellow"]
        self.__color = colors_list[colors_list.index(self.__color) + 1 % 3]

    def start(self):
        self.__running = true

    def stop(self):
        self.__running = false



