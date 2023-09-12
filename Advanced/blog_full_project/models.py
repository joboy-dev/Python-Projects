from flask_sqlalchemy import SQLAlchemy
import sqlalchemy as sa
from flask_login import UserMixin

db = SQLAlchemy()


class User(db.Model, UserMixin):
    '''Users table/model'''
    
    id = sa.Column(sa.Integer, primary_key=True)
    full_name = sa.Column(sa.Text, nullable=False)
    username = sa.Column(sa.String, unique=True, nullable=False)
    email = sa.Column(sa.String, unique=True, nullable=False)
    password = sa.Column(sa.String, nullable=False)
    
    posts = db.relationship('BlogPost', backref='author', lazy=True)
    
    def __str__(self):
        return f'{self.id} | {self.username} | {self.email}'


class BlogPost(db.Model):
    '''Posts table/model'''
    
    id =  sa.Column(sa.Integer, primary_key=True)
    title = sa.Column(sa.String(50), nullable=False)
    subtitle = sa.Column(sa.String(40), nullable=False)
    image_url = sa.Column(sa.String, nullable=False)
    blog_content = sa.Column(sa.Text, nullable=False)
    date = sa.Column(sa.String)
    
    author_id = sa.Column(sa.Integer, sa.ForeignKey('user.id'), nullable=False)
    
    def __str__(self):
        return f'{self.title}'
    

class Comment(db.Model):
    '''Comnents table/model'''
    
    id =  sa.Column(sa.Integer, primary_key=True)
    comment = sa.Column(sa.String, nullable=True)
