from utils import books

# ^ add_book Function
def add_book():
    name = input("Enter Book Name : ")
    books.append(name)
    print(name,"is added.")