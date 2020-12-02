from flask import Flask, jsonify, request, Response
from models import User

app = Flask(__name__)


@app.route('/user', methods=['GET', 'POST', 'PUT', 'DELETE'])
@app.route('/user/<string:user_id>', methods=['GET', 'POST', 'PUT', 'DELETE']) 
def user(user_id=None): 
    if request.method == "GET":
        users = User.objects()
        user_json = users.to_json()
        return Response(user_json, content_type='application/json')
    elif request.method == "POST": 
        user = User(**request.json).save()
        user_json = user.to_json() 
        return Response(user_json, content_type='application/json')
    elif request.method == "PUT" and user_id: 
        user = User.objects().get(id=user_id)
        user.update(**request.json)
        user.reload()
        return Response(user.to_json(), content_type='application/json')
    elif request.method == "DELETE":
        User.objects(id=user_id).delete()
        return jsonify({'status': 'deleted'})
    else:
        return jsonify({'status': 'error'})


if __name__ == "__main__":
    app.run(debug=True)