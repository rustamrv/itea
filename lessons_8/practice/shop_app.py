from flask import Flask, render_template, request
from manager_db import ManagerDb

app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index():
    mn_db = ManagerDb('shop.db')
    rows = mn_db.select_category()  
    return render_template('index.html', categories=rows)


@app.route('/category/<string:category_id>')
def get_detail_category(category_id):
    mn_db = ManagerDb('shop.db')
    products, name_category = mn_db.select_category_products(category_id)
    return render_template('products.html', products=products, name_category=name_category)


@app.route('/detail_product/<string:product_id>')
def get_detail_product(product_id):
    mn_db = ManagerDb('shop.db')
    product = mn_db.select_detail_product(product_id)
    try:
        return render_template('detail_product.html', product=product[0])
    except IndexError:
        return render_template('error.html', error=f'Not found product with id {product_id}')


@app.route('/detail_admin', methods=['GET'])
def detail_admin():
    mn_db = ManagerDb('shop.db')
    category = mn_db.get_category()
    return render_template('detail_admin.html', category=category)


@app.route('/add_category', methods=['POST'])
def add_category():
    mn_db = ManagerDb('shop.db')
    category = mn_db.get_category()
    data = dict(request.form)
    if data['category'] and data['name']:
        mn_db.add_category(data["name"], data["category"])
    return render_template('detail_admin.html', category=category)


@app.route('/add_product', methods=['POST'])
def add_product():
    mn_db = ManagerDb('shop.db')
    category = mn_db.get_category()
    data = dict(request.form)
    mn_db.add_product(data["name"], data["price"], data["count"], data["discription"], data["category"])
    return render_template('detail_admin.html', category=category)


if __name__ == "__main__":
    mn_db = ManagerDb('shop.db')
    # mn_db.create_category()
    # mn_db.create_product()
    app.run(debug=True)