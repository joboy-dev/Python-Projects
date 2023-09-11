from flask import Flask, render_template, request, redirect, typing as ft, url_for, flash
from flask_wtf.csrf import CSRFProtect
from flask.views import View
from flask_ckeditor import CKEditor

from dotenv import load_dotenv
from pathlib import Path
import os
from datetime import datetime

from email_password_regex_check import is_valid_email, is_valid_password
from WTF_Forms.user_forms import SignUpForm, EditProfileForm, LoginForm
from WTF_Forms.blog_forms import AddBlogForm, EditBlogFrom, AddCommentForm
from views import ListView, DetailView
import models
from models import BlogPost

BASE_DIR = Path(__file__).resolve().parent.parent.parent.parent
load_dotenv(os.path.join(BASE_DIR, ".env"))

app = Flask(__name__)
app.config['STATIC_FOLDER'] = 'static/'

# setting up csrf
csrf = CSRFProtect(app)
app.secret_key = os.getenv('FLASK_SECRET_KEY')

# setting up ckeditor
app.config['CKEDITOR_PKG_TYPE'] = 'full'
ckeditor = CKEditor(app)

# ----------------------- DATABASE CONFIG ------------------------- #

database = models.db
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog_app.db'
database.init_app(app)

with app.app_context():
    database.create_all()
    
# session = Session(db=database)
session = database.session

# ------------------------------ DATE -------------------------------- #

def get_date():
    date_posted = datetime.now().strftime('%d %B, %Y | %H:%M')
    return date_posted

# ----------------------- USER VIEWS ------------------------- #

@app.route('/')
def home():
    '''Hone page'''
    
    # Get request to get all blogs
    blogs = session.query(BlogPost).all()

    return render_template('index.html', blogs=blogs)

# class HomeView(ListView):
    
class SignUpView(View):
    '''View to handle sign up of users'''
    
    methods = ['GET', 'POST']
    
    def dispatch_request(self):
        message = None
        form = SignUpForm(request.form)
        
        if request.method == 'POST':
            
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
    
app.add_url_rule('/signup', view_func=SignUpView.as_view(name='signup'))


class LoginView(View):
    '''View to handle login of users'''
    
    methods = ['GET', 'POST']
    
    def dispatch_request(self):
        message = None
        authenticated = False
        
        form = LoginForm(request.form)
        
        if request.method == 'POST' and form.validate():
            # Perform authentication
            return redirect(url_for('home'))
            
        return render_template('forms/login.html', message=message, authenticated=authenticated, form=form)
    
app.add_url_rule('/login', view_func=LoginView.as_view(name='login'))


class LogoutView(View):
    '''View to handle logout of users'''
    
    def dispatch_request(self):
        return redirect(url_for('home'))

app.add_url_rule('/logout', view_func=LogoutView.as_view(name='logout'))


class GetUserDetailsView(View):
    '''View to get details of current logged in user'''
    
    def dispatch_request(self):
        return render_template('profile.html')

app.add_url_rule('/profile', view_func=GetUserDetailsView.as_view(name='getUserDetails'))


class EditProfileView(View):
    '''View to edit profile'''
    
    methods = ['GET', 'POST']
    
    def dispatch_request(self):
        form = EditProfileForm(request.form)
        
        if request.method == 'POST' and form.validate():
            # Check if username/email entered already belongs to another user
            
            flash(message='Changes Saved')
            return redirect(url_for('get_user_details'))
        
        return render_template('forms/edit-profile.html', form=form)
    
app.add_url_rule('/profile/edit', view_func=EditProfileView.as_view(name='editProfile'))


# ----------------------- BLOG VIEWS ------------------------- #

class GetUserBlogsView(View):
    '''View to get blog posts of current logged in user'''
    
    def dispatch_request(self):
        # id is needed
        # Check database for blogs for the current logged in user
        user_blogs = session.query(BlogPost).all()
        
        return render_template('my-blogs.html', user_blogs=user_blogs)

app.add_url_rule('/myblogs', view_func=GetUserBlogsView.as_view(name='getUserBlogs'))


class AddBlogView(View):
    '''View to handle adding of blogs'''
    
    methods = ['GET', 'POST']
    
    def dispatch_request(self):
        
        form = AddBlogForm(request.form)
        messages = None
        
        if request.method == 'POST' and form.validate_on_submit():
            
            date = get_date()
            
            blog = BlogPost(
                title=form.title.data,
                subtitle=form.subtitle.data,
                image_url='https://img.freepik.com/free-photo/toy-bricks-table-with-word-blog_144627-47465.jpg?size=626&ext=jpg&uid=R65046554&ga=GA1.2.163047648.1692182630&semt=sph' if len(form.image_url.data) == 0 else form.image_url.data,
                blog_content=form.blog_content.data,
                date=date
            )
            
            session.add(blog)
            session.commit()
            
            return redirect(url_for('home'))
        
        messages = form.form_errors
        print(messages)
        return render_template('forms/add-blog.html', form=form)
    
app.add_url_rule('/addBlog', view_func=AddBlogView.as_view(name='addBlog'))


class EditBlogView(View):
    '''View to handle editing of blogs'''
    
    methods = ['GET', 'POST']
    
    def dispatch_request(self, id):
        blog = database.get_or_404(BlogPost, id)
        
        form = EditBlogFrom(obj=blog)
        
        if request.method == 'POST' and form.validate_on_submit():
            form.populate_obj(blog)
            
            session.commit()
            return redirect(url_for('getUserBlogs'))
            
        return render_template('forms/edit-blog.html', form=form, blog=blog)
    
app.add_url_rule('/blog/<int:id>/edit', view_func=EditBlogView.as_view(name='editBlog'))


class GetBlogView(View):
    '''View to get individual blogs'''
    
    
    def dispatch_request(self, id):
        form = AddCommentForm(request.form)
        
        # Filter database for blogs based on id
        blog =  database.get_or_404(BlogPost, id)
        
        return render_template('blog-detail.html', blog=blog, form=form)

app.add_url_rule('/blog/<int:id>', view_func=GetBlogView.as_view(name='getBlog'))


class DeleteBlogView(View):
    '''View to get individual blogs'''
    
    def dispatch_request(self, id):
        # Filter database for blogs based on id
        blog =  database.get_or_404(BlogPost, id)
        
        session.delete(blog)
        session.commit()
        
        return redirect(url_for('getUserBlogs'))

app.add_url_rule('/blog/<int:id>/delete', view_func=DeleteBlogView.as_view(name='deleteBlog'))


# def upload_file():
#     if request.method == 'POST':
#         f = request.files['the_file']
#         f.save('/var/www/uploads/' + secure_filename(f.filename))

if __name__ == '__main__':
    app.run(debug=True)
