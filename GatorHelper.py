from GatorRedBlack import RBTree

class GatorLibrary():

    # Initializing the Gator Library object
    def __init__(self, outputFileName: str):

        # Initializing a Red Black Tree for this input file
        self.bst = RBTree()

        # Creating an output file
        self.output_file = open(outputFileName, 'w')

    # Handling Insert book operation
    def InsertBook(self, bookID: int, title: str, author: str, availability: str):
        self.bst.insertNode(bookID, title, author, availability)
        #Updating Color Flips after insert operation
        self.bst.updateColorFlips()

    # Handling Delete book operation
    def DeleteBook(self, bookID: int):
        self.output_file.write(self.bst.delete_node(bookID))
        # Updating Color Flips after delete operation
        self.bst.updateColorFlips()
        self.output_file.write("\n\n")

    # Handling Borrow book operation
    def BorrowBook(self, patronID: int, bookID: int, patronPriority: int):
        self.output_file.write(self.bst.borrowBook(patronID, bookID, patronPriority))
        self.output_file.write("\n\n")

    # Handling Return book operation
    def ReturnBook(self, patronID: int, bookID: int):
        self.output_file.write(self.bst.returnBook(patronID, bookID))
        self.output_file.write("\n\n")

    # Handling get Color Flip Count book operation
    def ColorFlipCount(self):
        self.output_file.write(self.bst.getColorFlipCount())
        self.output_file.write("\n\n")

    # Handling Print book operation
    def PrintBook(self, bookID: int):
        ans = self.bst.printBook(bookID)
        for i in ans:
            self.output_file.write(i)
        self.output_file.write("\n\n")

    # Handling Print books in given range operation
    def PrintBooks(self, bookID1: int, bookID2: int):
        ans = self.bst.printBooks(bookID1, bookID2)
        for i in ans:
            for j in i:
                self.output_file.write(j)
            self.output_file.write("\n\n")

    # Handling Find the closest book operation
    def FindClosestBook(self, bookID: int):
        ans= self.bst.findClosestBook(bookID)
        for i in ans:
            for j in i:
                self.output_file.write(j)
            self.output_file.write("\n\n")

    # Handling Quit operation
    def Quit(self):
        self.output_file.write("Program Terminated!!")
