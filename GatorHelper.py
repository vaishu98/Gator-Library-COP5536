from GatorRedBlack import RBTree

class GatorLibrary():

    def __init__(self):
        self.bst = RBTree()

    def InsertBook(self, bookID, title, author, availability):
        self.bst.insertNode(bookID, title, author, availability)
        self.bst.updateColorFlips()

    def DeleteBook(self, bookID):
        print(self.bst.delete_node(bookID))
        print()
        self.bst.updateColorFlips()

    def BorrowBook(self, patronID, bookID, patronPriority):
        print(self.bst.borrowBook(patronID, bookID, patronPriority))
        print()

    def ReturnBook(self, patronID, bookID):
        print(self.bst.returnBook(patronID, bookID))
        print()

    def ColorFlipCount(self):
        print(self.bst.getColorFlipCount())
        print()

    def PrintBook(self, bookID):
        ans = self.bst.printBook(bookID)
        for i in ans:
            print(i)
        print()

    def PrintBooks(self, bookID1, bookID2):
        ans = self.bst.printBooks(bookID1, bookID2)
        for i in ans:
            for j in i:
                print(j)
            print()

    def FindClosestBook(self, bookID):
        ans= self.bst.findClosestBook(bookID)
        for i in ans:
            for j in i:
                print(j)
            print()
