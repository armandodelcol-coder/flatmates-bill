class Bill:
    """
    Object that contains data about a bill, such as
    total amount and period of teh bill.
    """

    def __init__(self, amount: float, period: str):
        self.period = period
        self.amount = amount


class Flatmate:
    """
    Creates a flatmate person who lives in the flat
    and pays a share of the bill.
    """

    def __init__(self, name: str, days_in_house: int):
        self.days_in_house = days_in_house
        self.name = name

    def pays(self, bill: Bill, flatmate2: "Flatmate"):
        weight = self.days_in_house / (self.days_in_house + flatmate2.days_in_house)
        to_pay = bill.amount * weight
        return to_pay


class PdfReport:
    """
    Creates a Pdf file that contains data about
    the flatmates such as their names, their due amounts
    and the period of the bill.
    """

    def __init__(self, filename: str):
        self.filename = filename

    def generate(self, flatmate1: Flatmate, flatmate2: Flatmate, bill: Bill):
        pass
