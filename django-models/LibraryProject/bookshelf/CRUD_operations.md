# CRUD Operations Documentation

This document contains all CRUD (Create, Read, Update, Delete) operations performed on the `Book` model in the Django shell.

---

## CREATE Operation

### Command
```python
from bookshelf.models import Book

# Create a new Book instance
book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)
print(f"Created: {book.title} by {book.author} ({book.publication_year})")
```

### Output
```
Created: 1984 by George Orwell (1949)
```

### Description
Creates a new `Book` instance with the title "1984", author "George Orwell", and publication year 1949. The `create()` method instantiates and saves the object to the database in one step.

---

## RETRIEVE Operation

### Command
```python
from bookshelf.models import Book

# Retrieve the book
book = Book.objects.get(title="1984")
print(f"Title: {book.title}")
print(f"Author: {book.author}")
print(f"Publication Year: {book.publication_year}")
```

### Output
```
Title: 1984
Author: George Orwell
Publication Year: 1949
```

### Description
Retrieves the book with title "1984" from the database and displays all its attributes. The `get()` method returns a single object matching the lookup parameters.

---

## UPDATE Operation

### Command
```python
from bookshelf.models import Book

# Retrieve the book and update its title
book = Book.objects.get(title="1984")
book.title = "Nineteen Eighty-Four"
book.save()
print(f"Updated title: {book.title}")
```

### Output
```
Updated title: Nineteen Eighty-Four
```

### Description
Updates the title of the book from "1984" to "Nineteen Eighty-Four". The process involves:
1. Retrieving the book object
2. Modifying the title attribute
3. Calling `save()` to persist changes to the database

---

## DELETE Operation

### Command
```python
from bookshelf.models import Book

# Delete the book
book = Book.objects.get(title="Nineteen Eighty-Four")
book.delete()
print("Book deleted successfully")

# Confirm deletion by retrieving all books
all_books = Book.objects.all()
print(f"Total books in database: {all_books.count()}")
```

### Output
```
(1, {'bookshelf.Book': 1})
Book deleted successfully
Total books in database: 0
```

### Description
Deletes the book from the database and confirms the deletion:
1. Retrieves the book with the updated title
2. Calls `delete()` to remove it from the database
3. Confirms deletion by counting all remaining books (result: 0)

The tuple `(1, {'bookshelf.Book': 1})` indicates that 1 object of type `Book` was deleted.

---

## Summary

All CRUD operations were successfully performed on the `Book` model:
- ✅ **Create**: Added a new book to the database
- ✅ **Retrieve**: Retrieved and displayed book details
- ✅ **Update**: Modified the book's title
- ✅ **Delete**: Removed the book from the database

These operations demonstrate the basic functionality of Django's ORM (Object-Relational Mapping) system for database interactions.
