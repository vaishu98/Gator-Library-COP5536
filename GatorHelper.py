from GatorRedBlack import RBTree

class GatorLibrary():

    def __init__(self):
        self.bst = RBTree()

    def InsertBook(self, bookID, title, author, availability):
        '''print("BookID = "+str(bookID)+"")
        print("Title = \""+title+"\"") 
        print("Author = \""+author+"\"")
        print("Availability = \""+availability+"\"")
        print("BorrowedBy = None")
        print("Reservations = []")'''
        self.bst.insertNode(bookID, title, author, availability)

    def DeleteBook(self, bookID):
        print(self.bst.delete_node(bookID))

    def BorrowBook(self, patronID, bookID, patronPriority):
        print(self.bst.borrowBook(patronID, bookID, patronPriority))

    def ReturnBook(self, patronID, bookID):
        print(self.bst.returnBook(patronID, bookID))
