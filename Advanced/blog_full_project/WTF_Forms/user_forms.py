from wtforms import Form, fields, validators

class SignUpForm(Form):
    '''Form to handle sign up of users'''
    
    username = fields.StringField(
        label='Username',
        validators=[validators.Length(min=6, max=30, message=f'This field allows minimum of 6 characters and maximum of 30 characters')],
        render_kw={'placeholder': 'johndoe123', 'required': True}
    )
    
    email = fields.EmailField(
        label='Email', 
        render_kw={'placeholder': 'johndoe123@gmail.com', 'required': True}
    )
    
    password = fields.PasswordField(
        label='Password',
        render_kw={'placeholder': 'Johndoe@123', 'required': True}
    )
    
    password2 = fields.PasswordField(
        label='Confirm Password',
        render_kw={'placeholder': 'Johndoe@123', 'required': True}
    )
    
    submit = fields.SubmitField(
        render_kw={'value':'Sign Up'}
    )
    
    
class LoginForm(Form):
    '''Form to handle login  of users'''
    
    username = fields.StringField(
        label='Username',
        validators=[validators.Length(min=6, max=30, message=f'This field allows minimum of 6 characters and maximum of 30 characters')],
        render_kw={'placeholder': 'johndoe123', 'required': True}
    )
    
    password = fields.PasswordField(
        label='Password',
        render_kw={'placeholder': 'Johndoe@123', 'required': True}
    )
    
    submit = fields.SubmitField(
        render_kw={'value':'Sign Up'}
    )
    
        
class EditProfileForm(Form):
    '''Form to handle editing of user profile'''  
    
    username = fields.StringField(
        label='Username',
        validators=[validators.Length(min=6, max=30, message=f'This field allows minimum of 6 characters and maximum of 30 characters')],
        render_kw={'placeholder': 'johndoe123', 'required': True}
    )
    
    email = fields.EmailField(
        label='Email', 
        render_kw={'placeholder': 'johndoe123@gmail.com', 'required': True}
    )
    
    submit = fields.SubmitField(
        render_kw={'value':'Make Changes'}
    )
