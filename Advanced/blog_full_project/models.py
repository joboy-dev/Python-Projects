from flask_sqlalchemy import SQLAlchemy
import sqlalchemy as sa

db = SQLAlchemy()

class BlogPost(db.Model):
    '''Posts table/model'''
    
    id =  sa.Column(sa.Integer, primary_key=True)
    title = sa.Column(sa.String(50), nullable=False)
    subtitle = sa.Column(sa.String(40), nullable=False)
    image_url = sa.Column(sa.String, nullable=False)
    blog_content = sa.Column(sa.Text, nullable=False)
    date = sa.Column(sa.String)
    
    def __str__(self):
        return f'{self.title}'
    

class Comment(db.Model):
    '''Comnents table/model'''
    
    id =  sa.Column(sa.Integer, primary_key=True)
    comment = sa.Column(sa.String, nullable=True)
