from flask import Blueprint, jsonify
from Domain.book import Book
from Service.bookservice import GetBooks

bp_books = Blueprint('books', __name__)

@bp_books.route('/GetBooks', methods=['GET'])
def GetBooks():
    result = GetBooks()
    return jsonify(result), 200