import os
import json

class BookRepository:
    def GetBooks():
        path = os.path.join(os.path.dirname(os.path.realpath('__file__')), 'books.json')
        data_file = open(path)
        return json.loads(data_file.read())