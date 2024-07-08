import customtkinter as ctk
from customtkinter import CTkToplevel

class AddBook(CTkToplevel):
    def __init__(self, book_manager):
        super().__init__()
        self.book_manager = book_manager
        self.geometry("400x300")
        self.title("Dodaj książkę")

        title_label = ctk.CTkLabel(self, text="Tytuł:")
        title_label.pack(fill='both', expand=False, pady=5, padx=5)
        self.title_entry = ctk.CTkEntry(self)
        self.title_entry.pack(fill='both', expand=False, pady=5, padx=5)

        author_label = ctk.CTkLabel(self, text="Autor:")
        author_label.pack(fill='both', expand=False, pady=5, padx=5)
        self.author_entry = ctk.CTkEntry(self)
        self.author_entry.pack(fill='both', expand=False)

        publisher_label = ctk.CTkLabel(self, text="Wydawnictwo:")
        publisher_label.pack(fill='both', expand=False, pady=5, padx=5)
        self.publisher_entry = ctk.CTkEntry(self)
        self.publisher_entry.pack(fill='both', expand=False)

        self.add_book_button = ctk.CTkButton(self, text="Dodaj książkę", command=self.add_new_book)
        self.add_book_button.pack(fill='both', expand=False)

    def add_new_book(self):
        book_title = self.title_entry.get()
        book_author = self.author_entry.get()
        book_publisher = self.publisher_entry.get()

        self.book_manager.add_books(book_title, book_author, book_publisher)
        self.book_manager.save_books()
        self.destroy()
