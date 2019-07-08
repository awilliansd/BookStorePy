from Service.bookservice import BookService
from flask import Blueprint, jsonify
from Domain.book import Book
from flask_swagger import swagger

bp_books = Blueprint('books', __name__)

@bp_books.route('/getbooks', methods=['GET'])
def GetBooks():
    result = BookService.GetBooks()
    return jsonify(swagger(result)), 200