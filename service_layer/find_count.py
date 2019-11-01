class FindCount:

    @staticmethod
    def calculate_count(lines, target):
        """
        This method counts the number of times the target is in a sentence
        :param lines: 
        :param target: 
        :return: 
        """
        result = {}
        result['word'] = target.get('word')
        result['sentences'] = []
        for line in lines:
            count = 0
            words = line.split(" ")
            for word in words:
                word = word.replace('.', '')
                if word == target.get('word'):
                    print(word)
                    count += 1
                    result['sentences'].append({'sentence': '', 'count': ''})
        print(result)
        return result