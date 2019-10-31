from flask import Flask
from flask_restplus import Api, Resource

app = Flask(__name__)
api = Api(app)

@api.route('/count')
class Count_Words(Resource):
    def get(self):
        return {'hey': 'there'}


if __name__=='__main__':
    app.run(debug=True)