""""This module provides a function to show a list of commands and their descriptions."""

def show_commands():
    """Show list of commands"""
    commands = [
        ("hello", "Greets the user"),
        ("help", "Provides help information"),
        ("add-contact", "Adds a new contact"),
        ("delete-contact", "Deletes an existing contact"),
        ("search-contact", "Searches for a contact"),
        ("change-phone", "Changes the phone number of a contact"),
        ("phone", "Displays the phone number of a contact"),
        ("all", "Displays all contacts"),
        ("add-birthday", "Adds a birthday to a contact"),
        ("add-email", "Adds an email to a contact"),
        ("edit-email", "Edits the email of a contact"),
        ("add-address", "Adds an address to a contact"),
        ("edit-address", "Edits the address of a contact"),
        ("show-birthday", "Displays the birthday of a contact"),
        ("edit-birthday", "Edits the birthday of a contact"),
        ("birthdays", "Displays all birthdays"),
        ("add-note", "Adds a note to a contact"),
        ("show-notes", "Displays all notes for a contact"),
        ("edit-note", "Edits a note of a contact"),
        ("delete-note", "Deletes a note from a contact"),
        ("find-note-by-key", "Finds a note by keyword"),
        ("find-notes-by-tags", "Finds notes by tags"),
        ("sort-notes-by-tags", "Sorts notes by tags"),
        ("close", "Closes the application"),
        ("exit", "Exits the program")
    ]

    print(f"{'Command':<20} {'Description'}")
    print('-' * 40)
    for command, description in commands:
        print(f"{command:<20} {description}")
