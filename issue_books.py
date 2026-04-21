from utils import books, issued_books
from show_books import show_book

# ^ issue_book Function
def issue_book():
    show_book()
    print("-"*20)
    name = input("Enter Book Name : ")
    if name in books:
        books.remove(name)
        issued_books.append(name)
        print(name,'is issued.')
    else:
        print(name,"is not available.")