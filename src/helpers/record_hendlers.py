from datetime import datetime
from src.helpers.input_error import input_error
from src.models.address_book import AddressBook
from src.models.record import Record






@input_error
def add_contact(args: list, book: AddressBook) -> str:
    name, phone, *_ = args
    record = book.find(name)
    message = "Contact updated."
    if record is None:
        record = Record(name)
        book.add_record(record)
        message = "Contact added."
    if phone:
        record.add_phone(phone)
    return message

@input_error
def delete_contact(args: list, book: AddressBook) -> str:
    name = args[0]
    record = book.find(name)    
    if record is None:        
        return "Contact not found."
    book.delete(name)
    return "Contact deleted."


@input_error
def show_all(book: AddressBook) -> None :
    if len(book.data.items()) == 0:
        print("Trere is no any contact in the address book")
    else:
        print("My contacts:")    
        for _ , record in book.data.items():
            print(record)

@input_error
def show_phone(args, book: AddressBook) -> None:
    name, *_ = args
    record = book.find(name)
    if record is None:
        print("Contact not found.")
        return
    
    for number in record.phones:
        print(number)
    

@input_error
def change_contact(args: list, book: AddressBook) -> str:
    name, old_phone, new_phone = args
    record = book.find(name)
    if record is None:
        return "Contact not found."

    return record.edit_phone(old_phone, new_phone)

@input_error
def add_birthday(args, book: AddressBook):
    name, birthday, *_ = args
    record = book.find(name)

    if record is None:
        return "Contact not found."
    
    return record.add_birthday(birthday)

@input_error
def add_email(args, book: AddressBook):
    name, email, *_ = args
    record = book.find(name)

    if record is None:
        return "Contact not found."
    
    return record.add_email(email)

# @input_error
# def add_address(args, book: AddressBook):
#     name, *address_list, = args
#     address = ""
#     for item in address_list:
#         address = address + " " + item
#     record = book.find(name)

#     if record is None:
#         return "Contact not found."

#     return record.add_address(address)

@input_error
def add_address(args, book: AddressBook):
    
    name  = args[0]
    record = book.find(name)
    
    if record is None:
        return "Contact not found."
    country = input("Enter a country ")
    city = input("Enter a city ")
    street = input("Enter a street Name ")
    house = input("Enter a house number ")
    flat = input("Enter a room or appartment number ")    

    return record.add_address(country, city, street, house, flat)

@input_error
def show_birthday(args, book: AddressBook):
    """Print contact birthday"""
    name, *_ = args
    record = book.find(name)

    if record is None:
        return "Contact not found."

    if record.birthday is None:
        return record.birthday
    return f"{name} birthday {datetime.strftime(record.birthday.value, '%d.%m.%Y')}"

@input_error
def birthdays(args: list, book: AddressBook):
    """Print upcoming birthday"""
    input_date, *_ = args

    congratulations = book.get_upcoming_birthdays(datetime.strptime(input_date, '%d.%m.%Y').date())

    if len(congratulations) == 0:
        print("Not upcoming birthday")
        return

    for person in congratulations:
        print("Name: " + person['name'].capitalize()+
              ". Congratulation date - "+ person['congratulation_date'])


#search-contacts

@input_error
def search_contact(args, book):
    """
    Search for a contact by name in the address book.
    :param args: List of search criteria (e.g., name).
    :param book: Address book dictionary.
    :return: String with search results.
    """
    if not args:
        return "Please provide a name to search for."

    name_to_search = args[0].lower()
    results = [f"{name}: {details}" for name, details in book.items() if name_to_search in name.lower()]

    if results:
        return "\n".join(results)
    else:
        return f"No contacts found matching '{name_to_search}'."