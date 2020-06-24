'''
@author: wrileyherring
'''

class Patron(object):
    '''
    Patron object
    '''

    #assign class variables for patron object
    def __init__(self, name):
       
        self.name = name
        self.checkedOutBooks = []
    
    #addBook method allows tracking of which books a patron has checked out
    def addBook(self,book):
        
        #check if the patron has check out more than three books
        if len(self.checkedOutBooks) > 3:
            print("\nCan't borrow more books--MAX REACHED!")
        
        #add patron to queue
        elif isinstance(book.owner, Patron):
            book.bookQueue.append(self)
        
        #add the book to patrons checked out book list   
        else:
            self.checkedOutBooks.append(book)
            
    #print method to determine how many books the patron has checked out       
    def __str__(self):
        
        #return the number of books the patron has checked out
        return "{} has {} books.".format(self.name,len(self.checkedOutBooks))
