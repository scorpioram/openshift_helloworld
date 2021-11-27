from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)


class HelloWorld(Resource):
    # noinspection PyMethodMayBeStatic
    def get(self):
        return 'Hello, World!'

class HelloWorldRoot(Resource):
    # noinspection PyMethodMayBeStatic
    def get(self):
        return 'Hello, World! Root'

api.add_resource(HelloWorld, '/hello')
api.add_resource(HelloWorldRoot, '/')


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080)
