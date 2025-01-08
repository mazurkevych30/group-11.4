"""Modules"""
from src.helpers.save_in_file import load_data, save_data
from src.helpers.command_parser import parse_input
from src.helpers.record_hendlers import (
    add_contact,
    change_contact,
    show_phone,
    show_all,
    add_birthday,
    show_birthday,
    birthdays,
    add_email,
    add_address,
    )

def main():
    """Main script"""
    book = load_data()
    print("Welcome to the assistant bot!")

    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        match command:
            case "close" | "exit":
                save_data(book)
                print("Good bye!")
                break
            case "hello":
                print("How can I help you?")
            case "add":
                print(add_contact(args, book))
            case "change":
                print(change_contact(args, book))
            case "phone":
                show_phone(args, book)
            case "all":
                show_all(book)
            case "add-birthday":
                print(add_birthday(args, book))
            case "add-email":
                print(add_email(args, book))
            case "edit-email":
                print(add_email(args, book))
            case "add-address":
                print(add_address(args, book))
            case "edit-address":
                print(add_address(args, book))
            case "show-birthday":
                print(show_birthday(args, book))
            case "birthdays":
                birthdays(book)
            case _:
                print("Invalid command.")
