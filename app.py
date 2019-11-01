from flask import Flask
from flask_restplus import Api, Resource

app = Flask(__name__)
api = Api(app)

@api.route('/count')
class Count_Words(Resource):
    def get(self):
        """
        This method reads the text file
        :return:
        """
        lines = open('example.txt')
        result = self.find_count(self, l)
        return {'hey': 'there'}

    def find_count(self, lines, target):
        result = {}
        result['word'] = target
        result['sentences'] = []
        for line in lines:
            count = 0
            words = line.split(" ")
            for word in words:
                word = word.replace('.', '')
        #         print(word)
                if word == target:
                    count += 1
                    result['sentences'].append({'sentence': line, 'count': count})
        return result

if __name__=='__main__':
    app.run(debug=True)