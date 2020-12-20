from marshmallow import Schema, fields
from marshmallow.validate import Length, Range


class TagSchema(Schema):
    # id = fields.String(dump_only=True)
    name = fields.String(validate=Length(min=2, max=25), required=True)


class AuthorSchema(Schema):
    id = fields.String(dump_only=True)
    first_name = fields.String(validate=Length(min=2, max=44), required=True)
    last_name = fields.String(validate=Length(min=2, max=64))


class PostSchema(Schema):
    id = fields.String(dump_only=True)
    name = fields.String(validate=Length(min=2, max=25), required=True)
    description = fields.String(validate=Length(min=10, max=300))
    number_of_views = fields.String()
    author = fields.Nested(AuthorSchema())
    tag = fields.List(fields.Nested(TagSchema()))


class PostSchema_add(Schema):
    id = fields.String(dump_only=True)
    name = fields.String(validate=Length(min=2, max=25), required=True)
    description = fields.String(validate=Length(min=10, max=300))
    number_of_views = fields.String()
    author = fields.Nested(AuthorSchema())
    tag = fields.List(fields.String())
