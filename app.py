from flask import Flask, render_template, request, url_for,redirect
from flask_sqlalchemy import SQLAlchemy 
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///test.db'
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String(80), nullable=False)
    phone=db.Column(db.String(20),nullable=False)
    address=db.Column(db.String(200), nullable=False)
    crop_type=db.Column(db.String(50), nullable=False)
    quantity=db.Column(db.Float, nullable=False)
    center=db.Column(db.String(100),nullable=False)
    date_created=db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return '<Task %r>' % self.id


@app.route('/')
def home():
    return render_template('home.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form['name']
        phone = request.form['phone']
        address = request.form['address']
        crop_type = request.form['crop_type']
        quantity = request.form['quantity']
        center = request.form['center']
        new_user = User(name=name,phone=phone,address=address,
                        crop_type=crop_type,quantity=quantity,
                        center=center)
        try:
            db.session.add(new_user)
            db.session.commit()
            return redirect(url_for('thankyou'))
        except Exception as e:
            return f'There was an issur: {e}'  
    return render_template('register.html')

@app.route('/thankyou')
def thankyou():
    return render_template('thankyou.html')

with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)

