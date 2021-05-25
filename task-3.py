class Cell:
    count: int

    def __init__(self, count):
        self.count = count

    def __add__(self, other):
        return Cell(self.count + other.count)

    def __sub__(self, other):
        new_count = self.count - other.count
        if new_count > 0:
            return Cell(new_count)
        else:
            print("Вычитание невозможно. Итоговое число ячеек меньше нуля!")

    def __mul__(self, other):
        return Cell(self.count * other.count)

    def __truediv__(self, other):
        return Cell(round(self.count / other.count))

    def make_order(self, row_cells_count):
        rest_cells = self.count
        result = ""
        while rest_cells > row_cells_count:
            result += f"{row_cells_count * '*'}\n"
            rest_cells -= row_cells_count

        result += f"{rest_cells * '*'}"
        return result


cell_with_2 = Cell(2)
cell_with_3 = Cell(3)
cell_with_5 = Cell(5)

mega_cell = Cell(20)
print((mega_cell - cell_with_5 - cell_with_3).make_order(5))
print()
print((cell_with_5 * cell_with_3).make_order(5))
print()
print(((mega_cell + cell_with_2) / cell_with_3).make_order(3))
