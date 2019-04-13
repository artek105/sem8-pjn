import json
import os


class Dictionary:
    dic = {}

    def __init__(self):
        dic_file_dir = os.path.dirname(os.path.realpath(__file__))
        self.varieties_filename = dic_file_dir + '/varieties.txt'
        self.cache_filename = dic_file_dir + '/../cache/dic.cache.json'
        self.load_dic()

    def load_dic(self):
        if not os.path.isfile(self.cache_filename):
            self.dic = self.prepare()
        else:
            with open(self.cache_filename, 'r') as file:
                self.dic = json.load(file)

    def get_basic_form(self, word):
        return self.dic[word] if word in self.dic else None

    def get_words_list(self):
        return [word for word, basic in self.dic.items()]

    def prepare(self):
        dic = {}

        with open(self.varieties_filename, encoding='UTF-8') as file:
            for line in file:
                words = self.parse_line(line).split()
                basic = words[0]

                for word in words:
                    dic[word] = basic

        with open(self.cache_filename, 'w') as file:
            json.dump(dic, file)

        return dic

    @staticmethod
    def parse_line(line):
        return ''.join([c for c in line if c.isalpha() or c == ' ' or c == '\''])
