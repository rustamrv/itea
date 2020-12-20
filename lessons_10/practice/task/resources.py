from flask_restful import Resource
from marshmallow import ValidationError
from models import Tag, Post, Author
from schema import PostSchema, PostSchema_add
import json
from flask import request
from mongoengine.errors import ValidationError, NotUniqueError


class PostAuthorResource(Resource):
    def get(self, post_id=None):
        if post_id:
            author = Author.objects.get(id=post_id)
            post_list = Post.objects(author=author)
            for post in post_list:
                post.number_of_views += 1
                post.save()
            return PostSchema(many=True).dump(post_list)
        else:
            users = Post.objects()
            user_json = users.to_json()
            return json.loads(user_json)


class TagResource(Resource):
    def get(self, tag_id=None):
        if tag_id:
            tag_list = Tag.objects.get(name=tag_id)
            post_list = Post.objects(tag=tag_list)
            for post in post_list:
                post.number_of_views += 1
                post.save()
            return PostSchema(many=True).dump(post_list)
        else:
            users = Tag.objects()
            user_json = users.to_json()
            return json.loads(user_json)


class PostResource(Resource):

    def post(self):
        json_data = request.json
        errors = PostSchema_add().validate(json_data)
        if errors:
            return errors
        tags = json_data.get('tag')
        tags_list = []
        for i in tags:
            tag = Tag.objects(name=i)
            if len(tag) == 0:
                tag = Tag(name=i).save()
            else:
                tag = tag[0]
            tags_list.append(tag)
        author_field = json_data.get('author')
        if author_field is None:
            return {
                'errors': 'Not field author'
            }
        author = Author.objects(first_name=author_field['first_name'], last_name=author_field['last_name'])
        if len(author) == 0:
            author = Author(first_name=author_field['first_name'], last_name=author_field['last_name'])
            author.save()
        else:
            author = author[0]
        try:
            p = Post(name=json_data.get('name'), description=json_data.get('description'))
            p.author = author
            p.tag = tags_list
            p.save()
            user_json = p.to_json()
            return json.loads(user_json)
        except (ValidationError, NotUniqueError) as errors:
            print(errors)