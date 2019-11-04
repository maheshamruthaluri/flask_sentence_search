from flask_restplus import reqparse

TARGET_SENTENCE = reqparse.RequestParser(bundle_errors=True)
TARGET_SENTENCE.add_argument('word', type=str, required=True, location='args',
                             help='count the number of occurrences')