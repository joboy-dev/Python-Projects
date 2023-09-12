from flask import Flask, render_template, request, redirect, url_for, flash
from flask_wtf.csrf import CSRFProtect
from flask.views import View
from flask_ckeditor import CKEditor
from flask_login import LoginManager, login_required, login_url, logout_user, login_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash

from dotenv import load_dotenv
from pathlib import Path
import os
from datetime import datetime

from email_password_regex_check import is_valid_password
from WTF_Forms.user_forms import SignUpForm, EditProfileForm, LoginForm
from WTF_Forms.blog_forms import AddBlogForm, EditBlogFrom, AddCommentForm
import models
from models import BlogPost, User, Comment

BASE_DIR = Path(__file__).resolve().parent.parent.parent.parent
load_dotenv(os.path.join(BASE_DIR, ".env"))

app = Flask(__name__)
app.secret_key = os.getenv('FLASK_SECRET_KEY')

# setting up csrf
csrf = CSRFProtect(app)

# setting up ckeditor
app.config['CKEDITOR_PKG_TYPE'] = 'full'
ckeditor = CKEditor(app)

# setting up flask login manager
login_manager = LoginManager()
login_manager.init_app(app)

# ----------------------- DATABASE CONFIG ------------------------- #

database = models.db
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog_app.db'
database.init_app(app)

# crate all tables
with app.app_context():
    database.create_all()


session = database.session

# ------------------------------ DATE -------------------------------- #

def get_date():
    date_posted = datetime.now().strftime('%d %B, %Y | %H:%M')
    return date_posted


# --------------------- USER CONFIG -------------------------- #

@login_manager.user_loader
def load_user(user_id):
    return session.query(User).get(str(user_id))

# ----------------------- USER VIEWS ------------------------- #

class HomeView(View):
    '''Hone view to get all blogs from the database'''
    
    def dispatch_request(self):
        # Get request to get all blogs
        blogs = session.query(BlogPost).all()
        return render_template('index.html', blogs=blogs, user=current_user)
    
app.add_url_rule('/', view_func=HomeView.as_view(name='home'))

    
class SignUpView(View):
    '''View to handle sign up of users'''
    
    methods = ['GET', 'POST']
    
    def dispatch_request(self):
        message = None
        form = SignUpForm(request.form)
        
        if request.method == 'POST' and form.validate():
            full_name = form.full_name.data
            username = form.username.data
            email = form.email.data
            password = form.password.data
            password2 = form.password2.data
            
            if password != password2:
                message = 'Your passwords do not match.'
            elif not is_valid_password(password) or not is_valid_password(password2):
                message = 'One of your passwords is invalid.'
            # No problems with password
            else:
                username_data = session.query(User).filter_by(username=username).first()
                email_data = session.query(User).filter_by(email=email).first()
                
                # check if username and email exists
                if username_data:
                    message = 'This username is taken.'
                elif email_data:
                    message = 'Thus email is in use.'
                else:
                    # hash password
                    hashed_password = generate_password_hash(password, salt_length=8)
                    
                    # Adding to database
                    user = User(
                        full_name=full_name,
                        username=username,
                        email=email,
                        password=hashed_password,
                    )
                    session.add(user)
                    session.commit()
                    
                    flash(message='You have successfully signed up')
                    return redirect(url_for('login'))

        return render_template('forms/signup.html', form=form, message=message, user=current_user)
    
app.add_url_rule('/signup', view_func=SignUpView.as_view(name='signup'))


class LoginView(View):
    '''View to handle login of users'''
    
    methods = ['GET', 'POST']
    
    def dispatch_request(self):
        message = None
        
        form = LoginForm(request.form)
        
        if request.method == 'POST' and form.validate():
            username = form.username.data
            password = form.password.data
            
            # Perform authentication
            user = session.query(User).filter_by(username=username).first()
            
            if user is not None:
                # check for password
                if check_password_hash(pwhash=user.password, password=password):
                    login_user(user)
                    return redirect(url_for('home'))
                else:
                    message = 'Password is incorrect. Try again.'
            else:
                message = 'Account does not exist.'
            
        return render_template('forms/login.html', message=message, form=form, user=current_user)
    
app.add_url_rule('/login', view_func=LoginView.as_view(name='login'))


class LogoutView(View):
    '''View to handle logout of users'''
    
    decorators = [login_required]
    
    def dispatch_request(self):
        logout_user()
        return redirect(url_for('home'))

app.add_url_rule('/logout', view_func=LogoutView.as_view(name='logout'))


class GetUserDetailsView(View):
    '''View to get details of current logged in user'''
    
    decorators = [login_required]
    
    def dispatch_request(self):
        return render_template('profile.html', user=current_user)

app.add_url_rule('/profile', view_func=GetUserDetailsView.as_view(name='getUserDetails'))


class EditProfileView(View):
    '''View to edit profile'''
    
    methods = ['GET', 'POST']
    decorators = [login_required]
    
    def dispatch_request(self):
        form = EditProfileForm(request.form)
        
        if request.method == 'POST' and form.validate():
            # Check if username/email entered already belongs to another user
            
            flash(message='Changes Saved')
            return redirect(url_for('get_user_details'))
        
        return render_template('forms/edit-profile.html', form=form, user=current_user)
    
app.add_url_rule('/profile/edit', view_func=EditProfileView.as_view(name='editProfile'))


# ----------------------- BLOG VIEWS ------------------------- #

class GetUserBlogsView(View):
    '''View to get blog posts of current logged in user'''
    
    decorators = [login_required]
    
    def dispatch_request(self):
        # id is needed
        # Check database for blogs for the current logged in user
        user_blogs = session.query(BlogPost).all()
        
        return render_template('my-blogs.html', user_blogs=user_blogs, user=current_user)

app.add_url_rule('/myblogs', view_func=GetUserBlogsView.as_view(name='getUserBlogs'))


class AddBlogView(View):
    '''View to handle adding of blogs'''
    
    methods = ['GET', 'POST']
    decorators = [login_required]
    
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
                date=date,
                author_id=current_user.id
            )
            
            session.add(blog)
            session.commit()
            
            return redirect(url_for('home'))
        
        messages = form.form_errors
        print(messages)
        return render_template('forms/add-blog.html', form=form, user=current_user)
    
app.add_url_rule('/addBlog', view_func=AddBlogView.as_view(name='addBlog'))


class EditBlogView(View):
    '''View to handle editing of blogs'''
    
    methods = ['GET', 'POST']
    decorators = [login_required]
    
    def dispatch_request(self, id):
        blog = database.get_or_404(BlogPost, id)
        
        form = EditBlogFrom(obj=blog)
        
        if request.method == 'POST' and form.validate_on_submit():
            form.populate_obj(blog)
            
            session.commit()
            return redirect(url_for('getUserBlogs'))
            
        return render_template('forms/edit-blog.html', form=form, blog=blog, user=current_user)
    
app.add_url_rule('/blog/<int:id>/edit', view_func=EditBlogView.as_view(name='editBlog'))


class GetBlogView(View):
    '''View to get individual blogs'''
    
    decorators = [login_required]
    
    def dispatch_request(self, id):
        form = AddCommentForm(request.form)
        
        # Filter database for blogs based on id
        blog =  database.get_or_404(BlogPost, id)
        
        return render_template('blog-detail.html', blog=blog, form=form, user=current_user)

app.add_url_rule('/blog/<int:id>', view_func=GetBlogView.as_view(name='getBlog'))


class DeleteBlogView(View):
    '''View to get individual blogs'''
    
    decorators = [login_required]
    
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
