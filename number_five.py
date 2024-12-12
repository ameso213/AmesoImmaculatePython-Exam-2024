# i)

class Book:
    def __init__(self, title, author, pages):
        # Initialize the attributes of the book
        self.title = title
        self.author = author
        self.pages = pages
    
    def display_info(self):
        # Method to display the book's information
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Pages: {self.pages}")

# Creating an instance of the Book class
book1 = Book("Live Well", "Mr.Opio", 100)

# Displaying the information about the book
book1.display_info()


#ii)

# Derived class EBook inheriting from Book
class Book:
    def __init__(self, title, author, pages):
        # Initialize the attributes of the book
        self.title = title
        self.author = author
        self.pages = pages
    
    def display_info(self):
        
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Pages: {self.pages}")


class EBook(Book):
    def __init__(self, title, author, pages, format):
        # Call the parent class constructor
        super().__init__(title, author, pages)
        # Initialize the additional format attribute for EBook
        self.format = format
    
    def display_info(self):
        # Display information including the format for the EBook
        super().display_info()  # Call the display_info of the parent class
        print(f"Format: {self.format}")

# Creating an instance of the EBook class
ebook1 = EBook("Installing Flutter", "Ameso Immaculate", 300, "PDF")

# Displaying the information about the EBook
ebook1.display_info()




#iii)

# Base class Book
class Book:
    def __init__(self, title, author, pages):
        # Initialize the attributes of the book
        self.title = title
        self.author = author
        self.pages = pages
    
    def display_info(self):
        # Method to display the book's full information
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Pages: {self.pages}")
    
    def get_title_and_author(self):
        # Method to return the title and author of the book
        return f"Title: {self.title}, Author: {self.author}"

# Creating an instance of the Book class
book1 = Book("Live Well", "Mr.Opio", 100)

# Displaying only the title and author of the book
print(book1.get_title_and_author())


#iv)
# A class is a blueprint of creating an object
# An object is an instance of a class.