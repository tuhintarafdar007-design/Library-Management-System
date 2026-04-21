from utils import issued_books, books

# ^ return_book Function
def return_book():
    name = input("Enter Book Name : ")
    if name in issued_books:
        issued_books.remove(name)
        books.append(name)
        print(name, "is returned.")
    else:
        print(name,"was not issued from library.")