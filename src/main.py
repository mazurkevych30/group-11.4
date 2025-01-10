"""Modules"""
from src.helpers.save_in_file import save_address_book, load_address_book, save_notes_book, load_notes_book
from src.helpers.command_parser import parse_input
from src.helpers.record_hendlers import (
    add_contact,
    delete_contact,
    change_contact,
    show_phone,
    show_all,
    add_birthday,
    show_birthday,
    birthdays,
    add_email,
    add_address,
    search_contact
    )
from src.helpers.note_handlers import ( 
    add_note,
    show_notes,
    edit_note,
    delete_note,
    find_note_by_key,
    find_notes_by_tag,
    )

def main():
    """Main script"""
    book = load_address_book()
    note = load_notes_book()
    print("Welcome to the assistant bot!")

    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        match command:
            case "close" | "exit":
                save_address_book(book)
                save_notes_book(note)
                print("Good bye!")
                break
            case "hello":
                print("How can I help you?")
            case "add":
                print(add_contact(args, book))
            case "delete":
                print(delete_contact(args, book))
            case "change-phone":
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
            case "edit-birthday":
                print(add_birthday(args, book))
            case "birthdays":
                birthdays(book)
            case "add_note":
                print(add_note(args, note))
            case "show_notes":
                print(show_notes(note))
            case "edit_note":
                print(edit_note(args, note))
            case "delete_note":
                print(delete_note(args, note))
            case "find_note_by_key":
                print(find_note_by_key(args, note))
            case "find_notes_by_tag":
                print(find_notes_by_tag(args, note))
            case "search":
                print(search_contact(args, book))
            case _:
                print("Invalid command.")
