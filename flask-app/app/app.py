import config
import os

from flask import Flask
from flask import jsonify, make_response
from flask_graphql import GraphQLView

import graphene

app = Flask(__name__)

class Company(graphene.ObjectType):
    name = graphene.String()
    review = graphene.Int()

class FlaskInfo(graphene.ObjectType):
    flask_env = graphene.String()
    mode = graphene.String()
    debug_mode = graphene.Int()

class Demo(graphene.ObjectType):
    hello = graphene.String(description='Hello world...')

    def resolve_hello(self, info):
        return 'World'

    company = graphene.Field(Company, description='Company info')

    def resolve_company(root, info):
        return Company(name="JacksonLabs", review=5)
    
    flask_info = graphene.Field(FlaskInfo, description='Flask server info')

    def resolve_flask_info(root, info):
        return FlaskInfo(
            flask_env = os.environ['FLASK_ENV'],
            mode = os.environ['MODE'],
            debug_mode = os.environ['DEBUG_MODE'],
        )

schema = graphene.Schema(query=Demo, auto_camelcase=False)

app.add_url_rule(
    '/graphql',
    view_func=GraphQLView.as_view(
        'graphql',
        schema=schema,
        graphiql=True
    )
)

@app.route('/')
def hello():
    print("Hello World")
    return "Hello World"

@app.route('/env')
def environment():
    data = {
        "FLASK_ENV": os.environ['FLASK_ENV'],
        "MODE": os.environ['MODE'],
        "DEBUG_MODE": os.environ['DEBUG_MODE'],
    }
    return make_response(jsonify(data), 200)

if __name__ == '__main__':
    app.run()
