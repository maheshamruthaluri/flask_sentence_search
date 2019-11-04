import re


class FindCount:

    @staticmethod
    def calculate_count(lines, target):
        """
        This method counts the number of times the target is in a sentence
        :param lines: 
        :param target: 
        :return: 
        """
        sentences = []
        result = {}
        result['word'] = target
        result['sentences'] = sentences
        regex = re.compile('\\b' + target + '\\b')
        for line in lines:
            count = len(regex.findall(line))
            if count:
                sentences.append({'sentence': line.strip('\n').replace('.', ''),
                                            'count': count})
        result['sentences'] = sorted(result['sentences'], key=lambda item: item['count'],
                                     reverse=True)
        return result

