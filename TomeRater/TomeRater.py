""" TomeRater project for Programming with Python Capstone. --Joni Kontturi"""

from pprint import pprint
class User(object):
    """A User object to be used by TomeRater class.

    Attributes:
        name: String representing user name.
        email: String for email.
        books: Dictionary to hold Book objects.
    """
    def __init__(self, name, email):
        """Return a new User object."""
        self.name = name
        self.email = email
        self.books = {}
        
    def get_email(self):
        """Return user email."""
        return self.email
        
    def change_email(self, address):
        """Change users email."""
        self.email = address
        return "Email changed to : {}".format(address)

    def read_book(self, book, rating=None):
        """Adds book rating for User object."""
        self.books[book] = rating
        return "Book added {} to user : {}".format(book, self.name)

    def get_average_rating(self):
        """Return average rating for Users books."""
        total = 0
        books = 0
        for value in self.books.values():
            if value:
                total += value
                books += 1
        if total == 0:
            return total
        else:           
            return total / books

    def get_total_worth_of_books(self):
        """Method to get worth of users books"""
        total = 0
        for book in self.books:
            if book:
                total += book.get_price()
        if total == 0:
            return total
        else:           
            return total

    def __repr__(self):
        """Return a string represeting User object."""
        return "User {user}, email: {email}, books read : {books}".format(user=self.name, email=self.email, books=len(self.books))
        
    def __eq__(self, other_user):
        """Method to compare equality of User objects."""
        if self.name == other_user.name and self.email == other_user.email:
            return True
        else:
            return False
        
    def __hash__(self):
        """Method to fix unhashable type list while making dictionary."""
        return hash((self.name, self.email))   

class Book(object):
    """A Book object to be used by TomeRater class.

    Attributes:
        title: String representing books title.
        isbn: int for represeting isbn number.
        ratings: List to hold ratings for book objects.
        price: int for representing value of the book.
    """
    def __init__(self, title, isbn, price = 0):
        """Return a new Book object."""
        self.title = title
        self.isbn = isbn
        self.ratings = []
        self.price = price

    def get_title(self):
        """Return a title string."""
        return self.title

    def get_isbn(self):
        """Return a isbn number."""
        return self.isbn

    def get_price(self):
        """Return a price number."""
        return self.price

    def set_price(self, price):
        """Method to set new price for book object."""
        self.price = price
        print("price updated to {}".format(price))
        return None

    def set_isbn(self, isbn):
        """Method to set new isbn for book object."""
        self.isbn = isbn
        print("Isbn updated to {}".format(isbn))
        return None

    def add_rating(self, rating):
        """Method to add rating to book object."""
        if rating:
            if rating > 0 and rating < 5:
                self.ratings.append(rating)
            else:
                print("invalid Rating")

    def get_average_rating(self):
        """Method to get average rating of a book object."""
        total = 0
        for value in self.ratings:
            if value:
                total += value
        if total == 0:
            return total
        else:           
            return total / len(self.ratings)

    def __eq__(self, other_book):
        """Method to compare equality of book objects."""
        if self.title == other_book.title and self.isbn == other_book.isbn and self.price == other_book.price:
            return True
        else:
            return False

    def __hash__(self):
        """Method to fix unhashable type list while making dictionary in User class."""
        return hash((self.title, self.isbn, self.price))

    def __repr__(self):
        """Method to present the contents of book objects."""
        return "{title} isbn : {isbn} price : {price}".format(title=self.title, isbn=self.isbn, price=self.price)
    
        
class Fiction(Book):
    """A Fiction subclass of Book to be used by TomeRater class.

    Attributes:
        title: String representing books title.
        author: String represeting author of the book.
        isbn: int for represeting isbn number.
        price: int for representing value of the book.

        Inherits title and isbn from Book object.
    """
    def __init__(self, title, author, isbn, price):
        """Returns a new Fiction object."""
        super().__init__(title, isbn, price)
        self.author = author

    def get_author(self):
        """Method to get the author of Fiction book."""
        return self.author

    def __repr__(self):
        """Method to present the contents of Fiction objects."""
        return "{title} by {author}".format(title=self.title, author=self.author)

class Non_Fiction(Book):
    """A Non_Fiction subclass of Book to be used by TomeRater class.

    Attributes:
        title: String representing books title.
        subject: String represeting books subject.
        level: String representing level of the book.
        isbn: int for represeting isbn number.
        price: int for representing value of the book.

        Inherits title and isbn from Book object.
    """
    def __init__(self, title, subject, level, isbn, price):
        """Returns a new Non_fiction object."""
        super().__init__(title, isbn, price)
        self.subject = subject
        self.level = level

    def get_subject(self):
        """Method to get the subject of Non_Fiction book."""
        return self.subject

    def get_level(self):
        """Method to get the level of Non_Fiction book."""
        return self.level

    def __repr__(self):
        """Method to present the contents of Non_Fiction objects."""
        return "{title}, a {level} manual on {subject}".format(title=self.title, level=self.level, subject=self.subject)

class TomeRater():
    """A TomeRater App class.

    Attributes:
        users: Dictionary holding User objects.
        books: Dictionary holding Book objects.
    """
    #Used in valid_email and add user.
    allowed_ends = [".com", ".edu", ".org"]
    def __init__(self):
        """Returns a new instance of TomeRater."""
        self.users = {}
        self.books = {}

    def unique_isbn(self,isbn):
        """Method checks if isbn exists in another book"""
        for book in self.books.keys():
            if book.get_isbn() == isbn:
                print("Error ISBN has to be unique.")
                return False
        return True
            
    def create_book(self, title, isbn, price=0):
        """Method to create new instance of Book object"""
        if self.unique_isbn(isbn) == True:
            return Book(title, isbn, price)

    def create_novel(self, title, author, isbn, price=0):
        """Method to create new instance of Fiction object"""
        if self.unique_isbn(isbn) == True:
            return Fiction(title, author, isbn, price)

    def create_non_fiction(self, title, subject, level, isbn, price=0):
        """Method to create new instance of Non_fiction object"""
        if self.unique_isbn(isbn) == True:
            return Non_Fiction(title, subject, level, isbn, price)

    def add_book_to_user(self, book, email, rating=None):
        """Method to add book to a user by email with or without rating"""
        user = self.users.get(email, None)
        if user:
            user.read_book(book, rating)
            if book not in self.books:
                self.books[book] = 0
            self.books[book] += 1
            book.add_rating(rating)
        else:
            print("No user with email ( {} )".format(email))

    def valid_email(self, email):
        """Method to validate email address"""
        if "@" in email and email[-4::] in self.allowed_ends:
                    return True
        return False
        
    def add_user(self, name, email, books=None):
        """Method to add user with or without books"""
        if self.valid_email(email) == True:                
            if email in self.users.keys():
                print("User with that email {} exists".format(email))
            else:           
                self.users[email] = User(name, email)
                if books:
                    for book in books:
                        self.add_book_to_user(book, email)
        else:
            print("Invalid Email {} does not contain @ or valid domain. allowed : {}".format(email, self.allowed_ends))

    def print_catalog(self):
        """Method print Book catalog from TomeRater instance"""
        print("\nBooks in database : \n")
        for book in self.books.keys():
            print(book)

    def print_users(self):
        """Method print user catalog from TomeRater instance"""
        print("\nUsers in database : \n")
        for user in self.users.values():
            print(user, end="\n")

    def most_read_book(self, books=None):
        """Method to get most read book from TomeRater instance"""
        count = 0
        most_read_book = None
        if books == None:
            books = self.books
        for book in books:
            if books[book] > count:
                count = books[book]
                most_read_book = book               
        return most_read_book

    def most_expensive_book(self, books=None):
        """Method to get most expensive book from TomeRater instance"""
        count = 0
        most_expensive_book = None
        if books == None:
            books = self.books
        for book in books:
            if book.get_price() > count:
                count = book.get_price()
                most_expensive_book = book              
        return most_expensive_book

    def highest_rated_book(self):
        """Method to get the highest rated book from TomeRater instance"""
        top = 0
        bestbook = None
        for book in self.books:
            if book.get_average_rating() > top:
                top = book.get_average_rating()
                bestbook = book
        return bestbook

    def get_n_most_read_books(self, n):
        """Method to get n most read book from TomeRater instance
        Return in descending order"""
        output = {}
        items = self.books.copy()
        for i in range(0, n):
            most_read_book = self.most_read_book(items) 
            output[most_read_book] = items[most_read_book]    
            items.pop(most_read_book)
        return sorted(output.items(), key=lambda sortvariable: sortvariable[1], reverse=True)
        
    def get_n_most_prolific_readers(self, n):
        """Method to get n most profilic readers from TomeRater instance
        Return in descending order"""
        output = {}
        items = self.users.copy()
        for i in range(0, n):
            count = 0
            for users in items.values():
                if len(users.books) > count:
                    count = len(users.books)
                    most_read_user = users
            output[most_read_user] = len(most_read_user.books)   
            items.pop(most_read_user.get_email())
        return sorted(output.items(), key=lambda sortvariable: sortvariable[1], reverse=True)
    
    def get_n_most_expensive_books(self, n):
        """Method to get n most expensive book from TomeRater instance
        Return in descending order"""
        output = {}
        items = self.books.copy()
        for i in range(0, n):
            most_expensive_book = self.most_expensive_book(items) 
            output[most_expensive_book] = items[most_expensive_book]
            items.pop(most_expensive_book)
        return sorted(output.items(), key=lambda sortvariable: sortvariable[1], reverse=True)

    def get_worth_of_user(self, user_email):
        """Method to get worth of users books TomeRater instance"""
        return "Worth of user {}  {}".format(self.users[user_email].get_email(), self.users[user_email].get_total_worth_of_books())
        

    def most_positive_user(self):
        """Method to get most positive user from TomeRater instance"""
        total = 0
        positive = None
        for user in self.users.values(): 
            if user.get_average_rating() > total:
                total = user.get_average_rating()
                positive = user
        return positive

    def __repr__(self):
        """Return a string represeting TomeRater object."""
        print("Contents :")
        pprint(vars(self))
        return "TomeRater Object\n\nuse .print.catalog() and .print_users() methods to see the content"

    def __eq__(self, other_tomerater):
        """Method to compare equality of TomeRater objects."""
        if self.users == other_tomerater.users and self.books == other_tomerater.books: 
            return True
        else:
            return False


        






                      
            
            

        
