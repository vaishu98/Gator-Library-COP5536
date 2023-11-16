from GatorRedBlack import RBTree

class GatorLibrary():

    def __init__(self):
        self.bst = RBTree()

    def InsertBook(self, bookID, title, author, availability):
        self.bst.insertNode(bookID, title, author, availability)
        self.bst.updateColorFlips()

    def DeleteBook(self, bookID):
        print(self.bst.delete_node(bookID))
        self.bst.updateColorFlips()

    def BorrowBook(self, patronID, bookID, patronPriority):
        print(self.bst.borrowBook(patronID, bookID, patronPriority))

    def ReturnBook(self, patronID, bookID):
        print(self.bst.returnBook(patronID, bookID))

    def ColorFlipCount(self):
        print(self.bst.getColorFlipCount())

    def PrintBook(self, bookID):
        ans = self.bst.printBook(bookID)
        for i in ans:
            print(i)

    def PrintBooks(self, bookID1, bookID2):
        print("books range.....", bookID1, bookID2 )
        ans = self.bst.printBooks(bookID1, bookID2)
        for i in ans:
            for j in i:
                print(j)