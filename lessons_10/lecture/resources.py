from flask_restful import Resource
from marshmallow import ValidationError
from models import User
from schema import UserSchema
import json
from flask import request, Response


class UserResource(Resource):

    def get(self, id=None):
        if id:
            return UserSchema().dump(User.objects.get(id=id))
        else:
            users = User.objects()
            user_json = users.to_json()
            return json.loads(user_json)

    def post(self):
        try:
            UserSchema().load(request.json)
        except ValidationError as e:
            return {'error': str(e)}
        user = User(**request.json).save()
        return UserSchema().dump(user)

    def put(self):
        pass

    def delete(self):
        pass

