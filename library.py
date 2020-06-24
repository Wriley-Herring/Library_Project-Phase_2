'''

@author: wrileyherring
'''

class Library(object):
    '''
    
    Libarary Object
    
    '''


    def __init__(self, books):
        '''
        Set Library Variables
        '''
        self.books = books
        self.patrons = []
        
        #add patrons to library
    def addPatron(self,patron):
        self.patrons.append(patron)
        
        #borrow book from library
    def borrowBook(self,book, patron):
        
        patron.addBook(book)
        book.borrow(patron)
        
        #return book to library
    def returnBook(self,book):
        
        #remove book from patron name
        book.owner.checkedOutBooks.remove(book)
        
        #print returned output
        print('Returned: {}'.format(str(book)))
        
        #set owner to none
        book.owner = 'none'
        
        
        #set output for library
    def __str__(self):
        
        out =['Books: ']
        
        #output status for each book
        for book in self.books:
            
            out.append(str(book))
            
        
        out.append('Patrons: ')
        
        #output status for each patron
        for patron in self.patrons:
            out.append(str(patron))
         
        out.append('\n')   
        
        return '\n'.join(out)          
        
        
        
        
