from collections import UserDict
from src.models.note import Note

class NotesBook(UserDict):
    def __init__(self):
        self.data = {}

    def add_note(self, note):
        self.data[note.title] = note
        for _ , record in self.data.items():
            print(record)

    def find(self, keyword):
        found_notes = []
        for note in self.data.values():
            if keyword in note.title or keyword in note.content or keyword in note.tags:
                found_notes.append(note)
        return found_notes if found_notes else None

    def delete(self, title):
        if title in self.data:
            del self.data[title]
        else:
            return f"Note '{title}' not found."

    def edit_note(self, title, new_text = None, new_tags = None):
        if title in self.data:
            note = self.data[title]
            if new_text:
                note.text = new_text
            if new_tags is not None:
                note.tags = new_tags
        else:
            return f"Note '{title}' not found."

    def find_by_tag(self, tag: str) -> list:
        all_notes = []
        for note in self.data.values():
            if tag in note.tags:
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