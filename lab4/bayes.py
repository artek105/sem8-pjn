from lab2.sjp.dictionary import Dictionary
from lab3.levensthein import Levenshtein
import os
from lab2.wordngrams import WordNGrams
import json


class Bayes:
    alpha = 10
    part_ratio = 2
    p_c_smoothing_ratio = .2
    cached_n = None

    def __init__(self):
        bayes_file_dir = os.path.dirname(os.path.realpath(__file__))
        self.cache_filename = bayes_file_dir + '/cache/bayes.dic.cache.txt'
        self.dic = self.get_dic()
        self.dic_size = self.get_dic_size()
        self.counter = WordNGrams(1)

    def get_dic(self):
        if os.path.isfile(self.cache_filename):
            with open(self.cache_filename) as cache:
                return json.load(cache)

        dic = {}
        for c in Dictionary().get_words_list():
            length = len(c)
            if length not in dic:
                dic[length] = []
            dic[length].append(c)

        for length in dic.keys():
            dic[length].sort()

        with open(self.cache_filename, 'w') as cache:
            json.dump(dic, cache)

        return dic

    def get_dic_size(self):
        return sum([len(words) for words in self.dic.values()])

    # P(w|c)
    def p_w_c(self, w, c):
        norm = Levenshtein.norm(w, c, False)
        return 1 - norm / (norm + 5)

    def apply_file(self, filename):
        self.counter.apply_file(filename, encoding='UTF-8')

    # P(c)
    def p_c(self, c):
        if self.cached_n is None:
            self.cached_n = self.counter.get_all_ngrams_count()

        n = self.cached_n ** self.p_c_smoothing_ratio
        nc = self.counter.get_ngram_count(c) ** self.p_c_smoothing_ratio
        m = self.dic_size ** self.p_c_smoothing_ratio
        return (nc + self.alpha) / (n + self.alpha * m)

    # this method is in direct proportion to P(c|w)
    def p_c_w(self, c, w):
        return self.p_w_c(w, c) * self.p_c(c)

    def save(self, filename):
        with open(filename, mode='w') as file:
            json.dump(self.counter.map, file)

    def load(self, filename):
        with open(filename) as file:
            data = json.load(file)
            self.counter.map = data

    def get_best_corrections(self, w, num=10):
        length = len(w)
        part_size = int(length / self.part_ratio)

        char_groups = [w[start:start + part_size] for start in range(length - part_size + 1)]

        def consists_from_one_of_char_group(word):
            for char_group in char_groups:
                consists = True
                for char in char_group:
                    if char not in word:
                        consists = False
                        break

                if consists:
                    return True

            return False

        c_list = self.dic.get(str(length), [])
        c_list.extend(self.dic.get(str(length - 1), []))
        c_list.extend(self.dic.get(str(length + 1), []))
        filtered = [c for c in c_list if consists_from_one_of_char_group(c)]

        p_list = []
        for c in filtered:
            p_list.append((self.p_c_w(c, w), c))

        p_list.sort(key=lambda x: x[0], reverse=True)

        return [c[1] for c in p_list][:num]
