from Service.bookservice import BookService
from flask import Blueprint, jsonify
from Domain.book import Book

bp_books = Blueprint('books', __name__)

@bp_books.route('/getbooks', methods=['GET'])
def GetBooks():
    result = BookService.GetBooks()
    return jsonify(result), 200