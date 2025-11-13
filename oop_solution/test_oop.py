from library_oop import *
# Test Code for OOP Library System

def test_library_system_oop():
    """Comprehensive test of OOP Library System"""

    print("=" * 60)
    print("LIBRARY MANAGEMENT SYSTEM - COMPREHENSIVE TEST")
    print("=" * 60)

    # Initialize library
    lib = Libaray()

    # Test 1: Add Books
    print("\n--- TEST 1: Adding Books ---")
    lib.add_book("B001", "Python Crash Course", "Eric Matthes", 3)
    lib.add_book("B002", "Clean Code", "Robert Martin", 2)
    lib.add_book("B003", "The Pragmatic Programmer", "Hunt & Thomas", 1)
    lib.add_book("B004", "Design Patterns", "Gang of Four", 2)

    # Test 2: Add Members
    print("\n--- TEST 2: Registering Members ---")
    lib.add_member("101", "Alice Smith", "alice@email.com")
    lib.add_member("102", "Bob Jones", "bob@email.com")
    lib.add_member("103", "Carol White", "carol@email.com")

    # Test 3: Display Available Books
    print("\n--- TEST 3: Display Available Books ---")
    lib.display_available_books()

    # Test 4: Successful Book Borrowing
    print("\n--- TEST 4: Successful Borrowing ---")
    lib.borrow_book("101", "B001")  # Alice borrows Python Crash Course
    lib.borrow_book("101", "B002")  # Alice borrows Clean Code
    lib.borrow_book("102", "B001")  # Bob borrows Python Crash Course

    # Test 5: Display Member's Borrowed Books
    print("\n--- TEST 5: Display Member's Books ---")
    lib.display_member_books("101")  # Alice
    lib.display_member_books("102")  # Bob
    lib.display_member_books("103")  # Carol (none)

    # Test 6: Display Available Books After Borrowing
    print("\n--- TEST 6: Available Books After Borrowing ---")
    lib.display_available_books()

    # Test 7: Borrow Last Available Copy
    print("\n--- TEST 7: Borrowing Last Copy ---")
    lib.borrow_book("103", "B003")  # Carol borrows the only copy
    lib.display_available_books()

    # Test 8: Try to Borrow Unavailable Book
    print("\n--- TEST 8: Attempting to Borrow Unavailable Book ---")
    lib.borrow_book("102", "B003")  # Bob tries unavailable book

    # Test 9: Borrowing Limit Test (3 books max)
    print("\n--- TEST 9: Testing Borrowing Limit (3 books max) ---")
    lib.borrow_book("101", "B004")  # Alice borrows 3rd book
    lib.display_member_books("101")
    lib.borrow_book("101", "B003")  # Alice tries 4th book (should fail)

    # Test 10: Return Books
    print("\n--- TEST 10: Returning Books ---")
    lib.return_book("101", "B001")  # Alice returns Python Crash Course
    lib.return_book("102", "B001")  # Bob returns Python Crash Course
    lib.display_member_books("101")
    lib.display_available_books()

    # Test 11: Try to Return Book Not Borrowed
    print("\n--- TEST 11: Attempting Invalid Return ---")
    lib.return_book("102", "B002")  # Bob didn't borrow this

    # Test 12: Return and Borrow Again
    print("\n--- TEST 12: Return and Re-borrow ---")
    lib.return_book("103", "B003")  # Carol returns Pragmatic Programmer
    lib.borrow_book("102", "B003")  # Bob borrows it
    lib.display_member_books("102")

    # Test 13: Error Cases - Non-existent Member/Book
    print("\n--- TEST 13: Error Handling ---")
    lib.borrow_book("M999", "B001")  # Non-existent member
    lib.borrow_book("101", "B999")  # Non-existent book
    lib.return_book("M999", "B001")  # Non-existent member
    lib.display_member_books("M999") # Non-existent member

    # Test 14: Final Status
    print("\n--- TEST 14: Final Library Status ---")
    print("\nAll Borrowed Books:")
    for transaction in lib.member_list:
        if transaction.get_book_title() != "":
            for book_title in transaction.get_book_title():
                print(f"  {transaction.name} has '{(book_title)}'")
        
    print("\nAll Members and Their Books:")
    for member_obj in lib.member_list:
        print(f"\n{member_obj.name} ({member_obj.id}):")
        if member_obj.borrowed:
            for book in member_obj.borrowed:
                print(f"  - {book.title}")
        else:
            print("  (No books borrowed)")

    lib.display_available_books()

    print("\n" + "=" * 60)
    print("TEST COMPLETE")
    print("=" * 60)


# Run the comprehensive test
if __name__ == "__main__":
    test_library_system_oop()
