class Road:
    _length: int()
    _width: int()

    def __init__(self, len, width):
        self._length = len
        self._width = width

    def calculate_mass(self, thickness):
        return self._width * self._length * 25 * thickness


my_road = Road(20, 5000)
print(my_road.calculate_mass(5))
