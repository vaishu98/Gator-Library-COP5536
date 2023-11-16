from GatorHelper import GatorLibrary

if __name__ == "__main__":
    
    lib = GatorLibrary()

    #Testcase 1
    lib.InsertBook(101, "Introduction to Algorithms", "Thomas H. Cormen", "Yes")
    lib.InsertBook(48, "Data Structures and Algorithms", "Sartaj Sahni", "Yes")
    lib.PrintBook(48)
    lib.InsertBook(132, "Operating System Concepts", "Abraham Silberschatz", "Yes")
    lib.InsertBook(25, "Computer Networks", "Andrew S. Tanenbaum", "Yes")
    lib.BorrowBook(120, 48, 2)
    lib.BorrowBook(132, 101, 1)
    lib.InsertBook(73, "Introduction to the Theory of Computation", "Michael Sipser", "Yes")
    lib.InsertBook(12, "Artificial Intelligence: A Modern Approach", "Stuart Russell", "Yes")
    lib.InsertBook(6, "Database Management Systems", "Raghu Ramakrishnan", "Yes")
    lib.BorrowBook(144, 48, 3)
    lib.BorrowBook(140, 48, 3)
    lib.BorrowBook(142, 48, 2)
    lib.BorrowBook(138, 12, 4)
    lib.BorrowBook(150, 12, 3)
    lib.BorrowBook(162, 12, 1)
    lib.ReturnBook(120, 48)
    #lib.FindClosestBook(9)
    lib.DeleteBook(12)
    lib.ColorFlipCount()
    lib.InsertBook(125, "Computer Organization and Design", "David A. Patterson", "Yes")
    lib.InsertBook(180, "Introduction to Software Engineering", "Ian Sommerville", "Yes")
    lib.BorrowBook(111, 73, 3)
    lib.BorrowBook(52, 73, 1)
    lib.InsertBook(115, "Operating Systems: Internals and Design Principles", "William Stallings", "Yes")
    lib.BorrowBook(153, 25, 2)
    lib.PrintBooks(10, 150)
    lib.InsertBook(210, "Machine Learning: A Probabilistic Perspective", "Kevin P. Murphy", "Yes")
    lib.BorrowBook(171, 25, 3)
    lib.BorrowBook(2, 132, 2)
    #lib.FindClosestBook(50)
    lib.BorrowBook(18, 101, 2)
    lib.InsertBook(80, "Software Engineering: A Practitioner's Approach", "Roger S. Pressman", "Yes")
    lib.BorrowBook(210, 210, 1)
    lib.BorrowBook(43, 73, 1)
    lib.InsertBook(60, "Introduction to Computer Graphics", "David F. Rogers", "Yes")
    lib.PrintBook(210)
    lib.InsertBook(4, "Design Patterns: Elements of Reusable Object-Oriented Software", "Erich Gamma", "Yes")
    lib.InsertBook(2, "Introduction to the Theory of Computation", "Michael Sipser", "Yes")
    lib.BorrowBook(34, 210, 2)
    lib.InsertBook(65, "Computer Networks: Principles, Protocols, and Practice", "Olivier Bonaventure", "Yes")
    lib.ColorFlipCount()
    lib.DeleteBook(125)
    lib.DeleteBook(115)
    lib.DeleteBook(210)
    lib.ColorFlipCount()
    lib.DeleteBook(25)
    lib.DeleteBook(80)
    lib.ColorFlipCount()
    #lib.Quit()

    #Testcase 2
    '''lib.InsertBook(5, "The Secret Garden", "Jane Smith", "Yes");
    lib.BorrowBook(101, 5, 2)
    lib.InsertBook(3, "The Great Gatsby", "Mark Johnson", "Yes");
    lib.InsertBook(12, "To Kill a Mockingbird", "Sarah Lee", "Yes");
    lib.BorrowBook(101, 3, 2)
    lib.DeleteBook(12)
    #lib.PrintBooks(1,10)
    lib.DeleteBook(3)
    lib.DeleteBook(5)
    lib.PrintBook(5)
    lib.InsertBook(50, "The Catcher in the Rye", "Michael Brown", "Yes")
    lib.InsertBook(22, "The Alchemist", "Paul Coelho", "Yes")
    lib.BorrowBook(104, 22, 3)
    lib.BorrowBook(171, 22, 1)
    lib.BorrowBook(103, 22, 2)
    lib.InsertBook(10, "The Hobbit", "J.R.R. Tolkien", "Yes")
    lib.InsertBook(72, "Brave New World", "Aldous Huxley", "Yes")
    lib.InsertBook(94, "1984", "George Orwell", "Yes")
    lib.ColorFlipCount()
    lib.BorrowBook(171, 94, 1)
    lib.ReturnBook(104, 22)
    lib.BorrowBook(132, 50, 3)
    lib.BorrowBook(103, 10, 2)
    lib.InsertBook(28, "Lord of the Flies", "William Golding", "Yes")
    lib.BorrowBook(109, 72, 4)
    lib.BorrowBook(101, 50, 2)
    lib.DeleteBook(94)
    lib.BorrowBook(105, 22, 1)
    #lib.PrintBooks(5, 100)
    #lib.FindClosestBook(26)
    lib.ReturnBook(171, 22)
    lib.BorrowBook(171, 28, 1)
    lib.DeleteBook(50)
    lib.ColorFlipCount()
    lib.BorrowBook(107, 22, 2)
    lib.ReturnBook(103, 10)
    lib.BorrowBook(121, 10, 3)
    lib.DeleteBook(10)
    lib.DeleteBook(22)
    lib.ColorFlipCount()
    lib.Quit()
    lib.InsertBook(10, "The Hobbit", "J.R.R. Tolkien", "Yes")'''

    #Testcase 3
    '''lib.InsertBook(1, "Book1", "Author1", "Yes")
    lib.InsertBook(2, "Book2", "Author2", "Yes")
    lib.InsertBook(3, "Book3", "Author3", "Yes")
    lib.InsertBook(4, "Book4", "Author4", "Yes")
    lib.InsertBook(5, "Book5", "Author5", "Yes")
    lib.BorrowBook(102, 2, 2)
    lib.BorrowBook(103, 3, 3)
    lib.InsertBook(6, "Book6", "Author6", "Yes")
    lib.InsertBook(7, "Book7", "Author7", "Yes")
    lib.InsertBook(8, "Book8", "Author8", "Yes")
    lib.BorrowBook(104, 4, 4)
    lib.BorrowBook(105, 5, 5)
    lib.ReturnBook(102, 2)
    lib.ReturnBook(103, 3)
    lib.ReturnBook(104, 4)
    lib.ReturnBook(105, 5)
    lib.BorrowBook(101, 6, 1)
    lib.BorrowBook(102, 7, 2)
    lib.BorrowBook(103, 8, 3)
    lib.InsertBook(9, "Book9", "Author9", "Yes")
    lib.InsertBook(10, "Book10", "Author10", "Yes")'''


    #Testcase 4 
    '''lib.InsertBook(1, "Book1", "Author1", "Yes")
    lib.InsertBook(2, "Book2", "Author2", "Yes")
    lib.InsertBook(3, "Book3", "Author3", "Yes")
    lib.InsertBook(4, "Book4", "Author4", "Yes")
    lib.InsertBook(5, "Book5", "Author5", "Yes")
    lib.InsertBook(6, "Book6", "Author6", "Yes")
    lib.InsertBook(7, "Book7", "Author7", "Yes")
    lib.InsertBook(8, "Book8", "Author8", "Yes")
    lib.InsertBook(9, "Book9", "Author9", "Yes")
    lib.InsertBook(10, "Book10", "Author10", "Yes")
    lib.BorrowBook(101, 1, 1)
    lib.BorrowBook(102, 2, 2)
    lib.BorrowBook(103, 3, 3)
    lib.BorrowBook(104, 4, 4)
    lib.BorrowBook(105, 5, 5)
    lib.ReturnBook(101, 1)
    lib.BorrowBook(106, 1, 1)
    lib.BorrowBook(107, 2, 1)
    lib.BorrowBook(108, 3, 1)
    lib.BorrowBook(109, 4, 1)
    lib.BorrowBook(110, 5, 1)
    lib.ReturnBook(102, 2)
    lib.BorrowBook(107, 2, 1)
    lib.DeleteBook(1)
    #lib.FindClosestBook(10)
    lib.InsertBook(11, "Book11", "Author11", "Yes")
    lib.ReturnBook(103, 3)
    lib.BorrowBook(112, 11, 1)
    lib.DeleteBook(11)'''



