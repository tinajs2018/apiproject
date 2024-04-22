from flask import Flask, jsonify, request

app = Flask(__name__)

books = [
    {"id": 1, "title": "The Great Gatsby", "author": "F. Scott Fitzgerald"},
    {"id": 2, "title": "To Kill a Mockingbird", "author": "Harper Lee"},
]

@app.route('/books', methods=['GET'])
def get_books():
    return jsonify({"books": books})

if __name__ == '__main__':
    app.run(debug=True)
