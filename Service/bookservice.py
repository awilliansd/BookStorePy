from Repository.bookrepository import BookRepository

class BookService:
    def GetBooks():
        return BookRepository.GetBooks()