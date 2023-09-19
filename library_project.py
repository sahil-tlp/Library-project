### library books borrow - return project
class Book:
    def __init__(self,name,author,id):
        self.name=name
        self.author=author
        self.id=id
        self.present=True
    def is_present(self):
        return self.present


    def book_borrow(self):
        if self.present:
            self.present=False
            print(f"The mention {self.name} book is been borrowed")
        else:
            print(f"The mention {self.name} book is out of stock borrowed")


    def book_return(self):
        if not self.present:
            self.present=True
            print(f"The mention book {self.name} is return")
        else:
            print(f"The mention book {self.name} is already present")


class Library:
    def __init__(self):
        self.books_library=[]
    def add_book(self,mention_book):
        self.books_library.append(mention_book)
        print(f"the book name {mention_book.name} is added in library")

    def search_book(self,mention_name):
        found_books=[i for i in self.books_library if i.name.lower()==mention_name.lower()]
        if found_books:
            print(f"the {len(found_books)} book with name {mention_name} is found")
            for index,i in enumerate(found_books,start=1):
                print(f"book:{index}\nits name:{i.name}") 
        else:
            print("the book with this name not found")
    def borrow_book(self,mention_name):
        found_books=[i for i in self.books_library if i.name.lower()==mention_name.lower()]
        if found_books:
            in_stock=[i for i in self.books_library if i.is_present()]
            if in_stock:
                i=in_stock[0]
                i.book_borrow() 
            else:
                print(f"the book with name {mention_name} is already borrowed")
        else:
            print(f"the book with name {mention_name} not exist in library")
    def return_book(self,mention_name):
        found_books=[i for i in self.books_library if i.name.lower()==mention_name.lower()]
        if found_books:
            borrow_books=[i for i in self.books_library if not i.is_present()]
            if borrow_books:
                i=borrow_books[0]
                i.book_return()
            else:
                print(f"the book with name {mention_name} is already borrowed")
        else:
            print(f"the book with name {mention_name} not exist in library")
        
book1=Book("Harry Potter and the Sorcerer's Stone","J.K Rowling","343985901045")
book2=Book("To kill a Mockingbird","Harper Lee","94302012694")
book4=Book("1984","George Orwell","235290912489")
book3=Book("To kill a Mockingbird","Harper Lee","94302012394")
book5=Book("To kill a Mockingbird","Harper Lee","94302011394")


library=Library()
library.add_book(book1)
library.add_book(book2)

library.search_book("Harry Potter and the Sorcerer's Stone")
library.borrow_book("Harry Potter and the Sorcerer's Stone")
library.borrow_book("Harry Potter and the Sorcerer's Stone")
library.borrow_book("To kill a Mockingbird")