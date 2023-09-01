from flask import Flask

app = Flask(__name__)

def make_bold(func):
    def warapper():
        text = f'<b>{func()}</b>'
        return text
    return warapper

def make_italic(func):
    def warapper():
        text = f'<em>{func()}</em>'
        return text
    return warapper

def make_underlined(func):
    def warapper():
        text = f'<u>{func()}</u>'
        return text
    return warapper
        

@app.route('/')
def hello_world():
    return '<h1>Hello World!</h1>'

@app.route('/bye')
@make_bold
@make_italic
@make_underlined
def bye():
    return 'Bye'

# adding variable paths to url and converting path variables to a specific date type
@app.route('/user/<username>/<int:no>')
def show_user_profile(username, no):
    return f'Hello there {username} with number of {no}'

if __name__ == '__main__':
    app.run(debug=True)
