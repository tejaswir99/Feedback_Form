from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from send_mail import send_mail
# from flask_migrate import Migrate

app = Flask(__name__)

ENV = 'dev'

if ENV == 'dev':
    app.debug = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:root@localhost/practice_prcj'
else:
    app.debug = False
    app.config['SQLALCHEMY_DATABASE_URI'] = ''

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
class Feedback(db.Model):
    __tablename__ = 'feedback'
    id = db.Column(db.Integer, primary_key=True)
    customer = db.Column(db.String(200), unique=True)
    dealer = db.Column(db.String(200))
    rating = db.Column(db.Integer)
    comments = db.Column(db.Text())
    email = db.Column(db.String(200))

    def __init__(self, customer, dealer, rating, comments, email):
        self.customer = customer
        self.dealer = dealer
        self.rating = rating
        self.comments = comments
        self.email = email


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        '''request.form = dict(request.form)
        request.form['rating'] = 10'''
        customer = request.form['customer']
        dealer = request.form['dealer']
        rating = request.form['rating']
        comments = request.form['comments']
        email = request.form['email']
        # print(customer, dealer, rating, comments)
        if customer == '' or dealer == '':
            return render_template('index.html', message='Please enter required fields')
        if db.session.query(Feedback).filter(Feedback.email == email).count() == 0:
            db.session
            data = Feedback(customer, dealer, rating, comments, email)
            db.session.add(data)
            db.session.commit()
            send_mail(customer, dealer, rating, comments, email)
            return render_template('success.html')       
        return render_template('success.html')

if __name__ == '__main__':
    app.run()
