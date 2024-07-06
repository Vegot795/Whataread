import json
import os

class Book:
    def __init__(self):
        self.books = []
        self.load_books()
        if not self.books:
            self.books.append({
                'title': 'Sample Title',
                'author': 'Sample Author',
                'publisher': 'Sample Publisher'
            })
            self.save_books()

    def add_books(self, title, author, publisher):
        new_book = {
            'title': title,
            'author': author,
            'publisher': publisher
        }
        self.books.append(new_book)
        self.save_books()

    def get_books(self):
        return self.books

    def save_books(self):
        try:
            os.makedirs('saves', exist_ok=True)
            with open('saves/books.json', 'w') as f:
                json.dump(self.books, f, indent=4)
            print("Books saved successfully")
        except IOError as e:
            print(f"Error saving books: {e}")

    def load_books(self):
        if os.path.exists('saves/books.json'):
            try:
                with open('saves/books.json', 'r') as file:
                    self.books = json.load(file)
                print("Books loaded successfully")
            except json.JSONDecodeError as e:
                print(f"Failed to load books: {e}")
        else:
            self.books = []
