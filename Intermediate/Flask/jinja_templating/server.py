from flask import Flask, render_template
import random
from datetime import datetime
import requests

app = Flask(__name__)


@app.route('/')
def hello_world():
    no = random.randint(0, 10)
    year = datetime.now().year
    
    return render_template('index.html', num=no, current_year=year)

@app.route('/guess/<name>')
def get_age_and_gender(name):
    agify_url = f'https://api.agify.io?name={name}'
    agify_response = requests.get(agify_url).json()
    
    genderize_url = f'https://api.genderize.io?name={name}'
    genderize_response = requests.get(genderize_url).json()
    
    return render_template('details.html', name=name, age=agify_response['age'], gender=genderize_response['gender'])

@app.route('/blogs/<int:num>')
def get_blogs():
    blog_url = 'https://api.npoint.io/8a9a646d51cdf742b827'
    blog_data = requests.get(blog_url).json()
    
    return render_template('blog.html', posts=blog_data['posts'])


if __name__ == '__main__':
    app.run(debug=True)
