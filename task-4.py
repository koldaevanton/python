class Warehouse:
    def __init__(self, max_capacity):
        self.max_capacity = max_capacity
        self.items = {}

    def add_item(self, item, count):
        if not Warehouse.validate_count(count):
            return None
        if item.volume * count + self.total_volume() > self.max_capacity:
            print("Max capacity exceeded!")
            return None
        else:
            self.items[item] = count

    def total_volume(self):
        total_volume = 0
        for item in self.items.keys():
            total_volume += item.volume * self.items[item]
        return total_volume

    @staticmethod
    def validate_count(count):
        if type(count).__name__ != "int":
            print("Count must be an integer")
            return False
        if count < 0:
            print("Count must be positive")
            return False
        return True


    def transfer_item(self, needed_type, needed_count):
        types = ["printer", "scanner", "xerox"]
        found_units = 0
        for my_type in types:
            if needed_type.lower() == my_type:
                for item in self.items.keys():
                    if type(item).__name__.lower() == my_type:
                        found_units += self.items[item]
        if needed_count > found_units:
            print(f"We don't have {needed_count} {needed_type}s in stock.")
        else:
            items_to_transfer = {}
            items_left = needed_count
            for my_type in types:
                if needed_type.lower() == my_type:
                    for item_to_pick in self.items.keys():
                        if type(item_to_pick).__name__.lower() == my_type:
                            if items_left > self.items[item_to_pick]:
                                items_to_transfer[item_to_pick] = self.items[item_to_pick]
                                items_left -= self.items[item_to_pick]
                                self.items[item_to_pick] = 0
                            else:
                                items_to_transfer[item_to_pick] = items_left
                                self.items[item_to_pick] -= items_left
                                items_left = 0
            print(f"{needed_count} {needed_type}s has been transferred to the company.")
            return items_to_transfer


class Item:
    def __init__(self, price, weight, volume):
        self.price = price
        self.weight = weight
        self.volume = volume

    def __str__(self):
        return f"{type(self).__name__} ({self.price}/{self.weight}/{self.volume})"


class Printer(Item):
    color: bool
    speed: int


class Scanner(Item):
    resolution: int


class Xerox(Item):
    has_tray: bool


my_warehouse = Warehouse(20000)
xerox1 = Xerox(100, 50, 20)
my_warehouse.add_item(xerox1, 200)

printer1 = Printer(50, 25, 10)
my_warehouse.add_item(printer1, 100)

printer2 = Printer(100, 25, 10)
my_warehouse.add_item(printer2, 200)

printer3 = Printer(200, 25, 10)
my_warehouse.add_item(printer3, 300)

scanner1 = Scanner(50, 30, 8)
my_warehouse.add_item(scanner1, "100")

transfer = my_warehouse.transfer_item("printer", 350)
if transfer is not None:
    for transfer_item in transfer.keys():
        print(f"{transfer_item}: {transfer[transfer_item]}")
