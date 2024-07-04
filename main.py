import os
import customtkinter as ctk
import json
from customtkinter import CTkToplevel

class App(ctk.CTk):
    def __init__(self, books_instance):
        super().__init__()
        self.configure(fg_color='green')
        self.geometry("600x800")
        self.title("Whataread")
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(2, weight=1)
        my_books = books_instance
        current_books = my_books.get_books()

        self.title_label = ctk.CTkLabel(self, text="Whataread!", font=("default", 40))
        self.title_label.pack(fill='both', expand = False, pady=5, padx=5)
        self.search_entry = ctk.CTkEntry(self)
        self.search_entry.pack(fill='both', expand = False, pady=5, padx=5)

        self.book_list_frame = ctk.CTkFrame(self)
        self.book_list_frame.pack(fill='both', expand = True, pady=5, padx=5)

        for index, books in enumerate(current_books):
            book_list_frame = ctk.CTkFrame(self)
            book_list_frame.grid(row=index, column=1, sticky="nsew")

        self.button = ctk.CTkButton(self, text='Dodaj książkę', command=self.open_add_book)
        self.button.pack(fill='both', expand = False, pady=5, padx=5)

        self.add_book = None
        self.my_books = Book()

    def open_add_book(self):
        if self.add_book is not None and self.add_book.winfo_exists():
            self.add_book.destroy()

        self.add_book = AddBook(self.my_books)
        self.add_book.mainloop()

    def update_book_list(self):
        current_books = self.my_books.get_books()
        for widget in self.book_list_frame.winfo_children():
            widget.destroy()

        for index, book in enumerate(current_books):
            book_frame = ctk.CTkFrame(self.book_list_frame)
            book_title_label = ctk.CTkLabel(book_frame, text=f"Title: {book['title']}")
            book_title_label.pack(fill='both', expand = False)










class Book:
    def __init__(self):
        self.books = []
        if not os.path.exists('saves/books.json'):
            self.books.append({
                'title': 'title',
                'author': 'author',
                'publisher': 'publisher'
            })
            self.load_books()

    def add_books(self, title, author, publisher):
        new_book = {
            'title': title,
            'author': author,
            'publisher': publisher
        }
        self.books.append(new_book)

    def get_books(self):
        return self.books

    def save_books(self):
        try:
            with open('saves/books.json', 'w') as f:
                f.write(json.dumps(self.books, indent=4))
            print("books saved succesfully")
        except IOError as e:
            print(f"Error saving books: {e}")

    def load_books(self):
        if os.path.exists('saves/books.json'):
            with open('saves/books.json', 'r') as file:
                try:
                    self.books = json.load(file)
                    print("books loaded successfully")
                except json.JSONecodeError as e:
                    print (f"book load failed: {e}")
        else:
            self.books = []


class AddBook(CTkToplevel):
    def __init__(self, book_manager):
        super().__init__()
        self.book_manager = book_manager
        self.geometry("400x300")
        self.title("Dodaj książkę")

        title_label = ctk.CTkLabel(self, text="Tytuł:")
        title_label.pack(fill='both', expand = False, pady=5, padx=5)
        self.title_entry = ctk.CTkEntry(self)
        self.title_entry.pack(fill='both', expand = False, pady=5, padx=5)

        author_label = ctk.CTkLabel(self, text="Autor:")
        author_label.pack(fill='both', expand = False, pady=5, padx=5)
        self.author_entry = ctk.CTkEntry(self)
        self.author_entry.pack(fill='both', expand =False)

        publisher_label = ctk.CTkLabel(self, text="Wydawnictwo:")
        publisher_label.pack(fill='both', expand = False, pady=5, padx=5)
        self.publisher_entry = ctk.CTkEntry(self)
        self.publisher_entry.pack(fill='both', expand = False)

        self.add_book_button = ctk.CTkButton(self, text="Dodaj książkę", command=self.add_new_book)
        self.add_book_button.pack(fill='both', expand = False)

    def add_new_book(self):
        book_title = self.title_entry.get()
        book_author = self.author_entry.get()
        book_publisher = self.publisher_entry.get()

        self.book_manager.add_books(book_title, book_author, book_publisher)
        self.book_manager.save_books()
        self.destroy()



my_books = Book()
app = App(my_books)
app.mainloop()

