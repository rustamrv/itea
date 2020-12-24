from flask import Flask
from flask_restful import Api
from resources import CategoryResource, ProductResource, ProductTotalCost


app = Flask(__name__)
api = Api(app)

api.add_resource(CategoryResource, '/category', '/category/<string:category_id>')
api.add_resource(ProductResource, '/add_product')
api.add_resource(ProductTotalCost, '/show_cost')

app.run(debug=True)