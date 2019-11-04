import unittest

from sentence_search.service_layer.find_count import FindCount


class TestFindCount(unittest.TestCase):


    line = ["As he turned to go he heard the train."]

    lines_with_comma = ["As he turned, to go he heard the train."]

    lines = ["As he turned to go he heard the train.", "I'll have your all's orders up in just a minute."]

    def setUp(self):
        self.find_count = FindCount

    def test_calculate_count(self):
        result = self.find_count.calculate_count(self.line, 'he')

        assert result == {'word': 'he',
                           'sentences': [{'sentence': 'As he turned to go he heard the train', 'count': 2}]}


    def test_calculate_count_2(self):
        result = self.find_count.calculate_count(self.lines_with_comma, "turned")
        assert result == {'word': 'turned',
                           'sentences': [{'sentence': "As he turned, to go he heard the train", "count": 1}]}

    def test_calculate_count_3(self):
        result = self.find_count.calculate_count(self.lines, "all's")
        assert result == {"word": "all's",
                           "sentences": [{"sentence": "I'll have your all's orders up in just a minute", "count": 1}]}

