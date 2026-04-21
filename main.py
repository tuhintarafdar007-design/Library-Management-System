from add_books import add_book
from show_books import show_book
from issue_books import issue_book
from return_books import return_book

# ! Library Function
def library():
    while True:
        print("-"*30)
        print("Menu")
        print("1.Add Book")
        print("2.Show Books")
        print("3.Issue Book")
        print("4.Return Book")
        print("5.Exit")
        print("-"*30)

        choice = int(input("Enter Your Choice : "))
        print("-"*30)

        if choice == 1:
            add_book()
        elif choice == 2:
            show_book()
        elif choice == 3:
            issue_book()
        elif choice == 4:
            return_book()
        elif choice == 5:
            print("Thank You!")
            break
        else:
            print("Invalid Choice!")
            
library()