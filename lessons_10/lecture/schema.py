from marshmallow import Schema, fields
from marshmallow.validate import Length, Range


class UserSchema(Schema):
    id = fields.String(dump_only=True)
    first_name = fields.String(validate=Length(min=2, max=64), required=True)
    interest = fields.List(fields.String)
    age = fields.Integer(validate=Range(min=12, max=99), load_only=True)
    created_at = fields.DateTime()
    user_profile = fields.String()
