from flask import Flask, jsonify, request, Response
from flask_restful import Api
from resources import TagResource, PostResource, PostAuthorResource


app = Flask(__name__)
api = Api(app)

api.add_resource(TagResource, '/tags', '/tags/<string:tag_id>')
api.add_resource(PostResource, '/add_post')
api.add_resource(PostAuthorResource, '/posts', '/posts/<string:post_id>')

app.run(debug=True)