import os

from flask import Flask
from flask_restplus import Api, Resource

from .request_handler import TARGET_SENTENCE
from .service_layer.find_count import FindCount

app = Flask(__name__)
api = Api(app)


find_count = FindCount()

@api.route('/count')
class Count_Words(Resource):

    @api.expect(TARGET_SENTENCE)
    def get(self):
        """
        This method reads the text file
        :return:
        """
        result = {}
        arguments = TARGET_SENTENCE.parse_args(strict=True)
        lines = open(os.getenv('FILE_PATH'), 'r')
        if arguments.get('word'):
            result = find_count.calculate_count(lines, arguments.get('word'))
        else:
            result['word'] = ""
            result['sentences'] = []
        return result
