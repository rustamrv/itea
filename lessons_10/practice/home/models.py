from random import choice
import mongoengine as me
from datetime import datetime
me.connect('rest_api_lessons_10_home')


class Category(me.Document):
    name = me.StringField(min_length=2, max_length=25, unique=True)
    description = me.StringField(min_length=5, max_length=50)
    parent = me.ReferenceField('self')
    subcategories = me.ListField(me.ReferenceField('self'))

    def get_products(self):
        return Product.objects(category=self)

    @classmethod
    def get_root_categories(cls):
        return cls.objects(
            parent=None
        )

    def is_root(self):
        return not bool(self.parent)

    def add_subcategory(self, category):
        category.parent = self
        category.save()
        self.subcategories.append(category)
        self.save()


class Product(me.Document):
    name = me.StringField(min_length=2, max_length=50)
    price = me.FloatField(required=True)
    category = me.ReferenceField(Category, required=True)
    count = me.IntField(default=0)
    count_of_view = me.IntField(default=0)


if __name__ == "__main__":
    data_json = [
        {
            "name": 'Category-1',
            "description": 'about category-1',
            "parent": None
        },
        {
            "name": 'Category-2',
            "description": 'about category-2',
            "parent": None
        },
        {
            "name": 'Category-3',
            "description": 'about category-3',
            "parent": 'Category-1'
        },
        {
            "name": 'Category-4',
            "description": 'about category-4',
            "parent": 'Category-1'
        },
        {
            "name": 'Category-5',
            "description": 'about category-5',
            "parent": 'Category-2'
        },
    ]

    # for u in data_json:
    #     try:
    #         category = Category(**u)
    #         category.save()
    #         if u['parent']:
    #             parent = Category.objects.get(name=u['parent'])
    #             category.add_subcategory(parent)
    #
    #     except me.NotUniqueError:
    #         print('category unique')

    product_json = [
        {
            'name': 'Product-1',
            'price': 155.20,
            'category': Category.objects.get(name='Category-1'),
            'count': 100
        },
        {
            'name': 'Product-2',
            'price': 50.20,
            'category': Category.objects.get(name='Category-2'),
            'count': 32
        },
        {
            'name': 'Product-3',
            'price': 155.20,
            'category': Category.objects.get(name='Category-3'),
            'count': 0
        },
        {
            'name': 'Product-4',
            'price': 12.20,
            'category': Category.objects.get(name='Category-1'),
            'count': 10
        },
        {
            'name': 'Product-5',
            'price': 48.20,
            'category': Category.objects.get(name='Category-4'),
            'count': 100
        }
    ]

    for pr in product_json:
        product = Product(**pr)
        product.save()
