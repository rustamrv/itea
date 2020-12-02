from flask import Flask, render_template

app = Flask(__name__)

cars = [{
    'model':'BMW',
    'price': 12000
}]

@app.route('/cars')
def get_cars():
    return render_template('cars.html', cars=cars)

app.run(debug=True)