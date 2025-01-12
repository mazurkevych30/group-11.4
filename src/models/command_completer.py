""""This module provides the CommandCompleter class for autocompletion in the CLI application."""
from prompt_toolkit.completion import Completer, Completion

# List of available commands
commands_list = [
    "hello", "help", "add-contact", "delete-contact", "search-contact", "change-phone",
    "phone", "all", "add-birthday", "add-email", "edit-email", "add-address", "edit-address",
    "show-birthday", "edit-birthday", "birthdays", "add-note", "show-notes", "edit-note",
    "delete-note", "find-note-by-key", "find-notes-by-tags", "sort-notes-by-tags", "close", "exit"
]


class CommandCompleter(Completer):
    """Create a CommandCompleter class for autocompletion"""
    def get_completions(self, document, complete_event):
        text = document.text
        for cmd in commands_list:
            if cmd.startswith(text):
                yield Completion(cmd, start_position=-len(text))
