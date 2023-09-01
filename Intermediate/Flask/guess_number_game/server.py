from flask import Flask
import random

app = Flask(__name__)
number_to_guess = random.randint(0, 9)

@app.route('/')
def home():
    return "<h1>Guess a number between 0 and 9</h1>\n<img src='https://media3.giphy.com/media/l378khQxt68syiWJy/200w.webp?cid=ecf05e47n9znicp1sz2vrjmeoi0tqnfux4fkjmhy0nwi23hz&ep=v1_gifs_search&rid=200w.webp&ct=g' width=250px>"

@app.route('/guess/<int:number>')
def number_guess(number):
    
    if number_to_guess == number:
        return "<h1 style='color:green;'>You got it right</h1>\n<img src='https://media4.giphy.com/media/26tknCqiJrBQG6bxC/200.webp?cid=ecf05e4749cjek7w5qr3ghh2nf1btb44n30bc666dsrdklff&ep=v1_gifs_search&rid=200.webp&ct=g' width=250px>"
    elif number_to_guess < number:
        return "<h1 style='color:red;'>Too high</h1>\n<img src='https://media2.giphy.com/media/41g6S55zT5h9RpxgW0/200w.webp?cid=ecf05e47x1uy2qi1lvvdxbj1ap3zm9y9hlntzrq476izwn2u&ep=v1_gifs_search&rid=200w.webp&ct=g' width=250px>"
    elif number_to_guess > number:
        return "<h1 style='color:red;'>Too low</h1>\n<img src='https://media0.giphy.com/media/PR3585ZZSvcHO9pa76/200w.webp?cid=ecf05e4739npax4104w1xp2d9w87cdfhw6pr6rswcw17eta1&ep=v1_gifs_search&rid=200w.webp&ct=g' width=250px>"

if __name__ == '__main__':
    app.run(debug=True)