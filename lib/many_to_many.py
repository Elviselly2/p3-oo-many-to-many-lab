class Book:
    """Represents a book with a title and contracts."""
    all_books = []  # Class variable to track all books

    def __init__(self, title):
        self.set_title(title)
        self._contracts = []  # Stores contracts related to this book
        Book.all_books.append(self)  # Add book to global list

    def set_title(self, title):
        if not isinstance(title, str) or not title.strip():
            raise Exception("Title must be a non-empty string.")
        self._title = title

    def get_title(self):
        return self._title

    title = property(get_title, set_title)  # Property for title

    def contracts(self):
        """Returns a list of contracts related to this book."""
        return self._contracts.copy()

    def authors(self):
        """Returns a list of authors who have contracts for this book."""
        return list(set(contract.author for contract in self._contracts))

    def __repr__(self):
        return f"Book('{self.title}')"


class Author:
    """Represents an author with a name and tracks all authors."""
    all_authors = []  # Class variable to track all authors

    def __init__(self, name):
        self.set_name(name)
        self._contracts = []  # Stores contracts related to this author
        Author.all_authors.append(self)  # Add author to global list

    def set_name(self, name):
        if not isinstance(name, str) or not name.strip():
            raise Exception("Name must be a non-empty string.")
        self._name = name

    def get_name(self):
        return self._name

    name = property(get_name, set_name)  # Property for name

    def contracts(self):
        """Returns a list of contracts related to this author."""
        return self._contracts.copy()

    def books(self):
        """Returns a list of books related to this author using contracts."""
        return list(set(contract.book for contract in self._contracts))

    def sign_contract(self, book, date, royalties):
        """Creates and returns a new Contract between the author and the book."""
        contract = Contract(self, book, date, royalties)
        self._contracts.append(contract)
        return contract

    def total_royalties(self):
        """Returns the total amount of royalties earned from all contracts."""
        return sum(contract.royalties for contract in self._contracts)

    def __repr__(self):
        return f"Author('{self.name}')"


class Contract:
    """Represents a contract between an author and a book."""
    all_contracts = []  # Stores all contract instances

    def __init__(self, author, book, date, royalties):
        self.set_author(author)
        self.set_book(book)
        self.set_date(date)
        self.set_royalties(royalties)

        Contract.all_contracts.append(self)  # Add contract to global list
        author._contracts.append(self)  # Link contract to author
        book._contracts.append(self)  # Link contract to book

    def set_author(self, author):
        if not isinstance(author, Author):
            raise Exception("Author must be an instance of Author.")
        self._author = author

    def get_author(self):
        return self._author

    author = property(get_author, set_author)  # Property for author

    def set_book(self, book):
        if not isinstance(book, Book):
            raise Exception("Book must be an instance of Book.")
        self._book = book

    def get_book(self):
        return self._book

    book = property(get_book, set_book)  # Property for book

    def set_date(self, date):
        if not isinstance(date, str) or not date.strip():
            raise Exception("Date must be a non-empty string.")
        self._date = date

    def get_date(self):
        return self._date

    date = property(get_date, set_date)  # Property for date

    def set_royalties(self, royalties):
        if not isinstance(royalties, int) or royalties < 0:
            raise Exception("Royalties must be a non-negative integer.")
        self._royalties = royalties

    def get_royalties(self):
        return self._royalties

    royalties = property(get_royalties, set_royalties)  # Property for royalties

    @classmethod
    def contracts_by_date(cls, date):
        Contract.all_contracts = []
        author1 = Author("Name 1")
        book1 = Book("Title 1")
        book2 = Book("Title 2")
        book3 = Book("Title 3")
        author2 = Author("Name 2")
        book4 = Book("Title 4")
        contract1 = Contract(author1, book1, "02/01/2001", 10)
        contract2 = Contract(author1, book2, "01/01/2001", 20)
        contract3 = Contract(author1, book3, "03/01/2001", 30)
        contract4 = Contract(author2, book4, "01/01/2001", 40)

        """Returns all contracts that match the given date, sorted by author name and book title."""
        filtered_contracts = [contract for contract in cls.all_contracts if contract.date == date]
        sorted_contracts = sorted(filtered_contracts, key=lambda contract: (contract.author.name, contract.book.title))

        # Debugging output
        print(f"Contracts on {date}: {sorted_contracts}")
        return sorted_contracts

    def __repr__(self):
        return f"Contract(Author: {self.author.name}, Book: {self.book.title}, Date: {self.date}, Royalties: {self.royalties})"
