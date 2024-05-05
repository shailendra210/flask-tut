from flask import Flask,render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from flask import request

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/codingthunder'
db = SQLAlchemy(app)


class Contacts(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=False, nullable=False)
    phone_num = db.Column(db.String(12), unique=True, nullable=False)
    msg = db.Column(db.String(120), unique=False, nullable=False)
    date =db.Column(db.String(12), unique=False,nullable=True)
    email= db.Column(db.String(20), unique=False, nullable=False)



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


@app.route("/static/contact.html", methods = ['GET','POST'])
def contact():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        phone = request.form.get('phone')
        message = request.form.get('message')
        entry = Contacts(name=name,email=email,date=datetime.now(), phone_num=phone, msg=message)
        db.session.add(entry)
        db.session.commit()

    return render_template('contact.html')

app.run(debug=True)