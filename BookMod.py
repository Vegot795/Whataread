import json
import os
import uuid

class Book:
    def __init__(self):
        self.books = []
        self.load_books()
        self.id = uuid.uuid4
        if not self.books:
            self.books.append({
                'id': str(uuid.uuid4()),
                'title': 'Sample Title',
                'author': 'Sample Author',
                'publisher': 'Sample Publisher'
            })
            self.save_books()

    def add_books(self, title, author, publisher):
        new_book = {
            'id': id,
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

    def get_book_by_index(self, index):
        if 0 <= index < len(self.books):
            return self.books[index]
        else:
            return None

    def edit_book(self, index, updated_title, updated_author, updated_publisher):
        if 0 <= index < len(self.books):
            self.books[index]['title'] = updated_title
            self.books[index]['author'] = updated_author
            self.books[index]['publisher'] = updated_publisher
        else:
            print(f"Invalid index {index} for editing book")

    def move_book_up(self, index):
        if index > 0:
            self.books[index], self.books[index - 1] = self.books[index - 1], self.books[index]


    def move_book_down(self, index):
        if 0 <= index < len(self.books) - 1:
            self.books[index], self.books[index + 1] = self.books[index + 1], self.books[index]

    def delete_book(self, index):
        if 0 <= index < len(self.books):
            del self.books[index]
        else:
            print(f"Error: Index {index} is out of range")