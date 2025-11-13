# Library OOP

A simple Python program that manage library transaction using object-oriented programming

## Overview

This project is about managing library transaction like borrow or return using class

## Project Structure
```
oop_assigment1/
│
├── README.md                          # This file
│
├── procedural_version/
│   ├── library_procedural.py         # Original procedural code
│   └── test_procedural.py            # Comprehensive test suite
│
├── oop_solution/
│   ├── library_oop.py                # Student's OOP implementation (to create)
│   └── test_oop.py                   # Tests for OOP version (to create)
```

## Class Details

### `class Book`

Manages book state and available copies.

#### `__init__(self, id, title, author, total_copies)`
**Description:**  
Initialize book object.

**Attributes:**
- `id`: Book ID  
- `title`: Title of the book  
- `author`: Author name of the book  
- `total_copies`: Total copies available  

**Returns:**  
None

#### `is_me(self, check_id)`
Check if this book’s ID is the same as target book ID.  
**Returns:** `True` if same, otherwise `False`.

#### `is_available(self)`
Check if there are copies left.  
**Returns:** `True` if available copies > 0, otherwise `False`.

#### `get_borrow(self)`
Decrease available copies by 1.

#### `return_borrow(self)`
Increase book available copies by 1  
**Returns:** `True` if copies not exceeding total copies, otherwise `False`.

#### `__str__(self)`
Return formatted string `"- <title> by <author>"`.

#### `get_summary(self)`
Return formatted string with available copies.

#### `get_title(self)`
Return the book’s title.

---

### `class Member`

Handles library member data, borrowing and return actions.

#### `__init__(self, id, name, email)`
Initialize member information.

**Attributes:**
- `id`: Member ID  
- `name`: Member name  
- `email`: Contact email  
- `borrowed`: List of borrowed book objects  

#### `borrowing(self, book_obj)`
Add a book object to the member’s borrowed list.

#### `is_me(self, check_id)`
Check if target ID matches this member’s ID.  
**Returns:** `True` or `False`.

#### `is_borrow(self, borrow_id)`
Check if member borrow specific book by ID.  
**Returns:** The `Book` object if found, otherwise `False`.

#### `is_at_limit(self)`
Check if the member has reached the borrowing limit (3 books).  
**Returns:** `True` or `False`.

#### `return_book(self, book_id)`
Remove a borrowed book from the list by ID.

#### `get_book_title(self)`
Return a list of all book titles currently borrowed.

---

### `class Library`

Coordinates all book and member actions.

#### `__init__(self)`
Initialize empty book and member collections.

#### `add_book(self, id, title, author, copies)`
Register a new book in the library.

#### `add_member(self, id, name, email)`
Register a new member.

#### `borrow_book(self, member_id, book_id)`
Process a book borrowing transaction.

- Checks member and book existence  
- Ensures copies are available  
- Enforces borrowing limit  

#### `return_book(self, member_id, book_id)`
Handle a returning book transaction.  
Checks if the member actually borrowed the book.

#### `display_available_books(self)`
Display all books that have available copies.

#### `display_member_books(self, member_id)`
Display books borrowed by a specific member.

---

## Testing

### **Test Coverage (`test_oop.py` includes):**

**Basic Operations**
- Adding books and members  
- Borrowing and returning books  
- Displaying available books and member information  

**Edge Cases**
- Borrowing unavailable books  
- Exceeding borrowing limit (3 books)  
- Returning books not borrowed  
- Non-existent books or members  

---

## How to Run the Tests

1. Ensure all `.py` files (`book.py`, `member.py`, `library.py`, and `test_oop.py`) are in the same directory.  
2. Open a terminal and run:
   ```bash
   python test_oop.py