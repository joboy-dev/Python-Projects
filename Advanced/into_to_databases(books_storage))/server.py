from flask import Flask, render_template, redirect, request, typing as ft, url_for
from flask_sqlalchemy import SQLAlchemy
from flask.views import View
from flask_wtf.csrf import CSRFProtect
from dotenv import load_dotenv
from pathlib import Path
import os
import sqlite3

from forms import AddBookForm, EditRatingForm

BASE_DIR = Path(__file__).resolve().parent.parent.parent.parent
load_dotenv(os.path.join(BASE_DIR, ".env"))

app = Flask(__name__)
csrf = CSRFProtect(app)
app.secret_key = os.getenv('FLASK_SECRET_KEY')

# ------------------------ DATAASE ------------------------- #

# USING SQLITE3
# # connect to database
# books_db = sqlite3.connect('Advanced/into_to_databases(books_storage))/books.db')

# # create cursor to use in modifying database
# cursor = books_db.cursor()

# # run query
# cursor.execute("CREATE TABLE IF NOT EXISTS books (id INTEGER PRIMARY KEY AUTOINCREMENT, title varchar(250) NOT NULL UNIQUE, author varchar(250) NOT NULL, rating FLOAT NOT NULL)")

# cursor.execute("INSERT INTO books VALUES(1, 'Harry Potter', 'J. K. Rowling', '9.3')")
# books_db.commit()


# USING SQLALCHEMY
db = SQLAlchemy()
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///books.db'
db.init_app(app)


# define table
class Books(db.Model):
    '''Model for book data'''
    
    id = db.Column(db.Integer, primary_key=True)
    book_title = db.Column(db.String(80), unique=True, nullable=False)
    author = db.Column(db.String(120), nullable=False)
    rating = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return f'{self.book_title} || {self.author} || {self.rating}'
    
# create the tables
with app.app_context():
    db.create_all()


# ------------------------ VIEWS ------------------------- #

class HomeView(View):
    
    def dispatch_request(self):
        
        # query for all books
        books_list = db.session.query(Books).all()
        
        return render_template('index.html', books=books_list)

app.add_url_rule('/', view_func=HomeView.as_view(name='home'))


class AddBookView(View):
    
    methods = ['GET', 'POST']
    
    def dispatch_request(self):
        form = AddBookForm(request.form)
        
        # add to database
        book = Books(
            book_title=form.book_title.data,
            author=form.author.data,
            rating=form.rating.data,
        )
        
        # UPDATE
        # book = db.session.query(Books).filter_by(book_title='Harry Potter').first()
        # if book:
        #     book.book_title = 'New Harry Potter'
        #     db.session.commit()
        
        
        if request.method == 'POST' and form.validate():
            db.session.add(book)
            db.session.commit()
            return redirect(url_for('home'))
        
        return render_template('add_book.html', form=form)
    
app.add_url_rule('/addBook', view_func=AddBookView.as_view(name='addBook'))


class EditRatingView(View):
    
    methods = ['GET', 'POST']
    
    def dispatch_request(self, id):
        form = EditRatingForm(request.form)
        
        # book = db.session.query(Books).get(id)
        
        book = db.get_or_404(Books, id)
        
        if request.method == 'POST' and form.validate():
            book.rating = form.rating.data
            db.session.commit()
            
            return redirect(url_for('home'))
            
        return render_template('edit_rating.html', form=form, book=book)
    
app.add_url_rule('/edit/<int:id>', view_func=EditRatingView.as_view(name='editRating'))


class DeleteBookView(View):
    
    def dispatch_request(self, id):
        book = db.get_or_404(Books, id)
        
        db.session.delete(book)
        db.session.commit()
        
        return redirect(url_for('home'))

app.add_url_rule('/delete/<int:id>', view_func=DeleteBookView.as_view(name='delete'))


if __name__ == '__main__':
    app.run(debug=True)
    