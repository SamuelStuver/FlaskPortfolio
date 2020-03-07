from flask import Flask, render_template, url_for

app = Flask(__name__)
app.config['DEBUG'] = True

posts = [
    {
        "title": "Post 1",
        "author": "Sam Stuver",
        "date_posted": "March 7, 2020",
        "content": "First post content"
    },
    {
        "title": "Post 2",
        "author": "Sam Stuver",
        "date_posted": "March 7, 2020",
        "content": "Second post content"
    }
]


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', posts=posts)


@app.route('/about')
def about():
    return render_template('about.html', title="About")


if __name__ == '__main__':
    app.run()
