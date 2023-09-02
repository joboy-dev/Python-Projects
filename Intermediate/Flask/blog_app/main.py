from flask import Flask, render_template
from post import Post

app = Flask(__name__)

@app.route('/')
def home():
    post = Post()
    
    all_posts = post.get_all_posts()
    return render_template("index.html", posts=all_posts)

@app.route('/post/<int:id>')
def get_post(id):
    post = Post()
    
    single_post = post.get_post(id)
    print(single_post)
    return render_template('post.html', post=single_post)


if __name__ == "__main__":
    app.run(debug=True)
