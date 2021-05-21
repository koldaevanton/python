from abc import ABC, abstractmethod


class Clothes(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def calculate_cloth(self):
        pass


class Coat(Clothes):

    def __init__(self, size):
        self.__V = size

    @property
    def V(self):
        return self.__V

    @V.setter
    def V(self, V):
        if V > 60:
            self.__V = 60
        elif V < 40:
            self.__V = 40
        else:
            self.__V = V

    def calculate_cloth(self):
        return self.V/6.5 + 0.5


class Suit(Clothes):

    def __init__(self, height):
        self.__H = height

    @property
    def H(self):
        return self.__H

    @H.setter
    def H(self, H):
        if H > 220:
            self.__H = 220
        elif H < 130:
            self.__H = 130
        else:
            self.__H = H

    def calculate_cloth(self):
        return (self.__H * 2 + 0.3) / 100
        pass


my_suit = Suit(190)
print(f"{my_suit.calculate_cloth():.2f} м2")

my_coat = Coat(42)
print(f"{my_coat.calculate_cloth():.2f} м2")
