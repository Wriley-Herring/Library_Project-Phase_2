'''
Created on Jun 13, 2020

@author: wrileyherring
'''

class Book(object):
    '''
    Book Object
    '''
    
    #assign class vairiables
    def __init__(self, title,author):

        self.title = title
        self.author = author
        self.bookQueue = []
        self.owner = 'none'
    
    #borrow method allows books to be assigned to patrons
    def borrow(self,patron):
        
        #check if anyone is in the queue
        if len(self.bookQueue) == 0:
        
            #assign current owner of book
            self.owner = patron
            
    #create print method to tell current status of book (Owner and Queue
    def __str__(self):
        
        #check if the book is checked out
        if not isinstance(self.owner, str):
        
            out =['{}, {} in care of: {}\nWaiting:'.format(self.title,self.author,str(self.owner))]
            
            #print the waiting list for the book
            for i in range(0,len(self.bookQueue)):
                out.append('{}. {}\n'.format(i+1,str(self.bookQueue[i])))
            
            #return output string
            return '\n'.join(out)
        
        #return non checked out output
        elif len(self.bookQueue) == 0:
            return '{}, {} has not been borrowed\nWaiting:\n'.format(self.title,self.author)
        
        #return non checked out with waiting list
        else:
            out = ['{}, {} has not been borrowed\nWaiting:'.format(self.title,self.author)]
            
            #print the waiting list
            for i in range(0,len(self.bookQueue)):
                out.append('{}. {}\n'.format(i+1,str(self.bookQueue[i])))

            return '\n'.join(out)
        
        
        
        
        
        
        
        
        
        
        
        
        