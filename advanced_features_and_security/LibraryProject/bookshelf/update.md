# UPDATE Operation

## Command
```python
from bookshelf.models import Book

# Retrieve the book and update its title
book = Book.objects.get(title="1984")
book.title = "Nineteen Eighty-Four"
book.save()
print(f"Updated title: {book.title}")
```

## Expected Output
```
Updated title: Nineteen Eighty-Four
```

## Explanation

This command performs an update operation in three steps:

1. **Retrieve**: Get the book with title "1984" from the database
2. **Modify**: Change the title attribute to "Nineteen Eighty-Four"
3. **Save**: Call the `save()` method to persist the changes to the database

The output confirms that the title has been successfully updated.
