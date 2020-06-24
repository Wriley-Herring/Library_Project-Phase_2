'''
@author: wrileyherring
'''
#import packages
from book import Book
from patron import Patron
from library import Library

def main():
    
    #declare books and patrons
    book1 = Book("Of Mice and Men", "Steinbeck")
    book2 = Book("The Great Gatsby", "Fitzgerald")
    book3 = Book("1984","Orwell")
    book4 = Book("One Flew Over the Cuckoo's Nest","Kesey")
    patron1 = Patron("Ivan")
    patron2 =Patron("Jimmy")
    patron3 = Patron("Bob")
    
    #add books
    libraryBooks = []
    libraryBooks.append(book1)
    libraryBooks.append(book2)
    libraryBooks.append(book3)
    libraryBooks.append(book4)

    #create Library to store books and patrons
    myLibrary = Library(libraryBooks)
    
    #add patrons to library
    myLibrary.addPatron(patron1)
    myLibrary.addPatron(patron2)
    myLibrary.addPatron(patron3)
    
    #test borrowing features
    myLibrary.borrowBook(book1, patron2)
    myLibrary.borrowBook(book1, patron3)
    
    #Check Print Status
    print(str(myLibrary))
    
    #check return features
    myLibrary.returnBook(book1)
    
    #see if book was returned correctly
    print(str(myLibrary))
    

if __name__ == '__main__':
    main()
