from utils import books

# ^ show_books Function
def show_book():
    if len(books)==0:
        print("No Books Available.")
    else:
        print('Avaliable Books : ')
        for book in books:
            print(book)