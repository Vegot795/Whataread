import customtkinter as ctk
import BookMod
from AddBookMod import AddBook
from EditBookMod import EditBook
import json
from SortingLogicMod import sort_books
from customtkinter import StringVar

class App(ctk.CTk):
    def __init__(self, books_instance):
        super().__init__()
        self.configure(fg_color='green')
        self.geometry("600x800")
        self.title("Whataread")
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(2, weight=1)

        self.my_books = books_instance
        self.load_settings()

        self.title_label = ctk.CTkLabel(self, text="Whataread!", font=("default", 40))
        self.title_label.pack(fill='both', expand=False, pady=5, padx=5)

        sort_bar = ctk.CTkFrame(self)
        sort_bar.pack()

        sort_label = ctk.CTkLabel(sort_bar, text="Sortuj wg:")
        sort_label.grid(row=0, column=0, sticky='ew', padx=5)

        self.sort_options = ['Własne', 'Autor', 'Tytuł', 'Wydawca']
        self.sort_var = ctk.StringVar()
        self.sort_var.set(self.current_sort_option)
        self.search_entry = ctk.CTkComboBox(sort_bar, values= self.sort_options)
        self.search_entry.grid(row=0, column=1, sticky='ew', padx=5)

        self.book_list_frame = ctk.CTkFrame(self)
        self.book_list_frame.pack(fill='both', expand=True, pady=5, padx=5)

        self.button = ctk.CTkButton(self, text='Dodaj książkę', command=self.open_add_book)
        self.button.pack(fill='both', expand=False, pady=5, padx=5)

        self.add_book = None

        self.update_book_list()

    def load_settings(self):
        try:
            with open('books.json', 'r') as f:
                settings = json.load(f)
                self.current_sort_option = settings.get('sort_option', "Własne")
        except FileNotFoundError:
                self.current_sort_option = "id"

    def save_settings(self):
        settings = {
            'sort_options': self.current_sort_option
        }
        with open('books.json', 'w') as f:
            json.dump(settings, f)

    def on_sort_change(self, event):
        self.current_sort_option = self.sort_var.get()
        self.save_settings()
        self.update_book_list()


    def open_add_book(self):
        if self.add_book is not None and self.add_book.winfo_exists():
            self.add_book.destroy()

        self.add_book = AddBook(self.my_books)
        self.add_book.wait_window()
        self.update_book_list()

    def edit_book(self, index):
        edit_window = EditBook(self.my_books, index)
        edit_window.wait_window()
        self.update_book_list()

    def move_up_book(self, index):
        if index > 0:
            self.my_books.move_book_up(index)
            self.update_book_list()

    def move_down_book(self, index):
        if index < len(self.my_books.get_books()) - 1:
            self.my_books.move_book_down(index)
            self.update_book_list()

    def delete_book(self, index):
        self.my_books.delete_book(index)
        self.update_book_list()

    def update_book_list(self):
        for widget in self.book_list_frame.winfo_children():
            widget.destroy()

        current_books = self.my_books.get_books()
        sorted_books = sort_books(current_books, self.current_sort_option)

        for index, book in enumerate(sorted_books):
            book_frame = ctk.CTkFrame(self.book_list_frame)
            book_frame.pack(fill='x', pady=5, padx=5)
            book_frame.columnconfigure(0, weight=1)
            book_frame.columnconfigure(1, weight=0)

            info_frame = ctk.CTkFrame(book_frame)
            info_frame.grid(column=0, row=0, sticky='ew', padx=5)

            button_frame = ctk.CTkFrame(book_frame)
            button_frame.grid(column=1, row=0, sticky='ew', padx=5)

            book_title_label = ctk.CTkLabel(info_frame, text=f"Title: {book['title']}")
            book_title_label.pack(fill='x', expand=False)
            book_author_label = ctk.CTkLabel(info_frame, text=f"Author: {book['author']}")
            book_author_label.pack(fill='x', expand=False)
            book_publisher_label = ctk.CTkLabel(info_frame, text=f"Publisher: {book['publisher']}")
            book_publisher_label.pack(fill='x', expand=False)

            move_up_button = ctk.CTkButton(button_frame, width=5, height=5, text="↑", command=lambda idx=index: self.move_up_book(idx))
            move_up_button.grid(row=0, padx=5, pady=5)

            edit_button = ctk.CTkButton(button_frame, width=5, height=5, text="Edytuj", command=lambda idx=index: self.edit_book(idx))
            edit_button.grid(row=1, padx=5, pady=5)

            delete_button = ctk.CTkButton(button_frame, width=5, height=5, text="Usuń", command=lambda idx=index: self.delete_book(idx))
            delete_button.grid(row=2, padx=5, pady=5)

            move_down_button = ctk.CTkButton(button_frame, width=5, height=5, text="↓", command=lambda idx=index: self.move_down_book(idx))
            move_down_button.grid(row=3, padx=5, pady=5)
