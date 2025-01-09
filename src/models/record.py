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
        self.phones.append(Phone(phone))
        return "Added mobile phone number."

    def add_email(self, email = ""):
        """
        Method to add email to the record
        """
        self.email = Email(email)
        return "Email added."
    
    # def add_address(self, address = ""):
    #     """
    #     Method to add address to the record
    #     """
    #     self.address = Address(address)
    #     return "Address added."

    def add_address(self, country = "", city = "", street = "", house = "", flat = ""):
        """
        Method to add address to the record
        """
        self.address = Address(country, city, street, house, flat)
        return "Address added."
    
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
        self.birthday = Birthday(birthday)
        return "Birthday updated."

    def __str__(self):
        birthday_value = (
            datetime.strftime(self.birthday.value, "%d.%m.%Y") if self.birthday else "No birthday"
            )
        return f"Contact name: {self.name.value}, birthday: {birthday_value},\
        phones: {'; '.join(p.value for p in self.phones)},\
        email: {self.email if self.email else 'no email'},\
        address: {self.address if self.address else 'no address'}"
    
    # address: {self.address if self.address else 'no address'}