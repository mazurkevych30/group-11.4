"""Main module"""
from fuzzywuzzy import process
from src.helpers.save_in_file import (
    save_address_book,
    load_address_book,
    save_notes_book,
    load_notes_book
    )
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
    sort_notes_by_tags,
    )

commands_list = [
    "close", "exit", "hello", "add", "delete", "change", "phone", "all", 
    "add-birthday", "add-email", "edit-email", "add-address", "edit-address",
    "show-birthday", "birthdays", "add_note", "show_notes", "edit_note", 
    "delete_note", "find_note_by_key", "find_notes_by_tag", "sort_notes_by_tags"
]

# Function to search for the nearest command from available commands
def suggest_closest_command(user_input):
    closest_match = process.extractOne(user_input, commands_list)
    return closest_match

def main():
    """Main script"""
    book = load_address_book()
    note = load_notes_book()
    print("Welcome to the assistant bot!")

    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

    # Checking if the command is found
        if command not in commands_list:
            suggestion = suggest_closest_command(user_input)
            if suggestion[1] >= 40:  # If the similarity is more than 60% - we offer a team
                print(f"Did you mean '{suggestion[0]}'?")
            else:
                print("Invalid command.")
            continue

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
                birthdays(args, book)
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
            case "sort_notes_by_tags":
                print(sort_notes_by_tags(note))
            case "search":
                print(search_contact(args, book))
            case _:
                print("Invalid command.")
