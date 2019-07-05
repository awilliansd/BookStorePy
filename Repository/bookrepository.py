from Domain.book import Book
import json

def GetBooks():
    data_file = open('book.json')
    return json.loads(data_file.read())