import re
from datetime import datetime

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
    def __init__(self, value: str):
        if not value.strip():
            raise Exception("Name required field.")
        super().__init__(value.strip())

class Phone(Field):
    def __init__(self, phone):
        if not re.match(r'^\d{10}$', phone):
            raise Exception("The phone number must be 10 digits.")
        super().__init__(phone)

class Birthday(Field):
    def __init__(self, value):
        try:
            self.value = datetime.strptime(value, "%d.%m.%Y")
        except ValueError:
            raise ValueError("Invalid date format. Use DD.MM.YYYY")

class Email(Field):
    """
    Model of email field with validation
    """
    def __init__(self, email):
        if not re.match(r"(\w+)@(\w+\.\w+)", email):
            raise Exception("Invalid email.")
        super().__init__(email)
class Address:
    """
    Model of address
    """
    def __init__(self, country: str, city: str, street: str, house: str, flat: str):
        self.country = country.strip()
        self.city = city.strip()
        self.street = street.strip()
        self.house = house.strip()
        self.flat = flat.strip()

    def __str__(self) -> str:
        return f"{self.country+',' if self.country else ''} {self.city+',' if self.city else ''} \
        {self.street+',' if self.street else ''} {self.house+',' if self.house else ''} \
        {self.flat if self.flat else ''} "


# class Address(Field):
#     """
#     Model of address
#     """
#     def __init__(self, address: str):
#         super().__init__(address)