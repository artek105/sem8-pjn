from lab2.sjp.dictionary import Dictionary
from lab3.levensthein import Levenshtein
import os
from lab2.wordngrams import WordNGrams
import json
from datetime import datetime


class Bayes:
    alpha = 10
    part_ratio = .5
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

    def get_best_corrections(self, w, num=10, print_times=False):
        t1 = datetime.now()
        possible_corrections = self.get_possible_corrections(w)
        t2 = datetime.now()

        p_list = []
        for c in possible_corrections:
            p_list.append((self.p_c_w(c, w), c))
        t3 = datetime.now()

        p_list.sort(key=lambda x: x[0], reverse=True)
        t4 = datetime.now()

        if print_times:
            print('possible corrections:', (t2 - t1).total_seconds())
            print('p(c|w):', (t3 - t2).total_seconds())
            print('sort:', (t4 - t3).total_seconds())

        if num is None:
            num = len(p_list)

        return [c[1] for c in p_list][:num]

    def get_possible_corrections(self, w):
        length = len(w)
        part_size = int(length * self.part_ratio)

        char_groups = [w[start:start + part_size] for start in range(length - part_size + 1)]

        def has_ordered_chars(string, chars):
            s_len = len(string)
            c_len = len(chars)

            c_index = 0  # index of character in chars
            for s_index, char in enumerate(string):
                # s_len - s_index  - char num to check
                # part_size - c_index  - char num, which could be char to check
                # first expr should be grater or equal to second expr
                if s_len - s_index < part_size - c_index:
                    break

                if char == chars[c_index]:
                    c_index += 1

                if c_index >= c_len:
                    return True

            return False

        def consists_from_one_of_char_group(word):
            if len(char_groups) == 0:
                return True

            for char_group in char_groups:
                if has_ordered_chars(word, char_group):
                    return True

            return False

        possible_corrections = []
        for c_list in [
            self.dic.get(str(length), []),
            self.dic.get(str(length - 1), []),
            self.dic.get(str(length + 1), [])
        ]:
            for c in c_list:
                if (c[0:1] == w[0:1] or c[1:2] == w[0:1] or c[0:1] == w[1:2]) and consists_from_one_of_char_group(c):
                    possible_corrections.append(c)

        return possible_corrections
