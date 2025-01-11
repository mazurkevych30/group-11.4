from prompt_toolkit import prompt
from prompt_toolkit.completion import Completer, Completion
from prompt_toolkit.auto_suggest import AutoSuggestFromHistory
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
    sort_notes_by_tags
)

# List of available commands
commands_list = [
     "hello", "help", "add-contact", "delete-contact", "search-contact", "change-phone", "phone", "all",
    "add-birthday", "add-email", "edit-email", "add-address", "edit-address",
    "show-birthday", "edit-birthday", "birthdays", "add-note", "show-notes", "edit-note",
    "delete-note", "find-note-by-key", "find-notes-by-tag", "sort-notes-by-tags", "close", "exit"
]

# Create a CommandCompleter class for autocompletion
class CommandCompleter(Completer):
    def get_completions(self, document, complete_event):
        text = document.text
        for cmd in commands_list:
            if cmd.startswith(text):
                yield Completion(cmd, start_position=-len(text))


def main():
    """Main script"""
    # Load data
    book = load_address_book()
    note = load_notes_book()

    completer = CommandCompleter()

    print("Welcome to the assistant bot!")

    while True:
        # Get user input with autocompletion
        user_input = prompt("Enter a command: ", completer=completer, auto_suggest=AutoSuggestFromHistory())

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
                for idx, command in enumerate(commands_list, start=1):
                    print(f"{idx}. {command}")

            case "add-contact":
                print(add_contact(args, book))

            case "delete-contact":
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

            case "add-note":
                print(add_note(args, note))

            case "show-notes":
                print(show_notes(note))

            case "edit-note":
                print(edit_note(args, note))

            case "delete-note":
                print(delete_note(args, note))

            case "find-note-by-key":
                print(find_note_by_key(args, note))

            case "find-notes-by-tag":
                print(find_notes_by_tag(args, note))

            case "sort-notes-by-tags":
                print(sort_notes_by_tags(note))

            case "search-contact":
                print(search_contact(args, book))

# Start the program
if __name__ == "__main__":
    main()
