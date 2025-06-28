

# Are there any places that putting  try and except block will be good ?
class Book:
    _is_checked_out = False
    
    def __init__(self,title,author):
        self.title = title
        self.author = author
           
class Library:
    
    _books = []
    _books_inventory = []# this is a list to store all the books the library has. 
    
    def __init__(self):
        pass # should i even create this __init__ function , since i am not using it 
        
        
    def add_book(self,*book_objects): # should i and can i turn this to a lambda function
        for book in book_objects:
            Library._books.append(book)
            Library._books_inventory.append(book)
        
    def check_out_book(self,title):
        counter = 0
        for book in Library._books:
            counter += 1
            if book.title == title :
                book._is_checked_out = True # here should i use the book class (i.e Book._is_checked_out)
                
                del Library._books[counter - 1] # is it okay to delete a list without using the bracket. And is the counter - 1 okay ? how do i make it more descriptive
            else:
                continue
        if not Book._is_checked_out: # here should i have used an object of book class (i.e book_1._is_checked_out) ?
            print(f'The book doesn\'t exist')
            
    def return_book(self,title):
        returned = False # is this okay ?
        for book in Library._books_inventory: # instead of creating another list _books_inventory, is there a way to just use _books list, i thought of 'slicing' but i don't know ?
            if book.title == title:
                returned = True
                Library._books.append(book)
        if not returned:
            print(f'This is not the library\'s book')
        
    def list_available_books(self):
        for book in Library._books:
            print(f'{book.title} by {book.author}')
    
"""         
book_1 = Book("Brave New World", "Aldous Huxley")
book_2 = Book("1984", "George Orwell")
library_1 = Library()

library_1.add_book(book_1,book_2)
library_1.list_available_books()

library_1.check_out_book('1984')
library_1.list_available_books()
library_1.return_book('1984')
library_1.list_available_books()

"""
