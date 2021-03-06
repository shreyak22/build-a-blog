from flask import Flask, request, redirect, render_template, flash
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://build-a-blog:12356790@localhost:8889/build-a-blog'
app.config['SQLALCHEMY_ECHO'] = True
db = SQLAlchemy(app)
app.secret_key = 'wertyuiop1234'


class Post(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255))
    text = db.Column(db.String(255))
    
    def __init__(self, title, text):
        self.title = title
        self.text = text
        


@app.route('/blog', methods=['GET'])
def index():
    
    posts = Post.query.all()
    

    return render_template('index.html',title="Build A Blog!", posts=posts)


@app.route('/newpost', methods=['POST', 'GET'])
def add():
    if request.method == 'POST':
        title_name = request.form['title']
        post = request.form['post']   
        if title_name == "" or post == "":
            return render_template('add.html', title_error="This field is required", post_value=post, title_value=title_name)
        new_post = Post(title_name, post)
        db.session.add(new_post)
        db.session.commit()
        return render_template('add-post.html', post=new_post)

    
    return render_template('add.html')


@app.route('/blog-list', methods=['GET','POST'])
def blog_list():
    return render_template('add-post.html', title="blog-post")

@app.route('/post-title', methods=['GET'])
def post_title():
        
    post_id = int(request.args.get('id'))
    post = Post.query.get(post_id)   
    return render_template('add-post.html',post=post)


if __name__ == '__main__':
    app.run()