import pytest
import App.AddBookMod as AddBookMod


# Dummy BookManager class for testing purposes
class DummyBookManager:
    def __init__(self):
        self.books = []

    def add_books(self, title, author, publisher):
        self.books.append({
            'title': title,
            'author': author,
            'publisher': publisher
        })

    def get_books(self):
        return self.books

    def save_books(self):

        pass


def test_add_new_book():

    book_manager = DummyBookManager()


    add_book_mod = AddBookMod.AddBook(book_manager)


    add_book_mod.title_entry = DummyEntry('Sample Title')
    add_book_mod.author_entry = DummyEntry('Sample Author')
    add_book_mod.publisher_entry = DummyEntry('Sample Publisher')


    add_book_mod.add_new_book()


    assert len(book_manager.get_books()) == 1
    assert book_manager.get_books()[0]['title'] == 'Sample Title'
    assert book_manager.get_books()[0]['author'] == 'Sample Author'
    assert book_manager.get_books()[0]['publisher'] == 'Sample Publisher'



class DummyEntry:
    def __init__(self, value):
        self.value = value

    def get(self):
        return self.value

