from flask import Flask, request
app = Flask(__name__)
from flask_sqlalchemy import SQLAlchemy

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
db = SQLAlchemy(app)

class book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    book_name = db.Column(db.String(80), unique=True)
    author = db.Column(db.String(80))
    publisher = db.Column(db.String(80))

    def __repr__(self):
        return f"{self.book_name} - {self.author} - {self.publisher}"

@app.route('/')
def index():
    return 'Hello!'

@app.route('/books', methods=['GET'])
def get_books():
    books = book.query.all()

    output = []
    for nbook in books:
        book_data = {'book_name': nbook.book_name, 'author': nbook.author, 'publisher': nbook.publisher}

        output.append(book_data)

    return {"book": output}

@app.route('/books/<id>', methods=['GET'])
def get_book(id):
    individualbook = book.query.get_or_404(id)
    return {'book_name': individualbook.book_name, 'author': individualbook.author, 'publisher': individualbook.publisher}

@app.route('/books/', methods=['POST'])
def add_book():
    newbook = book(book_name=request.json["book_name"], author=request.json["author"], publisher=request.json["publisher"])
    db.session.add(newbook)
    db.session.commit()
    return {'id': newbook.id}

@app.route('/books/<id>', methods=['DELETE'])
def delete_book(id):
    remove_book = book.query.get(id)
    if remove_book is None:
        return {"error": "not found"}
    db.session.delete(remove_book)
    db.session.commit()
    return {"yes"}

with app.app_context():
    db.create_all()