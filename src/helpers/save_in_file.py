"""
Module for saving and loading data for the address book and notes.
Data is stored in files within the user's home directory.
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
    Checks the existence of the data storage folder.
    If the folder does not exist, it is created.
    """
    if not os.path.exists(DATA_FOLDER):
        os.makedirs(DATA_FOLDER)

def save_address_book(book, filename=ADDRESS_BOOK_FILE):
    """
    Saves the address book to the specified file.

    Parameters:
        book (AddressBook): The address book object to save.
        filename (str): Path to the file where data will be saved (default is ADDRESS_BOOK_FILE).
    """
    ensure_data_folder()
    with open(filename, "wb") as f:
        pickle.dump(book, f)

def load_address_book(filename=ADDRESS_BOOK_FILE):
    """
    Loads the address book from the specified file.

    Parameters:
    filename (str): Path to the file from which data will be loaded (default is ADDRESS_BOOK_FILE).

    Returns:
    AddressBook: The loaded address book object.
    If the file is not found, a new AddressBook object is returned.
    """
    ensure_data_folder()
    try:
        with open(filename, "rb") as f:
            return pickle.load(f)
    except FileNotFoundError:
        return AddressBook()

def save_notes_book(book, filename=NOTES_BOOK_FILE):
    """
    Saves the notes to the specified file.

    Parameters:
        book (NotesBook): The notes object to save.
        filename (str): Path to the file where data will be saved (default is NOTES_BOOK_FILE).
    """
    ensure_data_folder()
    with open(filename, "wb") as f:
        pickle.dump(book, f)

def load_notes_book(filename=NOTES_BOOK_FILE):
    """
    Loads the notes from the specified file.

    Parameters:
    filename (str): Path to the file from which data will be loaded (default is NOTES_BOOK_FILE).

    Returns:
    NotesBook: The loaded notes object.
    If the file is not found, a new NotesBook object is returned.
    """
    ensure_data_folder()
    try:
        with open(filename, "rb") as f:
            return pickle.load(f)
    except FileNotFoundError:
        return NotesBook()
