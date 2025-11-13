# Library Management System - OOP Style

books = []
members = []
borrowed_books = []

class Book:
    """"""
    def __init__(self,id, title, author, total_copies):
        self.id = id
        self.title = title
        self.author = author
        self.total_copies = total_copies
        self.available_copies = total_copies

    def is_me(self, check_id):
        if self.id == check_id:
            return True
        else:
            return False
    
    def is_avaiable(self):
        if self.available_copies > 0:
            return True
        else:
            return False
        
    def get_borrow(self):
        self.available_copies -= 1

    def return_borrow(self):
        if self.total_copies > self.available_copies:
            self.available_copies += 1
            return True
        else:
            return False

    def __str__(self):
        return(f"{self.title} by {self.author} - {self.available_copies} copies available")

class Member:

    def __init__(self, id, name, email):
        self.id = id
        self.name = name
        self.email = email
        self.borrowed = []
    
    def borrowing(self, book_obj):
        # book_obj.get_borrow()
        self.borrowed.append(book_obj)
    
    def is_me(self, check_id):
        if self.id == check_id:
            return True
        else:
            return False
    
    def is_borrow(self, borrow_id):
        for book in self.borrowed:
            if book.id == borrow_id:
                return book
            
        return False
        
    def is_at_limit(self):
        if len(self.borrowed) >= 3:
            return True
        else:
            return False
    
    def return_book(self, book_id):
        for book in self.borrowed:
            if book.id == book_id:
                self.borrowed.remove(book)
                break

class Libaray:

    def __init__(self):
        self.book_list = []
        self.member_list = []

    def add_book(self,id, title, author, copies):
        add_obj = Book(id,title,author,copies)
        print(f"Book '{title}' added successfully!")
        self.book_list.append(add_obj)
    
    def add_member(self, id, name, email):
        member_obj = Member(id, name, email)
        self.member_list.append(member_obj)
        print(f"Member '{name}' registered successfully!")

    def __find_member(self, target_id):
        for member_obj in self.member_list:
            if member_obj.is_me(target_id):
                return member_obj
        return False
    
    def __find_book(self, target_id):
        for book_obj in self.book_list:
            if book_obj.is_me(target_id):
                return book_obj
        return False

    def __return_book(self, target_id):
        for book_obj in self.book_list:
            if book_obj.is_me(target_id):
                book_obj.return_borrow()
                return True
        return False
        
    def borrow_book(self, member_id, book_id):
        """Process a book borrowing transaction"""
        borrow_member = False
        borrow_book = False
        
        borrow_member = self.__find_member(member_id)
        borrow_book = self.__find_book(book_id)
        
        if borrow_member == False:
            print("Error: Member not found!")
            return False
        
        if borrow_book == False:
            print("Error: Book not found!")
            return False
        
        if not borrow_book.is_avaiable():
            print("Error: No copies available!")
            return False       
        
        if borrow_member.is_at_limit():
            print("Error: Member has reached borrowing limit!")
            return False      
        
        
        borrow_member.borrowing(borrow_book)
        borrow_book.get_borrow()
        print(f"{borrow_member.name} borrowed '{borrow_book.title}'")

    def return_book(self,member_id, book_id):
        borrow_member = False
        borrow_book = False

        borrow_member = self.__find_member(member_id)

        if borrow_member == False:
            print("Error: Member or book not found!")
            return False
        
        borrow_book = borrow_member.is_borrow(book_id)
        
        if borrow_member == False or borrow_book == False:
            print("Error: Member or book not found!")
            return False
        
        self.__return_book(book_id)
        borrow_member.return_book(book_id)
        print(f"{borrow_member.name} returned '{borrow_book.title}'")

    def display_available_books(self):
        
        """Display all books with available copies"""
        print("\n=== Available Books ===")
        for book in self.book_list:
            if book.is_avaiable():
                print(book)
    
    def display_member_books(self,member_id):
        """Display books borrowed by a specific member"""
        member = self.__find_member(member_id)
        if not member:
            print("Error: Member not found!")
            return
        
        print(f"\n=== Books borrowed by {member.name} ===")
        if member.borrowed == []:
            print("No books currently borrowed")
        else:
            for book_obj in member.borrowed:
                print(book_obj)