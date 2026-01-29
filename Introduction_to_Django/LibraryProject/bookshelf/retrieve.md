# RETRIEVE Operation

## Command
```python
from bookshelf.models import Book

# Retrieve the book
book = Book.objects.get(title="1984")
print(f"Title: {book.title}")
print(f"Author: {book.author}")
print(f"Publication Year: {book.publication_year}")
```

## Expected Output
```
Title: 1984
Author: George Orwell
Publication Year: 1949
```

## Explanation

This command retrieves the `Book` instance with the title "1984" from the database using the `get()` method. The `get()` method returns a single object that matches the given lookup parameters.

All attributes of the book are then displayed:
- **title**: The book's title
- **author**: The book's author
- **publication_year**: The year the book was published# RETRIEVE Operation

## Command
```python
from bookshelf.models import Book

# Retrieve the book
book = Book.objects.get(title="1984")
print(f"Title: {book.title}")
print(f"Author: {book.author}")
print(f"Publication Year: {book.publication_year}")
```

## Expected Output
```
Title: 1984
Author: George Orwell
Publication Year: 1949
```

## Explanation

This command retrieves the `Book` instance with the title "1984" from the database using the `get()` method. The `get()` method returns a single object that matches the given lookup parameters.

All attributes of the book are then displayed:
- **title**: The book's title
- **author**: The book's author
- **publication_year**: The year the book was published
