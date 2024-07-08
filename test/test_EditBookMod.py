import pytest
from App.EditBookMod import EditBook
import customtkinter as ctk



class DummyBookManager:
    def __init__(self):
        self.books = [
            {'title': 'Sample Title',
             'author': 'Sample Author',
             'publisher': 'Sample Publisher'}
        ]

    def get_book_by_index(self,index):
        if 0 <= index < len(self.books):
            return self.books[index]
        else:
            return None

    def edit_book_window(self, index, title, author, publisher):
        if 0 <= index < len(self.books):
            self.books[index]['title'] = title
            self.books[index]['author'] = author
            self.books[index]['publisher'] = publisher
        else:
            print(f"Invalid index {index} for editing book")


def test_edit_book():

    book_manager = DummyBookManager()
    index = 0
    app = ctk.CTk()
    edit_book = EditBook(book_manager, index)

    edit_book.title_entry.delete(0, ctk.END)
    edit_book.author_entry.delete(0, ctk.END)
    edit_book.publisher_entry.delete(0, ctk.END)

    edit_book.title_entry.insert(0, 'Updated Title')
    edit_book.author_entry.insert(0, 'Updated Author')
    edit_book.publisher_entry.insert(0, 'Updated Publisher')

    edit_book.edit_existing_book()

    app.destroy()


    updated_book = book_manager.get_book_by_index(index)
    assert updated_book['title'] == ('Updated Title')
    assert updated_book['author'] == 'Updated Author'
    assert updated_book['publisher'] == 'Updated Publisher'

class DummyEntry:
    def __init__(self, value=''):
        self.value = value

    def get(self):
        return self.value

    def set(self, value):
        self.value = value