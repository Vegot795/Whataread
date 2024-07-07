import customtkinter as ctk
from customtkinter import CTkToplevel


class EditBook(CTkToplevel):
    def __init__(self, book_manager, index):
        super().__init__()
        self.book_manager = book_manager
        self.index = index
        self.geometry("400x300")
        self.title("Edytuj książkę")

        book = self.book_manager.get_book_by_index(self.index)

        if book is None:
            print(f"Book not found for index {self.index}")
        else:
            title_label = ctk.CTkLabel(self, text="Tytuł:")
            title_label.pack(fill='both', expand=False, pady=5, padx=5)
            self.title_entry = ctk.CTkEntry(self)
            self.title_entry.insert(0, book['title'])
            self.title_entry.pack(fill='both', expand=False, pady=5, padx=5)

            author_label = ctk.CTkLabel(self, text="Autor:")
            author_label.pack(fill='both', expand=False, pady=5, padx=5)
            self.author_entry = ctk.CTkEntry(self)
            self.author_entry.insert(0, book['author'])
            self.author_entry.pack(fill='both', expand=False)

            publisher_label = ctk.CTkLabel(self, text="Wydawnictwo:")
            publisher_label.pack(fill='both', expand=False, pady=5, padx=5)
            self.publisher_entry = ctk.CTkEntry(self)
            self.publisher_entry.insert(0, book['publisher'])
            self.publisher_entry.pack(fill='both', expand=False)

            self.edit_book_button = ctk.CTkButton(self, text="Zatwierdź edycję", command=self.edit_existing_book)
            self.edit_book_button.pack(fill='both', expand=False)

    def edit_existing_book(self):
        update_title = self.title_entry.get()
        update_author = self.author_entry.get()
        update_publisher = self.publisher_entry.get()

        self.book_manager.edit_book(self.index, update_title, update_author, update_publisher)
        self.destroy()
