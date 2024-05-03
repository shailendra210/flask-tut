from flask import Flask,render_template

app = Flask(__name__)


@app.route("/")
@app.route("/static/index.html")
def home():
    return render_template('index.html')

@app.route("/static/about.html")
def about():
    return render_template('about.html')

@app.route("/static/post.html")
def post():
    return render_template('post.html')



@app.route("/static/contact.html")
def contact():
    return render_template('contact.html')

app.run(debug=True)