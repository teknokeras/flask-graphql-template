from flask import Flask, request, jsonify
from flask_jwt_extended import JWTManager

from flask_graphql import GraphQLView

from flask_jwt_extended import (
    JWTManager, 
    jwt_required, 
    create_access_token,
    get_jwt_identity
)

from schemas.schema import schema
from database.base import db_session

from module.user.login import process

app = Flask(__name__)
app.config['JWT_SECRET_KEY'] = 'super-secret'  # Change this!
jwt = JWTManager(app)

app.add_url_rule(
    '/graphql',
    view_func=GraphQLView.as_view('graphql', schema=schema, graphiql=True))

@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()

@app.route('/api/login', methods=['POST'])
def get_tasks():
    return jsonify(process(request.get_json()))

if __name__ == '__main__':
    app.run(threaded=True, debug=True, host='0.0.0.0')