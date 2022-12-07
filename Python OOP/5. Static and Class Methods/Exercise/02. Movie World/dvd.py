import calendar


class DVD:
    def __init__(self, name: str, id: int, creation_year: int, creation_month: str, age_restriction: int):
        self.name = name
        self.id = id
        self.creation_year = creation_year
        self.creation_month = creation_month
        self.age_restriction = age_restriction
        self.is_rented = False


    @classmethod
    def from_date(cls, id: int, name: str, date: str, age_restriction: int): 
        day, month, year = [int(x) for x in date.split(".")]
        return cls(name, id, year, calendar.month_name[month], age_restriction)


    def __repr__(self):
        rented = "not remted"
        if self.is_rented:
            rented = "remted"

        return f"{self.id}: {self.name} ({self.creation_month} {self.creation_year}) has age restriction {self.age_restriction}. Status: {'rented' if self.is_rented else 'not rented'}"


