class LibraryBook:
    def init(self, title, author, publication_year):
        self.title = title
        self.author = author
        self.publication_year = publication_year
        self.is_checked_out = False

    def check_out(self):
        if not self.is_checked_out:
            self.is_checked_out = True
            return True
        return False

    def return_book(self):
        if self.is_checked_out:
            self.is_checked_out = False
            return True
        return False

class EnhancedLibraryBook:
    def init(self, library_book):
        self.library_book = library_book

    def check_out(self):
        return self.library_book.check_out()

    def return_book(self):
        return self.library_book.return_book()

    def is_available(self):
        return not self.library_book.is_checked_out

    def get_book_info(self):
        return {
            "title": self.library_book.title,
            "author": self.library_book.author,
            "publication_year": self.library_book.publication_year,
            "is_checked_out": self.library_book.is_checked_out
        }

    def check_condition(self):
        # Для прикладу, повернемо "Good" як умовний стан книги.
        return "Good"

book = LibraryBook("The Great Gatsby", "F. Scott Fitzgerald", 1925)
enhanced_book = EnhancedLibraryBook(book)

print(enhanced_book.check_out())  
print(enhanced_book.check_out())  
print(enhanced_book.is_available()) 
print(enhanced_book.return_book()) 
print(enhanced_book.is_available()) 
print(enhanced_book.get_book_info())
print(enhanced_book.check_condition())
