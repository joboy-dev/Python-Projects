from __init__ import *

# ----------------------- USER VIEWS ------------------------- #

class HomeView(View):
    '''Hone view to get all blogs from the database'''
    
    def dispatch_request(self):
        # Get request to get all blogs
        blogs = session.query(Blog).all()
        return render_template('index.html', blogs=blogs, user=current_user)
    
app.add_url_rule('/', view_func=HomeView.as_view(name='home'))

    
class SignUpView(View):
    '''View to handle sign up of users'''
    
    methods = ['GET', 'POST']
    
    def dispatch_request(self):
        message = None
        form = SignUpForm(request.form)
        
        if request.method == 'POST' and form.validate_on_submit():
            full_name = form.full_name.data
            username = form.username.data
            email = form.email.data
            password = form.password.data
            password2 = form.password2.data
            profile_picture = 'https://th.bing.com/th?id=OIP.2s7VxdmHEoDKji3gO_i-5QHaHa&w=250&h=250&c=8&rs=1&qlt=90&o=6&pid=3.1&rm=2'
            
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
                        profile_picture=profile_picture
                    )
                    session.add(user)
                    session.commit()
                    
                    login_user(user)
                    
                    flash('You have successfully signed up')
                    return redirect(url_for('home'))

        return render_template('forms/signup.html', form=form, message=message, user=current_user)
    
app.add_url_rule('/signup', view_func=SignUpView.as_view(name='signup'))


class LoginView(View):
    '''View to handle login of users'''
    
    methods = ['GET', 'POST']
    
    def dispatch_request(self):
        message = None
        
        form = LoginForm(request.form)
        
        if request.method == 'POST' and form.validate_on_submit():
            username = form.username.data
            password = form.password.data
            
            # Perform authentication
            user = session.query(User).filter_by(username=username).first()
            
            if user is not None:
                # check for password
                if check_password_hash(pwhash=user.password, password=password):
                    login_user(user)
                    flash('Successfully logged in.')
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
        flash('Logout successful. See you later.')
        return redirect(url_for('home'))

app.add_url_rule('/logout', view_func=LogoutView.as_view(name='logout'))


class GetUserDetailsView(View):
    '''View to get details of current logged in user'''
    
    decorators = [login_required]
    
    def dispatch_request(self):
        change_picture_form = ChangeProfilePictureForm(request.files)
        return render_template('profile.html', user=current_user, form=change_picture_form)

app.add_url_rule('/profile', view_func=GetUserDetailsView.as_view(name='getUserDetails'))


class EditProfileView(View):
    '''View to edit profile'''
    
    methods = ['GET', 'POST']
    decorators = [login_required]
    
    def dispatch_request(self):
        message = None
        
        user = database.get_or_404(User, current_user.id)
        form = EditProfileForm(obj=user)
        
        if request.method == 'POST' and form.validate_on_submit():
            form.populate_obj(user)
            session.commit()
            
            flash('Profile changes saved')
            return redirect(url_for('getUserDetails'))
    
        return render_template('forms/edit-profile.html', form=form, user=current_user, message=message)
    
app.add_url_rule('/profile/edit', view_func=EditProfileView.as_view(name='editProfile'))


class ChangePasswordView(View):
    '''View to change user password'''
    
    methods = ['GET', 'POST']
    decorators = [login_required]
    
    def dispatch_request(self):
        form = ChangePasswordForm(request.form)
        user = session.query(User).filter_by(username=current_user.username).first()
        
        message = None
        
        if request.method == 'POST' and form.validate_on_submit():
            old_password = form.old_password.data
            new_password = form.new_password.data
            new_password2 = form.new_password2.data
            
            if not check_password_hash(pwhash=user.password, password=old_password):
                message = 'Old password is incorrect.'
            else:
                if new_password != new_password2:
                    message = 'New passwords do not match.'
                elif not is_valid_password(new_password) or not is_valid_password(new_password2):
                    message = 'One of your new passwords is invalid.'
                else:
                    new_password_hash = generate_password_hash(new_password, salt_length=8)
                    user.password = new_password_hash
                    
                    session.commit()
                    
                    flash('Password changed successfully.')
                    return redirect(url_for('getUserDetails'))
                    
        return render_template('forms/change-password.html', form=form, user=current_user, message=message)
        
    
app.add_url_rule('/profile/change-password', view_func=ChangePasswordView.as_view(name='changePassword'))


class ChangeProfilePictureView(View):
    '''View to change user profile picture'''
    
    methods = ['POST']
    decorators = [login_required]
    
    def dispatch_request(self):
        form = ChangeProfilePictureForm(request.files)
        
        # if form.validate_on_submit() and 'picture' in request.files:
        #     return redirect(url_for('getUserDetails'))
        
        return redirect(url_for('getUserDetails'))
        
        # return render_template('profile.html', form=form, user=current_user)
    
app.add_url_rule('/profile/change-profile-picture', view_func=ChangeProfilePictureView.as_view(name='changeProfilePicture'))

# def upload_file():
#     if request.method == 'POST':
#         f = request.files['the_file']
#         f.save('/var/www/uploads/' + secure_filename(f.filename))


# ----------------------- BLOG VIEWS ------------------------- #

class GetUserBlogsView(View):
    '''View to get blog posts of current logged in user'''
    
    decorators = [login_required]
    
    def dispatch_request(self):
        print(current_user.id)
        # Check database for blogs for the current logged in user
        user_blogs = session.query(Blog).filter_by(author_id=current_user.id).all()
        
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
            
            blog = Blog(
                title=form.title.data,
                subtitle=form.subtitle.data,
                image_url='https://img.freepik.com/free-photo/toy-bricks-table-with-word-blog_144627-47465.jpg?size=626&ext=jpg&uid=R65046554&ga=GA1.2.163047648.1692182630&semt=sph' if len(form.image_url.data) == 0 else form.image_url.data,
                blog_content=form.blog_content.data,
                created=date,
                updated=date,
                author_id=current_user.id
            )
            
            session.add(blog)
            session.commit()
            
            flash('Blog post added.')
            return redirect(url_for('getUserBlogs'))
        
        messages = form.form_errors
        print(messages)
        return render_template('forms/add-blog.html', form=form, user=current_user)
    
app.add_url_rule('/addBlog', view_func=AddBlogView.as_view(name='addBlog'))


class EditBlogView(View):
    '''View to handle editing of blogs'''
    
    methods = ['GET', 'POST']
    decorators = [login_required]
    
    def dispatch_request(self, id):
        message = None
        blog = database.get_or_404(Blog, id)
        
        form = EditBlogFrom(obj=blog)
        
        if request.method == 'POST' and form.validate_on_submit():
            date = get_date()
            form.populate_obj(blog)
            
            if blog.author_id == current_user.id:
                blog.updated = date
                session.commit()
                
                flash('Blog post updated.')
                return redirect(url_for('getBlog', id=blog.id))
            else:
                message = 'You cannot edit another user\'s post'
                return abort(code=401)
            
        return render_template('forms/edit-blog.html', form=form, blog=blog, user=current_user, message=message)
    
app.add_url_rule('/blog/<int:id>/edit', view_func=EditBlogView.as_view(name='editBlog'))


class GetBlogView(View):
    '''View to get individual blogs'''
    
    # decorators = [login_required]
    
    def dispatch_request(self, id):
        form = AddCommentForm(request.form)
        
        # Filter database for blogs based on id
        blog =  database.get_or_404(Blog, id)
        
        return render_template('blog-detail.html', blog=blog, form=form, user=current_user)

app.add_url_rule('/blog/<int:id>', view_func=GetBlogView.as_view(name='getBlog'))


class DeleteBlogView(View):
    '''View to get individual blogs'''
    
    decorators = [login_required]
    
    def dispatch_request(self, id):
        message = None
        # Filter database for blogs based on id
        blog =  database.get_or_404(Blog, id)
        
        if blog.author_id == current_user.id: 
            session.delete(blog)
            session.commit()
            
            flash('Blog post deleted')
            return redirect(url_for('getUserBlogs'))
        else:
            message = 'You cannot delete another user\'s blog.'
            return abort(code=401)
            

app.add_url_rule('/blog/<int:id>/delete', view_func=DeleteBlogView.as_view(name='deleteBlog'))


class AddBlogCommentView(View):
    '''View to add comments to blogs'''
    
    methods = ['POST']
    
    def dispatch_request(self, id):
        form = AddCommentForm(request.form)
        blog = database.get_or_404(Blog, id)
        
        if request.method == 'POST' and form.validate_on_submit():
            date = get_date()
            
            # create comment object to add to database
            comment = Comment(
                comment=form.comment.data,
                created=date,
                blog_id=blog.id,
                author_id=current_user.id
            )
            
            session.add(comment)
            session.commit()
            
            flash('Comment added')
            
        return redirect(url_for('getBlog', id=blog.id))
        
        
app.add_url_rule('/blog/<int:id>/addComment', view_func=AddBlogCommentView.as_view(name='addComment'))



# Run app
if __name__ == '__main__':
    app.run(debug=True)
