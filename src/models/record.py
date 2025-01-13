"""Import module to work with dates"""
from datetime import datetime
from src.models.fields import Name, Phone, Birthday, Email, Address

class Record:
    """
    Model of the record in the address book
    """
    def __init__(self, name = ""):
        self.name = Name(name)
        self.phones = []
        self.birthday = None
        self.email = None
        self.address = None

    def add_phone(self, phone = ""):
        """
        Method to add phone number to the record
        """
        result = self.find_phone(phone)
        if not isinstance(result, str):
            raise ValueError("Phone number already exists")
        self.phones.append(Phone(phone))
        return "Added mobile phone number."

    def add_email(self, email = ""):
        """
        Method to add email to the record
        """
        message = "Email added." if (self.email is None) else "Email updated."
        self.email = Email(email)
        return message

    def add_address(self, country = "", city = "", street = "", house = "", flat = ""):
        """
        Method to add address to the record
        """
        message = "Address added." if (self.address is None) else "Address updated."
        self.address = Address(country, city, street, house, flat)
        return message

    def remove_phone(self, phone: str):
        """
        Method to remove phone number from the record
        """
        phone = self.find_phone(phone)
        if isinstance(phone, str):
            return phone

        self.phones.pop(self.phones.index(phone))
        return "Mobile number has been deleted."

    def edit_phone(self, old_phone, new_phone):
        """
        Method to edit phone number in the record
        """
        result = self.find_phone(new_phone)
        if not isinstance(result, str):
            raise ValueError("Phone number already exists")
        phone = self.find_phone(old_phone)
        if isinstance(phone, str):
            return phone

        self.phones[self.phones.index(phone)] = Phone(new_phone)
        return "Mobile number has been changed."

    def find_phone(self, phone):
        """
        Method to find phone number in the record
        """
        for number in self.phones:
            if phone == number.value:
                return number
        return "Mobile number not found."

    def add_birthday(self, birthday):
        """
        Method to add user birthday in the record
        """
        message = "Birthday added." if (self.birthday is None) else "Birthday updated."
        self.birthday = Birthday(birthday)
        return message

    def __str__(self):
        birthday_value = (
            datetime.strftime(self.birthday.value, "%d.%m.%Y") if self.birthday else "No birthday"
            )

        return (
            "Contact name: " + self.name.value + " birthday: " + birthday_value
            + " phones: " + '; '.join(p.value for p in self.phones)
            + " email: " + (str(self.email) if self.email else 'no email')
            + " address: " + (str(self.address) if self.address else 'no address')
            )
