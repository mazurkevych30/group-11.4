"""This module provides a command-line interface (CLI) for an assistant bot."""
from src.models.command_completer import colored_input, commands_list
from src.helpers.show_commands import show_commands
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
    find_notes_by_tags,
    sort_notes_by_tags
)

def main():
    """Main script"""
    # Load data
    book = load_address_book()
    note = load_notes_book()

    print("Welcome to the assistant bot!")

    while True:
        # Get user input with autocompletion
        user_input = colored_input()

        if not user_input.strip():
            print("No command entered. Type 'help' to see a list of commands.")
            continue

        command, *args = parse_input(user_input)
        if command not in commands_list:
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

            case "help":
                show_commands()

            case "add-contact":
                print(add_contact(args, book))

            case "delete-contact":
                print(delete_contact(args, book))

            case "change-phone":
                print(change_contact(args, book))

            case "show-phone":
                show_phone(args, book)

            case "all-contacts":
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

            case "add-note":
                print(add_note(args, note))

            case "show-notes":
                show_notes(note)

            case "edit-note":
                print(edit_note(args, note))

            case "delete-note":
                print(delete_note(args, note))

            case "find-note-by-key":
                print(find_note_by_key(args, note))

            case "find-notes-by-tags":
                print(find_notes_by_tags(args, note))

            case "sort-notes-by-tags":
                print(sort_notes_by_tags(note))

            case "search-contact":
                print(search_contact(args, book))

# Start the program
if __name__ == "__main__":
    main()
