"""Module with basic classes"""
import re
from datetime import datetime

class Field:
    """General field class"""
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
    """User name field class"""
    def __init__(self, value: str):
        if not value.strip():
            raise ValueError("Name is required field.")
        super().__init__(value.strip())

class Phone(Field):
    """User phone field class"""
    def __init__(self, phone):
        if not re.match(r'^\d{10}$', phone):
            raise ValueError("The phone number must be 10 digits.")
        super().__init__(phone)

class Birthday(Field):
    """User birthday field class"""
    def __init__(self, value):
        try:
            super().__init__(datetime.strptime(value, "%d.%m.%Y"))
        except ValueError as exc:
            raise ValueError("Invalid date format. Use DD.MM.YYYY") from exc

class Email(Field):
    """
    Model of email field with validation
    """
    def __init__(self, email):
        if not re.match(r"(\w+)@(\w+\.\w+)", email):
            raise ValueError("Invalid email.")
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
        return (
            f"{self.country + ',' if self.country else ''} "
            f"{self.city + ',' if self.city else ''} "
            f"{self.street + ',' if self.street else ''} "
            f"{self.house + ',' if self.house else ''} "
            f"{self.flat if self.flat else ''}"
            )
