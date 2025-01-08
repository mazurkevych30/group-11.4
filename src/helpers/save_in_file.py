import os
import pickle
from src.models.address_book import AddressBook
from src.models.notes_book import NotesBook

# Назва папки для зберігання даних
DATA_FOLDER = os.path.expanduser("~/.assistant_data")
ADDRESS_BOOK_FILE = os.path.join(DATA_FOLDER, "addressbook.pkl")
NOTES_BOOK_FILE = os.path.join(DATA_FOLDER, "notesbook.pkl")

# Перевірка наявності папки для зберігання даних
def ensure_data_folder():
    if not os.path.exists(DATA_FOLDER):
        os.makedirs(DATA_FOLDER)

# Збереження адресної книги
def save_address_book(book, filename=ADDRESS_BOOK_FILE):
    ensure_data_folder()
    with open(filename, "wb") as f:
        pickle.dump(book, f)

# Завантаження адресної книги
def load_address_book(filename=ADDRESS_BOOK_FILE):
    ensure_data_folder()
    try:
        with open(filename, "rb") as f:
            return pickle.load(f)
    except FileNotFoundError:
        return AddressBook()

# Збереження нотаток
def save_notes_book(book, filename=NOTES_BOOK_FILE):
    ensure_data_folder()
    with open(filename, "wb") as f:
        pickle.dump(book, f)

# Завантаження нотаток
def load_notes_book(filename=NOTES_BOOK_FILE):
    ensure_data_folder()
    try:
        with open(filename, "rb") as f:
            return pickle.load(f)
    except FileNotFoundError:
        return NotesBook()
