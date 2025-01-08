"""
Модуль для збереження та завантаження даних адресної книги та нотаток.
Дані зберігаються у файлах у домашній директорії користувача.
"""
import os
import pickle
from src.models.address_book import AddressBook
from src.models.notes_book import NotesBook

DATA_FOLDER = os.path.expanduser("~/.assistant_data")
ADDRESS_BOOK_FILE = os.path.join(DATA_FOLDER, "addressbook.pkl")
NOTES_BOOK_FILE = os.path.join(DATA_FOLDER, "notesbook.pkl")

def ensure_data_folder():
        """
    Перевіряє наявність папки для збереження даних.
    Якщо папка не існує, вона створюється.
    """
    if not os.path.exists(DATA_FOLDER):
        os.makedirs(DATA_FOLDER)

def save_address_book(book, filename=ADDRESS_BOOK_FILE):
    """
    Зберігає адресну книгу в зазначений файл.

    Parameters:
        book (AddressBook): Об'єкт адресної книги для збереження.
        filename (str): Шлях до файлу, куди зберігати дані (за замовчуванням ADDRESS_BOOK_FILE).
    """
    ensure_data_folder()
    with open(filename, "wb") as f:
        pickle.dump(book, f)

def load_address_book(filename=ADDRESS_BOOK_FILE):
    """
    Завантажує адресну книгу із зазначеного файлу.

    Parameters:
        filename (str): Шлях до файлу, звідки завантажувати дані (за замовчуванням ADDRESS_BOOK_FILE).

    Returns:
        AddressBook: Завантажений об'єкт адресної книги.
        Якщо файл не знайдено, повертається новий об'єкт AddressBook.
    """
    ensure_data_folder()
    try:
        with open(filename, "rb") as f:
            return pickle.load(f)
    except FileNotFoundError:
        return AddressBook()

def save_notes_book(book, filename=NOTES_BOOK_FILE):
    """
    Зберігає нотатки в зазначений файл.

    Parameters:
        book (NotesBook): Об'єкт нотаток для збереження.
        filename (str): Шлях до файлу, куди зберігати дані (за замовчуванням NOTES_BOOK_FILE).
    """
    ensure_data_folder()
    with open(filename, "wb") as f:
        pickle.dump(book, f)

def load_notes_book(filename=NOTES_BOOK_FILE):
    """
    Завантажує нотатки із зазначеного файлу.

    Parameters:
        filename (str): Шлях до файлу, звідки завантажувати дані (за замовчуванням NOTES_BOOK_FILE).

    Returns:
        NotesBook: Завантажений об'єкт нотаток.
        Якщо файл не знайдено, повертається новий об'єкт NotesBook.
    """
    ensure_data_folder()
    try:
        with open(filename, "rb") as f:
            return pickle.load(f)
    except FileNotFoundError:
        return NotesBook()
