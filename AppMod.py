import customtkinter as ctk
from AddBookMod import AddBook

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
        self.search_entry = ctk.CTkEntry(self)
        self.search_entry.pack(fill='both', expand=False, pady=5, padx=5)

        self.book_list_frame = ctk.CTkFrame(self)
        self.book_list_frame.pack(fill='both', expand=True, pady=5, padx=5)

        self.button = ctk.CTkButton(self, text='Dodaj książkę', command=self.open_add_book)
        self.button.pack(fill='both', expand=False, pady=5, padx=5)

        self.add_book = None

        self.update_book_list()

    def open_add_book(self):
        if self.add_book is not None and self.add_book.winfo_exists():
            self.add_book.destroy()

        self.add_book = AddBook(self.my_books)
        self.add_book.wait_window()
        self.update_book_list()

    def update_book_list(self):
        current_books = self.my_books.get_books()
        for widget in self.book_list_frame.winfo_children():
            widget.destroy()

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

            move_up_button = ctk.CTkButton(button_frame, width=5, height=5, text="UP")
            move_up_button.grid(row=0, padx=5, pady=5)

            edit_button = ctk.CTkButton(button_frame, width=5, height=5, text="Edit")
            edit_button.grid(row=1, padx=5, pady=5)

            move_down_button = ctk.CTkButton(button_frame, width=5, height=5, text="down")
            move_down_button.grid(row=2, padx=5, pady=5)
