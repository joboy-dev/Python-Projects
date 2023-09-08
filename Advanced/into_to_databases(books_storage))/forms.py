from wtforms import Form, fields, validators

class AddBookForm(Form):
    '''Form to handle sign up of users'''
    
    book_title = fields.StringField(
        label='Book Title',
        validators=[
            validators.Length(min=6, max=30, message=f'This field allows minimum of 6 characters and maximum of 30 characters'),
        ],
        render_kw={'required': True}
    )
    
    author = fields.StringField(
        label='Author', 
        render_kw={'required': True}
    )
    
    rating = fields.FloatField(
        label='Rating',
        render_kw={'required': True}
    )


class EditRatingForm(Form):
    '''Form to edit rating'''  
    
    rating = fields.FloatField(
        label='Rating',
        render_kw={'required': True}
    )
   