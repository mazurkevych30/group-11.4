from collections import UserDict
from src.models.note import Note

class NotesBook(UserDict):
    """ Model of noteBook"""

    def add_note(self, note):
        """ Function for adding a new note"""
        self.data[note.title] = note

    def find(self, keyword):
        """ Function for searching notes by keyword"""
        found_notes = []
        for note in self.data.values():
            if keyword in note.title or keyword in note.text or keyword in note.tags:
                found_notes.append(note)
        return found_notes if found_notes else None

    def delete(self, title):
        """ Function for delete note by title"""
        if title in self.data:
            del self.data[title]
        else:
            return f"Note '{title}' not found."

    def edit_note(self, title, new_text = None, new_tags = None):
        """ Function for editing note by title"""
        if title in self.data:
            note = self.data[title]
            if new_text:
                note.text = new_text
            if new_tags is not None:
                note.tags = list(new_tags[0].split(","))
        else:
            return f"Note '{title}' not found."

    def find_by_tag(self, tag: str) -> list:
        """ Function for searching notes by tags"""
        tags = [t.strip() for t in tag.split(',')]
        all_notes = []

        for note in self.data.values():
            if any(tag in note.tags for tag in tags):
                all_notes.append(note)
        return all_notes if all_notes else None


    def to_dict(self):
        return {"All notes": [note.to_dict() for note in self.data.values()]}

    @classmethod
    def from_dict(cls, data):
        notes_book = cls()
        for note_data in data['notes']:
            note = Note.from_dict(note_data)
            notes_book.add_note(note)
        return notes_book