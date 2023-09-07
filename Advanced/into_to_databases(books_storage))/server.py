from flask import Flask, render_template, redirect, request, url_for
from flask.views import View
from flask_wtf.csrf import CSRFProtect
from dotenv import load_dotenv
from pathlib import Path
import os

from add_book_form import AddBookForm


BASE_DIR = Path(__file__).resolve().parent.parent.parent.parent
load_dotenv(os.path.join(BASE_DIR, ".env"))

app = Flask(__name__)
csrf = CSRFProtect(app)
app.secret_key = os.getenv('FLASK_SECRET_KEY')

class HomeView(View):
    
    def dispatch_request(self):
        return render_template('index.html')

app.add_url_rule('/', view_func=HomeView.as_view(name='home'))


class AddBookView(View):
    
    methods = ['GET', 'POST']
    
    def dispatch_request(self):
        form = AddBookForm(request.form)
        
        if request.method == 'POST' and form.validate():
            return redirect(url_for('home'))
        
        return render_template('add_book.html', form=form)
    
app.add_url_rule('/addBook', view_func=AddBookView.as_view(name='addBook'))

if __name__ == '__main__':
    app.run(debug=True)