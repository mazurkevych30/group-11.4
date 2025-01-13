"""Import module that support UserDict type"""
from collections import UserDict
from datetime import datetime, timedelta


class AddressBook(UserDict):
    """
    Model of address book
    """
    def add_record(self, record):
        """
        Add record to the address book
        """
        if str(record.name).lower() in self.data:
            raise ValueError(f"AddressBook already have record with name {str(record.name)}")
        self.data[str(record.name).lower()] = record

    def find(self, name: str):
        """
        Find record by name in the address book
        """
        for name_record, record in self.data.items():
            if name_record == name.lower().strip():
                return record
        return None

    def delete(self, name: str):
        """
        Delete record from the address book by name
        """
        return self.data.pop(name.lower().strip(), None)

    def get_upcoming_birthdays(self, input_date : datetime) -> list:
        """Function that returns a list of contacts who have a birthday before a given date."""
        today = datetime.today().date()
        upcoming_birthdays = []

        for name, record in self.data.items():
            if record.birthday is None:
                continue
            birthday_this_year = record.birthday.value.date().replace(year=today.year)
            if today.month == 12 and today.day > 20:
                birthday_this_year = birthday_this_year.replace(year=birthday_this_year.year + 1)

            if birthday_this_year > today:
                if (birthday_this_year-today).days <= (input_date - today).days:
                    match birthday_this_year.weekday():
                        case 5:
                            birthday_this_year += timedelta(days=2)
                        case 6:
                            birthday_this_year += timedelta(days=1)

                    upcoming_birthdays.append({
                        "name": name,
                        "congratulation_date": datetime.strftime(birthday_this_year, "%d.%m.%Y")
                        })

        return upcoming_birthdays
