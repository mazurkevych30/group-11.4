""""This module provides the CommandCompleter class for autocompletion in the CLI application."""
from prompt_toolkit.formatted_text import HTML
from prompt_toolkit.styles import Style
from prompt_toolkit.completion import Completer, Completion
from prompt_toolkit.shortcuts import prompt as prompt_shortcut
from prompt_toolkit.auto_suggest import AutoSuggestFromHistory

# List of available commands
commands_list = [
    "hello", "help", "add-contact", "delete-contact", "search-contact", "change-phone",
    "phone", "all-contacts", "add-birthday", "add-email", "edit-email", "add-address", 
    "edit-address", "show-birthday", "edit-birthday", "birthdays", "add-note", "show-notes",
    "edit-note", "delete-note", "find-note-by-key", "find-notes-by-tags", "sort-notes-by-tags",
    "close", "exit", "show-phone"
]

class CommandCompleter(Completer):
    """Create a CommandCompleter class for autocompletion"""
    def get_completions(self, document, complete_event):
        text = document.text
        for cmd in commands_list:
            if cmd.startswith(text):
                yield Completion(cmd, start_position=-len(text))

# Define a style for the prompt and user input
style = Style.from_dict({
    'prompt': 'ansiblue',
    '': 'ansigreen',
})

def colored_input():
    """Function to get user input and display it with colors"""
    completer = CommandCompleter()
    user_input = prompt_shortcut(
        HTML('<prompt>Enter a command: </prompt>'),
        style=style,
        completer=completer,
        auto_suggest=AutoSuggestFromHistory()
    )
    return user_input
