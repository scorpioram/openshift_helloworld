from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)


class HelloWorld(Resource):
    # noinspection PyMethodMayBeStatic
    def get(self):
        return 'Hello, World!'


api.add_resource(HelloWorld, '/hello')
app.run()
