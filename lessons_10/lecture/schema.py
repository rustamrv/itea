from marshmallow import Schema, fields
from marshmallow.validate import Length, Range


class UserSchema(Schema):
    id = fields.String()
    first_name = fields.String(validate=Length(min=2, max=64), required=True)
    interests = fields.List(fields.String)
    age = fields.Integer(validate=Range(min=12, max=99))
    created_at = fields.DateTime()
