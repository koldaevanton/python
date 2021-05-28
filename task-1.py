class Date:
    def __init__(self, date):
        self.date = date
        converted = Date.convert(date)
        if converted is None:
            return
        self.day = converted[0]
        self.month = converted[1]
        self.year = converted[2]
        print(f"Day: {self.day} Month: {self.month} Year: {self.year}")

    @classmethod
    def convert(cls, date):
        s_date = date.split("-")
        if len(s_date) != 3:
            print("Error! Incorrect format!")
            return None
        try:
            day = int(s_date[0])
            month = int(s_date[1])
            year = int(s_date[2])
        except error:
            print(error)
            return None

        result = Date.validate(day, month, year)
        if result:
            return [day, month, year]
        else:
            return None

    @staticmethod
    def validate(day, month, year):
        days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        if year > 2100 or year < 1900:
            print("Error! Year is not valid")
            return False
        if year % 4 == 0 and year != 2000:
            days_in_month[1] += 1
        if month < 1 or month > 12:
            print("Error! Month is not valid")
            return False
        if day < 1 or day > days_in_month[month - 1]:
            print("Error! Day is not valid")
            return False
        return True


my_date = Date("21-05-2021")
my_date2 = Date("32-05-2021")
my_date3 = Date("0-05-2021")
my_date4 = Date("21-00-2021")
my_date5 = Date("21-13-2021")
my_date6 = Date("21-00-2021")
my_date7 = Date("21-02-20")
my_date8 = Date("21.02.2021")
