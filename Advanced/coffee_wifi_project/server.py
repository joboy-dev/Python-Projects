from flask import Flask, render_template, redirect, request, url_for
from flask.views import View
from flask_wtf.csrf import CSRFProtect
from dotenv import load_dotenv
from pathlib import Path
import os
import pandas as pd

from WTF_Forms.add_cafe_form import AddCafeForm

BASE_DIR = Path(__file__).resolve().parent.parent.parent.parent
load_dotenv(os.path.join(BASE_DIR, ".env"))

app = Flask(__name__)
csrf = CSRFProtect(app)
app.secret_key = os.getenv('FLASK_SECRET_KEY')

# VIEWS
class HomeView(View):
    '''View for home page'''
    
    def dispatch_request(self):
        return render_template('index.html')
    
app.add_url_rule('/', view_func=HomeView.as_view('home'))


class AllCafesView(View):
    '''View for all cafes page'''
    
    
    def dispatch_request(self):
        try:
            cafes_dataframe = pd.read_csv('Advanced/coffee_wifi_project/cafe-data.csv')
            all_cafe_data = cafes_dataframe.to_dict(orient='records')
            # print(all_cafe_data)
        except FileNotFoundError:
            with open('Advanced/coffee_wifi_project/cafe-data.csv', 'w') as file:
                file.write('Cafe Name,Location,Open,Close,Coffee,Wifi,Power')
                
            cafes_dataframe = pd.read_csv('Advanced/coffee_wifi_project/cafe-data.csv')
            all_cafe_data = cafes_dataframe.to_dict(orient='records')
        
        return render_template('cafes.html', cafe_data=all_cafe_data)
    
app.add_url_rule('/cafes', view_func=AllCafesView.as_view('cafes'))


class AddCafeView(View):
    '''View to add cafe to csv file page'''
    
    methods = ['GET', 'POST']
    
    def dispatch_request(self):
        cafes_dataframe = pd.read_csv('Advanced/coffee_wifi_project/cafe-data.csv')
        all_cafe_data = cafes_dataframe.to_dict(orient='records')
        
        form = AddCafeForm(request.form)
        
        if request.method == 'POST' and form.validate():
            # get all user input
            cafe_name = form.cafe_name.data
            location = form.location.data
            open = form.open.data.isoformat()
            close = form.close.data.isoformat()
            coffee_quality = form.coffee_quality.data
            wifi_strength = form.wifi_strength.data
            power_strength = form.power_strength.data
            
            data_dict = {
                'Cafe Name': cafe_name,
                'Location': location, 
                'Open': f'{open[0:5]}',
                'Close': f'{close[0:5]}', 
                'Coffee': coffee_quality, 
                'Wifi': wifi_strength, 
                'Power': power_strength
            }
            
            # append new data to dictionary list
            all_cafe_data.append(data_dict)
            
            # write data to csv file
            cafes_dataframe = pd.DataFrame(data=all_cafe_data)
            cafes_dataframe.to_csv('Advanced/coffee_wifi_project/cafe-data.csv', index=False)
            
            # redirect to cafes page
            return redirect(url_for('cafes'))
        
        return render_template('add.html', form=form)
    
app.add_url_rule('/cafes/add', view_func=AddCafeView.as_view('add_cafe'))


if __name__ == '__main__':
    app.run(debug=True)