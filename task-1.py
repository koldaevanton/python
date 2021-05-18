import time
from itertools import cycle


class TrafficLight:
    __color: str
    __running: bool

    def __init__(self):
        self.__color = "red"

    def switch(self):
        colors_list = ["red", "yellow", "green", "yellow"]
        for color in cycle(colors_list):
            self.__color = color
            yield color

    def start(self, seconds):
        self.__running = True
        color_times = {
            "green": 10,
            "yellow": 2,
            "red": 7
        }
        seconds_left = seconds
        switcher = self.switch()
        while seconds_left > 0:
            next(switcher)
            print(f"Current color is {self.__color}")
            time_to_switch = color_times[self.__color]
            time.sleep(time_to_switch)
            seconds_left -= time_to_switch

        print("Traffic Light stopped!")
        self.__running = False


tl = TrafficLight()
tl.start(60)
