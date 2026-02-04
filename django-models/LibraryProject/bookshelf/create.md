# CREATE Operation

## Command
```python
from bookshelf.models import Book

# Create a new Book instance
book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)
print(f"Created: {book.title} by {book.author} ({book.publication_year})")
```

## Expected Output
```
Created: 1984 by George Orwell (1949)
```

## Explanation

This command creates a new `Book` instance with:
- **Title**: "1984"
- **Author**: "George Orwell"
- **Publication Year**: 1949

The `create()` method both instantiates the object and saves it to the database in a single operation.# CREATE Operation

## Command
```python
from bookshelf.models import Book

# Create a new Book instance
book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)
print(f"Created: {book.title} by {book.author} ({book.publication_year})")
```

## Expected Output
```
Created: 1984 by George Orwell (1949)
```

## Explanation

This command creates a new `Book` instance with:
- **Title**: "1984"
- **Author**: "George Orwell"
- **Publication Year**: 1949

The `create()` method both instantiates the object and saves it to the database in a single operation.
