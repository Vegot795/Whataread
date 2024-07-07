

def sort_books(books, sort_option):
    if sort_option == "Własne":
        return sorted(books, key=lambda x: x['id'])
    elif sort_option == "Tytuł":
        return sorted(books, key=lambda x: x['title'])
    elif sort_option == "Autor":
        return sorted(books, key=lambda x: x['author'])
    elif sort_option == "Wycawca":
        return sorted(books, key=lambda x: x['publisher'])
    else:
        return sorted(books, key=lambda x: x['id'])
