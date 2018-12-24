from flask import Flask
import connexion

from flask_graphql import GraphQLView

from flask_jwt_extended import (
    JWTManager, 
    jwt_required, 
    create_access_token,
    get_jwt_identity
)

from schemas.schema import schema
from database.base import db_session

#app = Flask(__name__)
app = connexion.App(__name__, specification_dir='./')

app.add_api('swagger.yml')

app.add_url_rule(
    '/graphql',
    view_func=GraphQLView.as_view('graphql', schema=schema, graphiql=True))

#teardown_appcontext not in connexion
#@app.teardown_appcontext
#def shutdown_session(exception=None):
#    db_session.remove()


if __name__ == '__main__':
    app.run(threaded=True, debug=True, host='0.0.0.0')