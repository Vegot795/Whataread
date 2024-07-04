import os
import customtkinter as ctk
import json

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.configure(fg_color='green')
        self.geometry("600x800")
        self.title("Whataread")
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(2, weight=1)

        self.title_label = ctk.CTkLabel(self, text="Whataread!", font=("default", 40))
        self.title_label.pack(fill='both', expand = False, pady=5, padx=5)
        self.search_entry = ctk.CTkEntry(self)
        self.search_entry.pack(fill='both', expand = False, pady=5, padx=5)

        list_frame = ctk.CTkFrame(self)
        list_frame.pack(fill='both', expand = True, pady=5, padx=5)






class Book():
    def __init__(self):
        self.books = []
        if not os.path.exists('saves/books.json'):
            self.tasks.append({
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

        self.title = title
        self.author = author
        self.publisher = publisher


app = App()
app.mainloop()

