from heapq import heappush, heappop
from math import inf
from MinHeap import MinHeap
import time

class Node():
    def __init__(self, bookID, title, author, availability):
        self.bookID = bookID
        self.parent = None
        self.left = None
        self.right = None
        self.color = 1
        self.bookName = title
        self.authorName =  author
        self.availabilityStatus = availability
        self.borrowedBy = None
        self.reservationHeap = MinHeap(20)

class RBTree():
    def __init__(self):
        self.NULL = Node ( 0, None, None, None )
        self.NULL.color = 0
        self.NULL.left = None
        self.NULL.right = None
        self.root = self.NULL
        self.colorFlips = 0
        self.colorState = {}

    def updateColorFlips(self):
        currentColorStatus = {}
        #self.print_tree()
        def traverse(root):
            if root and root.bookID:
                currentColorStatus[root.bookID] = root.color
                if root.bookID in self.colorState:
                    if self.colorState[root.bookID] != root.color:
                        self.colorFlips += 1
                traverse(root.right)
                traverse(root.left)
        traverse(self.root)
        self.colorState = {}
        for i in currentColorStatus:
            self.colorState[i] = currentColorStatus[i]


    def insertNode(self, bookID, title, author, availability):
        node = Node(bookID, title, author, availability)
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
            #if node.color == 1:
                #self.colorFlips+=1
            node.color = 0
            return

        if node.parent.parent == None :
            return

        self.fixInsert ( node )

    def maximum(self, node):
        while node.right != self.NULL:
            node = node.right
        return node

    def LR ( self , x ) :
        y = x.right
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

    def RR ( self , x ) :
        y = x.left
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



    def fixInsert(self, k):
        while k.parent.color == 1:
            if k.parent == k.parent.parent.right:
                u = k.parent.parent.left
                if u.color == 1:
                    #self.colorFlips+=1
                    u.color = 0
                    #if k.parent.color == 1:
                        #self.colorFlips+=1
                    k.parent.color = 0
                    #if k.parent.parent.color == 0:
                        #self.colorFlips+=1
                    k.parent.parent.color = 1
                    k = k.parent.parent
                else:
                    if k == k.parent.left:
                        k = k.parent
                        self.RR(k)
                    #if k.parent.color == 1:
                        #self.colorFlips+=1
                    k.parent.color = 0
                    #if k.parent.parent.color == 0:
                        #self.colorFlips+=1
                    k.parent.parent.color = 1
                    self.LR(k.parent.parent)
            else:
                u = k.parent.parent.right
                if u.color == 1:
                    #self.colorFlips+=1
                    u.color = 0
                    #if k.parent.color == 1:
                        #self.colorFlips+=1
                    k.parent.color = 0
                    #if k.parent.parent.color == 0:
                        #self.colorFlips+=1
                    k.parent.parent.color = 1
                    k = k.parent.parent
                else:
                    if k == k.parent.right:
                        k = k.parent
                        self.LR(k)
                    #if k.parent.color == 1:
                        #self.colorFlips+=1
                    k.parent.color = 0
                    #if k.parent.parent.color == 0:
                        #self.colorFlips+=1
                    k.parent.parent.color = 1
                    self.RR(k.parent.parent)
            if k == self.root:
                break
        #if self.root.color == 1:
            #self.colorFlips+=1
        self.root.color = 0

    # Balancing the tree after deletion

    def delete_fix(self, x):
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

    def __rb_transplant(self, u, v):
        if u.parent == None:
            self.root = v
        elif u == u.parent.left:
            u.parent.left = v
        else:
            u.parent.right = v
        v.parent = u.parent

    # Node deletion
    def delete_node_helper(self, node, key):
        z = self.NULL
        while node != self.NULL:
            if node.bookID == key:
                z = node

            if node.bookID <= key:
                node = node.right
            else:
                node = node.left

        if z == self.NULL:
            print("Cannot find key in the tree")
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


    def delete_node ( self , val ) :
        return self.delete_node_helper ( self.root , val )

    def get_node ( self, val):
        z = self.NULL
        node = self.root
        while node != self.NULL :
            if node.bookID == val :
                z = node

            if node.bookID <= val :
                node = node.right
            else :
                node = node.left
        if z == self.NULL :
            return None
        return z


    def __printCall ( self , node , indent , last ) :
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

    def print_tree ( self ) :
        self.__printCall ( self.root , "" , True )

    def borrowBook(self, patronID, bookID, patronPriority):
        book = self.get_node(bookID)
        if book:
            if book.availabilityStatus=="Yes":
                book.borrowedBy=patronID
                book.availabilityStatus = "No"
                return "Book "+str(bookID)+" borrowed by Patron "+str(patronID)
            else:
                book.reservationHeap.insert((patronPriority, patronID, time.time()))
                return "Book "+str(bookID)+" reserved by Patron "+str(patronID)
        return "Book "+str(bookID)+" is no longer available"

    def returnBook(self, patronID, bookID):
        book = self.get_node(bookID)
        ret = "Book "+str(bookID)+" returned by Patron "+str(patronID)
        borrower=None
        availability = "Yes"
        if book.reservationHeap:
            allotedPatron = book.reservationHeap.remove()
            if allotedPatron:
                if not borrower:
                    borrower=allotedPatron[1]
                ret += "\n\nBook "+str(bookID)+" allotted to Patron "+str(allotedPatron[1])
                availability = "No"
        book.borrowedBy = borrower
        book.availabilityStatus = availability
        heapReservations = book.reservationHeap.getValues()
        return ret

    def deleteBook(self, book):
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

    def getColorFlipCount(self):
        return "Color Flip Count: "+str(self.colorFlips)

    def printBook( self, bookID):
        book = self.get_node(bookID)
        ret = []
        if book:
            reservations = []
            heapReservations=book.reservationHeap.getValues()
            for i in range(len(heapReservations)):
                if heapReservations[i]:
                    reservations.append(heapReservations[i][1])
            reservations.sort(reverse=True)
            ret.append("BookID = "+str(book.bookID))
            ret.append("Title = \""+book.bookName+"\"")
            ret.append("Author = \""+book.authorName+"\"")
            ret.append("Availability = \""+book.availabilityStatus+"\"")
            ret.append("BorrowedBy = "+str(book.borrowedBy) if book.borrowedBy else "BorrowedBy = None")
            ret.append("Reservations = "+str(reservations))
        else:
            ret.append("Book "+str(bookID)+" not found in the library")
        return ret

    def printBooks( self, bookID1, bookID2):
        ret = []
        min = bookID1
        max= bookID2

        def inorderTraversal(root):
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

    def findClosestBook(self, bookID):
        count=[0]
        mini=[9999999999]
        def inorderTraversal(root):
            if root!=self.NULL:
                inorderTraversal(root.left)
                if abs(root.bookID - bookID) == mini[0]:
                    count[0]=2
                if abs(root.bookID - bookID) < mini[0]:
                    if root.bookID - bookID <0:
                        count[0]=-1
                    if root.bookID - bookID == 0:
                        count[0] = 0
                    if root.bookID - bookID > 0:
                        count[0] = 1
                    mini[0] = abs(root.bookID - bookID)
                inorderTraversal(root.right)
            return
        inorderTraversal(self.root)
        ret = []
        if count[0] == 2:
            ret.append(self.printBook(bookID-mini[0]))
            ret.append(self.printBook(bookID+mini[0]))
        else:
            ret.append(self.printBook(bookID+(mini[0]*count[0])))
        return ret



