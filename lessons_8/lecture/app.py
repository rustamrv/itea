from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index(): 
    name = 'Rustam'
    return render_template('index.html', name=name)

products = {
    'Onion':{
        'price':12,
        'in_stock': 100,
        'description': 'Onion'
    }, 
    'Tomato':{ 
        'price':12,
        'in_stock': 100,
        'description': 'Tomato'
    }, 
    'Cucumber':{ 
        'price':12,
        'in_stock': 100,
        'description': 'Cucumber'
    },   
}
@app.route('/products')
def get_products():  
    return render_template('products.html', products=products)


@app.route('/products/<string:product_name>')
def get_detail_product(product_name):
    return render_template('product.html', product=products[product_name])

@app.route('/goodbye')
def bye():
    return 'bye'



app.run(debug=True)