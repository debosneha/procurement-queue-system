from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello World! Flask is working 🎉"

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form['name']
        phone = request.form['phone']
        address = request.form['address']
        crop_type = request.form['crop_type']
        quantity = request.form['quantity']
        center = request.form['center']

        # For now, just print it to the terminal to confirm it works
        print(f"New Registration: {name}, {phone}, {address}, {crop_type}, {quantity}, {center}")

        return f"Thanks {name}! You're registered for {crop_type} ({quantity} quintals) at {center}."
    
    return render_template('register.html')

if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello World! Flask is working 🎉"

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form['name']
        phone = request.form['phone']
        address = request.form['address']
        crop_type = request.form['crop_type']
        quantity = request.form['quantity']
        center = request.form['center']

        # For now, just print it to the terminal to confirm it works
        print(f"New Registration: {name}, {phone}, {address}, {crop_type}, {quantity}, {center}")

        return f"Thanks {name}! You're registered for {crop_type} ({quantity} quintals) at {center}."
    
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)