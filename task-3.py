class Worker:
    name: str
    surname: str
    position: str
    _income: {}

    def __init__(self, pos):
        if pos == "Janitor":
            self._income = {
                "wage": 500,
                "bonus": 50
            }
        elif pos == "Director":
            self._income = {
                "wage": 500000,
                "bonus": 50000
            }
        else:
            self._income = {
                "wage": 0,
                "bonus": 0
            }


class Position(Worker):
    def get_full_name(self):
        return f"{self.name} {self.surname}"

    def get_total_income(self):
        return self._income["wage"] + self._income["bonus"]


janitor = Position("Janitor")
janitor.name = "John"
janitor.surname = "Doe"
print(janitor.get_full_name())
print(f"Income: {janitor.get_total_income()}")
print()

director = Position("Director")
director.name = "Agent"
director.surname = "K"
print(director.get_full_name())
print(f"Income: {director.get_total_income()}")
print()
