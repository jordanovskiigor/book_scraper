from flask import Flask, render_template
import csv

app = Flask(__name__)

@app.route('/')
def index():
    books = []

    try:
        with open('books.csv', newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                books.append({
                    'title': row['Title'],
                    'price': row['Price'],
                    'rating': row['Rating']
                })
    except UnicodeDecodeError:
        with open('books.csv', newline='', encoding='ISO-8859-1') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                books.append({
                    'title': row['Title'],
                    'price': row['Price'],
                    'rating': row['Rating']
                })

    return render_template('index.html', books=books)

if __name__ == '__main__':
    app.run(debug=True)
