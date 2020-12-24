from flask_restful import Resource
from marshmallow import ValidationError
from models import Category, Product
from schema import ProductSchemaAdd, ProductSchema
import json
from flask import request, render_template
from mongoengine.errors import ValidationError, NotUniqueError


class CategoryResource(Resource):
    def get(self, category_id=None):
        if category_id:
            tag_list = Category.objects.get(id=category_id)
            product_list = Product.objects(category=tag_list)
            for product in product_list:
                product.count_of_view += 1
                product.save()
            return ProductSchema(many=True).dump(product_list)
        else:
            users = Category.objects()
            user_json = users.to_json()
            return json.loads(user_json)


class ProductResource(Resource):

    def post(self):
        json_data = request.json
        errors = ProductSchemaAdd().validate(json_data)
        if errors:
            return errors
        category_name = json_data.get('category')
        category = Category.objects(name=category_name)
        if len(category) == 0:
            category = Category(name=category_name)
            category.save()
        else:
            category = category[0]
        try:
            product = Product(**json_data)
            product.category = category
            product.save()
            user_json = product.to_json()
            return json.loads(user_json)
        except ValidationError as errors:
            print(errors)


class ProductTotalCost(Resource):

    def get(self):
        products = Product.objects
        data = {
            "total cost": products.sum('price')*products.sum('count'),
            "products": json.loads(products.to_json())
        }
        return data
