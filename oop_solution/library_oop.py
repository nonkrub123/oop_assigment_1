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
