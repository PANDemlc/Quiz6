from abc import ABC, abstractmethod

class ChangeCatalog(ABC):
    @abstractmethod
    def add_book(self, book_id):
        raise NotImplementedError("Implement function!")
    @abstractmethod
    def remove_book(self, book_id):
        raise NotImplementedError("Implement function!")
    
class Search(ABC):
    @abstractmethod
    def search_title(self, title):
        raise NotImplementedError("Implement function!")
    @abstractmethod
    def search_author(self, author):
        raise NotImplementedError("Implement function!")
    @abstractmethod
    def search_genre(self, genre):
        raise NotImplementedError("Implement function!")
    
class Borrow(ABC):
    @abstractmethod
    def borrow_book(self, book_id, user_id):
        raise NotImplementedError("Implement function!")
    @abstractmethod
    def return_book(self, book_id, user_id):
        raise NotImplementedError("Implement function!")
    
class GenerateReports(ABC):
    @abstractmethod
    def report_borrow_book(self):
        raise NotImplementedError("Implement function!")
    @abstractmethod
    def report_overdue_book(self):
        raise NotImplementedError("Implement function!")
    @abstractmethod
    def report_book_popularity(self):
        raise NotImplementedError("Implement function!")
    
class Guest(Search):
    def search_title(self, title):
        print(f"Searching for {title}")
    
    def search_author(self, author):
        print(f"Searching for books by {author}")
    
    def search_genre(self, genre):
        print(f"Searching for {genre} books")

class LibraryCardHolder(Search, Borrow):
    def search_title(self, title):
        print(f"Searching for {title}")
    
    def search_author(self, author):
        print(f"Searching for books by {author}")
    
    def search_genre(self, genre):
        print(f"Searching for {genre} books")

    def borrow_book(self, book_id, user_id):
        print(f"Checking out {book_id} for {user_id}")
    
    def return_book(self, book_id, user_id):
        print(f"Returning {book_id} for {user_id}")

class Librarian(Search, Borrow, GenerateReports):
    def search_title(self, title):
        print(f"Searching for {title}")
    
    def search_author(self, author):
        print(f"Searching for books by {author}")
    
    def search_genre(self, genre):
        print(f"Searching for {genre} books")

    def borrow_book(self, book_id, user_id):
        print(f"Checking out {book_id} for {user_id}")
    
    def return_book(self, book_id, user_id):
        print(f"Returning {book_id} for {user_id}")

    def report_borrow_book(self):
        print(f"Generating report for borrowed books")
    
    def report_overdue_book(self):
        print(f"Generating report for overdue books")
    
    def report_book_popularity(self):
        print(f"Generating report for book popularity and rankings")


def main():
    Joe = Guest()
    Joe.search_author("Batman")

    Bob = LibraryCardHolder() 
    # book_id  user_id
    Bob.borrow_book(123, 998)

    Batman = Librarian()
    Batman.report_borrow_book()
    Batman.report_overdue_book()

if __name__ == "__main__":
    main()