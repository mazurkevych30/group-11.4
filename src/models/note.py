"""
This module defines the Note class, which models individual notes with a title, text,
creation date, and optional tags. Notes can be converted to and from dictionary representations. 
"""
from datetime import datetime

class Note:
    """ Model of note"""
    def __init__(self, title, text, tags = None):
        self.title = title
        self.text = text
        self.created_date = datetime.now()
        self.tags = tags if tags else []

    def __str__(self):
        tags_str = ', '.join(self.tags) if self.tags else "No tags"
        return (
            f"Title: {self.title}\nText: {self.text}\nTags: {tags_str}\n"
            f"Created date: {self.created_date.strftime('%Y-%m-%d %H:%M:%S')}"
            )

    def __repr__(self):
        return (
            f"Title: {self.title}\nText: {self.text}\nTags: {', '.join(self.tags)}\n"
            f"Created date: {self.created_date.strftime('%Y-%m-%d %H:%M:%S')}"
            )

    def to_dict(self):
        """Convert the note to a dictionary representation."""
        return {
            "title": self.title,
            "text": self.text,
            "created_date": self.created_date.isoformat(),
            "tags": self.tags
        }

    @classmethod
    def from_dict(cls, data):
        """Create a Note instance from a dictionary."""
        note = cls(data['title'], data['text'], data['tags'])
        note.created_date = datetime.fromisoformat(data['created_date'])
        return note
