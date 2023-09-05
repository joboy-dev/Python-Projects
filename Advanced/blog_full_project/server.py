from flask import Flask, render_template, request, redirect, url_for, flash
from flask_wtf.csrf import CSRFProtect
from dotenv import load_dotenv
from pathlib import Path
import os

from email_password_regex_check import is_valid_email, is_valid_password
from WTF_Forms.user_forms import SignUpForm, EditProfileForm, LoginForm

BASE_DIR = Path(__file__).resolve().parent.parent.parent.parent
print(BASE_DIR)

load_dotenv(os.path.join(BASE_DIR, ".env"))

app = Flask(__name__)
# setting up csrf
csrf = CSRFProtect(app)
app.secret_key = os.getenv('FLASK_SECRET_KEY')

@app.route('/')
def home():
    '''Hone page'''
    
    # Get request to get all blogs
    blogs = []
    
    return render_template('index.html', blogs=blogs)


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    '''Function to handle sign up of users'''
    
    message = None
    form = SignUpForm(request.form)
    
    if request.method == 'POST' and form.validate():
        print(form.data)
        password = form.password.data
        password2 = form.password2.data
        
        print(password)
        
        if password != password2:
            message = 'Your passwords do not match.'
        elif not is_valid_password(password) or not is_valid_password(password2):
            message = 'One of your passwords is invalid.'
        else:
            if password == password2:
                # Adding to database
                flash(message='You have successfully signed up')
                return redirect(url_for('login'))
        
    return render_template('forms/signup.html', form=form, message=message)


@app.route('/login', methods=['GET', 'POST'])
def login():
    '''Function to handle login of users'''
    
    message = None
    authenticated = False
    
    form = LoginForm(request.form)
    
    if request.method == 'POST' and form.validate():
        # Perform authentication
        return redirect(url_for('home'))
        
    return render_template('forms/login.html', message=message, authenticated=authenticated, form=form)


@app.route('/logout')
def logout():
    '''Functiion to handle logout of users'''
    
    return redirect(url_for('home'))


@app.route('/myblogs')
def get_user_blogs():
    '''Function to get blog posts of current logged in user'''
    
    # Check database for blogs for the current logged in user
    user_blogs = []
    
    return render_template('my-blogs.html', user_blogs=user_blogs)


@app.route('/blog/<int:id>')
def get_blog(id):
    # Filter database for blogs based on id
    
    return render_template('blog-content.html')

@app.route('/profile')
def get_user_details():
    '''Function to get details of current logged in user'''
    
    return render_template('profile.html')

@app.route('/profile/edit', methods=['GET', 'POST'])
def edit_profile():
    '''Function to edit profile'''
    
    form = EditProfileForm(request.form)
    
    if request.method == 'POST' and form.validate():
        # Check if username/email entered already belongs to another user
        
        flash(message='Changes Saved')
        return redirect(url_for('get_user_details'))
    
    return render_template('forms/edit-profile.html', form=form)

# def upload_file():
#     if request.method == 'POST':
#         f = request.files['the_file']
#         f.save('/var/www/uploads/' + secure_filename(f.filename))

if __name__ == '__main__':
    app.run(debug=True)
