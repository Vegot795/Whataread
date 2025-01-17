import customtkinter as ctk
import BookMod
from App.AddBookMod import AddBook
from EditBookMod import EditBook


class App(ctk.CTk):
    def __init__(self, books_instance):
        super().__init__()
        self.configure(fg_color='green')
        self.geometry("600x800")
        self.title("Whataread")
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(2, weight=1)

        self.my_books = books_instance

        self.title_label = ctk.CTkLabel(self, text="Whataread!", font=("default", 40))
        self.title_label.pack(fill='both', expand=False, pady=5, padx=5)

        search_bar = ctk.CTkFrame(self)
        search_bar.pack(fill='both', expand=False, pady=5, padx=5)
        search_bar.columnconfigure(0, weight=0)
        search_bar.columnconfigure(1, weight=1)

        search_label = ctk.CTkLabel(search_bar, text="Wyszukaj: ")
        search_label.grid(column=0, row=0, sticky='e')

        self.search_entry = ctk.CTkEntry(search_bar)
        self.search_entry.grid(column=1, row=0, sticky='ew')
        self.search_entry.bind("<KeyRelease>", self.search_books)  # Bind key release event to search_books method

        self.book_list_frame = ctk.CTkFrame(self)
        self.book_list_frame.pack(fill='both', expand=True, pady=5, padx=5)

        self.button = ctk.CTkButton(self, text='Dodaj książkę', command=self.open_add_book_window)
        self.button.pack(fill='both', expand=False, pady=5, padx=5)

        self.add_book = None

        self.update_book_list()

    def open_add_book_window(self):
        if self.add_book is not None and self.add_book.winfo_exists():
            self.add_book.destroy()

        self.add_book = AddBook(self.my_books)
        self.add_book.wait_window()
        self.update_book_list()

    def edit_book_window(self, index):
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
        self.my_books.save_books()
        self.update_book_list()

    def search_books(self, event=None):
        query = self.search_entry.get().lower()
        filtered_books = [book for book in self.my_books.get_books() if
                          query in book['title'].lower() or
                          query in book['author'].lower() or
                          query in book['publisher'].lower()]
        self.update_book_list(filtered_books)

    def update_book_list(self, books=None):
        for widget in self.book_list_frame.winfo_children():
            widget.destroy()

        current_books = books if books is not None else self.my_books.get_books()

        for index, book in enumerate(current_books):
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

            move_up_button = ctk.CTkButton(button_frame, width=5, height=5, text="↑", corner_radius=50,
                                           command=lambda idx=index: self.move_up_book(idx))
            move_up_button.grid(row=0, padx=5, pady=5)

            edit_button = ctk.CTkButton(button_frame, width=5, height=5, text="Edytuj", corner_radius=15,
                                        command=lambda idx=index: self.edit_book_window(idx))
            edit_button.grid(row=1, padx=5, pady=5)

            delete_button = ctk.CTkButton(button_frame, width=5, height=5, text="Usuń", corner_radius=15,
                                          command=lambda idx=index: self.delete_book(idx))
            delete_button.grid(row=2, padx=5, pady=5)

            move_down_button = ctk.CTkButton(button_frame, width=5, height=5, text="↓", corner_radius=15,
                                             command=lambda idx=index: self.move_down_book(idx))
            move_down_button.grid(row=3, padx=5, pady=5)

