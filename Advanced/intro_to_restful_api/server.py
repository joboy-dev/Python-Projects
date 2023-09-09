import random
from flask import Flask, render_template, redirect, request, typing as ft, url_for, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_sqlalchemy.session import Session
from flask.views import MethodView
from flask_wtf.csrf import CSRFProtect
from dotenv import load_dotenv
from pathlib import Path
import os

BASE_DIR = Path(__file__).resolve().parent.parent.parent.parent
load_dotenv(os.path.join(BASE_DIR, ".env"))

app = Flask(__name__)
csrf = CSRFProtect(app)
app.secret_key = os.getenv('FLASK_SECRET_KEY')

db = SQLAlchemy()
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafe.db'
db.init_app(app)

session = Session(db)

class Cafe(db.Model):
    '''Table for cafe details'''
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True, nullable=False)
    map_url = db.Column(db.String, nullable=False)
    img_url = db.Column(db.String, nullable=False)
    location =db.Column(db.String, nullable=False)
    seats = db.Column(db.String, nullable=False)    
    has_toilet = db.Column(db.Boolean, nullable=False)
    has_wifi = db.Column(db.Boolean, nullable=False)
    has_sockets =db.Column(db.Boolean, nullable=False)
    can_take_calls = db.Column(db.Boolean, nullable=False)
    coffee_price = db.Column(db.Float, nullable=False)
    
with app.app_context():
    db.create_all()


class AllCafesView(MethodView):
    
    def get(self):
        cafes = session.query(Cafe).all()
        cafes_list = [cafe.__dict__ for cafe in cafes]
        
        for cafe in cafes_list :
            del cafe['_sa_instance_state']
        
        return jsonify(cafes=cafes_list)

app.add_url_rule('/', view_func=AllCafesView.as_view('home'))


class SingleCafeView(MethodView):
    
    decorators = [csrf.exempt]
    def get(self, id):
        cafe = session.get(Cafe, id)
        if cafe:
            cafe_item = cafe.__dict__
            del cafe_item['_sa_instance_state']
            return jsonify(cafe_item)
        else:
            return jsonify(response={'error': 'This cafe does not exist'})
        
    def delete(self, id):
        # query paramaters
        api_key = request.args.get('api_key')
        
        if api_key == 'joboy':
            cafe = session.get(Cafe, id)
            if cafe:
                session.delete(cafe)
                session.commit()
                return jsonify(response={'success': f'Cafe {cafe.name} deleted.'})
            else:
                return jsonify(error={'message': 'This cafe does not exist'}) 
        else:
            return jsonify(error={'message': 'You do not have permission to delete this cafe.'}) 
            
app.add_url_rule('/cafes/<int:id>', view_func=SingleCafeView.as_view('cafe'))

        
class AddCafeView(MethodView):

    decorators = [csrf.exempt]
    
    def get(self):
        return jsonify(response={'error': 'This request is not supported'})
        
    def post(self):
        new_cafe = Cafe(
            name=request.form.get("name"),
            map_url=request.form.get("map_url"),
            img_url=request.form.get("img_url"),
            location=request.form.get("loc"),
            has_sockets=bool(request.form.get("sockets")),
            has_toilet=bool(request.form.get("toilet")),
            has_wifi=bool(request.form.get("wifi")),
            can_take_calls=bool(request.form.get("calls")),
            seats=request.form.get("seats"),
            coffee_price=request.form.get("coffee_price"),
        )
        session.add(new_cafe)
        session.commit()
        
        # print(new_cafe.__dict__)
        return jsonify(response={'success': f'Cafe {new_cafe.name} successfully added'})
    
app.add_url_rule('/add', view_func=AddCafeView.as_view('addCafe'))



if __name__ =='__main__':
    app.run(debug=True)


