import json
import os


class Dictionary:
    varieties_filename = './sjp/varieties.txt'
    cache_filename = './cache/dic.cache.json'
    dic = {}

    def __init__(self):
        self.load_dic()

    def load_dic(self):
        if not os.path.isfile(Dictionary.cache_filename):
            self.dic = Dictionary.prepare()
        else:
            with open(Dictionary.cache_filename, 'r') as file:
                self.dic = json.load(file)

    def get_basic_form(self, word):
        return self.dic[word] if word in self.dic else None

    @staticmethod
    def prepare():
        dic = {}

        with open(Dictionary.varieties_filename, encoding='UTF-8') as file:
            for line in file:
                words = Dictionary.parse_line(line).split()
                basic = words[0]

                for word in words:
                    dic[word] = basic

        with open(Dictionary.cache_filename, 'w') as file:
            json.dump(dic, file)

        return dic

    @staticmethod
    def parse_line(line):
        return ''.join([c for c in line if c.isalpha() or c == ' ' or c == '\''])
