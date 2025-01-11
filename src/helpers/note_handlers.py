from src.helpers.input_error import input_error
from src.models.notes_book import NotesBook
from src.models.note import Note

@input_error
def add_note(args, notes_book: NotesBook):
    """ Function for adding a new note"""
    if len(args) < 1:
        return "Please enter a note title"
    title = args[0]
    text = input("Enter note text: ").strip()
    tags_input = input("Tags must be separated by commas: ").strip()
    tags = [tag.strip() for tag in tags_input.split(",")] if tags_input else []
    if title in notes_book.data:
        return f"Note '{title}' already exists."
    note = Note(title=title, text=text, tags=tags)
    notes_book.add_note(note)
    return f"Note '{title}' added successfully."

@input_error
def show_notes(notes_book: NotesBook)  -> None:
    """ A function that displays all notes from a notebook"""
    print("All notes:")
    for _ , note in notes_book.data.items():
        print("--------------")
        print(note) 

@input_error
def edit_note(args, notes_book: NotesBook):
    """ Function for editing note by title"""
    if len(args) < 2:
        return "Please enter more than 1 argument"
    title = args[0]
    new_text = args[1]
    new_tags = args[2:]
    
    result = notes_book.edit_note(title, new_text, new_tags)
    if result:
        return result
    return f"Note '{title}' updated."

@input_error
def delete_note(args, notes_book: NotesBook):
    """ Function for delete a note by title"""
    if len(args) != 1:
        return "Please enter a note title"
    title = args[0]
    result = notes_book.delete(title)
    if result:
        return result
    return f"Note '{title}' deleted."

@input_error
def find_note_by_key(args, notes_book: NotesBook):
    """ Function for searching notes by keyword in title, text or tags"""
    if len(args) != 1:
        return "Please enter a search key"
    key = args[0]
    found_notes = notes_book.find(key)
    if not found_notes:
        return f"No notes with key '{key}'."
    
    result = "\n\n".join(str(note) for note in found_notes)
    return result

@input_error
def find_notes_by_tag(args, notes_book: NotesBook):
    """ Function for searching notes by tag"""
    if len(args) != 1:
        return "Please enter a note tag"
    tag = args[0]
    found_notes = notes_book.find_by_tag(tag)
    if not found_notes:
        return f"No notes with tag '{tag}'."
    
    result = "\n\n".join(str(note) for note in found_notes)
    return result

@input_error
def sort_notes_by_tags(notes_book: NotesBook)  -> None:
    """ Function for sorting notes by tag"""
    tagged_notes = {}

    for note_key, note in notes_book.data.items():
        for tag in note.tags:
            if tag not in tagged_notes:
                tagged_notes[tag] = []
            tagged_notes[tag].append(note)
    sorted_tags = sorted(tagged_notes.keys())
    for tag in sorted_tags:
        print(f"Notes with tag- {tag}:")
        print("----------------")
        for note in tagged_notes[tag]:
            print(note)
            print()