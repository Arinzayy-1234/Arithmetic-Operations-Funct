

# Are there any places that putting  try and except block will be good ?
class Book:
    
    
    def __init__(self,title,author):
        self.title = title
        self.author = author
        self._is_checked_out = False
           
    def check_out(self): # this checks the book out and returns True or doesn't do anything cause the book has already been checked out and returns False
        if not self._is_checked_out:
            self._is_checked_out = True
            return True #checkout sucessful
        else:
            return False # Indicates the book has been checked out already
             
    def return_book(self): # this returns the book that was checked out and returns True or doesn't do anything cause the book has already been returned or wasn't taken at all and returns False
        if self._is_checked_out:
            self._is_checked_out = False
            return True #Indicates that the book has been returned
        else:
            return False # Book hasn't been taken yet
class Library:
    def __init__(self):
        self._books = []
    
    def add_book(self,book_object):
        if isinstance(book_object,Book): # Good practice: ensure it's a Book object
            self._books.append(book_object)
        else:
            print(f'You can\'t add this {book_object}, only book objects can be added')
        
    def check_out_book(self,title): # this checks out a book it recieves and displays the status of a book, whether it has been checked out already, or it has just been succesfully checked out now or it doesn't  exists in the library  
        found_book = None
        for book in self._books:
            if book.title == title :
                found_book = book
                break
        if found_book:
            if not found_book._is_checked_out:
                found_book.check_out()
                print(f'The book {title} has been checked out sucessfully')
            else:
                print(f'The book {title} has already been checked out')
        else:
            print(f'This book {title} isn\'t in this library')

            
    def return_book(self,title):
        found_book = None
        for book in self._books:
            if book.title == title:
                found_book = book
                break
        if found_book:
            if found_book._is_checked_out:
                found_book.return_book()
                print(f'Book {title} has been returned')
            else:
                print(f'This Book {title} was never checked out')
        else:
            print(f'This book {title} doesn\'t exist')
        
        
        
        
    def list_available_books(self):
        found_available = False
        for book in self._books:
            if not book._is_checked_out:
                print(f'{book.title} by {book.author}')
                found_available = True
        if not found_available:
            print(f'No books currently available.')
    
            
book_1 = Book("Brave New World", "Aldous Huxley")
book_2 = Book("1984", "George Orwell")
library_1 = Library()

library_1.add_book(book_1)
library_1.add_book(book_2)

library_1.list_available_books()

library_1.check_out_book('1984')

library_1.list_available_books()

