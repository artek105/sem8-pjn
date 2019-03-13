from lab1.langhelper import get_lang_n_grams
import json
from os.path import exists
from lab1.ngrams import NGrams


def get_base_n_grams(lang, n, cache=True):
    filename = './cache/' + lang + '_' + str(n) + '.json'

    if cache and exists(filename):
        with open(filename, 'r') as file:
            return NGrams(n, json.load(file))

    n_grams = get_lang_n_grams(lang, n)

    if cache:
        with open(filename, 'w') as file:
            json.dump(n_grams.map, file)

    return n_grams
