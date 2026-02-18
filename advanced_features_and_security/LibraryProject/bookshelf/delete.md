# DELETE Operation

## Command
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

## Expected Output
```
(1, {'bookshelf.Book': 1})
Book deleted successfully
Total books in database: 0
```

## Explanation

This command performs a delete operation and confirms the deletion:

1. **Retrieve**: Get the book with title "Nineteen Eighty-Four"
2. **Delete**: Call the `delete()` method to remove the object from the database
   - The output `(1, {'bookshelf.Book': 1})` indicates that 1 object was deleted
3. **Confirm**: Retrieve all books to verify the deletion
   - The count of 0 confirms that no books remain in the database

The `delete()` method permanently removes the object from the database.
