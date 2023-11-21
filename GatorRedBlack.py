# Importing custom MinHeap implementation
from MinHeap import MinHeap
import time

# Defining Node() -> each node in the Red Black Tree
class Node():

    def __init__(self, bookID: int, title: str, author: str, availability: str):

        # Initializing Values in a Node
        self.bookID = bookID
        self.parent = None
        self.left = None
        self.right = None
        self.color = 1
        self.bookName = title
        self.authorName =  author
        self.availabilityStatus = availability
        self.borrowedBy = None

        # Reservation Heap to store the borrow requests
        self.reservationHeap = MinHeap(20)


# Defining the Red Black Tree Class
class RBTree():

    def __init__(self):

        # Empty Node() definition
        self.NULL = Node ( 0, None, None, None )

        # Deafult Color of the node
        self.NULL.color = 0
        self.NULL.left = None
        self.NULL.right = None
        self.root = self.NULL

        # Initializing colorFlips variable to track color flips until now
        self.colorFlips = 0

        # Hashmap to store the color states of ll the nodes in the tree
        self.colorState = {}


    # Function to compute color flips after an operation using the state stored in colorState variable
    def updateColorFlips(self):

        # Variable to store the current color states
        currentColorStatus = {}

        # Function to compute color flips
        def traverse(root):
            if root and root.bookID:
                currentColorStatus[root.bookID] = root.color
                if root.bookID in self.colorState:
                    # Color flip has occurred
                    if self.colorState[root.bookID] != root.color:
                        self.colorFlips += 1        # Increment Color flips variable
                traverse(root.right)
                traverse(root.left)

        traverse(self.root)
        self.colorState = {}
        # Updating the previous colorState with current color state
        for i in currentColorStatus:
            self.colorState[i] = currentColorStatus[i]


    # Inserting a new Node into the Red Black Tree
    def insertNode(self, bookID: int, title: str, author: str, availability: str):

        # Initializing the node
        node = Node(bookID, title, author, availability)

        # Setting the values for that node
        node.parent = None
        node.bookID = bookID
        self.title = title
        self.author = author
        self.availability = availability
        node.left = self.NULL
        node.right = self.NULL
        node.color = 1

        y = None
        x = self.root

        # Inserting using Binary Search Tree logic
        while x != self.NULL :
            y = x
            if node.bookID < x.bookID :
                x = x.left
            else :
                x = x.right

        node.parent = y
        if y == None :
            self.root = node
        elif node.bookID < y.bookID :
            y.left = node
        else :
            y.right = node

        if node.parent == None :
            node.color = 0
            return

        if node.parent.parent == None :
            return

        # Fixing colors and balancing the Red Black Tree after Insertion
        self.fixInsert ( node )

    # Function to get the maximum value in the subtree
    def maximum(self, node: Node):
        while node.right != self.NULL:
            node = node.right           # Larger value always lies in the right subtree
        return node


    # Function to perform the LR (Left-Right) Rotation
    def LR ( self , x: Node ) :
        y: Node = x.right
        x.right = y.left
        if y.left != self.NULL :
            y.left.parent = x

        y.parent = x.parent
        if x.parent == None :
            self.root = y
        elif x == x.parent.left :
            x.parent.left = y
        else :
            x.parent.right = y
        y.left = x
        x.parent = y

    # Function to perform the RR (Right-Right) Rotation
    def RR ( self , x: Node ) :
        y: Node = x.left
        x.left = y.right
        if y.right != self.NULL :
            y.right.parent = x

        y.parent = x.parent
        if x.parent == None :
            self.root = y
        elif x == x.parent.right :
            x.parent.right = y
        else :
            x.parent.left = y
        y.right = x
        x.parent = y


    # Function to check the colors and perform Rotations of each node after Insertion operation
    def fixInsert(self, k: Node):
        while k.parent.color == 1:
            if k.parent == k.parent.parent.right:
                u = k.parent.parent.left
                if u.color == 1:
                    u.color = 0
                    k.parent.color = 0
                    k.parent.parent.color = 1
                    k = k.parent.parent
                else:
                    if k == k.parent.left:
                        k = k.parent
                        self.RR(k)
                    k.parent.color = 0
                    k.parent.parent.color = 1
                    self.LR(k.parent.parent)
            else:
                u = k.parent.parent.right
                if u.color == 1:
                    u.color = 0
                    k.parent.color = 0
                    k.parent.parent.color = 1
                    k = k.parent.parent
                else:
                    if k == k.parent.right:
                        k = k.parent
                        self.LR(k)
                    k.parent.color = 0
                    k.parent.parent.color = 1
                    self.RR(k.parent.parent)
            if k == self.root:
                break
        self.root.color = 0


    # Balancing the tree after deletion
    def delete_fix(self, x:Node):
        while x != self.root and x.color == 0:
            if x == x.parent.left:
                s = x.parent.right
                if s.color == 1:
                    s.color = 0
                    x.parent.color = 1
                    self.LR(x.parent)
                    s = x.parent.right

                if s.left.color == 0 and s.right.color == 0:
                    s.color = 1
                    x = x.parent
                else:
                    if s.right.color == 0:
                        s.left.color = 0
                        s.color = 1
                        self.RR(s)
                        s = x.parent.right

                    s.color = x.parent.color
                    x.parent.color = 0
                    s.right.color = 0
                    self.LR(x.parent)
                    x = self.root
            else:
                s = x.parent.left
                if s.color == 1:
                    s.color = 0
                    x.parent.color = 1
                    self.RR(x.parent)
                    s = x.parent.left

                if s.right.color == 0 and s.left.color == 0:
                    s.color = 1
                    x = x.parent
                else:
                    if s.left.color == 0:
                        s.right.color = 0
                        s.color = 1
                        self.LR(s)
                        s = x.parent.left

                    s.color = x.parent.color
                    x.parent.color = 0
                    s.left.color = 0
                    self.RR(x.parent)
                    x = self.root
        x.color = 0

    def __rb_transplant(self, u: Node, v: Node):
        if u.parent == None:
            self.root = v
        elif u == u.parent.left:
            u.parent.left = v
        else:
            u.parent.right = v
        v.parent = u.parent

    # Node deletion
    def delete_node_helper(self, node: Node, key: int):
        z = self.NULL
        while node != self.NULL:
            if node.bookID == key:
                z = node

            if node.bookID <= key:
                node = node.right
            else:
                node = node.left

        if z == self.NULL:
            return
        ret = self.deleteBook(z)
        y = z
        y_original_color = y.color
        if z.left == self.NULL:
            x = z.right
            self.__rb_transplant(z, z.right)
        elif (z.right == self.NULL):
            x = z.left
            self.__rb_transplant(z, z.left)
        else:
            y = self.maximum(z.left)
            y_original_color = y.color
            x = y.left
            if y.parent == z:
                x.parent = y
            else:
                self.__rb_transplant(y, y.left)
                y.left = z.left
                y.left.parent = y

            self.__rb_transplant(z, y)
            y.right = z.right
            y.right.parent = y
            y.color = z.color
        if y_original_color == 0:
            self.delete_fix(x)
        return ret


    def delete_node ( self , val: int ) :
        return self.delete_node_helper ( self.root , val )

    def get_node ( self, val: int):
        z = self.NULL
        node = self.root
        while node != self.NULL :
            # Node found
            if node.bookID == val :
                z = node

            # Value of BookID in Node is less than the val we are searching for
            if node.bookID <= val :
                node = node.right
            else :
                # Value of BookID in Node is more than the val we are searching for
                node = node.left
        if z == self.NULL :
            # Node not present with val as BookID
            return None
        return z

    # Print tree helper function
    def __printCall ( self , node: Node , indent: chr , last: bool ) :
        if node != self.NULL :
            print(indent, end=' ')
            if last :
                print ("R----",end= ' ')
                indent += "     "
            else :
                print("L----",end=' ')
                indent += "|    "

            s_color = "RED" if node.color == 1 else "BLACK"
            print ( str ( node.bookID ) + "(" + s_color + ")" )
            self.__printCall ( node.left , indent , False )
            self.__printCall ( node.right , indent , True )

    # Debugging function to print the tree with the colors
    def print_tree ( self ) :
        self.__printCall ( self.root , "" , True )

    # Function to handle the BorrowBook call
    def borrowBook(self, patronID: int, bookID: int, patronPriority: int):

        # Fetching the book 
        book = self.get_node(bookID)
        if book:
            # Book is available to be borrowed
            if book.availabilityStatus=="Yes":
                book.borrowedBy=patronID
                book.availabilityStatus = "No"
                return "Book "+str(bookID)+" borrowed by Patron "+str(patronID)
            else:
                # Book is currently not available. Add to reservation Heap based on priority and timestamp
                book.reservationHeap.insert((patronPriority, patronID, time.time()))
                return "Book "+str(bookID)+" reserved by Patron "+str(patronID)
        # Book is no longer available
        return "Book "+str(bookID)+" is no longer available"


    # Request to handle the ReturnBook request
    def returnBook(self, patronID: int, bookID: int):

        # Fetching the book
        book = self.get_node(bookID)
        ret = "Book "+str(bookID)+" returned by Patron "+str(patronID)
        borrower=None
        availability = "Yes"

        # Checking the Reservations heap
        if book.reservationHeap:

            # Fetching the borrower based on priority and timestamp
            allotedPatron = book.reservationHeap.remove()
            if allotedPatron:
                if not borrower:
                    borrower=allotedPatron[1]
                ret += "\n\nBook "+str(bookID)+" allotted to Patron "+str(allotedPatron[1])
                availability = "No"

        # Allocating the book to a new Borrower
        book.borrowedBy = borrower
        book.availabilityStatus = availability
        return ret

    # Function to handle Delete Book request
    def deleteBook(self, book: Node):
        patrons = []
        cancelled=""
        heapReservations = book.reservationHeap.getValues()
        for i in range(len(heapReservations)):
            if heapReservations[i]:
                patrons.append(str(heapReservations[i][1]))
        if patrons:
            patronsIDS = ", ".join(patrons)
            pronoun = "have" if len(patrons)>1 else "has"
            count="s" if len(patrons)>1 else ""
            cancelled = ". Reservation"+count+" made by Patron"+count+" "+patronsIDS+" "+pronoun+" been cancelled!"
        return "Book "+str(book.bookID)+" is no longer available"+cancelled

    # Function to fetch the total color flip count after operations until now in the tree
    def getColorFlipCount(self):
        return "Color Flip Count: "+str(self.colorFlips)

    # Function to print details of a particular Book
    def printBook( self, bookID: int):

        # Get the node with the BookID val
        book = self.get_node(bookID)
        ret = []
        if book:
            reservations = []
            heapReservations=book.reservationHeap.getValues()
            heapReservations.sort(key = lambda x: [x[0],x[2]])
            for i in range(len(heapReservations)):
                if heapReservations[i]:
                    reservations.append(heapReservations[i][1])

            ret.append("BookID = "+str(book.bookID)+"\n")
            ret.append("Title = \""+book.bookName+"\""+"\n")
            ret.append("Author = \""+book.authorName+"\""+"\n")
            ret.append("Availability = \""+book.availabilityStatus+"\""+"\n")
            ret.append("BorrowedBy = "+str(book.borrowedBy) +
                       "\n" if book.borrowedBy else "BorrowedBy = None"+"\n")
            ret.append("Reservations = "+str(reservations))
        else:
            ret.append("Book "+str(bookID)+" not found in the library")
        return ret


    # Function to print all the books with BookIDs in the given range
    def printBooks( self, bookID1: int, bookID2: int):
        ret = []

        # Function to recursively iterate through all the trees and fetch books in the given range
        def inorderTraversal(root: Node):
            if root:
                if root.bookID > bookID2:
                    return
                inorderTraversal(root.left)
                if (root.bookID >= bookID1) and (root.bookID <= bookID2):
                    ret.append(self.printBook(root.bookID))
                inorderTraversal(root.right)
            return
        inorderTraversal(self.root)
        return ret

    # Function to fetch the closest book to the given bookID
    def findClosestBook(self, bookID: int):

        # Variable to store the count of closest books
        count=[0]
        mini=[9999999999]

        # Inorder traversal to fetch nodes in ascending order
        def inorderTraversal(root):
            if root!=self.NULL:
                inorderTraversal(root.left)

                # Book found with same minimum distance
                if abs(root.bookID - bookID) == mini[0]:
                    count[0]=2

                # Closer book found
                if abs(root.bookID - bookID) < mini[0]:

                    # Closest book has bookID less than the given bookID
                    if root.bookID - bookID <0:
                        count[0]=-1

                    # Book with same bookID found
                    if root.bookID - bookID == 0:
                        count[0] = 0

                    # Closest book has bookID more than the given bookID
                    if root.bookID - bookID > 0:
                        count[0] = 1
                    
                    # Computing difference between closest book and the given bookID
                    mini[0] = abs(root.bookID - bookID)
                inorderTraversal(root.right)
            return

        inorderTraversal(self.root)

        # Initializing with no closest books
        ret = []
        # Two closest books found
        if count[0] == 2:
            ret.append(self.printBook(bookID-mini[0]))
            ret.append(self.printBook(bookID+mini[0]))
        
        # Only one closest book found
        else:
            ret.append(self.printBook(bookID+(mini[0]*count[0])))
        return ret



