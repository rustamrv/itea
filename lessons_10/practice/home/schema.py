from marshmallow import Schema, fields
from marshmallow.validate import Length, Range


class CategorySchema(Schema):
    # id = fields.String(dump_only=True)
    name = fields.String(validate=Length(min=2, max=25), required=True)
    description = fields.String(validate=Length(min=5, max=50))
    parent = fields.Nested('self')


class ProductSchema(Schema):
    name = fields.String(validate=Length(min=2, max=50), required=True)
    price = fields.Float()
    count = fields.Int()
    count_of_view = fields.Int()


class ProductSchemaAdd(Schema):
    name = fields.String(validate=Length(min=2, max=50), required=True)
    price = fields.Float()
    count = fields.Int()
    category = fields.String()

