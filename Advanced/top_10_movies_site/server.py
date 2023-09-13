from flask import Flask, render_template, redirect, request, url_for
from flask_sqlalchemy import SQLAlchemy
from flask.views import View
from flask_wtf.csrf import CSRFProtect
from flask_bootstrap import Bootstrap
from dotenv import load_dotenv
from pathlib import Path
import os

BASE_DIR = Path(__file__).resolve().parent.parent.parent.parent
load_dotenv(os.path.join(BASE_DIR, ".env"))

app = Flask(__name__)
bootstrap = Bootstrap(app)
csrf = CSRFProtect(app)
app.secret_key = os.getenv('FLASK_SECRET_KEY')

db = SQLAlchemy()
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///movies.db'
db.init_app(app)

# -------------------- MODELS ------------------------ #


# --------------------- VIEWS ------------------------ #
class HomeView(View):
    '''View for home page'''
    
    def dispatch_request(self):
        return render_template('index.html')
    

app.add_url_rule('/', view_func=HomeView.as_view(name='home'))

if __name__ == '__main__':
    app.run(debug=True)